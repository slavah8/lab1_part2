temperature=float(input("Enter temperature:"))
unitinput=str(input(" Enter unit in F/f or C/c: "))

if unitinput == "C" or unitinput == "c":
  temperature2 = (temperature * 9/5) + 32
  print(f"{temperature}° in Celsius is equivalent to {temperature2}° Fahrenheit.\n")
elif unitinput == "F" or unitinput == "f":
  temperature2 = (temperature - 32) / 9.0 * 5
  print(f"{temperature}° in Fahrenehit is equivalent to {temperature2}° Celsius.\n")
else:
  print(f"Invalid unit({unitinput}).\n")

