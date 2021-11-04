#include <iostream>

int main() {    
    char shell[1000];
    
    while (true) {
        std::cout << "x_lang > ";
        std::cin >> shell;
        std::cout << "Output: " << shell << std::endl;
    }

    return 0;
}