# condetional if/else logic- these are keywords that instruct your
# programe to do specific instruction based on specfic data
# or conditions

# condetina; syntax (how is it written)
bill_amount = int(input("please type in a ball tender (1,5,10) ")
# if usally indicates the somthing in a possible option

if bill_amount ==1
         print("here are 4 quarts")

# elif allows us to indicate that are more possible options
 you can have as many alif as you want
 elif bill_amount ==5:
 pritn ("here are 20 quarters")
 
 elif bill_amount ==10:
print("here are 40 quarters")

elif bill_amount ==20
print("sorry we do not accept 20s please enter an accpted amount")

elif bill_amount ==50:
print("sorry we do not accept 50s please enter an accpted amount")

elif bill_amount ==100:
print("sorry we do not accept 100s please enter an accpted amount")
# else is always your last option
else:
print ("sorry tgat type of bill is not accepted")

# creat a calculatar function that uses if/else logic to
# allowthe user'# to change or select different arithhemic operation
# example an input where if the usr enters 1, it will do
# additons, 2 to will do suntration
# 3 will do multiplication and 4 divisions

def calculate_add():
print("programe has started please type 2 numbers to add")
num1 = int(input())
num2 = int(input())
print(num1+ num2)
print("programe had endede")

def micalculator():
# take in a user selection as a number
selction= input()

if selection ==1:
calculate_add()
elif selection ==2
calculate_subtraction()
elif selection ==3
calculate_divide()
elif selection ==4
calculate_multiply()
else
print("sorry somthing went wrong")