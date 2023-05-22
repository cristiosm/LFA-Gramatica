#CITIRE FISIER
with open("date.in", "r") as f:
    M = [line.strip().split() for line in f.readlines()]
F = M.pop()

#ALFABETUL
lit = sorted(set([x[1] for x in M]))

#STARILE
s = [x[0] for x in M]
s1 = [x[2] for x in M]
stari = sorted(set(s + s1))

#TABELUL
tabel = [['aux' for i in range(len(lit) + 1)] for j in range(len(stari))]
for linie in M:
    i = stari.index(linie[0])
    ind = lit.index(linie[1])
    tabel[i][0] = linie[0]
    tabel[i][ind + 1] = linie[2]


#TABEL AUXILIAR
tabel_aux=[[0 for j in range(len(lit)+1)]for i in range(len(stari))]
for i in range(len(stari)):
    tabel_aux[i][0]=stari[i]

#SE NOTEAZA STARILE INITIALE CU A SI CELE FINALE CU B
litera=ord('A')
for i in range(len(stari)):
    for j in range(len(lit)):
        if tabel[i][j+1] not in F:
            tabel_aux[i][j+1]=chr(litera)
        else:
            tabel_aux[i][j+1]=chr(litera+1)

# SE CREEAZA DICT CU A SI B
schimbari=True
izolat=[]
izolat.extend(F)
dct=dict()
litera=ord('A')
dct[chr(litera)]=[stari.index(stari[i]) for i in range(len(stari)) if stari[i] not in F]
dct[chr(litera+1)]=[stari.index(F[i]) for i in range(len(F))]

#STARI NEFINALE
nef=[stari[i] for i in range(len(stari)) if stari[i] not in F]

while schimbari==True:
    schimbari=False
    dct1=dct
    dct=dict()
    dctn=dict()
    dctf=dict()
    litera=ord('A')
    dctn[chr(litera)]=[stari.index(nef[0])]

    for i in range(1,len(nef)):
        for key in dctn:
            if (tabel_aux[stari.index(nef[i])][1] , tabel_aux[stari.index(nef[i])][2])==(tabel_aux[dctn[key][0]][1] , tabel_aux[dctn[key][0]][2]):
                dctn[key].append(stari.index(nef[i]))
                break
        else:
                litera+=1
                dctn[chr(litera)]=[stari.index(nef[i])]

    for i in range(0,len(F)):
        for key in dctf:
            if (tabel_aux[stari.index(F[i])][1] , tabel_aux[stari.index(F[i])][2])==(tabel_aux[dctf[key][0]][1] , tabel_aux[dctf[key][0]][2]):
                dctf[key].append(stari.index(F[i]))
                break
        else:
                litera+=1
                dctf[chr(litera)]=[stari.index(F[i])]

    dct=dctn | dctf

    if dct1!=dct:
        schimbari=True

    for i in range(len(stari)):
        for j in range(len(lit)):
                for key in dct:
                    if stari.index(tabel[i][j+1]) in dct[key]:
                        tabel_aux[i][j+1]=key

for key in dct:
    for ind in dct[key]:
        for l in range(len(M)):
            if M[l][0]==stari[ind]:
                 M[l][0]=stari[dct[key][0]]
            if  M[l][2]==stari[ind]:
                 M[l][2]=stari[dct[key][0]]

stari=[dct[a][0] for a in dct]

N=[]
for l in M:
    if l not in N:
        N.append(l)

for l in N:
    print(*l,end='\n')