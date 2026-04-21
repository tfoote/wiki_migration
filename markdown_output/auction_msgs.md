{}

The *auction_msgs* was created with the objective of defining a more
user-friendly mechanism to deal with auction information.

ROS uses a "simplified messages description language for describing the
data values (aka messages) that ROS nodes publish. This description
makes it easy for ROS tools to automatically generate source code for
the message type in several target languages. Message descriptions are
stored in .msg files in the msg/ subdirectory of a ROS package".

For simplicity instead of defining a msg/ folder in each package for the
auction protocols, we use a dedicated package for defining the specific
Auction and Bid messages. This procedure is a common practice and is
advised by the good practices for development in ROS. There are two
parts to a .msg file: fields and constants. Fields are the data that is
sent inside of the message. Constants define useful values that can be
used to interpret those fields (i.e. enum-like constants for an integer
value).

The auction messages are defined in the Auction.msg and the Bid.msg
files, stored in the msg/ of the auction_msgs package.

Message descriptions are referred to using package resource names. For
example, the file auction_msgs/msg/Auction.msg is commonly referred to
as auction_msgs/Auction.

To import our auction message types we need to import the auction_msgs
module and declare an object that will be of type
auction_msgs.msg.Auction or auction_msgs.msg.Bid. The advantages of
defining a type of message for both Auction and Bid is evidenced at the
development stage when avoiding the definition of numerous variables to
define the auction information.

Another advantage is the increased assertiveness while developing the
programs since the risk of defining different variable values or
omitting others is greatly decreased. The Auction.msg and Bid.msg are
defined according to the tables **auction_msg** and **bid_msg**.

  -- --------------------- -- ---------------- -- ------------------------------------------------------------------------------------------------------------------------ -- -- -- -- --
                                                  **Auction.msg**                                                                                                                      
     **Data type**            **Field name**      **Description**                                                                                                                      
     Header                   header              Header information regarding sequence number, timestamp, and frame_id                                                                
     string                   command             Information about the command sent from node to node. Accepting values 'join_auction' or 'close_auction'                         
     string                   task_type_name      The type of the task. Accepting values 'go_to'                                                                                     
     string                   subject             Field to control the audience of the auction. This related with k-hop. Accepting values 'all' or 'k'                             
     string                   metrics             Identify the used metrics for the current auction. Accepting values 'distance'                                                     
     duration                 length              Identify the duration for the task. Accepting any value for duration. (Currently not in use)                                         
     geometry_msgs/Point      task_location       Location where the action is needed. Accepting values task_location.x, task_location.y and task_location.z are float64               
  -- --------------------- -- ---------------- -- ------------------------------------------------------------------------------------------------------------------------ -- -- -- -- --

  -- ----------- -- --------------- -- ----------------------------------------------------------------------- -- -- -- -- --
                                       **Bid.msg**                                                                         
     Data type      Field name         Description                                                                         
     Header         header             Header information regarding sequence number, timestamp, and frame_id               
     string         buyer_id           Referenced name of the bidding node with role 'buyer'                             
     int64          cost_distance      Value for the cost in terms of Euclidean distance                                   
  -- ----------- -- --------------- -- ----------------------------------------------------------------------- -- -- -- -- --
