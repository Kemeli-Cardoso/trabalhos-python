funcionario=int(input("Digite o numero do funcionário: "))
horas=float(input("Digite a quantidade de horas trabalhadas: "))
valorhora=float(input("digite o valor da hora: "))
Filhos14= int(input("Digite o numero de filhos até 14 anos: "))
sf= 56.59*Filhos14
sb= horas*valorhora
inss= ((sb)/100)*8.5
ir=1
if sb>1500:
    ir=((sb-inss)/100)*15
elif sb>500.00 and sb<1500:
    ir= ((sb-inss)/100)*8
elif sb<500:
    ir=0

print (f"Funcionario nº: {funcionario:.2f}")
print (f"Salario bruno: {sb+sf:.2f}")
print (f"O valor total de descontaos é de {inss+ir:.2f}")
print (f"O salario liquido é de: R$ {sb-inss-ir+sf:.2f}")

