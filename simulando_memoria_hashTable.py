import os 
#import sys


# Teste para verificar a extensão do ariquivo
name,extension = os.path.splitext('C:\\Users\\dany_\\Desktop\\Hash_Table\\cdagger.cd')

if(extension == '.cd'):
    print(extension)

# Teste para verificar a extensão do ariquivo

def criarMemoria(arquivo, tamMemoria):
    with open(arquivo,'w') as f:
        for x in range(tamMemoria):
            f.write(f'{x}.None.None\n')

def getMemoria(arquivo):
    with open(arquivo,'r') as f:
        fileLine = f.readlines()
    return fileLine

def substituir(arquivo, chave, dado, pos):
    with open(arquivo, 'r') as file:
        data = file.readlines()
    i = 0
    while(i < len(data)):
        d = data[i].split('.')
        
        if(int(d[0]) == pos):
            d[1] = chave
            d[2] = dado
            data[i] = f'{d[0]}.{d[1]}.{d[2]}\n'
            
            break
        i +=1
    with open(arquivo,'w') as file:
        for x in data:
            file.write(x)

# criarMemoria('cdagger.cd', 18)

# print(getMemoria('cdagger.cd'))

# substituir('cdagger.cd', 'chave', 'dado', 5)

# print(getMemoria('cdagger.cd'))

class Hash:
    def __init__(self, tamTabela, nomeArquivo):
        self.tamTabela = tamTabela 
        criarMemoria('cdagger.cd', tamTabela)
        
    def funcaoHash(self, chave):
        return chave % self.tamTabela
    
    def atualizaHash(self, chaveAntiga):
        return (chaveAntiga+1)%self.tamTabela
    
    def adiciona(self,chave,dado):
        valorHash = self.funcaoHash(chave)
        memoria = getMemoria('cdagger.cd')
        
        if 'None.None' in memoria[valorHash]:
            substituir('cdagger.cd', chave, dado, valorHash)
        else:
            if memoria[valorHash].split('.')[1] == chave:
                substituir('cdagger', chave,dado,valorHash)
            else:
                proximo=self.atualizaHash(valorHash)
                while not('None.None' in memoria[proximo]) and memoria[proximo].split('.')[1] != chave:
                    proximo = self.atualizaHash(proximo)
                
                if 'None.None' in memoria[proximo]:
                    substituir('cdagger.cd', chave, dado, proximo)
                else:
                    memoria[proximo] = dado
    
    def busca(self, chave):
        chaveInicial = self.funcaoHash(chave)
        memoria = getMemoria('cdagger.cd')

        posicao = chaveInicial
        
        while not('None.None' in memoria[posicao]):
            if(int(memoria[posicao].split('.')[1]) == chave):
                return memoria[posicao].split('.')[2]
            posicao = self.atualizaHash(posicao)
        return None
           

       

hash = Hash(11, 'cdagger.cd')

hash.adiciona(54, 'ola mundo')
hash.adiciona(26,'arvore')
hash.adiciona(77, 'penultimo')
hash.adiciona(31,'ola' )
hash.adiciona(44,'ola1' )
hash.adiciona(55,'ola2' )
hash.adiciona(20,'ola3' )

print(hash.busca(26))


