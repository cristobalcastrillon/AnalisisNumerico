import numpy as np

n = 3                      
a = []                      
b = []   

def seidel(a, x, b): 
          
    n = len(a)                    
    
    for j in range(0, n):         
        d = b[j]                   
        for i in range(0, n):      
            if(j != i): 
                d-=a[j][i] * x[i]         
        x[j] = d / a[j][j] 
        para=(b[j]-d)/ a[j][j]
        if x[j]==para:
          print("PARAAAAAAAAAAAAAR")     
    return x     

def matrizTransicionGS(a):
  #d (diagonal).
  d = np.diag(a)
  d = np.diag(d)
  if(not(np.linalg.det(d))): #Evaluando que tenga inversa...
    return
  dInv = np.linalg.inv(d)
  #l (lower): matriz inferior triangular.
  l = np.tril(a)
  #u (upper): matriz superior triangular.
  u = np.triu(a)
  ident = np.identity(len(a))
  dInv_l = np.dot(dInv, l)
  _dInv_u = np.dot(-dInv, u)
  if(not(np.linalg.det(_dInv_u))): #Evaluando que tenga inversa...
    return
  else:
    if(np.linalg.det(ident + dInv_l)): #Evaluando que tenga inversa...
      t = np.dot(np.linalg.inv(ident + dInv_l), _dInv_u)
      return(t)
    return

def radioEspectral(a):
  t = matrizTransicionGS(a)
  eigenValues = np.linalg.eigvals(t)
  #Calcular y retornar el valor máximo de 'eigenValues'.
  return max(eigenValues)
    
x = [0, 0, 0]                         
a = [[4, 3, 0],[3, 4, -1],[0, -1, 4]] 
#a1: matriz idéntica a 'a' para radio espectral.
a1 = np.array([[4, 3, 0],
              [3, 4, -1],
              [0, -1, 4]])
a2 = [[4, 3, -2],[3, 4, -1],[0, -1, 4]] 
b = [0.254,-1.425,2.978] 

print("PUNTO 2:\n")
print("PUNTO A  ")
print(radioEspectral(a1), '\n\n\n')

print("PUNTO B  ")  
for i in range(0, 25):        
    x = seidel(a, x, b) 
    print(i,x) 
print('\n\n\n')

print("PUNTO C  ")
for i in range(0, 25):        
    x = seidel(a2, x, b) 
    print(i,x) 
