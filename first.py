# Get started with interactive Python!

# You can also write comments for your students to read like this.
# When you're done, add this to your website using the embed code.
import sys

def menu():
  print("This is a simple calculation program")
  
def pause_for_a_while():
  print("press any key to continue")
  input()


menu()
a=int(input( "Enter a="))
b=int(input( "Enter b="))
c=int(input( "Enter c="))

result = a*b+c
print("The required result is " , result)



# Chapter 2 - Python 101 Book Example
# String practice

zen_of_python="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense."""

first_name ="M"
last_name ="Rahman"

print ("String length is " ,  len(zen_of_python)) 

full_name = first_name + ' ' + last_name
print("Full name is " , full_name)

# use of import module sys

win_version = sys.version
print("Current python version is " , win_version)



# for example
# ---------------
namta = int(input("Enter namota to populate :"))
for i in range(1,11):
    print(namta,"X", i ,"=", namta*i)



# calling function
pause_for_a_while()




