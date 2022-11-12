#include <bits/stdc++.h>
using namespace std;

bool compare(int a, int b){
    return a > b;
}

// 10으로 나눌 때 마다 몫과 나머지를 이용해 자릿수를 표현할 수 있게됨
int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    vector<int> arr;

    int n;
    cin >> n;

    while(n){
        arr.push_back(n%10);
        n /= 10; 
    }

    sort(arr.begin(), arr.end(), compare);
    
    for(int i=0; i<arr.size(); i++){
        cout << arr[i]; 
    }
}