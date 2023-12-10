"""Write a Python program to store marks scored in subject “Fundamental of Data Structure” by N 
students in the class. Write functions to compute following:
a) The average score of class 
b) Highest score and lowest score of class
1) Count of students who were absent for the test
2) Display mark with highest frequency

"""

n=int(input("Enter the no. of students"))
present,sum,min,max,a3
absent = 0,0,51,-1,0
mark=[]

for i in range(n):
    temp=(input("Enter the marks of student :  "+str(i+1)+"or AB if absent : "))
    mark.append(temp)
    if temp!="AB":
        present+=1
        sum+=int(temp)
        if int(temp)>max:
            max=int (temp)
        if int(temp)<min:
            min=int (temp)
    else:
        absent+=1
avg=sum/present

max_f = 0
mark =[]
for i in range(0,51):
    f=0
    for j in mark:
        if j!="AB" and i == int(j):
            f+=1
        if f > max_f:
            max_f=f
            mark.clear()
            mark.append(i)
        elif f==max_f:
            mark.append(i)

 
print("The average score of class : ",avg) 
print("Highest score and lowest score of class" ,max, "and", min)
print("Count of students who were absent for the test",absent)
print("Display mark with highest frequency")
