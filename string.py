str="Mumbai is capital of Maharashtra"
def long_len():
    s=str.split()
    max=0
    for i in s:
        if len(i)>max:
            max_word=i
            print("Word with longest lendth : ",max_word)
            print("Length of longest word : ",len(max_word))
            long_len()
            def freq_char():
                c=input("Enter a character for finding its frequency :")
                print("c =",c)
                g=str.count(c)
                print(g)
                freq_char()

                def str_pali():
                    str=input("Enter character for checking palindrome :")
                    m=str[::-1]
                    print(m)
                    if str==m:
                        print("String is palinndrome")
                    else:
                        print("String is not palindrome")
                str_pali()


            def index_substr():
                                str_sub=input("Enter the substring : ")
                                list_str=str.split()
                                for i in rsnge(len(list_str)):
                                    if str_sub==list[i]:
                                        print(str)
                                        print(i)
                                        break
                                    index_substr()

                                def freq_word():    
                                     list_str=str.split()
                                     print("Count of esch word in string")
                                     for i in range(len(list_str)):
                                        print(list_str[i],list_str.count(list_str[i]))
                                freq_word()
                                        
