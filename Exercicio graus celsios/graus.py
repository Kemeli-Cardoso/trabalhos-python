"""
Escreva um programa que converta uma temperatura de um padrão a outro usando estas fórmulas:

Celsius para Fahrenheit: °F = 9/5 (°C) + 32
Kelvin para Celsius: °C = K - 273,15
Fahrenheit para Kelvin: K = 5/9 (°F - 32) + 273,15
O Programa deve perguntar a temperatura em Celsius e exibir a temperatura em Kelvin e  Fahrenheit
"""
celsius= float(input("Digite os graus celsius: "))
fahrenheit= (9/5)*celsius+32
kelvin= 5/9*(fahrenheit-32)+273.15

print(f"A temperatura em Fahrenheit é de: {fahrenheit}")
print(f"A temperatura em kelvin é de: {kelvin}")