## About

Remote monitoring package for navigation with
[OpenVPN](https://openvpn.net/). We actually succeeded in remotely
monitoring [Robots/CIR-KIT-Unit03](Robots/CIR-KIT-Unit03)'s pose
running in Tsukuba from Fukuoka
([1200 km away](https://www.google.com/maps/dir/%E6%97%A5%E6%9C%ACFukuoka-ken/Tsukuba+Station,+Tsukuba,+Ibaraki+Prefecture,+Japan/@34.8284911,133.016243,7z/data=!3m1!4b1!4m14!4m13!1m5!1m1!1s0x3541817af77eb125:0x97a20ffb4a51384d!2m2!1d130.418297!2d33.6065756!1m5!1m1!1s0x60220c62d3552d37:0x3487ddbc353229bd!2m2!1d140.1116438!2d36.0827702!3e4))

How to connect remote PCs with OpenVPN can be seen in
[Qiita: 図解！UbuntuでOpenVPNを使う (Japanese Page)](http://qiita.com/MoriKen/items/7fe17fda8442adb599d9).

Tutorial to integrate OpenVPN and ROS is
[ROS で OpenVPN を使う (Japanese Page)](http://qiita.com/MoriKen/items/00c2006e0c7ae914a9ba).

## Demo Video

[![remote_monitor\|width="600"](attachment:remote_monitor.png)](https://youtu.be/hpAnaV-bylQ)

下記のコマンドで上記動画のように遊べるはずです

```
$ roslaunch cirkit_unit03_autorun autorun_gazebo.launch 
$ roslaunch remote_monitor remote_monitor_server_gazebo.launch
$ roslaunch remote_monitor remote_monitor_client_gazebo.launch
```

## Nodes

### monitor_server

-   遠隔監視PC側`node`．`service`で受信した位置と姿勢を地図上に表示させる．

### monitor_client

-   移動ロボット側`node`．一定距離毎に現在位置と姿勢を`service`で送信する．
-   デフォルトでは`/amcl_pose`を`subscribe`する．

## Installation

以下のコマンドにしたがってインストールしてください．
なお`<catkin_ws>`は，任意のcatkinizeされたワークスペースへのパスを表します．

### Clone the repository

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```

### Clone the dependent repository via wstool

```
$ cd <catkin_ws>
$ wstool init src
$ wstool merge -t src src/remote_monitor/remote_monitor.rosinstall
$ wstool update -t src
```

### Clone the dependent repository via rpsdep

```
$ rosdep update && rosdep install -r -y --from-paths src --ignore-src
```

### Build

```
$ cd <catkin_ws>
$ catkin_make
$ source devel/setup.bash
```

## How to launch

### service server

-   地図の在処として，下記のパッケージ配下のフォルダを見に行きます．
-   \$(find cirkit_unit03_maps)/map/`
-   地図名は引数で指定して下さい．

#### 実機の場合のコマンド

```
$ roslaunch remote_monitor remote_monitor_server.launch map_yaml:=hogehoge.yaml
```

#### `Gazebo`の場合のコマンド

```
$ roslaunch remote_monitor remote_monitor_server_gazebo.launch map_yaml:=hogehoge.yaml
```

### service client

#### サーバー側のグローバルIPを設定する．

-   まずサーバ側の人にグローバルIPを聞く．
-   以下の要領で設定ファイルに反映させる．

```
$ cd /etc/openvpn
$ emacs client.conf
```

client.conf ```
# 省略

# グローバルIPアドレスを指定する．
remote 101.102.103.xxx 1194

# 省略
```

#### OpenVPNを再起動する.

```
$ service openvpn restart
```

#### ネットワークを確認する．

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```0

-   下記のような`tun`デバイスが表示される．少し時間がかかる場合がある．

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```1

-   そしてサーバにping．

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```2

#### ROSネットワークの設定

-   必ず「全てのコンソール」で下記の設定をすること．

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```3

-   下記をsourceでもよい．

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```4

-   一応確認する．

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```5

#### ROSネットワークの確認

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```6

-   下記のサービスがあることを確認する．

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```7

#### モニタークライアントを起動する

##### 実機設定

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```8

##### Gazebo設定

```
$ cd <catkin_ws>/src
$ git clone https://github.com/CIR-KIT/remote_monitor.git
```9

## parameters

### /config/remote_monitor_server.yaml

```
$ cd <catkin_ws>
$ wstool init src
$ wstool merge -t src src/remote_monitor/remote_monitor.rosinstall
$ wstool update -t src
```0

### /config/third_robot_client.yaml

```
$ cd <catkin_ws>
$ wstool init src
$ wstool merge -t src src/remote_monitor/remote_monitor.rosinstall
$ wstool update -t src
```1

## Commands

地図画像をアクティブにした状態で下記キーを入力するとモードを切り替えられます．

```
$ cd <catkin_ws>
$ wstool init src
$ wstool merge -t src src/remote_monitor/remote_monitor.rosinstall
$ wstool update -t src
```2
