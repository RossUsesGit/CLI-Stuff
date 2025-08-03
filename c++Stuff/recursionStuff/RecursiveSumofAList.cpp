#include <iostream>
#include <vector>
using namespace std;

// Recursive sum of a list in C++

double sumlist(const vector<double>& num_list, size_t index = 0) {
    if (index == num_list.size()) {
        return 0;
    }
    return num_list[index] + sumlist(num_list, index + 1);
}

void get_numbers(int list_length, vector<double>& num_list) {
    if ((int)num_list.size() == list_length) {
        return;
    }

    cout << "Input a number: ";
    double num;
    if (!(cin >> num)) {
        cin.clear();
        cin.ignore(10000, '\n');
        cout << "Invalid number." << endl;
    } else {
        num_list.push_back(num);
    }

    get_numbers(list_length, num_list);
}

int main() {
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

    vector<double> num_list;
    get_numbers(list_length, num_list);

    double total = sumlist(num_list);

    cout << "\nThe total of your numbers is " << total << endl;

    return 0;
}
