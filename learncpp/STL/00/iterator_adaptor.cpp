#include <iostream>
using namespace std;
#include <vector>
#include <algorithm>
// 1.insert iterator
// 2.stream iterator
// 3.reverse iterator
// 4.move iterator (c++ 11)
int main()
{
    vector<int> v1 = {2, 3, 6, 8};
    vector<int> v2 = {13, 15, 23};
    vector<int>::iterator it = find(v1.begin(), v1.end(), 3);

    return 0;
}