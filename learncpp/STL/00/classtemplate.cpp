// A class template working with a function template.
#include <iostream>
using namespace std;
#include <vector>

template <typename T>
T square(T x)
{
    return x*x;
}

template <typename T>
class BoVector
{
    int size;
    T arr[1000];
public:
    BoVector():size(0){};
    void push(T x)
    {
       arr[size]=x;
       size++; 
    }
    int getsize(){return size;}
    T get(int i){return arr[i];}
    void print()
    {
        for(int i=0;i<size;i++)
        {
            cout<<arr[i]<<endl;
        }
    }
};

template <typename T>
BoVector<T> operator*(BoVector<T>& bv1,BoVector<T>& bv2)
{
    BoVector<T> ret;
    for(int i=0;i<bv1.getsize();i++)
    {
        ret.push(bv1.get(i)*bv2.get(i));
    }
    return ret;
}

int main()
{
    BoVector<int> bv; //The data type of T must be specified here.
    bv.push(2);
    bv.push(21);
    bv.push(32);
    bv.push(43);
    bv.print();
    cout<<bv.getsize()<<endl;
    cout<<bv.get(3)<<endl;
    cout<<square(8)<<endl;
    cout<<"The square of bv:"<<endl;
    bv=square(bv);  //invoke the square function with the datatype of BoVector,return bv*bv,this will invoke the operator* we defined for bovector.
    bv.print();
    return 0;
}