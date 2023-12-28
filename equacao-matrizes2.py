import numpy as np
l=int(input('digite o numero de linhas: '))
c=int(input('digite o numero de colunas: '))
vetor1=[]
vetor2=[]
matrix1=[]
matrix2=[]
def gerar_vetor1():
    if l==1 and c==2:
        for i in range(0,2):
            n=float(input('digite um numero: '))
            vetor1.append(n)
        matrix1.append(vetor1)
        print(matrix1)
        
    elif l==2 and c==1:
        for i in range(0,2):
            n=float(input('digite um numero: '))
            vetor1.append(n)
        matrix1.append(vetor1)
        print(matrix1)
    elif l==1 and c==3:
        for i in range(0,3):
            n=float(input('digite um numero: '))
            vetor1.append(n)
        matrix1.append(vetor1)
        print(matrix1)
    elif l==3 and c==1:
        for i in range(0,3):
            n=float(input('digite um numero: '))
            vetor1.append(n)
        matrix1.append(vetor1)
        print(matrix1)
l=int(input('digite o numero de linhas: '))
c=int(input('digite o numero de colunas: '))    
def gerar_vetor2():
    if l==1 and c==2:
        for i in range(0,2):
            n=float(input('digite um numero: '))
            vetor2.append(n)
        matrix2.append(vetor2)
        print(matrix2)
        
    elif l==2 and c==1:
        for i in range(0,2):
            n=float(input('digite um numero: '))
            vetor2.append(n)
        matrix2.append(vetor2)
        print(matrix2)
    elif l==1 and c==3:
        for i in range(0,3):
            n=float(input('digite um numero: '))
            vetor2.append(n)
        matrix2.append(vetor2)
        print(matrix2)
    elif l==3 and c==1:
        for i in range(0,3):
            n=float(input('digite um numero: '))
            vetor2.append(n)
        matrix2.append(vetor2)
        print(matrix2)        
gerar_vetor1()
gerar_vetor2()
array=np.array(matrix1)
array2=np.array(matrix2)
print(array)
print(array2)
def operacao_vetor(array,array2):
    print('as operacoes:  + -  x ou escalar  ')
    operacao=str(input('insira a operacão:  '))
    if operacao=="soma":
        soma=array + array2
        print(soma)
    elif operacao=="multiplicacao":
        multiplicacao=array1*array2
        print(soma)
    elif operacao=="escalar":
        print('1 para o array 1')
        print('2 para o array 2')
        opcao=int(input('escolha o array: '))
        if opcao==1:
            escalar=int(input('insira o escalar: '))
            print(array*escalar)
            
        elif opcao==2:
            escalar=int(input('insira o escalar:'))
            print(array2*escalar)
    else:
        subtracao=array-array2
        print(subtracao)
        
operacao_vetor(array,array2)       