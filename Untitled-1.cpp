#include <iostream>
#include <array>

using namespace std;

string elem[] = {"b", "c", "f", "h", "i", "k", "n", "o", "p", "s", "u", "v", "w", "y", "ac", "ag", "al", "am", "ar", "as", "at", "au", "ba", "be", "br", "ca", "cd", "ce", "cl", "cm", "cr", "db", "ds", "dy", "er", "es", "eu", "fe", "fl", "fm", "fr", "ga", "gd", "ge", "he", "hg", "ir", "kr", "la", "li", "lr", "lu", "lv", "md", "mg", "mn", "mo", "mt", "na", "nd", "ne", "pa", "pd", "pm", "pr", "pt", "ra", "rb", "re", "rf", "rg", "rh", "rn", "ru", "se", "sg", "sm", "sr", "ta", "tb", "tc", "te", "th", "ti", "tl", "tm", "xe", "zn", "zr"};

void solve(string word) {
    int n = word.size();
    bool pog[n];
    for (int i=0;i<n;i++) pog[i] = false;

    for (int i=0;i<n;i++) {
        for (auto e : elem) {
            if (e.size() <= i+1) {
                if (e.size()-1) {
                    if (e[1] == word[i] && e[0] == word[i-1] && (pog[i-2] || i == 1)) {
                        pog[i] = true;
                        continue;
                    }
                }
                else {
                    if (e[0] == word[i] && (pog[i-1] || i == 0)) {
                        pog[i] = true;
                        continue;
                    }
                }
            
            }
        }
    }
    if (pog[n-1]) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    int cases;
    string word;
    cin >> cases;

    for (int i = 0;i<cases;i++) {
        cin >> word;
        solve(word);
    }
    return 0;
}