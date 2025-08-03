#include <iostream> 

using namespace std;


float ktof (float kelvin){

    return (kelvin - 273.15) * (1.8) + 32;

}

int main(){

    float kelvin;

    cout << "Kelvin: ";
    cin >> kelvin;
    
    float fahrenheit = ktof(kelvin);

    
    cout << "Fahrenheit: " << fahrenheit;

    return 0;
}
