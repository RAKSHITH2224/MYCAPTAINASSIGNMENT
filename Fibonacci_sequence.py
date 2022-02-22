#fibonacci formula is Fn=Fn-1 + Fn-2 where n>1

n = int(input("how many terms? "))

#The first 2 terms of the fibonacchi sequence is 0 , 1

n1, n2 = 0,1
count = 0

#validation of the entered number
if n<=0:
    print("Please Enter Positive Integer")
    
#if there is onl one term, return n1
elif n==1:
    print("Fibonacchi sequence upto", n ,":")
    print(n1)
    
#generate Fibonacchi sequence
else:
    print("Fibonacchi Sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
#updation      
        n1 = n2
        n2 = nth
        count = count + 1