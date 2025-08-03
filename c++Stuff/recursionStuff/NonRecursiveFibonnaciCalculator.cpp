#include <iostream>
using namespace std;

// Non Recursive Fibonnaci Calculator in C++

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

    int num1 = 0;
    int num2 = 1;

    for (int i = 0; i < n; i++) {
        int temp = num2;
        num2 = num1 + num2;
        num1 = temp;
    }

    cout << num1 << " is the " << n << "st/nd/th fibonacci number." << endl;


    return 0;
}

