import numpy as np
#Vetores: INTENSIDADE, UNITÁRIO, PRODUTO ESCALAR E VETORIAL, ANGULOS

def produto_escalar(vetor1, vetor2): #v1.v2
    return (vetor1[0]*vetor2[0]+vetor1[1]*vetor2[1])

def intensidade(vetor): #||v|| norma do vetor
    return (np.sqrt(vetor[0]**2 + vetor[1]**2))

def vetorunit(vetor): #vetor unitário, norma = 1
    comprimento = intensidade(vetor)
    unitvec = [vetor[0]/comprimento, vetor[1]/comprimento]
    print("intesidade do vetor unitario", intensidade(unitvec))
    if round(intensidade(unitvec)) == 1:
        print("Comprimento =", comprimento, "e o vetor unitario é", unitvec)

def getangle(vetor1, vetor2): #angulo entre vetores
    intensitidadevet1 = intensidade(vetor1)
    intensitidadevet2 = intensidade(vetor2)
    escalar = produto_escalar(vetor1, vetor2)
    angle = np.arccos(escalar/(intensitidadevet1*intensitidadevet2))
    print("Intensidade vetor1", vetor1, "=", intensitidadevet1)
    print("Intensidade vetor2", vetor2, "=", intensitidadevet2)
    print("Produto escalar = ", escalar)
    print("angulo =", angle*(180/np.pi), "º (", angle, "radians )")

def produto_vetorial(vetor1,vetor2): #v1 x v2
    produto_vetorial = np.cross(vetor1,vetor2)
    return produto_vetorial
    
#---------------------------------------------------------------------------------------------------------------#
#1 EXEMPLOS
#vec = np.array([3,4])
#print(intensidade(vec))
#vetorunit(vec)
#vec2 = 2*vec
#print(intensidade(vec2))
#---------------------------------------------------------------------------------------------------------------#

#2
#vec1 = np.array([1,2])
#vec2 = np.array([-2,3])
#getangle(vec1,vec2)

#---------------------------------------------------------------------------------------------------------------#

#3
#vec1 = np.array([1,2])
#vec2 = np.array([-2,1])
#getangle(vec1,vec2)

#---------------------------------------------------------------------------------------------------------------#

#4
#vec = np.array([3,4]) 
#vec2 = np.array([-4,3])  
#print(produto_escalar(vec,vec2))


#---------------------------------------------------------------------------------------------------------------#

#5
#vec = np.array([2,1.2]) 
#vec2 = np.array([-3,5.1])  
#vec3 = vec+vec2
#print(vec3)
#print(intensidade(vec3))

#---------------------------------------------------------------------------------------------------------------#

#6
#vecy = np.sqrt(6**2-2**2)
#vec = np.array([2,vecy])
#print(intensidade(vec))

#---------------------------------------------------------------------------------------------------------------#

#7
#vec1 = np.array([1,2])
#vec2 = np.array([-2,1])
#print(produto_vetorial(vec1,vec2))

    