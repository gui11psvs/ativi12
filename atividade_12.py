# Crie um programa que receba a nota de um aluno e informe se ele foi aprovado ou reprovado. Considere que a média para aprovação é 7.
def verificar_aprovacao(nota):
    if nota >= 7:
        return "aprovaçao"
    else:
        return "reprovaçao"

try:
    nota = float(input("digete a nota do aluno: "))

    if 0 <= nota <= 10:
        situacao = verificar_aprovacao(nota)
        print(f"o aluno com {nota} foi {situacao}.")
    else:
        print("a nota deve estar entre 0 a 10.")
except valueerror:
    print("por favor, insirs um valor numérico válido para a nota.")
    
