## Compiling & Linking

Include the following at the top of any translation unit:



```cplusplus
#include <ecl/mpl.hpp>

// The concept definition/validation classes.
using ecl::Bool;        // compile time logic testing of template parameters
using ecl::enable_if;   // selective specialisation of classes via the template parameters   
using ecl::Unsigned;    // type converters
```



## Tutorials

- [Boolean Logic](#boolean-logic) :
  using compile time boolean types for metaprogramming.
- [Enable If](#enable-if) : an if
  operator for template type arguments.
- [Converters](#converters) : compile
  time type converters.

## Boolean Logic

- **Description:** Using compile time boolean types for metaprogramming.
- **Tutorial Level:** INTERMEDIATE

### Overview

It provides a compile-time boolean type used to make logical inferences
in the template parameters supplied to template classes. It is often
used in the is_such_and_such_class traits testing classes (there are
some in [ecl_traits](ecl_traits)).

### Usage



```cplusplus

#include <ecl/mpl/bool.hpp>

// Parent template which defaults to false
template <typename T>
class is_foo_bar : public ecl::False {}; 

// Specialisations (in this case, class Tango) for which it is true
template <>
class is_foo_bar< Tango > : public ecl::True {}; 

// A class that will use it
template <bool B = false>
class Cash {
    static void says() {
        std::cout << "Cash is fine." << std::endl;
    }
};

// specialisation of that class for true
template <>
class Cash <true> {
    static void says() {
        std::cout << "Cash is foobar too." << std::endl;
    }
};

int main() {
    Cash<is_foo_bar<Tango>::value>::says(); // Cash is foobar too...
    return 0;
}
```

## Enable If

- **Description:** An if operator for template type arguments.
- **Keywords:** ecl mpl
- **Tutorial Level:** INTERMEDIATE

### Usage

These allow you to various compile tricks with SFINAE (Substitution
Failure Is Not An Error). One usage case is to eliminate template
instantiations for any type you do not wish to explicitly support.



```cplusplus
// This will instantiate if it is anything except float or double.
template <typename T, typename Enable = void>
class TestObject {
public:
    bool isFloatSpecialisation() { return false; }
};

// This specialisation will instantiate it T is float or double.
template <typename T>
class TestObject< T, typename enable_if< is_float<T> >::type > { 
public:
    bool isFloatSpecialisation() { return true; }
};
```



### Reporting Errors at Compile Time

`FailedObject` is a simple class that guarantees a compile time
failure if an attempt to instantiate it is made (private constructor).
This is useful in tandem with the if function to report bad
instantiations.

For example, the parent template definition above could be instead:



```cplusplus
#include <ecl/mpl/failed_object.hpp>

template <typename T, typename Enable = void>
class TestObject : public ecl::FailedObject {};
```

## Converters

- **Description:** Compile time type converters.
- **Keywords:** ecl converters
- **Tutorial Level:** INTERMEDIATE

### Usage

Convert from one type to another in compile time. Currently there is
only the unsigned type converter.



```cplusplus
char c = 0x33;
Unsigned<char>::type uc = 0x03;
```



That example is trivial, but is more useful when using it for template
arguments in a class.



```cplusplus
template <typename T>
class Foo {
private:
    Unsigned<T>::type my_unsigned_variable;    
};
```

## Tutorials

- [Boolean Logic](#boolean-logic):
  Using compile time boolean types for metaprogramming.
- [Converters](#converters): Compile
  time type converters.
- [Enable If](#enable-if): An if
  operator for template type arguments.
