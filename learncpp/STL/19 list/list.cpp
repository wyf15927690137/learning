#include <iostream>
using namespace std;
#include <list>

void test01()
{
    list<int> mlist1(5, 6); // 5个6
    list<int> mlist2(mlist1);
    list<int> mlist3(mlist2.begin(), mlist2.end());
    for (list<int>::iterator it = mlist3.begin(); it != mlist3.end(); it++)
    {
        cout << *it << " ";
    }
    cout << endl;
    cout << "--------------------------" << endl;
}

void test02()
{
    list<int> mlist;
    mlist.push_back(10);
    mlist.push_back(20);
    mlist.push_front(10);
    mlist.insert(mlist.begin(), 5);
    mlist.insert(mlist.end(), 55);
    mlist.remove(20);
    for (list<int>::iterator it = mlist.begin(); it != mlist.end(); it++)
    {
        cout << *it << "  ";
    }
    cout << endl;
    list<int>::iterator it = mlist.begin();
    list<int>::iterator it1 = ++mlist.begin(); // it1++ 合法，it1+num是不合法的
    mlist.erase(it, ++it1);                    //删除迭代器之间的元素，[)
    for (list<int>::iterator it = mlist.begin(); it != mlist.end(); it++)
    {
        cout << *it << "  ";
    }
    cout << endl;
    cout << "--------------------------" << endl;
}

void test03()
{
    list<int> mlist;
    mlist.push_back(34);
    mlist.push_back(24);
    mlist.push_back(67);
    mlist.push_back(57);
    list<int> mlist1;
    mlist1.push_front(15);
    mlist1.push_front(25);
    mlist1.swap(mlist); // swap two lists

    for (list<int>::iterator it = mlist1.begin(); it != mlist1.end(); it++)
    {
        cout << *it << "  ";
    }
    cout << endl;

    mlist1.sort(); // sort() function只支持可以随机访问的容器，因此list容器要用自己的sort
    for (list<int>::iterator it = mlist1.begin(); it != mlist1.end(); it++)
    {
        cout << *it << "  ";
    }
    cout << endl;

    mlist1.reverse();
    for (list<int>::iterator it = mlist1.begin(); it != mlist1.end(); it++)
    {
        cout << *it << "  ";
    }
    cout << endl;
}

int main()
{
    test01();
    test02();
    test03();
    return 0;
}