# To create a BMI calculator


def calculate_bmi(weight,height):
    bmi = weight/(pow(height,2))
    return bmi


weight = float(input('Enter your weight in KG: '))
height = float(input('Enter your height in metres: '))
bmi = calculate_bmi(weight,height)
print(bmi)
