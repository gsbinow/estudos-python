import math

print('-'*40)
print('Bem vindo ao operador de raizes!')
print('-'*40)
while True:

    # 1. Entrada de dados
    num = float(input("Digite o número que deseja calcular as raízes: "))
    limite = int(input("Até qual ordem de raiz você deseja ver (ex: 10)? "))

    print(f"\n--- Tabuada de Radiciação para o número {num} ---")

    # 2. Laço de repetição para gerar a "tabuada"
    for ordem in range(2, limite + 1): # ( inicio | fim )
        # Calculando a raiz de ordem 'ordem'
        # Usamos 1/ordem como expoente
        resultado = math.pow(num, 1 / ordem)

        # 3. Exibição formatada
        print(f"Raiz de ordem {ordem:2}: {resultado:.4f}")

    print("-" * 45)