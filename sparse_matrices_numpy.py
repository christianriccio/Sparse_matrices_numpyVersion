import numpy as np
import time 

def matrix(n):
    a = np.zeros((n, n))
    return a


def riempimento_matrice(matrice, elementi):
    flag = True 
    conta=0
    while flag == True:
        i = np.random.randint(0, matrice.shape[0])
        j = np.random.randint(0, matrice.shape[1])
        matrice[i][j] = np.random.randint(1,31)
        conta +=1
        if conta ==elementi:
            flag=False
        else: 
            flag =True
    return matrice


def prodotto(matrice1, matrice2):
    prod = np.dot(matrice1, matrice2)
    lista = []
    for elem in prod.ravel():
        if elem > 0:
            lista.append(elem)
    return np.array(lista)
            
    
def main():
    start =time.time()
    m1 = matrix(10**2)
    m2 = matrix(10**2)
    m1 = riempimento_matrice(m1, 100)
    m2 = riempimento_matrice(m2, 100)
    prod = prodotto(m1, m2)
    print(prod)
    fine = time.time()-start
    print('time to process', fine)

if __name__ == '__main__':
    main()
