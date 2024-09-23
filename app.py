from modulo import *

if __name__ == "__main__":
    usuario = Pessoa('',0,0.0)

    usuario.nome = input('Digite o nome: ')
    usuario.idade = int(input('Digite a idade: '))
    usuario.altura = float(input('Digite a altura: ').replace(',', '.'))

    print(str(usuario))