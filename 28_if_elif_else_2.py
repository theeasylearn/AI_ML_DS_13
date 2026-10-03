'''
write a program to findout person's obesity level using B.M.I(body to mass index) technique. and display obesity level of person as below rule 
obesity level 
    Extremely Obese: BMI 35.0 and above
    Obese: BMI between 30.0  34.9
    Overweight: BMI between 25.0  29.9
    Normal: BMI between 18.5 to 24.9
    Underweight: BMI less than 18.5
    ---------------------------------------------------------------------
    formula to calculate BMI IS 
    bmi = weight(Kg ) / (height_in_meter * height_in_meter)
    
    input:
        weight, foot, inch 
    steps 
    1   accept input weight, foot, inch
    2   convert foot and inches into total inch 
    3   total inch convert into meter 
    5   calculate BMI 
    5   calculate & display person obesity level
'''
weight = float(input("Enter weight"))
print("Enter your height in foot and inches")
foot = int(input("Enter only foots"))
inches = int(input("Enter remaining inches"))
#calculate total inches 
total_inches = (foot * 12) + inches
#convert inch into meter 
meter = total_inches / 39.37
#calculate  bmi
bmi = weight / (meter * meter)
print("BMI ",bmi)   