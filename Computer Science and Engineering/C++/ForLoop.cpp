
void forLoopPractice() { // Source: Code at the 2013 June Apple Dev Conference, edited by Instructor Stephen DeSalvo

    /** 1. About size_t
     * When it comes to the for loops that just index a vector, Instructor Stephen DeSalvo suggests using size_t instead of int.
     * The data type size_t is usually equivalent to an unsigned long, but the benefit is that size_t is platform independent.
     * In contrast, the numbers of bytes for an int can differ from computer to computer.
     * **/

    /** 1. About various versions of variable definition when using for loop
     * **/
    // Version 1: variable i declared outside of the loop
    vector<int> a(3,5);
    size_t i=0;
    for(i=0; i<a.size(); ++i) {
        std::cout << i << " " << std::endl;
    } // PROBLEM: variable i still exists after the loop

    // Version 2: variable i is declared inside the loop
    vector<int> a(3,5);
    for(size_t i=0; i<a.size(); ++i) {
        std::cout << i << " " << std::endl;
    } // PROBLEM: a.size() gets called after each iteration in the loop

    // Version 3: create a variable to store a.size()
    vector<int> a(3,5);
    size_t n=a.size();
    for(size_t i=0; i<n; ++i) {
        std::cout << i << " " << std::endl;
    } // PROBLEM: variable n still exists after the loop

    // Version 4: create the variable to store a.size() in the init-statement of for loop
    vector<int> a(3,5);
    for(size_t i=0, n=a.size(); i<n; ++i) {
        std::cout << i << " " << std::endl;
    }

}