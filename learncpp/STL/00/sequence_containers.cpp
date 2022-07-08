//vector, deque, list, forward list, array(array and linked list)  sequence containes
// set, multiset, map, multimap(binary tree)  associative containers
// unorder set/multiset, unordered map/mutimap(hash table)  unorderd containers
#include <iostream>
using namespace std;
#include <vector>
#include <deque>
#include <list>
#include <algorithm>
int main()
{
    vector<int> v1;
    v1.push_back(3);
    v1.push_back(5);
    v1.push_back(23);
    v1.push_back(31);
    v1.push_back(13);
    cout<<v1[2]<<endl;  //23 (no range check)
    cout<<v1.at(2)<<endl;   //23 (throw a range_error exception of out of range)
    //cout<<v1.at(10)<<endl;    //throw an exception
    vector<int>::iterator itr1=v1.begin();
    vector<int>::iterator itr2=v1.end();
    for(vector<int>::iterator itr=itr1;itr!=itr2;itr++)     //half-open:[begin,end)
    {
        cout<<*itr<<"  "<<endl;
    }
    sort(v1.begin(),v1.end());      //Algotithms don't work on containers directly,they worked on iterator.
    cout<<"after sort:"<<endl;
    for(vector<int>::iterator itr=itr1;itr!=itr2;itr++)
    {
        cout<<*itr<<"  "<<endl;
    }

    //vector:
    // 1.fast insert/remove at the end O(1);
    // 2.slow insert/remoce at the end/middle O(n);
    // 3.slow search O(n);

    deque<int> de;
    de.push_back(23);
    de.push_back(3);
    de.push_back(2);
    de.push_back(45);
    de.push_front(43);
    //deque:
    //1.fast insert/remove at the beginning/end;
    //2.slow insert/remove at the middle;
    //3.slow search;

    cout<<"list test:"<<endl;
    list<int> mylist;
    mylist.push_back(3);
    mylist.push_back(4);
    mylist.push_back(5);
    mylist.push_front(12);
    mylist.push_back(21);  //{12,3,4,5,21}

    list<int>::iterator itr=find(mylist.begin(),mylist.end(),4);
    mylist.insert(itr,56);  //{12,3,56,4,5,21}
    itr++;
    mylist.erase(itr);  //{12,3,56,4,21}
    for(list<int>::iterator itr=mylist.begin();itr!=mylist.end();itr++) 
    {
        cout<<*itr<<"  ";
    }
    cout<<endl;
    //list
    // 1.fast insert/remove at anyplace.
    // 2.slow search.
    // 3.no random access,no [] operator.
    return 0;
}
