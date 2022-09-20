from errno import ELOCKUNMAPPED


valor1=float(input("Digite o valor 1: "))
valor2=float(input("Digite o valor 2: "))
valor3=float(input("Digite o valor 3: "))
if valor1>0:
    print(f"{valor1**0.5}")
elif valor1<0:
    print(f"{valor1**0.5}")
elif valor2>10 and valor2<100:
    print("Número esta entre 10 e 100 - intervalo permitido.")
elif valor3<valor2:
    print (f"{valor2-valor3}")
elif valor3>valor2:
    print(f"{valor3+valor2}")
