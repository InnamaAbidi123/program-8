length=int(input("enter list length:"))
my_list=[]
for i in range(length):
    temp=int(input("enter list item:"))
    my_list.append(temp)
histogram_char="*"
for item in my_list:
    print(histogram_char*item)
