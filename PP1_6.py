4534
'''
	File Name: errors.py
	Author: Mr. Kalisz
	Date Created: March 29, 2019
	Date Last Edited: Sept 23, 2024
'''
import math

# From input, recieve two integers from the user and add them together.  Output the result.
def q1():
  num1 = int(input("Input a number: "))
  num2 = int(input("Input a number: "))
  num3 = num1 + num2
  print(num3)
# From input recieve two integers.  Output the quotient rounded down.
def q2():
  num4 = input("Input a number: ")
  num5 = input("Input a number: ")
  num6 = int(num4)
  num7 = int(num5)
  num8 = num6 / num7
  print(math.floor(num8))
# Output the phrase "hello Mr. Kalisz have you seen my work yet?"
def q3():
	
  print("hello Mr. Kalisz have you seen my work yet?")
	
# From input recieve two numbers (can be decimal fractions).  
# Output their result multiplied together.  Then round down to the nearest whole number
def q4():
  num9 = input("Input a number: ")
  num10 = input("Input a number: ")
  num11 = int(num9)
  num12 = int(num10)
  num13 = (num11 * num12)
  print(math.floor(num13))

#q1()
#q2()
#q3()
#q4()
