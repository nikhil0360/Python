l1 = [3,4,4,1,9,7]
l2 = [-99999999,999999999]
for i in range(len(l1)):
  
  a = l1.pop(0)
  for j in range(len(l2)):
    if(l2[j]<a and l2[j+1]>a):
      l2.insert(j+1,a)
     # break is not required // try dry run and you will see .
     # this program also remove repeated number in array 
l2.pop(0)
l2.pop(len(l2)-1)

print l2 
