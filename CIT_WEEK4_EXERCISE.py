##a 2-D array
import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])


#sort array element in the ascending/descending order
my_list = [79, 67, 100, 42, 9, 97, 78, 89, -9, -1]
print("The list is :")
print(my_list)
#ascending  order
my_list.sort()
print("The list after sorting is :")
print(my_list)
#descending order
my_list.sort(reverse = True)
print("The list after sorting is :")
print(my_list)

#Create a set
array_list = [5, 10, 3, 15, 2, 20]
print("Original set elements of the array:")
print(array_list)
print(type(array_list))
print("\nMaximum value of the said array:")
print(max(array_list))
print("\nMinimum value of the said array:")
print(min(array_list))

# Python Program to Calculate Total Marks Percentage and Grade

print("Enter the marks of five subjects::")

subject_1 = float (input ())
subject_2 = float (input ())
subject_3 = float (input ())
subject_4 = float (input ())
subject_5 = float (input ())

total, average, percentage, grade = None, None, None, None

# It will calculate the Total, Average and Percentage
total = subject_1 + subject_2 + subject_3 + subject_4 + subject_5
percentage = (total / 500.0) * 100

if percentage <= 50:
    grade = 'c'
elif percentage >= 50 and percentage < 80:
    grade = 'B'
elif percentage >= 80 and percentage <= 100:
    grade = 'A'

else:
    grade = 'NO GRADE'

# It will produce the final output
print ("\nThe Total marks is:   \t", total, "/ 500.00")
print ("\nThe Percentage is:    \t", percentage, "%")
print ("\nThe Grade is:         \t", grade)

#fetch only Email ID from text file
import urllib.request 
import re 
openfile = open('text.txt', 'r')
with openfile as input:
    print (re.findall(r'\b([a-z0-9-_.]+?@[a-z0-9-_.]+)\b', f_input.read(), re.I))



#checking the speed of drivers.
def checkSpeed(speed):
    if speed <= 70:
        return "OK"

    else:
        speed1 = (speed-70)//5

        if speed1 <= 12:
            print(f"Point: {speed1}")

        else:
            print("License suspended")


checkSpeed(int(input("Enter speed: ")))


#function called show_stars(rows)
def show_stars(rows):
  rows = int(input("Enter the number of rows"));
  k = 1
  for i in range(0, rows):
      for j in range(0, k):
          print("* ", end="")
      k = k + 1
      print()
show_stars(5)


#find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)
Factor=[]
for x in range(2000, 3200):
    if (x%7==0) and not (x%5==0):
        Factor.append(str(x))
print (','.join(Factor))

#sequence of comma-separated numbers from console and generate a list and a tuple which contains every number
my_list = str(input("Enter sequence of comma-separated numbers"))
my_list1 = my_list.split(',')
My_tuple = tuple(my_list1)
my_list1 = list(my_list1)
print(My_tuple)
print(my_list1)


#program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H]
import math
c=50
h=30
value = []
items=[x for x in input("Enter number seperated by comma").split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))


###Write a function to compute 5/0 and use try/except to catch the exceptions.
def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError:
    print("divisble by ZERO!!")
except:
    print("Any other exception")



#buble sorting algorithms
def bubble_sort(array):
    my_list = len(array)

    for i in range(my_list):
        
        already_sorted = True

        for j in range(my_list - i - 1):
            if array[j] > array[j + 1]:
               
                array[j], array[j + 1] = array[j + 1], array[j]

                already_sorted = False
        if already_sorted:
            break

    return array

