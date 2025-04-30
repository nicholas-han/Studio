#include <iostream>

int main() {
    int i=2, &r1=i;
    double d=4.5, &r2=d;    
    std::cout << i << " " << r1 << "; " << d << " " << r2 << std::endl;

    r2 = 3.14159; // (a)
    std::cout << i << " " << r1 << "; " << d << " " << r2 << std::endl;
    r2 = r1; // (b)
    std::cout << i << " " << r1 << "; " << d << " " << r2 << std::endl;
    i = r2; // (c)
    std::cout << i << " " << r1 << "; " << d << " " << r2 << std::endl;
    r1 = d; // (d)
    std::cout << i << " " << r1 << "; " << d << " " << r2 << std::endl;

    std::cout << /* "*/" /* "/*" */ << std::endl;
    // int ii = 09;
    return 0;
}
