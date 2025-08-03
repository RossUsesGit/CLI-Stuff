#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

// This is an activity I submitted in a course.

class Triangle {
private:
    double totalAngle, angleA, angleB, angleC;
    double sideA, sideB, sideC;

public:

    Triangle(double A, double B, double C);
    void setAngles(double A, double B, double C);
    const bool validateTriangle();
    void setSides(double A, double B, double C);
    double calculatePerimeter();
    double calculateArea();
    const string triangleType();
};

int main() {
    
    Triangle set1(90,60,30);
    set1.setSides(5,8.66,10);

    if (set1.validateTriangle()) {

        double perimeter = set1.calculatePerimeter();
        double area = set1.calculateArea();
        string type = set1.triangleType();
        cout << "The shape is a valid triangle.\n";
        cout << "The perimeter of the given triangle is: " << perimeter << endl;
        cout << "The area of the given triangle is: " << area << endl;
        cout << "The triangle is a/an " << type << " triangle.";
    } 
    
    else {
        cout << "The shape is NOT a valid triangle.\n";
    }

    return 0;
}

Triangle::Triangle(double A, double B, double C) {
    angleA = A;
    angleB = B;
    angleC = C;
    totalAngle = A + B + C;
}

void Triangle::setAngles(double A, double B, double C) {
    angleA = A;
    angleB = B;
    angleC = C;
    totalAngle = A + B + C;
}

const bool Triangle::validateTriangle() {
    return (totalAngle == 180);
}

void Triangle::setSides(double A, double B, double C){

    sideA = A;
    sideB = B;
    sideC = C;

}

double Triangle::calculatePerimeter(){

    return sideA + sideB + sideC;
}

double Triangle::calculateArea(){

    double s = (sideA + sideB + sideC) / 2;
    return sqrt(s*(s-sideA)*(s-sideB)*(s-sideC));
}

const string Triangle::triangleType(){

    double a = sideA, b = sideB, c = sideC;

   
    if (a > c) swap(a, c);
    if (b > c) swap(b, c);

    double a2 = pow(a, 2);
    double b2 = pow(b, 2);
    double c2 = pow(c, 2);

    if (fabs(c2 - (a2 + b2)) < 1e-6)
        return "Right";
    else if (c2 < a2 + b2)
        return "Acute";
    else
        return "Obtuse";
}



