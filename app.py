import numpy as np

#declarare matrice

M= np.random.randint(5, size=(6,6))
rows = M.shape[0]
cols = M.shape[0]
print(cols)
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
def cautare_p():
    for i in range(0,rows):
        print('\ni:',i)
        for j in range(0,cols):
            if(M[i,j]!=0):
                if(j<cols-1):
                    k=j+1
                    nr_c = 1 #numar de cifre consecutive egale
                    while(M[i,j]==M[i,k] and k<cols-1):
                        nr_c=nr_c+1
                        k+=1
                        if(k==cols-1 and M[i,j]==M[i,k]):
                            nr_c=nr_c+1
                    print('nr_c',nr_c,end=" ")
                    if(nr_c>=3):
                        if(k==cols-1 and M[i,j]==M[i,k]):
                            k+=1
                        poz_s=j
                        poz_f=k
                        linie=i
                        eliminare_p(poz_s,poz_f,linie)
                        print("GASIT")

def eliminare_p(start,finish,linie):
    for j in range(start,finish):
        M[linie][j]=0
    print('LINIE:',linie)
    for j in range(start,finish):
        for i in range(linie,-1,-1):
            print(i)
            if(M[i][j]!=0):
                if(M[i+1][j]==0):
                    print('da')
                    nr=2
                    ok=1
                    while(ok!=0):
                        if(M[nr][j]==0):
                            ok=1
                            nr+=1
                        else: ok=0
                    M[nr+1][j]==M[i][j]
                else:
                    M[i+1][j]=M[i][j]
                    M[i][j]=0


def afisareM(rows,cols):
    for i in range(0, rows):
        for j in range(0, cols):
            culoare(i,j)
            print(culoare(i,j),M[i,j],end=' ')
        print('\n')
#main
print('Matricea generata random:\n')
afisareM(rows,cols)
cautare_p()
print('\nAfisare dupa eliminare p:\n')
afisareM(rows,cols)
cautare_p()
print('\nAfisare dupa eliminare p:\n')
afisareM(rows,cols)
