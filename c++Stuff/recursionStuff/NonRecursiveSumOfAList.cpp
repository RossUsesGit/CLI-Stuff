#include <iostream>
#include <vector>
using namespace std;

// Non-Recursive Sum of a List Calculator in C++

double sumlist(const vector<double>& num_list) {
    double total = 0;
    for (double num : num_list) {
        total += num;
    }
    return total;
}

int main() {
    vector<double> num_list;
    int list_length;

        while (true) {
        cout << "How many numbers are you going to add?: ";
        if (!(cin >> list_length)) {
            cin.clear();
            cin.ignore(10000, '\n');
            cout << "Invalid number." << endl;
            continue;
        }
        break;
    }

      while (true) {
        try {
            if (num_list.size() == (size_t)list_length)
                break;

            cout << "Input a number: ";
            double num;
            if (!(cin >> num)) {
                cin.clear();
                cin.ignore(10000, '\n');
                throw invalid_argument("Invalid number.");
            }
            num_list.push_back(num);
        }
        catch (const invalid_argument& e) {
            cout << e.what() << endl;
        }
    }

    double total = sumlist(num_list);

    cout << "\nThe total of your numbers is " << total << endl;

    return 0;
}
