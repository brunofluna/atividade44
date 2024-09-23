from dataclasses import dataclass
# Java_lizando o Python, e ficou uma coisa muito paia.
@dataclass
class Pessoa:
    # atributos
    nome: str
    idade: int
    altura: float
    def __str__(self):
        return f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e {self.altura} metros de altura.'

    # destrutor
    def __del__(self):
        return f'{self.nome} destruido com sucesso.'