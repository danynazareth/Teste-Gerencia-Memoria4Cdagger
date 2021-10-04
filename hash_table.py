import os

'''
Referência:

https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/Hashing.html
'''
class Hash:
    def __init__(self, tamTabela, nomeArquivo, tamMemoria):
        self.tamTabela = tamTabela
        self.tamMemoria = tamMemoria
        self.chaves = [None] * self.tamTabela
        self.dados = [None] * self.tamTabela
        
        
        
    
    def funcaoHash(self, valorChave):
        return valorChave % self.tamTabela
    
    def atualizaHash(self,hashAntiga):
        return (hashAntiga+1) % self.tamTabela
    
    def adicionar(self, chave, dado):
        valorHash = self.funcaoHash(chave)
        
        if self.chaves[valorHash] == None:
            self.chaves[valorHash] = chave
            self.dados[valorHash] = dado
            
        else:
            if self.chaves[valorHash] == chave:
                self.dados[valorHash] = dado
            else:
                proximo = self.atualizaHash(valorHash)
                while self.chaves[proximo] != None and self.chaves[proximo] != chave:
                    proximo = self.atualizaHash(proximo)
                    
                if self.chaves[proximo] == None:
                    self.chaves[proximo] = chave
                    self.dados[proximo] = dado
                else:
                    self.dados[proximo] = dado
                    
                    
    def busca(self, chave):
        inicialChave = self.funcaoHash(chave)
        
        dado = None
        stop = False
        dadoEncontrado =  False
        
        posicao = inicialChave
        
        while self.chave[posicao] != None and not dadoEncontrado and not stop:
            if self.chaves[posicao] == chave:
                dadoEncontrado = True
                dado = self.dados[posicao]
            else:
                posicao = self.atualizaHash(posicao)
                if posicao == inicialChave:
                    stop = True
        return dado

    def retornaChave(self, chave):
        return self.busca(chave)
    def alteraChave(self, chave, dado):
        self.adicionar(chave, dado)
    def __getitem__(self, chave):
        return self.busca(chave)
    def __setitem__(self, chave, dado):
        self.adicionar(chave, dado)


H=Hash(11)
H[54]="cat"
H[26]="dog"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
# print(H.chaves)
# print(H.dados)

