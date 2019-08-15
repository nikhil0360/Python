print("type corresponding no. for the fuctions needed\n"
      "1) Add \n"
      "2) multiply \n"
      "3) Average\n")

a = int(input())
# a is for storing no. for the function.
n1 = float(input()) # input 1
n2 = float(input()) # input 2
if(a==1):
    print(n1+n2)
elif(a==2):
    print(n1*n2)
elif(a==3):
    print(n1/2+n2/2)
