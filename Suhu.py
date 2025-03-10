def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
    
celsius = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} derajat Celcius sama dengan {fahrenheit} derajat Fahrenheit.")
