"if"
"""
if condition :
    statements
    """
#write a python program to find whether a number is positive or not

num = int(input("enter a number"))
if num>0:
    print("the number is positive",num)

    #write a program to find biggest of two numbers 
    a = int(input("enter a number:"))
    b = int(input("enter a number:"))
    if a>b:
        print("A is greater:",a)
    else:
        print("B greater:",b)



#Accept the percentage from the user and display the grade according to the following crteria
"""
below D - 25
25 to 45 -- C
45 to 50 -- B
50 to 60 -- B+
60 to 80 -- A
Above 80 ---A+
"""
pr= int(input("enter your percentage"))
if pr<=25:
    print("the code is D")
elif pr>=25 and pr<=45:
    print(" your grade is C..")
elif pr>45 and pr<=50:
    print("your grade is B..")
elif pr>50 and pr<=60:
    print(" your grade is B+")
elif pr>60 and pr<=80:
    print("your grade is A..")
elif pr>80:
    print(" your grade is A++..")

    #write a program to display the famous monuments
    # according to city given by user
city= input("enter city name:....")
if city =="paris":
    print("eiffel tower")
elif city== "korea":
    print("N seoul tower")
elif city =="hyderabad":
    print("charminar")
elif city =="delhi":
    print("tajmahal")
elif city=="goa":
    print("beach")
else:
    print("wrong city selected")



#write a program to display week names by taking input from user
day=int(input("enter your day:.."))
if day ==1:
    print("sunday")
elif day==2:
    print("monday")
elif day ==3:
    print("tuesday")
elif day ==4:
    print("wednesday")
elif day ==5:
    print("thursday")
elif day ==6:
    print("friday")
elif day ==7:
    print("saturday")
else: 
    print(" check your input")


#accept the number of days from the 
# user and calculate the charge the library according to the following
"""
till five days : Rs2/day
six ten : Rs3/day
11 to 15 : Rs4/day
After 15 days : Rs5/day
"""

num  = int(input("enter the days"))
if num<=5:
    print("the charge is ",num*2)
elif num>=5 and num<=10:
    print("the charge is ",num*3)
elif num>=11 and num<=15:
    print("the charge is ",num*4)
elif num>15:
    print("the charge is ",num*5)
else:
    print("wrong days selected")

"""
wite a program to accept two numbers from user and an operator and
perform operations accordingly
num1 = 5
num2 = 10
opr : +
answer : 15
"""
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
opr  = input("enter a operator")
if opr=="+":
    print("enter a number:", num1+num2)
elif opr=="-":
    print("enter a number:", num1-num2)
elif opr=="*":
    print("enter a number:", num1*num2)
elif opr=="/":
    print("enter a number:", num1/num2)
else:
    print("wrong operator..")

#write a program to accept a number from 1 to 12 and display name of the month and days in that month like one for jan 31 days

mon_num = int(input("enter the month number 1 to 12"))
if mon_num==1:
    print("the month is jan it has.. 30 days")
elif mon_num==2:
    print("the month is feb it has.. 28 days ")
elif mon_num==3:
    print("the month is march it has.. 31 days ")
elif mon_num==4:
    print("the month is apr it has.. 30 days ")
elif mon_num==5:
    print("the month is may it has.. 31 days ")
elif mon_num==6:
    print("the month is june it has.. 30 days ")
elif mon_num==7:
    print("the month is july it has.. 31 days ")
elif mon_num==8:
    print("the month is aug it has.. 31 days")
elif mon_num==9:
    print("the month is sep it has.. 30 days ")
elif mon_num==10:
    print("the month is oct it has.. 31 days ")
elif mon_num==11:
    print("the month is nov it has.. 30 days")
elif mon_num==12:
    print("the month is dec it has.. 31 days")
else:
    print("wrong number")

"""
write a program to display "Hello" if a number entered by user 
is a multiple of five otherwise print "Bye"
"""

num = int(input("enter a number"))
if num%5==0:
    print("Hello")
else:
    print("Bye")


    """
    nested if : A if within a "if" is called nested if
    syntax : if condition :
                    outer if statements
                    if condition :
                    inner if statements
                else :
                    inner else statements
            """
#A program on weather advisories (nested if)
is_snowing = True
tem = int(input("enter the temperature"))
if is_snowing<10:
    print("please carry umbrella")
    if is_snowing>-10:
        print("please carry umbrella and jacket")
    else :
        print("enjoy the sunny day!!")
else :
        print("you have a great day")


#Express delivery
weight=int(input("enter the weight"))
if weight==4:
    print("the delivery can be expected within 24 hrs")
    if weight<=10:
        print("need to pay an extra amount for extra weight")
    else:
        print("no need to pay an extra charge have a great delivery!!")
else:
    print("need to wait 3-5 business days to except the delivery")

    
"""
shorthand if : writing a "if" in a line is called shoorthand if 
syntax : if condition: statements
"""
a = 10
    