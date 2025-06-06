def convert_cel_to_fah( c ):
	F = c * 9/5 + 32
	return F 

def convert_fah_to_cel( F ):
	Ce = (F - 32) * 5/9
	return Ce 

c1 = input("Enter the Temperature in Celcius ")
print(f"The Temperature in fahrenheit is " + str(round(convert_cel_to_fah(float(c1)) , 2 ) ) )

f1 = input("Enter the Temperature in fahrenheit ")
print(f"The Temperature in Celcius is " + str(round(convert_fah_to_cel(float(f1)) , 2) ) )
