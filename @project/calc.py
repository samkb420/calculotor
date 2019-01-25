
import time
from Add import Add
from Sub import Sub
from Div import Div
from Mult import Mult
print("\t[!!]\t[!!]\t Author:Sam kb @ pablo254\t[!!]\t[!!]\t\n")
print("\t[$$]\t[$$]\t E-mail:kagosamuel07@yahoo.comm\t[&&]\t[&&]\t\n")
print("\t\t........Project:Software Development.......\t\n")


time.sleep(0.5)

print("\t\t\t\/\/\/\/\/\/\/\/\/\/\/\n")
time.sleep(0.5)

count = 0
while (count < 2 ):
   print ("\t\t[+]\t[-]\t[+]\t[-]\t[+]")
   time.sleep(0.5)
   print ("\t\t[-]\t[+]\t[-]\t[+]\t[-]")
   time.sleep(0.5)
   count = count + 1


x=int(input("[#]>Enter a number:"))
y=int(input("[#]>Enter a number:"))
A=Add(x,y)
S=Sub(x,y)
D=Div(x,y)
M=Mult(x,y)

print("The sum  is:",A)
time.sleep(0.5)
print("The diffrence  is:",S)
time.sleep(0.6)
print("The division is :",D)
time.sleep(0.7)
print("The Multiple is: ",M)
time.sleep(0.8)
