#include <iostream>
using namespace std;

template <typename T>
void Print(T* arr,int len)
{
	for (int i = 0; i < len; i++)
	{
		cout << arr[i] << "  ";
	}
	cout << endl;
}

template <typename T>
void MySort(T* arr,int len)
{
	for (int i = 0; i < len - 1; i++)
	{
		for (int j = 0; j < len - 1 - i; j++)
		{
			T temp = arr[j];
			if (arr[j] > arr[j + 1])
			{
				temp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = temp;
			}
		}
	}
}

void test01()
{
	int arr1[] = { 2,3,5,4,8,13,12 };
	int len = sizeof(arr1) / sizeof(int);
	Print(arr1,len);
	MySort(arr1, len);
	Print(arr1, len);
	cout << "---------------------" << endl;
	char arr2[] = { 'a','z','b','k' };
	len = sizeof(arr2) / sizeof(char);
	Print(arr2, len);
	MySort(arr2, len);
	Print(arr2, len);
}

int main()
{
	test01();
	return 0;
}