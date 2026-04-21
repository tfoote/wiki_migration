## About

This package detects lower step as a obstacle when you use a LRF with a
lower angle.

## Installation

To install the `lower_step_detector` package, you can install from
source with the following commands:

. 

```shell
cd /(your catkin workspace)/src
git clone https://github.com/CIR-KIT/lower_step_detector.git
cd ..
catkin_make
```



## Usage

. 

```shell
roslaunch lower_step_detector hogehoge.launch
```



## Parameters

-   laser_intensity_max: 1.5
-   直線上のレーザ長で何\[m\]を平面とみなすか．段差がなければこれが最大値になるはず．デフォルトは1.5\[m\]．
-   margine_between_plane_and_down_step: 1.0
-   計算上平面と思うintensityから何\[m\]以上大きい場合に段差とみなすか．デフォルトは1.0\[m\]
-   virtual_laser_intensity: 1.0
-   段差とみなした場合、何\[m\]の位置に障害物があると仮定するか．デフォルトは1\[m\]．
-   laser_scan_range_deg: 180
-   LRF の認識範囲\[°\]．デフォルトは180\[°\]．
-   detect_step_angle_min_deg: 10.0
-   LRF
    認識範囲の両端で段差検出を除外する範囲\[°\]．指定方法は片側の角度設定．デフォルトは10\[°\]．左右それぞれ10°カットする．
-   例えば、高さ0.75\[m\],
    30\[°\]傾けたセンサが地面を検出した際に出力する値を計算すると、中心から左右に50\[°\]傾く辺りから急激に大きな値を取り始め、80\[°\]から指数関数のような形状で増加する。
-   両端はノイズが乗りやすいので、判定から除外すべき。
-   chunk_angle_for_noise_deg: 5.0
-   ノイズ対策．セグメントを何度毎に区切るか．デフォルトは5.0\[°\]
-   ratio_detect_in_chunk: 0.8
-   ノイズ対策．セグメント内でどの程度閾値を超えたら段差と判定するか．0.8\[raito\].
