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
                choices=['+', '-', '*', '/'],
            ),
]
print("--------------------------------------------")
answers = inquirer.prompt(questions)

while True:
	questions = [
	 inquirer.List('op',
	                message="choose an opperation",
	                choices=['+', '-', '*', '/'],
	            ),
	]

	answers = inquirer.prompt(questions)

	if answers["op"]== '+':
		print("--------------------------------------------")
		print('matrix1 + matrix2 : \n',matrixx + matrixx2)
	elif answers["op"]== '-':
		print("--------------------------------------------")
		print('matrix1 - matrix2 : \n',matrixx - matrixx2)
	elif answers["op"]== '*':
		print("--------------------------------------------")
		print('matrix1 * matrix2 : \n',matrixx * matrixx2)
	else :
		print("--------------------------------------------")
		print('matrix1 / matrix2 : \n',matrixx / matrixx2)


	
