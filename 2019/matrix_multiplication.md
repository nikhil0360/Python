# Matrix multiplication A x B
# A(i,j) , B(j,k)

```python3 
def matrix_multiply(A, B):
	i = len(A)
	j = len(B)
	k = len(B[0])
	
	matrix = []
	for a in range(i):
		row = []
		for b in range(k):
			value = 0
			for c in range(j):
				value += A[a][c] * B[c][b]
			row.append(value)
		matrix.append(row)

	for i in range(len(matrix)):
		print(matrix[i])


A = [[1,2],[3,4]]
B = [[1],[1]]

matrix_multiply(C, D)
```

# Or 
we can use **[numpy](https://numpy.org/)**, which has a function dot, for matrix multiplication.  
Numpy uses a method called *Single instruction, multiple data* (**SIMD**), 
thus making mathematical operation such as Matrix multiplication fast, very fast.

```python3
import numpy as np

A = [[1,2],[3,4]]
B = [[1],[1]]

C = np.dot(A,B) 
```
