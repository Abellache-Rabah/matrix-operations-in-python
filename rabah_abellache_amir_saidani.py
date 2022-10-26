import numpy as np  
import inquirer


Rows = int(input("Give the number of rows:"))  
Columns = int(input("Give the number of columns:"))  
print("--------------------------------------------")
 # matrix 1
print("First matrix (separated by a space): ")  
elements = list(map(int, input().split()))  
matrixx = np.array(elements).reshape(Rows, Columns)  
print("Matrix 1 :\n" , matrixx)

print("--------------------------------------------")

# matrix 2
print("seacond matrix (separated by a space): ")  
numbers = list(map(int, input().split()))  
matrixx2 = np.array(numbers).reshape(Rows, Columns)  
print("Matrix 2 :\n" , matrixx2)

questions = [
  inquirer.List('op',
                message="choose an opperation",
                choices=['Add', 'Subtraction', 'Multiplication', 'Division','transpose','Determinant','Inverse'],
            ),
]
print("--------------------------------------------")
answers = inquirer.prompt(questions)

while True:
	questions = [
	 inquirer.List('op',
	                message="choose an opperation",
	                choices=['Add', 'Subtraction', 'Multiplication', 'Division',"Transpose",'Determinant','Inverse'],
	            ),
	]

	answers = inquirer.prompt(questions)

	if answers["op"]== 'Add':
		print("--------------------------------------------")
		print('matrix1 + matrix2 : \n',matrixx + matrixx2)
	elif answers["op"]== 'Subtraction':
		print("--------------------------------------------")
		print('matrix1 - matrix2 : \n',matrixx - matrixx2)
	elif answers["op"]== 'Multiplication':
		print("--------------------------------------------")
		print('matrix1 * matrix2 : \n',matrixx * matrixx2)
	elif answers["op"] == "Transpose":
		print("--------------------------------------------")
		print("transpose matrix1 \n",np.transpose(matrixx),"\ntranspose matrix2\n",np.transpose(matrixx2))
	elif answers["op"] == 'Determinant':
		print("--------------------------------------------")
		print("det 1 \n",np.linalg.det(matrixx),"\n det 2 \n",np.linalg.det(matrixx2))
	elif answers["op"] == 'Inverse':
		print("--------------------------------------------")
		print("inverse matrix 1 \n",np.linalg.inv(matrixx),"\ninverse matrix 2 \n",np.linalg.inv(matrixx2))
	else :
		print("--------------------------------------------")
		print('matrix1 / matrix2 : \n',matrixx / matrixx2)