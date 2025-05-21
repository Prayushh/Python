weight=input("Enter your weight ")
weight=float(weight)
wt= input("Enter K if you entered your wt in kgs and L if you entered your weight in pounds ")
if wt=='K':
    weight = weight* 2.2
    print("Weight in pounds is, ", weight)
else:
    weight=weight/ 2.2
    print("Weight in kgs is, ", weight)