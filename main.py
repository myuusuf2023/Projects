name = input("what is your name?  ")
print("Hello "+ name)
birth_year = input("Enter your birth year?  ")
age= 2023 - int(birth_year)
print(age)
#
weight = int(input("Enter your weight: "))
unit = input("(K)g or (L)lbs: ")

if unit.upper() == "K":
    converted =float = weight / 0.45
    print('weight in Lbs: ' + str(converted))
else:
    converted = weight * 0.45
    print("weight in Kgs" +str( converted))
siblings = input("enter your siblings ")
print("may allah bless them ")

i = 1
while i <=10 :
    print(i*("i"))
    i = i+1
destricts =["Boondheere","Kaaraan","Shingaani","Yaqshid"]
destricts [0] = "bondhere"
# # print(destricts)
numbers =[1,2,3,4,5,6]
for item in numbers:
     print (item)
     i =0
#waa isku mid balse while loop ayaa dheer
while i < len (numbers):
    print(numbers[i])
    i = i+1
    numbers = range(5,10 , 2)
for number in numbers:
    print(number)

print(1 in numbers )
print(10 in numbers)
print(len (numbers))
numbers.remove (3)
numbers.clear()
print(numbers)
numbers.append(7)
print(numbers)

course = 'Mohamed Yusuf Ali'
print(len(course))
print(course.upper())
print(course.lower())
print(course)
print(course.replace("M" , "J"))
x= (2+4)*10-8
print(x)
x=2.9
print(round(x))
print(abs(-2.9))
is_hotday=False
is_cold=False
if is_hotday:
   print("it's hot day")
   print("Enjoy your day "+"and don't forget to Drink more water.")
elif is_cold:
   print("it's cold day")
   print("wear worm clothes")
else:
 print("its lovely day")
 print("Enjoy your day")
price = 1000000
has_good_credit =True
if has_good_credit:
    down_payment=0.1*price
else:
   down_payment=0.2*price
print(f"down payment:$ {down_payment}")
high_icome = False
has_agood_cridet=False
if high_icome or has_agood_cridet:
    print("ellegble for loan")
else:
    print("we can't give you a loan")

