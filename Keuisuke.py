from csp import *
import sys
import math
import time
"""__________________________________________________________________________________________________________________________________"""
"""Mia synarthsh h opoia ths dinetai san orisma mia lista apo uposunola(p.x to orizontio h katheto sunolo)kai to mhkos n ths ouras h ths sthlhs kai epistrefei ton elaxisto arithmo seirwn h sthlwn pou mporoun
na xoresoun  ta uposunola tou orizontiou h kathetou synolou"""
def find_maxspace(Os,n):
       lista=Os[:]
       li=list()
       z=0
       t=0
       v=0
       while (len(lista)!=0):
              maxi=0
              for z in range(0,len(lista)):
                     if len(lista[z])>=len(lista[maxi]):
                            maxi=z
              li.append(lista[maxi])
              lista.pop(maxi)
       z=0
       k=0
       while(z<len(li)):
              v=n
              k=1
              v=v-len(li[z])
              while(v>0):
                     v=v-len(li[z])
                     k=k+1
              if v<0:
                     k=k-1
              t=t+1
              z=z+k
       return t
"""__________________________________________________________________________________________________________________________________""" 
"""Mia synarhthsh pou aferei apo mia lista listwn autes tis listes pou exoun synexomena mhdenika"""
def chop_chop(Os):
       k=0
       while k<len(Os):
              n=len(Os[k])
              for i in range(0,n):
                     if n==1:
                            break
                     if (Os[k][i]==0 ):
                            if (i!=n-1) and (i!=0):
                                   if ((Os[k][i+1])==0 or (Os[k][i-1]==0)  ):
                                          Os.pop(k)
                                          k=k-1
                                          break
                            elif(i==n-1):
                                   if (Os[k][i-1]==0 ):
                                          Os.pop(k)
                                          k=k-1
                                          break
                            elif(i==0):
                                   if (Os[k][i+1]==0  ):
                                          Os.pop(k)
                                          k=k-1
                                          break
              k=k+1
       return Os
"""__________________________________________________________________________________________________________________________________"""
"""Mia synarthsh pou xrhsimopoieita gia na diagrafei apo mia lista listwn tis listes pou exoun synexomena -1(oudetera stoixeia)"""
def chop_chop3(Os):
       k=0
       while k<len(Os):
              n=len(Os[k])                     
              for i in range(0,n):
                     if n==1:
                            break
                     if (Os[k][i]==-1 ):
                            if (i!=n-1) and (i!=0):
                                   if ((Os[k][i+1])==-1 or (Os[k][i-1]==-1)  ):
                                          Os.pop(k)
                                          k=k-1
                                          break
                            elif(i==n-1):
                                   if (Os[k][i-1]==-1 ):
                                          Os.pop(k)
                                          k=k-1
                                          break
                            elif(i==-1):
                                   if (Os[k][i+1]==-1  ):
                                          Os.pop(k)
                                          k=k-1
                                          break
              k=k+1
       return Os
"""__________________________________________________________________________________________________________________________________""" 
"""Mia sunarthsh h opoia pernei san orisma mia lista listwn kai aferei tis idies upolistes"""
def chop_chop2(Os):
       O=list()
       for i in range(0,len(Os)):
              if Os[i] not in O:
                     O.append(Os[i])
       return O
"""__________________________________________________________________________________________________________________________________"""
"""Mia synarthsh pou pernei san orisma mia lista lista kai mia akoma lista listwn paterna  kai tsekarei sthn lista poies paternes emfanizontai apo thn lista listwn paterna
epita afou brei pies paternes emfanizontai epistrefei mia lista listwn me tis perioxomenes paternes pou sthn lista"""
def find_patern(lista,paterna):
       pat=list()
       paterns=list()
       i=0
       t=0
       paternaa=paterna[:]
       while (len(paternaa)!=0):
              maxi=0
              for z in range(0,len(paternaa)):
                   if len(paternaa[z])>=len(paternaa[maxi]):
                          maxi=z
              paterns.append(paternaa[maxi])
              paternaa.pop(maxi)
       while i in range (0,len(lista)):
              flg=0
              for j in range(0,len(paterns)):
                     if (i>=len(lista)):
                            break
                     if (len(paterns[j]))>(len(lista)-i):
                            continue
                     for k in range(0,len(paterns[j])):
                            if i >=len(lista):
                                   break
                            if (lista[i]!=paterns[j][k]):
                                   i=i-k
                                   break
                            else:
                                   if (k==len(paterns[j])-1):
                                          pat.append(paterns[j])
                                          flg=1
                                          j=0
                                   i=i+1
                                   continue
                     if flg==1:
                            break
              if (j==len(paterns)-1)and(flg==0):
                     i=i+1
       return pat
"""__________________________________________________________________________________________________________________________________"""
"""H sunarthsh all possible epistrefei olous tous pithanous sundiasmous xwris epanalipsh apo ta stoixeia tis lista to t mas deixnei se poio bathos ths anadromikhs klhshs eimaste kai to n to megethos pou theloume na xei o
sundiasmos"""
def allposible(lista,n,t):
       Slista=list()
       if t>=n:
              return -1
       elif (len(lista)-1==0):
              ret=list()
              ret.append(lista[0])
              ret=tuple(ret)
              return ret 
       else:
              for i in range(0,len(lista)):
                     temp=lista.pop(i)
                     Llista=allposible(lista,n,t+len(temp))
                     lista.insert(i,temp)
                     if Llista!=-1:
                            for j in range (0,len(Llista)):
                                   Slista.append(Llista[j])
                                   Slista.append(list(lista[i])+list(Llista[j]))
                     else:
                            Slista.append(list(lista[i]))
              Slista=chop_chop(Slista)
              Slista=chop_chop3(Slista)
              return Slista
"""__________________________________________________________________________________________________________________________________"""
"""__________________________________________________________________________________________________________________________________"""
"""H klash Keuisuke upoklash ths klashs CSP
       To D einai mia lista pou periexei duo dictionarys.To ena periexei tis pithanes times pou mporoun na paroun oi metablhtes seires  dhladh oi metablhtes se range(0,n) kai sta paterns orizontiou sunolou pou spane autes
       to allo periexei tis pithanes times pou mporoun na paroun oi metablhtes sthles dhldadh oi metablhtes sto range(n,2*n) kai sta paterns kathetou sunolou pou spane autes"""
class Keuisuke(CSP) :
       D=0
       cc=0
       cc_1=0
       """H keuisuke_constrain pernei san orismata dyo metablhtes kai tis times tous kai tsekarei an uparxei conflict h oxi.Yparxoun 2 periptwseis syndiasmwn metablhtwn h na exoume thn A na einai typou seiras h sthlhs kai
       thn Bmetablhth typou seiras h sthlhs antistoixa dhladh na einai idiou tupou metablhth h A me thn B tote apla tsekaroume na mhn emfanizetai h idia paterna sto A kai sto B.H allh periptwsh einai h A kai h B na einai
       diaforetikou typou dhladh h mia na einai typou seira kai h allh sthlhs tote tsekaroume an to stoixeio diastaurwshs einai -1 (oudetero)  kai sthn sthlh kai sthn seira an einai kai sta duo exoume conflict ,epishs an exoume
       keno stoixeio(mhdeniko) panw se -1 einai conflict se opoia allh periptwsh apla zhtame to shmeio diastaurwseis na einai koino"""
       def keuisuke_constraint(self,A, a, B, b):
              self.cc+=1
              n=len(vars)/2
              if (A <n):
                     if (B<n):
                            pata=((self.D)[0])[tuple(a)]
                            patb=((self.D)[0])[tuple(b)]
                            for i in range (0,len(pata)):
                                   for j in range (0,len(patb)):
                                          if pata[i]==patb[j]:
                                                 return 0
                     elif(B>=n):
                            if (a[B-n]==-1)or(b[A]==-1):
                                   if (a[B-n]==b[A]):
                                          return 0
                                   if (a[B-n]==0)or(b[A]==0):
                                          return 0
                            else:
                                   if a[B-n]!=b[A]:
                                          return 0

              elif (A >=n):
                     if (B>=n):
                            pata=((self.D)[1])[tuple(a)]
                            patb=((self.D)[1])[tuple(b)]
                            for i in range (0,len(pata)):
                                   for j in range (0,len(patb)):
                                          if pata[i]==patb[j]:
                                                 return 0
                     elif(B<n):
                            if (b[A-n]==-1)or(a[B]==-1):
                                   if (b[A-n]==a[B]):
                                          return 0
                                   if (b[A-n]==0)or(a[B]==0):
                                          return 0
                            else:
                                   if a[B]!=b[A-n]:
                                          return 0
              self.cc_1+=1
              return 1
       def __init__(self, n,vars,domains,neigbhors,d):
               self.D=d
               self.cc=0
               self.cc_1=0
               CSP.__init__(self, vars, domains,neigbhors,self.keuisuke_constraint)
"""__________________________________________________________________________________________________________________________________"""
"""                                              MAIN PART-------------------------------------------------------------------------------------MAIN PART"""
"""__________________________________________________________________________________________________________________________________""" 
print "Dwse mou to platos/mhkos tou tetragwnikou pinaka.\n"
n=input()
print'Dwse:To orizontio synolo se morfh [[a1,a2,3],[b1,b2,b3,...,zn],...,[z1,z2,z3,...,zn]]\n'
Os=input()
print'Dwse:To katakoryfo synolo se morfh [[a1,a2,3],[b1,b2,b3,...,zn],...,[z1,z2,z3,...,zn]]\n'
Ks=input()
T=[Os,Ks]
print'Dwse:\n'
print'0:Backtracking ,1:Backtracking+MRV ,2:Backtracking+FC ,3:MRV+FC,4:Min-Conflicts\n'
mechanism=input()
domains=dict()
geitones=dict()
A=Os[:]
B=Ks[:]
oudetero=list()
"""Oi metablhtes einai duo eidwn apo to 0 ews to n kai apo to n ews to 2*n oi prwtes antiprosopeuoun seires kai oi deuteres steiles"""
vars=list(i for i in range (0,2*n))
"""______________________________________"""
"""Prosthetoume math.ceil(n/2.0) mhdenika( kena )sto orizontio kai katheto synolo kai math.ceil(n/2.0)-1 oudetera stoixeia (-1),epipleon kataskeuazoume kai to oudetero stoixeio pou einai h timh mia metablhths an se ayth
anatethei keno oudetero keno oudetero keno oudetero enalaks mexri na gemisei h seira h sthlh""" 
oudetero=list()
for i in range(0,int(math.ceil(n/2.0))):
       Os=list(Os)
       Ks=list(Ks)
       oudetero=oudetero+[0]
       Os.append([0])
       Ks.append([0])
       if i!=int(math.ceil(n-1/2.0)):
              oudetero=oudetero+[-1]
              Os.append([-1])
              Ks.append([-1])
       Os=tuple(Os)
       Ks=tuple(Ks)
"""______________________________________"""
"""Prosthetw to oudetero stoixeio stis orizonties kai kathetes paternes ,eksigoume parakatw giati ginetai"""
A.append(oudetero)
B.append(oudetero)
"""Prosthetw epishs to -[1] stis orizonties kai kathetes paternes,auto ginetai gia na mhn uparksei megalh epanalhpsh tou [-1] anamesa se idiou typou metablhtes alla kai epeidh h aksia tou [-1] ws oudetero den mporei na einai
mhden afou den einai keno,etsi den afereitai apo ton elegxo aksia pou ginetai pio katw"""
A.append([-1])
B.append([-1])
"""Pernw olous tous pithanous syndiasmous xwris epanalipsh orizontiwn kai kathetwn synolwn"""
Os=allposible(list(Os),n,0)
Ks=allposible(list(Ks),n,0)
"""______________________________________"""
"""Diwxnoume tous tyxon syndiasmous pou einai panw apo n"""
i=0
while i<len(Os):
       if len(Os[i])!=n:
              Os.pop(i)
              continue
       i=i+1
i=0
while i<len(Ks):
       if len(Ks[i])!=n:
              Ks.pop(i)
              continue
       i=i+1
"""______________________________________"""
"""Diwxnoume ta diplotypa"""
S=list()
Os=(chop_chop2(Os))
Ks=(chop_chop2(Ks))
"""______________________________________"""
"""Diwxnoume tis times me xamhlh aksia ,me thn ennoia oti dinoun poio polla kena kai aprosdiorista oudetera stoixeia (-1) apo oti ofelimo ergo sthn lush.Parapanw prosthesame to oudetero stoixeio
keno oudetero keno oudetero..(enalaks) stis paternes gia na mhn eksafanistei plhrws apo ta domain dioti einai xrhsimo etsi tou dwsame aksia n kai den afereite."""
i=0
while i<len(Os):
       ptrn=find_patern(Os[i],A)
       ofelimo=0
       for z in range (0,len(ptrn)):
              ofelimo=ofelimo+len(ptrn[z])
       if n-ofelimo>ofelimo:
              Os.pop(i)
              continue
       i=i+1
i=0
while i<len(Ks):
       ptrn=find_patern(Ks[i],B)
       ofelimo=0
       for z in range (0,len(ptrn)):
              ofelimo=ofelimo+len(ptrn[z])
       if n-ofelimo>ofelimo:
              Ks.pop(i)
              continue
       i=i+1
S.append(Os)
S.append(Ks)
"""______________________________________"""
"""Briskoume tis elaxistes seires kai steiles pou mporoun na fuloksenithoun ta stoixeia tou orizontiou kai kathetou synolou antistoixa kai an den mas eparkei o xwros gia oudetero stoixeio[keno oudetero keno ...]to
diwxnoume wste na mpoun oles oi paternes apo mia fora toulaxiston"""
om=find_maxspace(T[0],n)
km=find_maxspace(T[1],n)
if om>=n:
       S[0].remove(oudetero)
if km>=n:
       S[1].remove(oudetero)
"""______________________________________"""
"""Orizoume ta domains kai geitones oles tis upoloipes metablhtes ektos ths idias"""
for i in range(0,2*n):
               if i<n:
                                                                   domains[i]=S[0]
               elif i>=n:
                                                                   domains[i]=S[1]
for i in range(0,2*n):
              geit=vars[:]
              geit.remove(i)
              geitones[i]=geit
"""______________________________________"""
"""Ftiaxnoume ta duo dictionary pou tha mpoun se mia lista gia na dwthoun sto problhma gia na ksereis kathe timh kathe fora ti paterns krybei mesa ths"""
D1=dict()
D2=dict()
D=list()
D.append(D1)
D.append(D2)
Z=list()
Z.append(A)
Z.append(B)
for i in range(0,2):
       for j in range(0,len(S[i])):
              (D[i])[tuple(S[i][j])]=find_patern(S[i][j],Z[i])
"""______________________________________"""
k=Keuisuke(n,vars,domains,geitones,D)
ti1=int(round(time.time() * 1000))
if mechanism==0:
       print'Backtracking...\n'
       out=backtracking_search(k)
elif mechanism==1:
       print'Backtracking+MRV...\n'
       out=backtracking_search(k,mrv)
elif mechanism==2:
       print'Backtracking+Forward checking...\n'
       out=backtracking_search(k,inference = forward_checking)
elif mechanism==3:
       print'MRV+Forward checking...\n'
       out=backtracking_search(k,mrv,inference = forward_checking)
elif mechanism==4:
       print'Dwse:max steps\n'
       max_steps=input()
       print'Min-Conflicts...\n'
       out=min_conflicts(k,max_steps)
else:
       print'Wrong input\n'
ti2=int(round(time.time() * 1000))
ti_s=ti2-ti1
print'Ta stoixeia apo 0-n antistoixoun stis seires enw auta apo n-2*n stis steiles opou n to mhkos pinaka\n'
print'Ta stoixeia me arithmo mhden antistoixoun se kena,enw ta stoixeia me arithmo -1  mia seiras h sthlhs epikaliptonte apo to antistoixo stoixeio ths antistoixhs sthlhs h seiras antoistoixa\n '
print'____________________________________________________________________________\n '
print out
print'____________________________________________________________________________\n '
print 'Time to find the solution in miliseconds:' + ' ' ,ti_s ,' .\n'
print 'Nodes that visited in the search tree:' + ' ' ,k.cc_1 ,' .\n'
print 'Constrain checks:' + ' ' ,k.cc ,' .\n'
