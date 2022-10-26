import numpy as np  
import inquirer


Rows = int(input("Give the number of rows:"))  
Columns = int(input("Give the number of columns:"))  
  
 # matrix 1
print("First matrix (separated by a space): ")  
elements = list(map(int, input().split()))  
matrixx = np.array(elements).reshape(Rows, Columns)  
print("Matrix 1 :\n" , matrixx)



# matrix 2
print("seacond matrix (separated by a space): ")  
numbers = list(map(int, input().split()))  
matrixx2 = np.array(numbers).reshape(Rows, Columns)  
print("Matrix 2 :\n" , matrixx2)

questions = [
  inquirer.List('op',
                message="choose an opperation",
                choices=['+', '-', '*', '/'],
            ),
]

answers = inquirer.prompt(questions)

if answers["op"]== '+':
	print(matrixx + matrixx2)
elif answers["op"]== '-':
	print(matrixx - matrixx2)
elif answers["op"]== '*':
	print(matrixx * matrixx2)
else :
	print(matrixx / matrixx2)
	

while True:
	questions = [
	 inquirer.List('op',
	                message="choose an opperation",
	                choices=['+', '-', '*', '/'],
	            ),
	]

	answers = inquirer.prompt(questions)

	if answers["op"]== '+':
		print('matrix1 + matrix2 : \n',matrixx + matrixx2)
	elif answers["op"]== '-':
		print('matrix1 - matrix2 : \n',matrixx - matrixx2)
	elif answers["op"]== '*':
		print('matrix1 * matrix2 : \n',matrixx * matrixx2)
	else :
		print('matrix1 / matrix2 : \n',matrixx / matrixx2)


	