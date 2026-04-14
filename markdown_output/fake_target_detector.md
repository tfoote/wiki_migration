### About

\`fake_target_detector\`を使って探索対象が見つかったことにできます。
まず、どこに探索対象がいることにするかを決めます。地図を\`rviz\`で表示しながら探索対象が居る場所に\`Publish
point\`を使ってクリックします。

```
rostopic echo /clicked_point
```

をすればクリックした座標がわかります。その\`x,
y\`座標を\`targetlist/targetlist.csv\`におきます。

```
rosrun fake_target_detector fake_target_detector
```

とすれば\`targetlist.csv\`に書かれた座標にBoundingBoxが表示されているはずです。そうすればちゃんとpublishもされています。
到達したwaypointが探索エリアでロボットから5\[m\]以内に探索対象がいればアプローチするはずです。
また一度アプローチした探索対象から近い場合には無視します。
