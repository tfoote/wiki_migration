This package contains tools to validate lanelet2 maps, similar to a
linter.

To test a map, simply run `rosrun lanelet_validation lanelet2_validate
<mymap>`, or better `rosrun lanelet2_validation lanelet2_validate
<mymap> \--lat <lat> \--lon <lon>`, where lat/lon is an origin
close to your map data. The tool will output errors and warnings that
were found in your map.

For advanced usage like running only a fraction of the tests, try
`rosrun lanelet2_validation lanelet2_validate \--help`.
