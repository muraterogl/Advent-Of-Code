#include <bits/stdc++.h>
using namespace std;
//I know it is terrible but it works

string line;
vector<string> lines;

int main() {
    
    ifstream MyFile("input.txt");
    vector<vector<int>> m;
    vector<vector<int>> seen;
    while(getline(MyFile, line)) {
        vector<int> l;
        vector<int> s;
        lines.push_back(line);
        
        for (int i = 0; i<line.length(); i++) {
            l.push_back((int)line[i]-'0');
            s.push_back(999999999);
        }
        m.push_back(l);
        seen.push_back(s);
        
    }
    
    MyFile.close();
    queue<pair<pair<int,int>,int>> q;
    int endy= m.size()-1;
    int endx = m[0].size()-1;
    q.push({{0,0},0});
    while (!q.empty()) {
        auto b = q.front();
        q.pop();
        auto xy = b.first;
        int l = b.second;
        int y = xy.first;
        int x = xy.second;
        if (l < seen[y][x]) {
            seen[y][x] = l;
            if (x < endx) {
                q.push({{y,x+1},l+m[y][x+1]});
            }
            if (y < endy) {
                q.push({{y+1,x},l+m[y+1][x]});
            }
        }
    }

    cout << "part1: " << seen[endy][endx] << endl;

    vector<vector<int>> m2;
    vector<vector<int>> seen2;

    for (int a = 0; a < 5; a++) {
        for (int y = 0; y < lines.size(); y++) {
            vector<int> l2;
            vector<int> s2;
            for (int b = 0; b < 5; b++) {
                for (int x = 0; x<lines[y].length(); x++) {
                    int risk = ((int)lines[y][x]-'0'+b+a)%9;
                    if (risk==0) risk =9;
                    l2.push_back(risk);
                    s2.push_back(999999999);
                }
            }
            m2.push_back(l2);
            seen2.push_back(s2);
        }
        
    }
    
    int endy2= m2.size()-1;
    int endx2 = m2[0].size()-1;
    q.push({{0,0},0});
    while (!q.empty()) {
        auto b = q.front();
        q.pop();
        auto xy = b.first;
        int l = b.second;
        int y = xy.first;
        int x = xy.second;
        if (l < seen2[y][x]) {
            seen2[y][x] = l;
            if (x < endx2) {
                q.push({{y,x+1},l+m2[y][x+1]});
            }
            if (x > 1) {
                q.push({{y,x-1},l+m2[y][x-1]});
            }
            if (y < endy2) {
                q.push({{y+1,x},l+m2[y+1][x]});
            }
            if (y > 1) {
                q.push({{y-1,x},l+m2[y-1][x]});
            }
        }
    }
    cout << "part2: " << seen2[endy2][endx2] << endl;
    return 0;
}