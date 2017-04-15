#include <iostream>
#include <queue>
using namespace std;

const int maxn = 10000;

int main() {
    priority_queue<int, vector<int>, less<int> > pLess;
    priority_queue<int, vector<int>, greater<int> > pGreater;
    int n, data;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> data;
        pLess.push(data);
        pGreater.push(data);
    }
    for (int i = 0; i < n; i++) {
        cout << pLess.top() << ' ';
        pLess.pop();
    }
    cout << endl;
    for (int i = 0; i < n; i++) {
        cout << pGreater.top() << ' ';
        pGreater.pop();
    }
    cout << endl;

}
