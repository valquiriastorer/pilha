# Classe Pilha

> Este programa foi realizado como exercício de programação para a disciplina de Princípios de Desenvolvimentos de Algoritmos (MAC0122) oferecida pela Universidade de São Paulo em 2021, ministrada pelos professores José Coelho de Pina Junior e Carlos Hitoshi Morimoto.

## Descrição

O objetivo deste exercício é introduzir o tipo abstrato de dados conhecido como pilha (stack). 

Uma pilha (=stack) é uma estrutura linear dinâmica em que todas as operações:

inserções;
remoções; e
consultas
são feitas em uma mesma extremidade chamada de topo da pilha, como ilustrado abaixo.

  empilha --->---+       +-->----> desempilha
  (=push)        |       |         (=pop)  
                 V       |
               +-----------+
               | vvvvvvvvv |
               +-----------+
               | wwwwwwwww |
               +-----------+
               | zzzzzzzzz |
               +-----------+
               | yyyyyyyyy |
               +-----------+
               | xxxxxxxxx |
               +-----------+

Neste exercício foi implementada a classe Pilha e a função palindromo(), explicada a seguir.

##### Função palindromo()

Palíndromo é uma palavra, frase ou número que permanece igual quando lida de trás para diante. Por extensão, palíndromo é qualquer série de elementos com simetria linear, ou seja, que apresenta a mesma sequência de unidades nos dois sentidos.

No mesmo arquivo pilha.py, se encontra a função palindromo() que recebe uma string e retorna True caso a string seja um palíndromo, e retorna False caso contrário. 
