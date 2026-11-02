## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/containers.hpp>

// The container types
using ecl::Array;
using ecl::Stencil;
using ecl::FiFo
using ecl::PushAndPop;
```



## Tutorials

- [Arrays](#arrays) - fixed and
  dynamic arrays, comma initialisation and blueprints.
- [Stencils](#stencils) -
  windows onto ecl arrays.
- [Buffer Overflow Detection](#buffer-overflow-detection) -
  detecting array under and over runs.
- [Fifo](#fifo) - A simple
  first in, first out class.
- [Utilities](#container-utilities) -
  container formatters and converters.

## Examples

See the programs in the `src/test` and `src/examples`
subdirectories.

## Arrays

- **Description:** Introduction to c++ style arrays, both fixed and
  dynamic.
- **Keywords:** ecl containers arrays
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Stencils](#stencils)
  [Buffer Overflow Detection](#buffer-overflow-detection)

### Overview

Ecl arrays provide a typical c++ style stl interface. There are, however
a couple of features of arrays that stand out from stl containers.

- Fixed arrays store data on the stack -> faster for small arrays.
- _Comma Initialisation_ : eigen style initialisation.
- _Blueprint Instantiation_ : efficient construction without costly
  copies.

### Fixed Arrays

Fixed arrays provide a fixed size container (enabled via a template
parameter) that can be saved as contiguous memory on the stack. This is
in contrast to typical stl containers that are dynamic and thus use the
heap for storage, which is typically much slower. This is especially
true for small arrays, though other considerations become more important
as the array size increases.

#### Comma Initialisation

This concept is brought in (with slightly modified form) from Blitz++
and Eigen.



```cplusplus
ecl::Array<int,5> array; // be careful, at this point, the contents are uninitialised.
array << 1,2,3,4,5;      // comma initialisation
```



Comman initialisers will throw an exception if the range is exceeded in
debug mode (beware release mode!).

#### BluePrint Instantiations

These provide an efficient means of instantiating array classes without
a costly copy-on-the-fly slowdown. It uses a blueprint coupled with what
is referred to as a blueprint factory to do this (refer to
[ecl_concepts](https://index.ros.org/p/ecl_concepts) for more details.).
However, the construction makes the usage of this transparent.



```cplusplus
// construction.
Array<int,5> array = Array<int,5>::Constant(3); 
// assignment, no costly copy operation used.
array = Array<int,5>::Constant(3);
```



### Dynamic Arrays

These arrays are almost exactly the same as the former fixed arrays,
however they are dynamically sizeable (though not as automatically nor
flexibly as vectors) with their storage on the heap, not the stack. The
lack of flexibility isn't a serious disadvantage as a control program
should generally manage vector memory careful (read, manually!) anyway.
Their other feature is again, like the fixed arrays, the _comma
initialiser_.



```cplusplus
// Construct without storage allocated.
Array<int> array1;    
// Initialise a vector with storage space for four integers.
Array<int> array2(4); 
// Initialise space for four integers filled with a value of 3.
Array<int> array3 = Array<int>::Constant(4,3); 

array1.clear();       // Clear - delete and point buffer to NULL.
array1.resize(10);    // Resize - delete and recreate uninitialised buffer.
```

## Stencils

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [Arrays](#arrays).
- **Description:** Windows onto ecl arrays.
- **Keywords:** ecl arrays
- **Tutorial Level:** INTERMEDIATE
- **Next Tutorial:**
  [Buffer Overflow Detection](#buffer-overflow-detection)

Often you require a window onto a container (array) and stencils provide
a safe way to do this. Stencils avoid the use of dangerous pointers
which can cause problems if the underlying container goes out of scope
or is resized. It does this by including the underlying container as a
reference and also includes similar out of range checks that arrays
perform (exception throwing in debug mode for \[\] and always for at()).



```cplusplus
typedef Array<int,5> FixedArray;
typedef Stencil< FixedArray > FixedStencil;

FixedArray array;
array << 1,2,3,4,5;
FixedStencil stencil(array,1,3); // windows from index 1 to 3
std::cout << stencil[1] << std::endl; // accesses array[2];
```

## Buffer Overflow Detection

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [Arrays](#arrays),
  [Stencils](#stencils).
- **Description:** Detecting ecl array over/under runs.
- **Keywords:** ecl arrays buffer overflow
- **Tutorial Level:** INTERMEDIATE

Arrays also provide a feature to allow for buffer overflow checking -
for both fixed and dynamic arrays. Often programs pull pointers to
various elements on the contiguous array (especially in really low level
routines like vision routines), it is important to know when the stack
or heap is being under or over run.

Such functionality can be enabled by declaring the
`ECL_MEM_CHECK_ARRAYS` macro when compiling.

Internally, this entails pre/appending some magic characters to the
underlying array and then occasionally performing manual checks to
ensure that the magic chars haven't been disturbed.



```cplusplus
#define ECL_MEM_CHECK_ARRAYS

void worker_function( int* i) {
    // do some work here, possibly overrunning or underrunning
}

int main() {
    Array<int,4> array; array << 1, 2, 3, 4;
    while ( control_loop_running ) {

        int* istart = array[0];
        worker_function(i_start);

        if ( array.bufferUnderRun() ) { std::cout << "WARNING! We have an underrun problem houston!" << std::endl; }
        if ( array.bufferOverRun() ) { std::cout << "WARNING! We have an overrun problem houston!" << std::endl; }
        if ( array.bufferOverFlow() ) { std::cout << "WARNING! We have an unknown problem houston!" << std::endl; }
    }
```

## Fifo

- **Description:** A simple first in, first out class.
- **Keywords:** ecl containers fifo
- **Tutorial Level:** BEGINNER

During the construction of fifo, typically length of buffer may be
important.



```cplusplus
FiFo<double> fifo(4);               // reserved only (not filled)
fifo.push_back( data_incoming );
```



An initialised buffer can be important in variaous situation. For
example, if you wish to calculate a moving average, you should wait for
N (length of buffer) pieces of incoming of data. However, if you
initialise the whole buffer as above, you can proceed immediately.



```cplusplus
FiFo<double> fifo_initialised(4, initial_value); // reserved and filled
fifo.push_back( next_data );                // set next data
// ...                                                              
// calculate the average here
```

## Container Utilities

- **Note:** This tutorial assumes that you have completed the previous
  tutorials: [Arrays](#arrays),
  [Stencils](#arrays).
- **Description:** container formatters and converters.
- **Keywords:** ecl container utilities
- **Tutorial Level:** INTERMEDIATE

### Formatters

Currently there is only limited support for formatters of the array and
stencil classes classes:

- precision/width formatting for float arrays.
- hex formatting for byte arrays (signed char/char/unsigned char).
- default formatting for other types of arrays (provided they have the
  required Format for the element type).
- formatting extends to stencils operating on the array.



```cplusplus
#include <ecl/array.hpp>

Array<unsigned char>::Formatter format;
Array<unsigned char> array;
array << 0x01, 0x02, 0x03, 0x04;
std::cout << format(array) << std::endl;
// OR
#include <ecl/array.hpp>
#include <ecl/format.hpp>

Format< Array<unsigned char> > format;
Array<unsigned char> array;
array << 0x01, 0x02, 0x03, 0x04;
std::cout << format(array) << std::endl;
```



See also [ecl_formatters](https://index.ros.org/p/ecl_formatters).

### Byte Array Converters

These are often useful for interacting with io devices.

Some converters utilising the `FromByteArray` template class from
[ecl_converters](https://index.ros.org/p/ecl_converters) have
specialisations here for arrays and stencils respectively. These allow
conversion to integers of any time from a corresponding, little endian
filled array/stencil of chars.



```cplusplus
typedef Array<char, 4> ByteArray;
ByteArray byte_array;

byte_array << 0x01, 0x02, 0x03;
ecl::Converter<int,ByteStencil> toInt;
std::cout << "Conversion: " << toInt(byte_array) << std::endl; // results in 197121
std::cout << "Conversion: " << toInt(byte_array.stencil(0,2)) << std::endl; // only first two bytes -> 513
```



and going the other way, we pass it the byte array for storage when
converting (works on both arrays and stencils)\...



```cplusplus
Array<char,20> byte_array = Array<char,20>::Constant(0x00);
Stencil< Array<char, 20> > stencil = byte_array.stencil(2,4);
ecl::Converter< Stencil< Array<char, 20> >, ecl::int32 > fromInt;
fromInt(stencil, ecl::int32(197121));
std::cout << byte_array << std::endl;    // 0x00, 0x00, 0x01, 0x02, 0x03, 0x00, 0x00, 0x00, ...
std::cout << stencil << std::endl;       // 0x01, 0x02, 0x03, 0x00
```

## Tutorials

- [Arrays](#arrays):
  Introduction to c++ style arrays, both fixed and dynamic.
- [Buffer Overflow Detection](#buffer-overflow-detection):
  Detecting ecl array over/under runs.
- [Fifo](#fifo): A simple first
  in, first out class.
- [Stencils](#stencils):
  Windows onto ecl arrays.
- [Container Utilities](#container-utilities):
  container formatters and converters.
