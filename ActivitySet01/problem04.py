# Conditional Execution

hrs = float(input("Enter hours? "))
h=float(hrs)
rate=float(input("Enter the rate per hour? "))
if h<=40:
  pay=hrs*rate
elif h>40:
  pay=(rate*1.5)*(h-40)+((h-5)*rate)
print(pay)

