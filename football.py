#In second year computer engineering class, group A student’s play cricket, group B students play 
#badminton and group C students play football. 
#3Write a Python program using functions to compute following: -
#a) List of students who play both cricket and badminton 
#b) List of students who play either cricket or badminton but not both 
#(Note- While realizing the group, duplicate entries should be avoided, Do not use SET built-in 
#functions

def union(a, b):
    ans = a.copy()
    for i in b:
        if i not in a:
            ans.append(i)
    return ans
def minus(a, b):
    ans = []
    for i in a:
        if i not in b:
            ans.append(i)
    return ans

def intersection(a, b):
    ans = []
    for i in a:
        if i in b:
            ans.append(i)
    return ans

u = input("Enter the union list: ").split(",")
b = input("Enter the badminton list: ").split(",")
c = input("Enter the cricket list: ").split(",")
f = input("Enter the football list: ").split(",")

print("List of students who play both cricket and badminton : ",intersection(b,c))
print("List of students who play either cricket or badminton but not both : ",union(minus(c,intersection(b,c)),minus(b,intersection(b,c))))
