## urdf_to_collada command-line tool

The urdf_to_collada tool will convert `.urdf` files into COLLADA
`.dae` files.

Usage:



```
rosrun collada_urdf urdf_to_collada <input-urdf> <output.dae>
```



Example:



```
rosrun collada_urdf urdf_to_collada pr2.urdf pr2.dae
```



### Limitations

-   Only binary STL mesh geometries are supported
-   Mesh scale is not exported
-   Materials are not exported

## collada to urdf command-line tool

Usage:



```
rosrun collada_urdf collada_to_urdf <input.dae> <output.urdf>
```


