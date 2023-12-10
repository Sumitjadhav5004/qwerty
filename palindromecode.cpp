#include <iostream>
#include <stack>
using namespace std;

void reverseSent(string s) {
    stack<string> st;
    for (int i = 0; i < s.length(); i++) {
        string word = "";
        while (s[i] != ' ' && i < s.length()) {
            word += s[i];
            i++;
        }
        st.push(word);
    }

    while (!st.empty()) {
        cout << st.top() << " ";
        st.pop();
    }
    cout << endl;
}

bool isPalindrome(string s) {
    int left = 0, right = s.length() - 1;
    while (left < right) {
        if (s[left] != s[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main() {
    string s;
    cout<<"Enter a string : "<<endl;
    cin>>s;
    
    
    // Reverse the sentence
    cout << "Reversed Sentence: ";
    reverseSent(s);

    // Check if the sentence is a palindrome
    if (isPalindrome(s)) {
        cout << "The sentence is a palindrome." << endl;
    } else {
        cout << "The sentence is not a palindrome." << endl;
    }

    return 0;
}
