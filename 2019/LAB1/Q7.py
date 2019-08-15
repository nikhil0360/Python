# let n is the input amount
n = int(input())
# a is the note counter
a = int(n/200)
b = n%200
if(b>=50):
            a = a + int(b/50)
            b = b % 5 

if(b<50 and b>=10):
            a = a + int(b/10)
            b = b % 10

if(b<10 and b>=5):
            a = a + int(b/5)
            b = b % 5

if(b<5 and b>=2):
            a = a + int(b/2)
            b = b % 2

if(b<2 and b>=1):
            a = a + int(b/1)

print(a)

