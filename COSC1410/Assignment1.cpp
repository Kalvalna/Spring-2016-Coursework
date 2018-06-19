/*	Assignment 1: Conversion of inches and centimeters	*/

#include <iostream>
using namespace std;

int main()
{
	// Initializing the variables
	int input = 0;
	double inch = 0;
	double centi = 0;

	// Selection prompt
	cout << "1: Inch to Centimeter conversion" << endl;
	cout << "2: Centimeter to Inch conversion" << endl;
	cout << "Please select the desired conversion: ";
	cin >> input;
	
	// Inches to centimeters conversion
	if (input == 1)
	{
		// Prompt for inputting inches
		cout << "Please enter the value of inches to convert: ";
		cin >> inch;

		// Conversion of inch to centimeters if input is valid
		if (inch > 0)
		{
			cout << inch << " inches = " << inch * 2.54 << " centimeters" << endl;
		}
		
		// If input is invalid for inches, give an error message
		else 
		{
			cout << "Invalid input. Please enter a positive number." << endl;
		}
	}

	// conversion of centimeters to inches 
	else if (input == 2)
	{
		// Prompt for inputting centimeters
		cout << "Please enter the value of centimeters to convert: ";
		cin >> centi;

		// Conversion of centimeters to inches if input is valid
		if (centi > 0)
		{
			cout << centi << " centimeters = " << centi / 2.54 << " inches" << endl;
		}

		// If input is invalid for centimeters, give an error message
		else
		{
			cout << "Invalid input. Please enter a positive number." << endl;
		}
	}

	// If input is not one of the options, give an error message
	else 
	{
		cout << "Invalid input. Please make a valid selection." << endl;
	}

	// Program termination
	return 0;
}