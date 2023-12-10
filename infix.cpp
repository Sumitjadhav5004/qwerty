/*Implement C++ program for expression conversion as infix to postfix and its evaluation 
using stack based on given conditions: 
1. Operands and operator, both must be single character.
2. Input Postfix expression must be in a desired format.
3. Only '+', '-', '*' and '/ ' operators are expected*/
#include<iostream>
#include <stack>
using namespace std;
int prec(char c)
{
    if(c=='^')
    {
        return 3;
    }
    else if (c=='*' || c=='/')
    {
       return 2;
    }
    else if (c=='+' || c=='-')
    {
        return 1;
    }
    else
    {
        return -1;
    }
    
}
string intopo(string s)
{
  stack <char> st;
  string res;
  for(int i=0;i<s.length();i++)
  {
    if((s[i]>='a' && s[i]<='z')||(s[i]>='A' && s[i]<='Z'))
    {
        res+=s[i];

    }
    else if(s[i]=='(')
    {
        st.push(s[i]);
    }
    else if(s[i]==')')
    {
        while(!st.empty() && st.top()!='(')
        {
            res+=st.top();
            st.pop();
        }
        if(!st.empty())
        {
            st.pop();
        }
    }

    else
    {while(!st.empty() && prec(st.top())>prec(s[i]))
    {
        res+=st.top();
        st.pop();
    }
    st.push(s[i]);

    }
    while(!st.empty())
    {
        res+=st.top();
        st.pop();
    }

  }

  return res;
}

int main()
{
cout<<intopo("q*(w+)/a");

    return 0;
}
