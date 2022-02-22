#Write a python program to print all positive numbers in range.

list1 = []

#input number of elements
n = int(input("Enter number of elements in the List: "))

#iterating upto the range
for i in range(0,n):
    print("Enter element number-{}: ".format(i+1))
    elm = int(input())
    list1.append(elm)
print("list_1: \n", list1)

#to print all the positive numbers in the list1.
for num in list1:
    if num>=0:
        print(num, end =" ")




#for second list
list2 = []

#input number of elements
n = int(input("Enter number of elements to be in the List: "))

#iterating upto the range
for i in range(0,n):
    print("Enter element number-{}: ".format(i+1))
    elm = int(input())
    list2.append(elm)
print("list_2: \n", list2)

#to print all the positive numbers in the list2.
m=[x for x in list2 if x>=0]
print(m)
