import numpy as np

#declarare matrice

M= np.random.randint(5, size=(11,11))
rows = M.shape[0]
cols = M.shape[0]
print(cols)
print(rows)

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

def cautare_p_l():
    for i in range(0,rows):
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
                    if(nr_c==3):
                        print('avem')
                        #pentru formele complexe L T
                        if(M[i,j]==M[i-1,j]):
                            #if(i>0):
                                w=i-1
                                nr_l = 1 #numar de cifre consecutive egale
                                while(M[i,j]==M[w,j] and w>0):
                                    nr_l=nr_l+1
                                    w-=1
                                    if(w==0 and M[i,j]==M[w,j]):
                                        nr_l=nr_l+1
                                print('linia:',i)
                                print('nr_l',nr_l)
                                if(nr_l==3):
                                    poz_s=j
                                    poz_f=k #k ==3 deci k o sa fie finish pentru ambele foruri
                                    linie=i
                                    ce='1'
                                    print(poz_f)
                                    eliminare_p_c(poz_s,poz_f,linie,ce)
                        elif(M[i,j]==M[i-1,j+2]):
                                #if(i>0):
                                w=i-1
                                nr_l = 1 #numar de cifre consecutive egale
                                while(M[i,j+2]==M[w,j+2] and w>0):
                                    nr_l=nr_l+1
                                    w-=1
                                    if(w==0 and M[i,j]==M[w,j+2]):
                                        nr_l=nr_l+1
                                print('linia:',i)
                                print('nr_l',nr_l)
                                if(nr_l==3):
                                    poz_s=j
                                    poz_f=k # k reprezinta POZITIA deci k o sa fie finish pentru ambele foruri
                                    linie=j
                                    ce='2'
                                    print(poz_f)
                                    eliminare_p_c(poz_s,poz_f,linie,ce)
                        if(i<rows-2):
                            if(M[i,j]==M[i+1,j]):
                                w=i+1
                                nr_l = 1 #numar de cifre consecutive egale
                                while(M[i,j]==M[w,j] and w<rows-1):
                                    nr_l=nr_l+1
                                    w+=1
                                    if(w==rows-1 and M[i,j]==M[w,j]):
                                        nr_l=nr_l+1
                                print('linia:',i)
                                print('nr_l',nr_l)
                                if(nr_l==3):
                                    poz_s=j
                                    poz_f=k # k reprezinta POZITIA deci k o sa fie finish pentru ambele foruri
                                    linie=i
                                    ce='3'
                                    print(poz_f)
                                    eliminare_p_c(poz_s,poz_f,linie,ce)
                            elif(M[i,j]==M[i+1,j+2]):
                                w=i+1
                                nr_l = 1 #numar de cifre consecutive egale
                                while(M[i,j]==M[w,j] and w<rows-1):
                                    nr_l=nr_l+1
                                    w+=1
                                    if(w==rows-1 and M[i,j]==M[w,j]):
                                        nr_l=nr_l+1
                                print('linia:',i)
                                print('nr_l',nr_l)
                                if(nr_l==3):
                                    poz_s=j
                                    poz_f=k # k reprezinta POZITIA deci k o sa fie finish pentru ambele foruri
                                    linie=i
                                    ce='4'
                                    print(poz_f)
                                    eliminare_p_c(poz_s,poz_f,linie,ce)
                if(nr_c>=3):
                    if(k==cols-1 and M[i,j]==M[i,k]):
                            k+=1
                    poz_s=j
                    poz_f=k
                    linie=i
                    ce='linie'
                    eliminare_p(poz_s,poz_f,linie,ce)


def cautare_p_c():
    for j in range(0,cols):
        for i in range(0,rows):
            if(M[i,j]!=0):
                if(i<rows-1):
                    k=i+1
                    nr_c = 1 #numar de cifre consecutive egale
                    while(M[i,j]==M[k,j] and k<rows-1):
                        nr_c=nr_c+1
                        k+=1
                        if(k==rows-1 and M[i,j]==M[k,j]):
                            nr_c=nr_c+1
                    if(nr_c>=3):
                        if(k==rows-1 and M[i,j]==M[k,j]):
                            k+=1
                        poz_s=i
                        poz_f=k #aici avem cate elemente consecutive egale am gasit asa ca atatea o sa le transformam in 0
                        linie=j #folosim j pentru ca e numarul coloaneai la care suntem
                        ce='coloana'
                        eliminare_p(poz_s,poz_f,linie,ce)

def eliminare_p(start,finish,linie,ce):
    if(ce=='coloana'):
        for i in range(start,finish):
            M[i][linie]=0
        #reordonare
        print('s',start)
        print('f',finish)
        j=linie #aici ii dam  coloana pe care sa faca reordonarea
        for i in range(finish-1,-1,-1):
                if(M[i][j]!=0):
                    if(M[i+1][j]==0):
                        nr=i+1 #ne arata pana la ce linie trebuie sa coboare numarul
                        ok=1
                        while(ok!=0):
                            if(M[nr][j]==0):
                                ok=1
                                nr+=1
                                if(nr==cols):
                                    ok=0
                            else: ok=0
                        M[nr-1][j]=M[i][j]
                        M[i][j]=0
                    else:
                        M[i+1][j]=M[i][j]
                        M[i][j]=0
    if(ce=='linie'):
        for j in range(start,finish):
                M[linie][j]=0
        #reordonare
        print('s',start)
        print('f',finish)
        for j in range(start,finish):
            for i in range(linie,-1,-1):
                if(M[i][j]!=0):
                    if(M[i+1][j]==0):
                        nr=i+1 #ne arata pana la ce linie trebuie sa coboare numarul
                        ok=1
                        while(ok!=0):
                            if(M[nr][j]==0):
                                ok=1
                                nr+=1
                                if(nr==rows):
                                    ok=0
                            else: ok=0
                        M[nr-1][j]=M[i][j]
                        M[i][j]=0
                    else:
                        M[i+1][j]=M[i][j]
                        M[i][j]=0

def eliminare_p_c(start,finish,linie,ce):
    if(ce=='1'):
            for j in range(start,finish):
                M[linie][j]=0
            for i in range(linie,linie-3,-1):
                M[i][start]=0
    if(ce=='2'):
            for j in range(start,finish):
                M[linie][j]=0
            for i in range(linie,linie-3,-1):
                M[i][finish-1]=0
    if(ce=='3'):
            for j in range(start,finish):
                M[linie][j]=0
            for i in range(linie,linie+3):
                M[i][start]=0
    if(ce=='4'):
            for j in range(start,finish):
                M[linie][j]=0
            for i in range(linie,linie+3):
                M[i][finish-1]=0

    #reordonare
    print('s',start)
    print('f',finish)
    for j in range(start,finish):
        for i in range(linie,-1,-1):
            if(M[i][j]!=0):
                if(M[i+1][j]==0):
                        nr=i+1 #ne arata pana la ce linie trebuie sa coboare numarul
                        ok=1
                        while(ok!=0):
                            if(M[nr][j]==0):
                                ok=1
                                nr+=1
                                if(nr==rows):
                                    ok=0
                            else: ok=0
                        M[nr-1][j]=M[i][j]
                        M[i][j]=0
                else:
                    M[i+1][j]=M[i][j]
                    M[i][j]=0

def afisareM(rows,cols):
    for i in range(0, rows):
        for j in range(0, cols):
            print(culoare(i,j),M[i,j],end=' ')
        print('\n')

#main

print('Matricea generata random:\n')
afisareM(rows,cols)
cautare_p_l()
print('\nAfisare dupa eliminare p/complex de pe linii:\n')
afisareM(rows,cols)
cautare_p_c()
print('\nAfisare dupa eliminare p de pe coloana:\n')
afisareM(rows,cols)

