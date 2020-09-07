#Author: Vyacheslav Hlushko vqh5091@psu.edu
#Collaborator Brian Chettle bjc5969@psu.edu
#Collaborator Ching-Ju Chen cxc6001@psu.edu
#Collaborator Youngjae Bae yvb5135@psu.edu
temperature=float(input("Enter temperature:"))
unitinput=str(input(" Enter unit in F/f or C/c: "))

if unitinput == "C" or unitinput == "c":
  temperature2 = (temperature * 9/5) + 32
  print(f"{temperature}° in Celsius is equivalent to {temperature2}° Fahrenheit.")
elif unitinput == "F" or unitinput == "f":
  temperature2 = (temperature - 32) / 9.0 * 5
  print(f"{temperature}° in Fahrenheit is equivalent to {temperature2}° Celsius.")
else:
  print(f"Invalid unit({unitinput}).")

