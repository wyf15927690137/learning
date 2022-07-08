#include <iostream>
using namespace std;

template <typename T>
class MyArray
{
public:
    MyArray(int capacity)
    {
        this->mCapacity = capacity;
        this->mSize = 0;
        this->pAddr = new T[this->mCapacity];
    }

    MyArray(const MyArray<T> &arr)
    {
        this->mCapacity = arr.mCapacity;
        this->mSize = arr.mSize;
        this->pAddr = new T[this->mCapacity];
        for (int i = 0; i < mSize; i++)
        {
            this->pAddr[i] = arr.pAddr[i];
        }
    }
    MyArray<T> &operator=(MyArray<T> &arr)
    {
        if (this->pAddr != nullptr)
            delete[] this->pAddr;
        this->mCapacity = arr.mCapacity;
        this->mSize = arr.mSize;
        this->pAddr = new T[this->mCapacity];
        for (int i = 0; i < mSize; i++)
        {
            this->pAddr[i] = arr[i];
        }
        return *this;
    }

    T operator[](int size)
    {
        return *(this->pAddr + size);
    }

    void PushBack(T &data)
    {
        if (this->mSize == this->mCapacity)
            return;
        *(this->pAddr + mSize) = data;
        this->mSize++;
    }

    void PushBack(T &&data)
    {
        if (this->mSize == this->mCapacity)
            return;
        *(this->pAddr + mSize) = data;
        this->mSize++;
    }

    void show()
    {
        for (int i = 0; i < this->mSize; i++)
        {
            cout << this->pAddr[i] << "  ";
        }
        cout << endl;
    }

public:
    int mCapacity;
    int mSize;
    T *pAddr;
};

void test01()
{
    MyArray<int> arr1(10);
    arr1.PushBack(12);
    int a = 3;
    int b = 9;
    int c = 20;
    arr1.PushBack(a);
    arr1.PushBack(b);
    arr1.PushBack(c);
    arr1.show();

    MyArray<int> arr2 = arr1;
    arr2.show();
    MyArray<int> arr3(arr1);
    arr3.PushBack(45);
    arr3.show();
}

class Person
{
};
void test02()
{
    Person p1, p2;
    MyArray<Person> arr(10);
    arr.PushBack(p1);
    arr.PushBack(p2);
}
int main()
{
    test01();
    return 0;
}