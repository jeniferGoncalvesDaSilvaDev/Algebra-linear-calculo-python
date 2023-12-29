import numpy as np
matrix=[]
matrix2=[]
vetor=[]
vetor2=[]
vetor3=[]
vetor4=[]
vetor5=[]
vetor6=[]
vetor7=[]
vetor8=[]
vetor9=[]
vetor10=[]
vetor11=[]
vetor12=[]
def gerar_matrix():
      ordem=int(input('insira a ordem: '))
      if ordem==2:
          for i in range(0,2):
              n=float(input('insira um numero: '))
              vetor.append(n)
          
          
          for i in range(0,2):
              n=float(input('insira um numero: '))
              vetor2.append(n)
          matrix.append(vetor)
          matrix.append(vetor2)
          print(matrix)
          global array
          array=np.array(matrix)
          print(array)
      elif ordem==3:
           for i in range(0,3):
               n=float(input('insira um numero: '))
               vetor.append(n)
          
          
           for i in range(0,3):
              n=float(input('insira um numero: '))
              vetor2.append(n)
           for i in range(0,3):
              n=float(input('insira um numero: '))
              vetor3.append(n)
           matrix.append(vetor)
           matrix.append(vetor2)
           matrix.append(vetor3)
          
           print(matrix)
           array=np.array(matrix)
           print(array)
      elif ordem==4:
           for i in range(0,4):
               n=float(input('insira um numero: '))
               vetor.append(n)
          
          
           for i in range(0,4):
              n=float(input('insira um numero: '))
              vetor2.append(n)
           for i in range(0,4):
              n=float(input('insira um numero: '))
              vetor3.append(n)
           
           for i in range(0,4):
              n=float(input('insira um numero: '))
              vetor4.append(n)
           matrix.append(vetor)
           matrix.append(vetor2)
           matrix.append(vetor3)
           matrix.append(vetor4)
          
           print(matrix)
           array=np.array(matrix)
           print(array)
      elif ordem==5:
           for i in range(0,5):
               n=float(input('insira um numero: '))
               vetor.append(n)
          
          
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor2.append(n)
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor3.append(n)
           
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor4.append(n)
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor5.append(n)
           matrix.append(vetor)
           matrix.append(vetor2)
           matrix.append(vetor3)
           matrix.append(vetor4)
           matrix.append(vetor5)
          
           print(matrix)
           array=np.array(matrix)
           print(array)
      elif ordem==6:
          for i in range(0,6):
               n=float(input('insira um numero: '))
               vetor.append(n)
          
          
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor2.append(n)
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor3.append(n)
           
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor4.append(n)
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor5.append(n)
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor6.append(n)
          matrix.append(vetor)
          matrix.append(vetor2)
          matrix.append(vetor3)
          matrix.append(vetor4)
          matrix.append(vetor5)
          matrix.append(vetor6)
          
          print(matrix)
          array=np.array(matrix)
          print(array)
      else:
          print('ordem errada!')


def gerar_matrix2():
       ordem=int(input('insira a ordem: '))
       if ordem==2:
          for i in range(0,2):
              n=float(input('insira um numero: '))
              vetor7.append(n)
          
          
          for i in range(0,2):
              n=float(input('insira um numero: '))
              vetor8.append(n)
          matrix2.append(vetor7)
          matrix2.append(vetor8)
          print(matrix2)
          global array2
          array2=np.array(matrix2)
          print(array2)
       elif ordem==3:
           for i in range(0,3):
               n=float(input('insira um numero: '))
               vetor7.append(n)
          
          
           for i in range(0,3):
              n=float(input('insira um numero: '))
              vetor8.append(n)
           for i in range(0,3):
              n=float(input('insira um numero: '))
              vetor9.append(n)
           matrix2.append(vetor7)
           matrix2.append(vetor8)
           matrix2.append(vetor9)
          
           print(matrix2)
           array2=np.array(matrix2)
           print(array2)
       elif ordem==4:
           for i in range(0,4):
               n=float(input('insira um numero: '))
               vetor7.append(n)
          
          
           for i in range(0,4):
              n=float(input('insira um numero: '))
              vetor8.append(n)
           for i in range(0,4):
              n=float(input('insira um numero: '))
              vetor9.append(n)
           
           for i in range(0,4):
              n=float(input('insira um numero: '))
              vetor10.append(n)
           matrix2.append(vetor7)
           matrix2.append(veto8)
           matrix2.append(vetor9)
           matrix2.append(vetor10)
          
           print(matrix2)
           array2=np.array(matrix2)
           print(array2)
       elif ordem==5:
           for i in range(0,5):
               n=float(input('insira um numero: '))
               vetor7.append(n)
          
          
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor8.append(n)
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor9.append(n)
           
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor10.append(n)
           for i in range(0,5):
              n=float(input('insira um numero: '))
              vetor11.append(n)
           matrix2.append(vetor7)
           matrix2.append(vetor8)
           matrix2.append(vetor9)
           matrix2.append(vetor10)
           matrix2.append(vetor11)
          
           print(matrix2)
           array2=np.array(matrix2)
           print(array2)
       elif ordem==6:
          for i in range(0,6):
               n=float(input('insira um numero: '))
               vetor7.append(n)
          
          
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor8.append(n)
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor9.append(n)
           
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor10.append(n)
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor11.append(n)
          for i in range(0,6):
              n=float(input('insira um numero: '))
              vetor11.append(n)
          matrix2.append(vetor7)
          matrix2.append(vetor8)
          matrix2.append(vetor9)
          matrix2.append(vetor10)
          matrix2.append(vetor11)
          matrix2.append(vetor12)
          
          print(matrix2)
          array=np.array(matrix2)
          print(array2)
       else:
          print('ordem errada!')
       
    


#gerar_matrix() 
#gerar_matrix2()


igualdade=[]
igualdade2=[]

def igualdade_matrix():
    n=int(input('quantas igualdades: '))  
    if n==2:
        for i in range(0,2):
            v=float(input('insira a igualdade: '))
            igualdade.append(v) 
        print(igualdade)
    elif n==3:
        for i in range(0,3):
            v=float(input('insira a igualdade: '))
            igualdade.append(v) 
        print(igualdade)
    elif n==4:
        for i in range(0,4):
            v=float(input('insira a igualdade: '))
            igualdade.append(v) 
        print(igualdade)
    elif n==5:
        for i in range(0,5):
            v=float(input('insira a igualdade: '))
            igualdade.append(v) 
        print(igualdade)
    elif n==6:
        for i in range(0,6):
           v=float(input('insira a igualdade: '))
           igualdade.append(v) 
        print(igualdade)
    else:
        print('numero de igualdades invalidos')


def igualdade_matrix2():
    n=int(input('quantas igualdades: '))  
    if n==2:
        for i in range(0,2):
            v=float(input('insira a igualdade: '))
            igualdade2.append(v) 
        print(igualdade2)
    elif n==3:
        for i in range(0,3):
            v=float(input('insira a igualdade: '))
            igualdade2.append(v) 
        print(igualdade2)
    elif n==4:
        for i in range(0,4):
            v=float(input('insira a igualdade: '))
            igualdade2.append(v) 
        print(igualdade2)
    elif n==5:
        for i in range(0,5):
            v=float(input('insira a igualdade: '))
            igualdade2.append(v) 
        print(igualdade2)
    elif n==6:
        for i in range(0,6):
           v=float(input('insira a igualdade: '))
           igualdade2.append(v) 
        print(igualdade2)
    else:
        print('numero de igualdades invalidos')
    

#igualdade_matrix()
#igualdade_matrix2()


def equacao_linear(array,igualdade):
    print('resultado do sistema de equação')
    res=np.linalg.solve(array,igualdade)
    print(res)
    print('o determimante da matrix ')
    deter=np.linalg.det(array)
    print(deter)
    
    
def equacao_linear2(array2,igualdade2):
    print('resultado do sistema de equação')
    res2=np.linalg.solve(array2,igualdade2)
    print(res2)
    print('o determimante da matrix ')
    deter2=np.linalg.det(array2)
    print(deter2)

    
    
    




def operacao_vetor(array,array2):
    print('as operacoes:  soma,  subtração,  multiplicação  ')
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
        
#operacao_vetor(array,array2)       
while True:
    print('resolução de equações matriciais e operação de matrizes')
    print('----------------------------------')
    print('1 para a matrix 1')
    print('2 para a matrix 2')
    print('3 para a matrix 1 e 2')
    print('m1 - para multiplicar o escalar com a matrix 1 ')
    print('m2 - para multiplicar o escalar com a matrix 2 ')
    print('ambas -  para multiplicar o escalar com a matrix 1 e 2')
    print('----------------------------------')
    comecar=str(input('vamos começar? s/n '))
    if comecar.lower()=='n':
        print('saindo')
        break 
    print('1 para a matrix 1')
    print('2 para a matrix 2')
    print('3 para a matrix 1 e 2')
    opcao=int(input('qual matrix? '))
    
    
    
    if opcao==1:
            gerar_matrix() 
            igualdade_matrix()
            equacao_linear(array,igualdade)
            
    elif opcao==2:
            gerar_matrix2()
            igualdade_matrix2()
            equacao_linear2(array2,igualdade2)
            
    elif opcao==3:
            gerar_matrix() 
            igualdade_matrix()
            gerar_matrix2()
            igualdade_matrix2()
            equacao_linear(array,igualdade)
            equacao_linear2(array2,igualdade2)
            operacao_vetor(array,array2)     
            
    
    
    
    
    continuar=str(input('vamos continuar? s/n '))
    if continuar.lower()=='n':
        print('saindo')
        break 
    opcao_escalar=str(input('deseja multiplicar por um escalar? s/n  '  ))
    if opcao_escalar.lower()=='n':
        print('saindo')
        break 
    
    print('m1 - para multiplicar o escalar com a matrix 1 ')
    print('m2 - para multiplicar o escalar com a matrix 2 ')
    print('ambas -  para multiplicar o escalar com a matrix 1 e 2')
    escalar=str(input('multiplicar qual matrix pelo escalar? '))
    if escalar=="m1":
            valor=float(input('digite o escalar: '))
            multiplicacao=array*valor
            print(multiplicacao)
    elif escalar=="m2":
            valor=float(input('digite o escalar: '))
            multiplicacao=array2*valor
            print(multiplicacao)
    elif escalar=="ambas":
            valor=float(input('digite o escalar: '))
            multiplicacao=array*valor
            valor2=float(input('digite o escalar: '))
            multiplicacao2=array2*valor2
            print(multiplicacao)
            print(multiplicacao2)
    
             
             
           
           
    
    
    
    
    
    
            
            
            
            
        
            