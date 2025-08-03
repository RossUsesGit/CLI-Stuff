#include <iostream>

using namespace std;

int main(){

float quizscore;
float total;

for(int i = 0; i < 3; i++){
    
cout << "Enter your quiz score: ";
cin >> quizscore;
total += quizscore;

}

float average = total/3;

cout << endl;
cout << "The total of your three quiz scores is: " << total << endl;
cout << "The average of your three quiz scores is: " << average;

return 0;

}
