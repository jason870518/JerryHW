from sources import calculator
try:
    x = input ("input x:")    
    y = input ("input y:")
    x = float(x) 
    y = float(y)
    operator = input("input operator")
    type(x) == 'str'
    type(y) == 'str'    
except: 
    print("Please input number.")
else:
    print(calculator.calculator(x ,y , operator))
    
    
