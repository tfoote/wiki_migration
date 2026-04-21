**rve_interface_gen** turns an interface definition into an easy to use
proxy class and inheritable server class that use [rve_rpc](rve_rpc) for
communication.

For example: 

```
interface Bar
{
  bar(uint32 x, uint32 y, string blah) returns (geometry_msgs/Vector3 v);
}
```



generates a number of messages: 

```
Bar_barRequest.msg  
Bar_barResponse.msg
```



a proxy class: 

```cplusplus
struct BarProxy : public Bar
{
  BarProxy(rve_rpc::Client& client);
  void bar(uint32_t x, uint32_t y, const std::string& blah, geometry_msgs::Vector3& out_v);
  void barAsync(uint32_t x, uint32_t y, const std::string& blah, const barResponseCallback& cb);
  barResponseConstPtr bar(const barRequestConstPtr& in);
  void barAsync(const barRequestConstPtr& in, const barResponseCallback& cb);
};
```



And a server class: 

```cplusplus
struct BarServer : public Bar
{
  BarServer(rve_rpc::Server& server);
  virtual void bar(uint32_t x, uint32_t y, const std::string& blah, geometry_msgs::Vector3& out_v) {ROS_BREAK();}
  virtual void bar(barHandle& handle);
};
```



along with a bunch of typedefs in a base class 

```cplusplus
struct Bar : public rve_interface_gen::Interface
{
  virtual ~Bar() {}

  typedef rve_interface_gen::Bar_barRequest barRequest;
  typedef boost::shared_ptr<barRequest> barRequestPtr;
  typedef boost::shared_ptr<barRequest const> barRequestConstPtr;
  typedef rve_interface_gen::Bar_barResponse barResponse;
  typedef boost::shared_ptr<barResponse> barResponsePtr;
  typedef boost::shared_ptr<barResponse const> barResponseConstPtr;
  typedef rve_rpc::CallHandle<barRequest, barResponse> barHandle;
  typedef rve_rpc::MethodResponse<barResponse> barMethodResponse;
  typedef boost::function<void(const barMethodResponse&)> barResponseCallback;

};
```


