# ino_agv

## Özellikler

  -- ------------------------------------------------ -- -------- --
     \<tablewidth=\"400px\"\>\'\'\' Platform \'\'\'               
     En                                                  728mm    
     Boy                                                 1026mm   
     Yükseklik                                           325mm    
     Ana Tekerlek                                        2x       
     Sarhoş Tekerlek                                     4x       
  -- ------------------------------------------------ -- -------- --

  -- ------------------------------------------------- -- ----------- --
     \<tablewidth=\"400px\"\>\'\'\' Sensörler \'\'\'                  
     Kızılötesi                                           8x          
     Lazer Tarayıcı                                       1x (270')   
  -- ------------------------------------------------- -- ----------- --

Kızılötesinin yayınladığı Topicler

-   /agv1/ir1
-   /agv1/ir2
-   /agv1/ir3
-   /agv1/ir4
-   /agv1/ir5
-   /agv1/ir6
-   /agv1/ir7
-   /agv1/ir8

Lazer Tarayıcının yayınladığı Topicler

-   /agv1/laser

## Kurulum

Terminal ( Ctrl + Alt + T ) açılarak oluşturulan workspace e girilir.

```
$ git clone https://github.com/inomuh/agvsim_v2_ros.git
``` Githubtan agvsim_v2_ros dosyası indirilir.

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
``` komutuyla agv_v2 modeli zipten çıkartılır.

Aşağıdaki komutlarla gerekli kütüphaneler indirilir.

ROS Navigasyon paketinin çalışması için gerekli olan kütüphane
indirilir.

```
$ sudo apt-get install ros-kinetic-navigation
``` ROS Slam paketi ile harita oluşturma ve
kaydetme işlemleri gerçekleştirilir.

```
$ sudo apt-get install ros-kinetic-gmapping
``` Launch dosyalarının belirlenen zaman
aralıklarında açılması için kullanılır.

```
$ sudo apt-get install ros-kinetic-timed-roslaunch
``` ROS'ta dinamik olarak parametre değişikliği
için kullanılmaktadır.

```
$ sudo apt-get install ros-kinetic-dynamic-reconfigure
``` ROS Smach paketinin uygulamalarını
görselleştirmek için kullanılmaktadır.

```
$ sudo apt-get install ros-kinetic-smach-viewer
``` Bashrc açılır ve Gazebo ortamı için modellerin
bulunduğu dosya, GAZEBO_MODEL_PATH' e eklenir.

```
$ gedit ~/.bashrc
``` ```
$ export GAZEBO_MODEL_PATH=/<WORKSPACE_NAME>/src/agvsim_v2_ros/building_editor_models:/<WORKSPACE_NAME>/src/agvsim_v2_ros/model_editor_models:$GAZEBO_MODEL_PATH
``` Workspace'e girilerek
catkin_make yapılır.

```
$ cd <WORKSPACE_NAME>

$ catkin_make

$ catkin_make install
```

## Uygulama Çalıştırma

Tüm uygulamayı açmak için

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```0 Gazebo'yu açmak için

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```1 Navigasyonu açmak için

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```2 Uygulama için özelleştirilmiş Rviz'i açmak
için

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```3 Smach Viewer'ı açmak için

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```4 Smach uygulamasını çalıştırmak için

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```5 Slam yaparak harita oluşturmak için

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```6 Hata Aşağıdaki gibi bir hata alınır ise ERROR:
cannot launch node of type \[agv2_smach/agv_task_plan_service.py\]:
can\'t locate node \[agv_task_plan_service.py\] in package
\[agv2_smach\]

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```7 konumuna giderek aşağıda belirtilen yetki
komutları çalıştırılır

```
Unzip ~/agvsim_v2_ros/agv2_description/meshes/22-10-2019-OTAv07/OTA-v0.7.stl.zip
```8
