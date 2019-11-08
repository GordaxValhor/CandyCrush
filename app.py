import numpy as np

#declarare matrice

M= np.random.randint(5, size=(6,6))
rows = M.shape[0]
cols = M.shape[0]

#functii
def culoare(i,j):
    alb =  '\u001b[30m'
    galben =  '\u001b[33m'
    rosu ='\u001b[31m'
    verde ='\u001b[32m'
    albastra ='\u001b[34m'
    if(M[i,j]==0):
        return alb
    if(M[i,j]==1):
        return rosu
    if(M[i,j]==2):
        return galben
    if(M[i,j]==3):
        return verde
    if(M[i,j]==4):
        return albastra

def afisareM(rows,cols):
    for i in range(0, rows):
        for j in range(0, cols):
            culoare(i,j)
            print(culoare(i,j),M[i,j],end=' ')
        print('\n')
#main
print('Matricea generata random:\n')
afisareM(rows,cols)
