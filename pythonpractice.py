print("Hello Prayush")
print("""Hi 
      gang""")
print("*"*5)
name="Prayush"
print(name)
naam=input("Enter your name: ")
print("Hello "+ naam)
color=input("What is your fav color?")
print(name+" likes "+color)

weight=input("Enter your weight in pounds: ")
weight_kgs=float(weight)*0.45
print("Weight in kgs is ", weight_kgs)

string='hi'
hello=string
print(hello)
print(f'hello {hello}')

course='python'
print(course.replace('p','q'))
import math
math.ceil(2.7)
math.floor(2.9)

good_credit=False
price=1000000
if good_credit:
    down_payment=price-(10/100)*price
else:
    down_payment=price-(20/100)*price

print(down_payment)

for item in range(10):
    print(item)