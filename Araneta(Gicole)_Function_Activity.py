def same_num(a, b, c):
    result = a * b * c
    print(f"Result is {result}")
    return


def diff_num(a, b, c):
    result = a + b + c
    print(f"Result is {result}")
    return


First_Num = int(input("Enter the first number: "))
Second_Num = int(input("Enter the second number: "))
Third_Num = int(input("Enter the third number: "))

if First_Num == Second_Num:
    if Second_Num == Third_Num:
        same_num(First_Num, Second_Num, Third_Num)
    elif First_Num != Third_Num:
        diff_num(First_Num, Second_Num, Third_Num)
    elif Second_Num != Third_Num:
        diff_num(First_Num, Second_Num, Third_Num)
else:
    diff_num(First_Num, Second_Num, Third_Num)
