#1

def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))


#2

def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1

	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('madam'))


#3

def pascal_triangle(n):
   trow = [1]
   y = [0]
   for x in range(max(n,0)):
      print(trow)
      trow=[l+r for l,r in zip(trow+y, y+trow)]
   return n>=1
pascal_triangle(6)


#4

import string
def ispangram(str):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str.lower():
         return False
   return True
# main
string = 'The five boxing wizards jump quickly.'
if(ispangram(string) == True):
   print("Yes")
else:
   print("No")


#5

word=input("Enter hyphen-separated sequence of words :-")
items=[n for n in word.split('-')]
items.sort()
print('-'.join(items))


#6

def student_data(student_id, **kwargs):
    print(f'\nStudent ID: {student_id}')
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")

    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_class']}")


student_data(student_id='SV12', student_name='Jean Garner')

student_data(student_id='SV12', student_name='Jean Garner', student_class ='V')


#7

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))


#8

def findTriplets(arr, n):

    found = False
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True

    if (found == False):
        print(" not exist ")

arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)


#9

class validity:

    def f(str):

        a= ['()', '{}', '[]']

        while any(i in str for i in a):

            for j in a:

                str = str.replace(j, '')

        return not str

s = input("enter : ")

print(s, "-", "is balanced"

      if validity.f(s) else "is Unbalanced")