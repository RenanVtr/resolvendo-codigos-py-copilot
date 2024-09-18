#Vamos testar se uma palavra é um palíndromo?!

print("Vamos testar se uma palavra é um palíndromo?!")
palavra = input("Digite a palavra: ")

palavra_invertida = palavra[::-1]

if (palavra_invertida == palavra) :
    print(f"A palavra {palavra} é um palindromo!")
else :
    print(f"A palavra {palavra} não é um palindromo")