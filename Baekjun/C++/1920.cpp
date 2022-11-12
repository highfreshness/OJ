#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int n;
    cin >> n;
    vector<int> v;
    for(int i=1; i<=n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    int m;
    cin >> m;
    sort(v.begin(),v.end());
    while(m--){
        int s = 0, e = v.size() - 1;
        int key;
        bool check = false;
        cin >> key;
        while(s <= e) {
            int mid = (s + e) / 2;
            if(v[mid] > key){
                e = mid - 1;
            }
            else if(v[mid] < key){
                s = mid + 1;
            }
            else {
                check = true;
                break;
            }
        }
        cout << (check == true ? 1 : 0) << '\n';
    }

}
