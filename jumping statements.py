"""
    jumping/transfer statements:
    These statements are used to  contol the normal
    1.Break : this statements are used to terminate/break the loop 
    2.continue : this statements are used to skip current iteration and run the text iteration
"""

i=0
while i<=10:
    i+=1
    if i==6:
        break#terminate/stop the program
    print(i)


i=1
while i<=10:
    i+=1
    if i==6:
        break#terminals/stop the program
    print(i)

    i=0
while i<=9:
    i+=1
    if i==3:
        continue
    print(i)
