#include <iostream>

using namespace std;

int main(){

float x,y,temp;

cout << "Enter x: ";
cin >> x;
cout << "Enter y: ";
cin >> y;

temp = x;
x = y;
y = temp;


cout << "x = " << x << " || " << "y = " << y;

}
