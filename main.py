# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = weight /(height**2)
if BMI < 18.5:
  print("Your BMI is "+str(BMI)+", You are underweight")
elif BMI > 18.5 and BMI<25:
  print("Your BMI is "+str(BMI)+", You have normal weight")
elif BMI > 25 and BMI<30:
  print("Your BMI is "+str(BMI)+", You are slightly overweight") 
elif BMI > 30 and BMI<35:
  print("Your BMI is "+str(BMI)+", You are obese")
elif BMI>35:
  print("Your BMI is "+str(BMI)+", You are clinically obese") 


