#include <bits/stdc++.h>
using namespace std;

string line;
vector<string> lines;

int main() {
    
    ifstream MyFile("input.txt");
    while(getline(MyFile, line)) {
        lines.push_back(line);
    }
    MyFile.close();
    unordered_map<string, vector<string>> m;
    for (string line : lines) {
        string a = line.substr(0, line.find('-'));
        string b = line.substr(line.find('-')+1, line.length());
        m[a].push_back(b);
        m[b].push_back(a);
    }
    vector<vector<string>> result;
    stack<vector<string>> s;
    s.push(vector<string>{"start"});
    while (!s.empty()) {
        vector<string> currentPath = s.top();
        s.pop();
        if (currentPath.back() == "end") {
            result.push_back(currentPath);
            continue;
        }
        unordered_set<string> visited;
        bool ok = true;
        for (auto i=currentPath.begin(); i != currentPath.end(); i++) {
            if ((*i)[0] >= 97) {
                //small cave
                if (visited.find(*i) != visited.end()) {
                    ok = false;
                    break;
                }
                visited.insert(*i);
            }
        }
        if (ok) {
            for (auto i=m[currentPath.back()].begin(); i!=m[currentPath.back()].end(); i++) {
                vector<string> newPath {currentPath};
                newPath.push_back(*i);
                s.push(newPath);
            }
        }
    }
    cout << "part1: " << result.size() << endl;


    result = {};
    s.push(vector<string>{"start"});
    while (!s.empty()) {
        vector<string> currentPath = s.top();
        s.pop();
        if (currentPath.back() == "end") {
            result.push_back(currentPath);
            continue;
        }
        unordered_map<string, int> visited;
        bool ok = true;
        int moreThanOneVisitedCount = 0;
        for (auto i=currentPath.begin(); i != currentPath.end(); i++) {
            if ((*i)[0] >= 97) {
                //small cave
                visited[*i]++;
                if (visited[*i]>1) moreThanOneVisitedCount++;
                if ((*i=="start" && visited[*i]>1) || 
                    (*i=="end" && visited[*i]>1) ||
                    moreThanOneVisitedCount>1){
                        ok = false;
                        break;
                    }
            }
        }
        if (ok) {
            for (auto i=m[currentPath.back()].begin(); i!=m[currentPath.back()].end(); i++) {
                vector<string> newPath {currentPath};
                newPath.push_back(*i);
                s.push(newPath);
            }
        }
    }
    cout << "part2: " << result.size() << endl;
    return 0;
}