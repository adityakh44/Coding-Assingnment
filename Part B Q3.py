
Num1 = int(input("Enter your num1 :- "))
Num2 = int(input("Enter your num2 :- "))
Num3 = int(input("Enter your num3 :- "))
    
def add(Num1, Num2, Num3):
    if Num1%3 != 0 and Num2%3 != 0 and Num3%3 != 0 :
       return Num1 + Num2 + Num3
    elif Num1%3 == 0 and Num2%3 != 0 and Num3%3 != 0 :
        return Num2 + Num3
    elif Num1%3 != 0 and Num2%3 == 0 and Num3%3 != 0 :
        return Num1 + Num3
    elif Num1%3 != 0 and Num2%3 != 0 and Num3%3 == 0 :
        return Num1 + Num2
    elif Num1%3 == 0 and Num2%3 == 0 and Num3%3 != 0 :
        return Num3
    elif Num1%3 != 0 and Num2%3 == 0 and Num3%3 == 0 :
        return Num1
    elif Num1%3 == 0 and Num2%3 != 0 and Num3%3 == 0 :
        return Num2
    else :
        return 0
   

print(add(Num1, Num2, Num3))