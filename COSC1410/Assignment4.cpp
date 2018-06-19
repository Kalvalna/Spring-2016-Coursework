#include <iostream>
#include <time.h>
using namespace std;

// Function that initializes random integers from 0 to 99 to each element in the array
void initializeArray(int numbers[])
{
	// Call to predefined functions srand and time
	srand(time(NULL));
	// Loop that assigns a random integer from 0 to 99 to an element in the array
	for (int i = 0; i < 10; i++)
	{
		numbers[i] = rand() % 100;
	}
}

// Function that sorts the indexes array that corresponds to the values of the numbers array in ascending order
void indexSort(int numbers[], int indexes[])
{
	// Creates a new array
	int *ptr = new int[10];
	// Initializes the variable temp
	int temp;
	// Loop that copies elements of numbers array to newly created array
	for (int i = 0; i < 10; i++)
	{
		ptr[i] = numbers[i];
	}
	// Loop that sorts the newly created array in ascending order
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			if (ptr[i] < ptr[j])
			{
				temp = ptr[i];
				ptr[i] = ptr[j];
				ptr[j] = temp;
			}	
		}
	}
	// Loop that compares values from the sorted array that was created and the original numbers array
	for (int i = 0; i < 10; i++)
	{
		for (int j = 0; j < 10; j++)
		{
			// Checks if both values are equal. If equal, assigns index value to the indexes array
			if (ptr[i] == numbers[j])
				indexes[i] = j;
		}
	}
	// Deletes created array and deallocates the memory
	delete[]ptr;
}

int main()
{
	// Declare variables
	int numbers[10], indexes[10];
	// Randomly initialize the array numbers
	initializeArray(numbers);
	// Initialize the array indexes
	for (int i = 0; i<10; i++)
		indexes[i] = i;
	// Display the arrays before the sorting
	cout << "numbers:";
	for (int i = 0; i<10; i++)
		cout << numbers[i] << " ";
	cout << "\nindexes:";
	for (int i = 0; i<10; i++)
		cout << indexes[i] << " ";
	// Sort the array
	indexSort(numbers, indexes);
	// Display the arrays after the sorting
	cout << "\n*****************************\n";
	cout << "numbers:";
	for (int i = 0; i<10; i++)
		cout << numbers[i] << " ";
	cout << "\nindexes:";
	for (int i = 0; i<10; i++)
		cout << indexes[i] << " ";
	return 0;
}