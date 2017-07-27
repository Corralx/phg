# Platform Header Generator

## About

PHG is a simple python script used to generate a set of useful macros used throughout all my projects, personalized with a custom prefix.

**NOTE:** All the macros are always defined so that they can be used as constant expressions in your code.

### Features

* Platform macros to distinguish Windows, Linux, macOS, iOS and Android
* Compiler macros to distinguish MSVC, GCC, Clang
* Architecture macros ti distinguish 64-bit and 32-bit targets
* Visibility macros to correctly export functions/classes from a dynamic library
* Utility macros for local declarations, unused variables or parameters, and asserts
* Features checking macro to conditionally enable custom features

## Future Work

* Write a proper help/usage message
* Add an usage example
* Report compiler version
* Support ARM architecture

## License

It is licensed under the very permissive [MIT License](https://opensource.org/licenses/MIT).
For the complete license see the provided [LICENSE](https://github.com/Corralx/phg/blob/master/LICENSE.md) file in the root directory.

## Thanks

[Valentino "xpicox" Picotti](https://github.com/xpicox) for the *\_IF\_FEATURE macro trick.