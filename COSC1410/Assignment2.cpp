/*	Assignment 2: Basic Login Process Simulator */

#include <iostream>			
#include <string>
using namespace std;

// Function for determining if a character is a number
bool isNumber(char n)				
{
	return n >= '0' && n <= '9';
}

// Function for determining if the username is six digits
bool isSixDigits(string username)	
{
	return username.size() == 6;
}

// Function for determining if the password is four digits
bool isFourDigits(string password)	
{
	return password.size() == 4;
}

// Function that determines if all characters in the username and password are strings
bool allNumbers(string input)		
{
	int length = input.size();
	for (int i = 0; i <= length - 1; i++)
	{
		if (input.at(i) = !isNumber(input.at(i)))
			return false;
	}
}

int main()
{
	// Declaring the variables and initializing the temporary password as 1234
	string username, password, usernameCheck, passwordCheck;		
	string tempPw = "1234";									

	// For loop that determines if username is valid and password matches temporary password
	for (int i = 1; i <= 3; i++)
	{
		// Username and password input prompts
		cout << "Please enter a six digit username: ";
		cin >> username;
		cout << "Please enter the temporary password (1234): ";
		cin >> password;

		// Checks if username and password fulfills all of the conditions
		if (!isSixDigits(username) || allNumbers(username) == false || !isFourDigits(password) || allNumbers(password) == false || password != tempPw)
		{
			// Error message that displays number of failed attempts
			if (i <= 2)
			{
				cout << "Invalid credentials. Program terminates after 3 failed attempts. Number of failed attempts: " << i << endl;
				// Dashed line to separate inputs and makes it easier to read text on screen
				cout << "---------------------------------------------------------------------------\n\n";
			}

			// Error message for the third failed attempt that terminates the program
			else
			{
				cout << "Invalid credentials. Program terminates after 3 failed attempts. Number of failed attempts: " << i << endl;
				cout << "You cannot access the system. Terminating the program" << endl;
				// Dashed line to separate inputs and makes it easier to read text on screen
				cout << "---------------------------------------------------------------------------\n\n";		
				return 0;
			}
		}

		// Breaks out of loop if username and password are accepted
		else
		{
			break;
		}
	}

	// Dashed line to separate inputs and makes it easier to read text on screen
	cout << "---------------------------------------------------------------------------\n\n";

	// Successful login display message
	cout << "Login successful. Please enter new password." << endl;

	// While loop that continues until user inputs a valid password
	while (!isFourDigits(password) || allNumbers(password) == false || password == tempPw)
	{
		// Dashed line to separate inputs and makes it easier to read text on screen
		cout << "---------------------------------------------------------------------------\n\n";
		// New password input prompt
		cout << "New password must be 4 digits and different from the temporary password." << endl;
		cout << "New Password: ";
		cin >> password;
	}

	// Dashed line to separate inputs and makes it easier to read text on screen
	cout << "---------------------------------------------------------------------------\n\n";

	// For loop for logging in that determines if the username and password match what is stored
	for (int i = 1; i <= 3; i++)
	{
		// Login prompt
		cout << "Username: ";
		cin >> usernameCheck;
		cout << "Password: ";
		cin >> passwordCheck;

		// Checks if the username and password match what is stored
		if (usernameCheck != username || passwordCheck != password)
		{
			// Error message that displays number of failed attempts
			if (i <= 2)
			{
				cout << "Invalid credentials. Program terminates after 3 failed attempts. Number of failed attempts: " << i << endl;
				// Dashed line to separate inputs and makes it easier to read text on screen
				cout << "---------------------------------------------------------------------------\n\n";
			}
			// Error message for the third failed attempt that terminates the program
			else
			{
				cout << "Invalid credentials. Program terminates after 3 failed attempts. Number of failed attempts: " << i << endl;
				cout << "You cannot access the system. Terminating the program" << endl;
				// Dashed line to separate inputs and makes it easier to read text on screen
				cout << "---------------------------------------------------------------------------\n\n";
				return 0;
			}
		}

		// Breaks out of loop if username and password are the same as what is stored
		else
		{
			break;
		}
	}
	
	// Dashed line to separate inputs and makes it easier to read text on screen
	cout << "---------------------------------------------------------------------------\n\n";
	// Access granted message
	cout << "Access granted." << endl;

	// Program termination
	return 0;
}


/*
Your program is not working unless you comment all conditions related to the function "allNumbers(string)"﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿﻿ inside if statements.
*/