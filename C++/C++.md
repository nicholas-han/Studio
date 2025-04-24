# C++




## C++ Topics
### Entry-Level Questions
1. Difference between pointer and reference?
2. Which one is better, i++ or ++i?
3. Why to use virtual destructor?
4. What is the signature of a copy constructor or assignment operator?
5. How to specialize a class template?
6. What are the four types of casts in C++? What are the usages?

### Algorithm Questions
Complexity of data structures in Standard Template Library and their implementation.

1. What does reserve() do on std::vector?
2. What is the complexity of adding element to a  std::vector?
3. Underlying data structure of std::map/std::unordered_map?
4. Implementation outline.
5. K-way merge sort.
6. How would you implement atoi and itoa functions?
7. Max sum subarray problem.
8. How to compute max drawdown of a price time series? 

### Advanced Questions
#### C++ Standard Library
Realizations: GC, SGI, Clang. The realization of Clang is clear. If you use GCC compiler, understanding the realization of GCC is beneficial for effectively utilizing STL containers.
Common C++ build systems include Make、CMake、Automake、scons、Visual Studio.
#### C++11 Features
move sematic, rvalue reference, range based for loop, override keyword, static  assert, initializer list, lambda

1. What is strong exception guarantee? Cost of exception handling? Why?
2. C++11 deprecate exception specification?
3. What is type trait?
4. What is smart pointer? Difference between std::shared_ptr and  boost::instrusive_ptr? Implementation outline.
5. How is virtual function call implemented? What is the cost of virtual function calls?
6. What is CRTP? What is the limitation of that?
7. What is the runtime cost of a lambda function?
8. What is the cost of std::function compare to a function pointer?
9. What does std::function gain from that cost?

### Reference
- **Books**: Effective Modern C++, Effective ST
- **Debugging/Profiling Tools**: Valgrind, memcheck, Cachegrind, gprof, OProfile
- **Cmake**: https://cmake.org/cmake/help/v2.8.8/cmake.html
- **Shared_ptr**: https://www.boost.org/doc/libs/1_55_0/libs/smart_ptr/shared_ptr.htm
- https://www.boost.org/doc/libs/1_55_0/doc/html/circular_buffer.html
