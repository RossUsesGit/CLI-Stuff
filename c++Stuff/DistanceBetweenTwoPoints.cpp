#include <iostream>
#include <cmath>

using namespace std;



float disttwop(float x1, float x2, float y1, float y2){

    return sqrt((pow(x2-x1,2)) + pow(y2-y1,2));

}


int main(){


    float x1,x2,y1,y2;

    cout << "x1: ";
    cin >> x1;
    cout << endl;

    cout << "y1: ";
    cin >> y1;
    cout << endl;

    cout << "x2: ";
    cin >> x2;
    cout << endl;

    cout << "y2: ";
    cin >> y2;
    cout << endl;

    float ans = disttwop(x1,x2,y1,y2);

    cout << "The distance between the 2 points is: " << ans;

    return 0;





}
