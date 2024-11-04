#Defining function for tempretur conversion
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Test function with given temperatures using a loop
temperatures_celsius = [22, 46, 51, 76]
for temp in temperatures_celsius:
    print(f"{temp}C is {celsius_to_fahrenheit(temp)}F")
