# -*- coding: utf-8 -*-
#------------------------------------------------------------------

PONTUAÇÃO = ' .?!,;:()—"()'

def testes():

    print("Testes da classe Pilha")
    pil = Pilha()   ## cria uma Pilha vazia
    print(f"pil.dados = {pil.dados}  --> deve ser a lista vazia []")
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser True")
    pil.empilhe('todos')
    pil.empilhe(4)
    pil.empilhe('paz')
    # Pilha.topo() apenas pega o valor no topo mas sem desempilher
    print(f"pil.topo() = {pil.topo()}  --> deve ser 'paz'") 
    pil.empilhe(True)
    print(f"len(pil) = {len(pil)} --> deve ser 4")  ## implemente o método __len__
    print(f"pil.vazia() = {pil.vazia()}  --> deve ser False")
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz', True]")
    pil.empilhe(2.7)
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser 2.7")
    print(f"pil.desempilhe() = {pil.desempilhe()} --> deve ser True")
    print(f"len(pil) = {len(pil)} --> deve ser 3") 
    print(f"pil.dados = {pil.dados}  --> deve ser ['todos', 4, 'paz']")
    
    print()
    print("Testes da função palindromo()")
    print(f'MUTUM = {palindromo("MUTUM")}')
    print(f'Amor a Roma = {palindromo("Amor a Roma")}')
    print(f'Neuquén = {palindromo("Neuquén")}')
    print(f'Lava esse aval = {palindromo("Lava esse aval")}')
    print(f'A cara rajada da jararaca = {palindromo("A cara rajada da jararaca")}')
    print(f'O lobo ama o bolo = {palindromo("O lobo ama o bolo")}')
    print(f'Olé! Maracujá, caju, caramelo! = {palindromo("Olé! Maracujá, caju, caramelo!")}')
    print(f'Socorram-me, subi no ônibus em Marrocos! = {palindromo("Socorram-me, subi no ônibus em Marrocos!")}')
    print(f'anilina = {palindromo("anilina")}')
    print(f'A babá baba = {palindromo("A babá baba")}')
    print(f'A diva em Argel alegra-me a vida. = {palindromo("A diva em Argel alegra-me a vida.")}')
    print(palindromo('A porta rangia à ignara tropa.'))
    print(palindromo('Acata o danado... e o danado ataca!'))
    print(palindromo('Amo Omã. Se Roma me tem amores, amo Omã!'))
    print(palindromo('Som, só com o cosmos!'))
    print(palindromo('Ser belo: lebres.'))
    print(palindromo('Banana'))
    print(palindromo('Ratoeira'))
    

## ==================================================================
## Escreva a sua função palindromo()

def palindromo( s ):
    ''' (str) -> bool
    Recebe uma string e retorna True caso a string seja um palíndromo, 
    e False caso contrário.
    
    Palíndromos são palavras, frases ou números que são iguais quando lidas de
    trás para frente. 
    
    Exemplo: a string 'asa' retornará True.
    '''    
    original = Pilha()
    original_copia = Pilha()
    inversa = Pilha()
    # remove acentos, pontuações e letras maiúsculas da string 's'.
    s = limpa_letras(s)
    s = tira_pontuacoes(s)

    for i in range(len(s)):
        # empilha cada letra da string 's' nas pilhas original e 
        # original_copia, desconsiderando espaçamentos ' '.
        if (s[i] != ' '):
            original.empilhe(s[i])
            original_copia.empilhe(s[i])

    for j in range(len(original)):
        letra = original_copia.desempilhe()
        inversa.empilhe(letra)

    for k in range(len(original)):
        if original.dados[k] != inversa.dados[k]:
            return False
    return True 
   


## ==================================================================
##
class Pilha:

    def __init__(self):
        '''(Pilha) -> None
        Chamado pelo construtor da classe. 

        Recebe uma referência `self` ao objeto que está sendo
        construído e
        '''
        self.dados = []
    
    def vazia(self):
        ''' (Pilha) -> bool
        Testa se a pilha está vazia
        Recebe uma referência `self` ao objeto do tipo Pilha
        e retorna True se a pilha estiver vazia, e False caso contrário.
        '''
        return self.dados == []
    
    def empilhe(self, item):
        ''' (Pilha, obj) -> None
        Insere um novo item na pilha.
        '''
        self.dados.append(item)
        
    
    def desempilhe(self):
        ''' (Pilha) -> obj
        Remove o item do topo da pilha
        Recebe e retorna o item do topo da pilha.
        '''
        return self.dados.pop()
    
    def topo(self):
        ''' (Pilha) -> obj
        Retorna o item no topo da pilha mas não o remove da pilha
        '''
        return self.dados[-1]
    
    def __len__(self):
        '''(Pilha) -> int
        Retorna o número de itens da pilha
        '''
        return len(self.dados)

## ==================================================================
## Escreva outras funções e classes caso desejar
def limpa_letras( s ):
    ''' string -> string
    verifica se há acentos em alguma vogal da string 's' e os remove.
    '''
    s = s.replace('â','a')
    s = s.replace('á','a')
    s = s.replace('à','a')
    s = s.replace('ã','a')
    s = s.replace('ê','e')
    s = s.replace('é','e')
    s = s.replace('è','e')
    s = s.replace('í','i')
    s = s.replace('î','i')
    s = s.replace('ì','i')
    s = s.replace('ô','o')
    s = s.replace('ó','o')
    s = s.replace('ò','o')
    s = s.replace('õ','o')
    s = s.replace('ú','u')
    s = s.replace('ù','u')
    s = s.replace('û','u')
    s = s.replace('ü','u')
    s = s.replace('ç','c')
    return s.lower()
#------------------------------------------------------------
def tira_pontuacoes(s):
    '''string -> string
    Remove pontuações e sinais da string 's' e a retorna.
    '''
    s = s.replace('.','')
    s = s.replace(',','')
    s = s.replace(':','')
    s = s.replace('-','')
    s = s.replace('_','')
    s = s.replace('?','')
    s = s.replace('!','')
    s = s.replace(';','')
    s = s.replace('"','')
    s = s.replace('”','')
    s = s.replace('“','')
    s = s.replace('(','')
    s = s.replace(')','')
    s = s.replace('[','')
    s = s.replace(']','')
    s = s.replace('/','')
    return s

## ==================================================================
if __name__ == '__main__':
    palindromo( '' )
    
if __name__ == '__main__':
    testes()

