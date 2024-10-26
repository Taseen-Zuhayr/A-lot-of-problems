try:
    num1 , num2 = eval(input("Enter number seperated by commas : "))
    result = num1/num2
    print(result)
except SyntaxError:
    print("Make my life easier by using commas.")
except ZeroDivisionError:
    print("Make my life easier by giving zero(0) in the second number.")
except NameError:
    print("Make my life easier by giving numbers instead of alphabet.")
else:
    print("Make my life easier by giving everything properly.")
finally:
    print("Congratulations! You made my life easier.")