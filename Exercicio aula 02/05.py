cod_funcionario= input("Digite o código do funcionário: ")
horas_trabalhadas=int(input("Digite o número de horas trabalhadas: "))
valor_por_hora_trab=float(input("Digite o valor da hora trabalhada: "))
salario=horas_trabalhadas*valor_por_hora_trab
print(f"O salário do funcionário {cod_funcionario} é R${salario:.2f}")



#:.2f determina que o valor de casas decimal é 2, pode alterar o numoro de acordo com as casa que quer