

num_list = [1,2,3,4,5,6,7,8,9]

key=int(input("Enter key value to be search : "))
n=len(num_list)

#Linear Search

def linear_search(lst,key,n):
    for i in range(0,n):
        if lst[i]==key:
            print("Element found at index ",i)
            return
    print("Element not found")
linear_search(num_list,key,n)


#sentinal search



def sentinel(num_list, key):
    num_list.append(key)
    i = 0
    while(num_list[i] != key):
        i += 1
    if(i == n):
        print("element not present")
        
    else:
       print("Elememt is present at index ",i)
    
sentinel(num_list,key)
