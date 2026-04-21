## Why?

`rve_rpc` is essentially a service replacement. You may ask, then,
what the advantages of `rve_rpc` are vs. services.

-   `rve_rpc` is topic based. This means any topic-based tools such as
    [rosbag](rosbag) will work with `rve_rpc`. Note that things like
    `rostopic echo` will not work properly due to how `rve_rpc`
    works internally. A [rostopic](rostopic) equivalent for `rve_rpc`
    is planned. Also, because it is topic based, `rve_rpc` clients are
    always connected to their servers, meaning every `rve_rpc` call is
    equivalent to a persistent service call.
-   `rve_rpc` allows multiple rpc methods to be called over a single
    connection. This means fewer lookups to the master, and the ability
    to order asynchronous calls to different rpc methods.
-   `rve_rpc` provides an asynchronous interface, both for server
    callback responses, and for client method calls. These could be
    implemented for services as well.
-   `rve_rpc` can use any pair of messages as a request/response, and
    does not require a separate definition or separate generated code.

## Examples

`rve_rpc` was mainly designed for use by
[rve_interface_gen](rve_interface_gen), so its API could probably use
some work. Using it standalone is still fairly easy though.

### Server

A server callback looks something like this:

```cplusplus
void callback(rve_rpc::CallHandle<RequestMessage, ResponseMessage>& handle)
{
  const RequestMessageConstPtr& req = handle.getRequest();
  // do stuff with req
  // ...
  TestResponsePtr res(new TestResponse);
  handle.respond(res);
}
```

`handle` here allows you to either respond immediately (like in the
example), or store it off and respond later. If an
`rve_rpc::CallHandle` is destroyed without ever responding, it
responds with an exception.

To indicate an error, you can either call `handle.except("my error
message goes here")`, or you can throw an exception derived from
`std::exception` from within your callback.

Setting up the server is done using the `rve_rpc::Server` class, like
so: ```cplusplus
Server s("server_name", nh);
s.addMethod<RequestMessage, ResponseMessage>("callMe", callback);
s.ready();
```

### Client

Use of a client looks something like this: ```cplusplus
Client c("server_name", nh);
Method<RequestMessage, ResponseMessage> m = c.addMethod<RequestMessage, ResponseMessage>("callMe");
c.connect();

ReqeustMessagePtr req(new RequestMessagePtr);
// fill out req...
ResponseMessageConstPtr res = m.call(req);
```

Alternatively, you can use it asynchronously like so:
```cplusplus
m.callAsync(req, callback);
```

where `callback` is of the form: ```cplusplus
void callback(const MethodResponse<ResponseMessage>& res)
{
  if (res.error_code == rve_rpc::Response::SUCCESS)
  {
    const ResponseMessageConstPtr& msg = res.response;
    //...
  }
}
```

## Internals

An `rve_rpc` client/server pair operate on a "request/response"
topic. For example: ```
/server_name/request
/server_name/response
```

These topics are always of the type `rve_rpc::Request` and
`rve_rpc::Response`. The request/response messages are serialized into
a uint8 array inside the container message. This is why "rostopic
echo" won't give you what you might expect with these topics.

`rve_rpc` uses `RequestWrapper` and `ResponseWrapper` classes that
serialize to the same wire format as the messages to support no-copy
"serialization" when running intraprocess.
