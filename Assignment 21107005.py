#Assignment
#Q1

word="Python is a case sensitive language"
#Find Lenght
print(len(word))

#Reverse order
print(word[::-1])

#Slicing
new_word=word[10:26]

#Replacing String
word=word.replace('a case sensitive', "object")

#Finding the index of "a"
print(word.find("a"))

#Removing the White spaces
word=word.replace(" ","")

#Q2
SID=21107005
name="Harshvardhan"
department="mechanical"
CGPA= 8.5

print("Hey," + name + "Here!")
print("my SID is %d" %SID )
print("I am from " + "department and my CGPA is ", CGPA)

#Q3
a=56
b=10
print("a&b=",a&b)
print("a|b=",a|b)
print("a^b",a^b)
print("a << 2 : ", a << 2, " and b << 2: ", b << 2)
print("a >> 2 :", a >> 2," and b >> 4:", b>> 4)

#Q4
input_string=input("Enter the string: ")
check_name=input_string.find("name")
if(check_name==-1):
    print("NO")
else:
    print("YES")

#Q5
slide_1=int(input("Enter the slide 1: "))
slide_2=int(input("Enter the slide 2: "))
slide_3=int(input("Enter the slide 3: "))

a=slide_1 + slide_2
b=slide_2 + slide_3
c=slide_3 + slide_1

x= (slide_1 < b)
y= (slide_2 < c)
z= (slide_3 < a)

answer = str(x & y & z)
answer = answer.replace("True", "Yes")
answer = answer.replace("False", "No")

print(answer)

#Q6
a= int(input("enter the number a: "))
b= int(input("enter the number b: "))

c= (a^b)
d= bin(c)

count= 0
for i in d[2:1]:
    if i == "1":
        count+= 1

print(count)