m1 = [ [1,2,3] , [4,5,6] ]
m2 = [ [1,2,3] , [2,3,4] , [3,4,5] ]
#m3 = [ [1,2,3] , [2,3,4] ]

m3 = []
for i in range(len(m2[0])):
  temp = []
  for j in range(len(m2)):
    temp.append(m2[j][i])
  m3.append(temp)

print(m3)
