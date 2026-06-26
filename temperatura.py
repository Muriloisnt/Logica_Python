
def fahrenheit_para_celsius(f):
    """Converte temperatura de Fahrenheit para Celsius"""
    Celsius = (f - 32) * 5 / 9
    return Celsius
temp = 98
celsius = fahrenheit_para_celsius(temp)
print(celsius)


temp_f = 98.6
resultado = fahrenheit_para_celsius(temp_f)
print(f'(temp_f)°F equivalem a {resultado:.2f}°C')

print(fahrenheit_para_celsius(32))
print(fahrenheit_para_celsius(212))