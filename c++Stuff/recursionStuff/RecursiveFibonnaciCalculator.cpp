#include <iostream>
using namespace std;

// Recursive Fibonacci Calculator in C++

int fibonacci(int n) {
    if (n <= 0)
        return 0;
    else if (n == 1)
        return 1;
    else
        return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int n;

    while (true) {
        cout << "Enter nth fibonacci number: ";
        if (!(cin >> n)) {
            cin.clear();
            cin.ignore(10000, '\n');
            cout << "Error. Choose an integer." << endl;
            continue;
        }

        if (n < 0) {
            cout << "Error. " << n << " is less than 0. Choose a positive integer." << endl;
        } else {
            break;
        }
    }

    int num = fibonacci(n);
    cout << num << " is the " << n << "th fibonacci number." << endl;

    return 0;
}
