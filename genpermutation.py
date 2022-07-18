import itertools
import random
import os
import sys

SIZE_BOARD=11
PRE_BOXES=6

if not os.path.isdir('snake'):
    os.system('mkdir snake')

if not os.path.isdir('snakeinvalid'):
    os.system('mkdir snakeinvalid')

boundings=[]
for i in range(1,SIZE_BOARD+1):
    boundings.append((1,i))
    boundings.append((SIZE_BOARD,i))

for i in range(2,SIZE_BOARD):
    boundings.append((i,1))
    boundings.append((i,SIZE_BOARD))

#print(len(boundings))
#boundings=[1,2,3,4,5]
boundings=sorted(boundings)
comb=list(itertools.combinations(boundings,PRE_BOXES))
#print(comb)

#t:(1,3)
#v:4
#out:134
def tupletostr(t,v):
    a,b=t
    return str(a)+str(b)+str(v)

def tupletostr2(t,v):
    a,b=t
    return 'filled('+str(a)+","+str(b)+","+str(v)+').'

def validdis(a,an,b,bn):
    a_x,a_y=a
    b_x,b_y=b
    dis_x=abs(a_x-b_x)
    dis_y=abs(a_y-b_y)
    dis=max(dis_x,dis_y)
    if dis>abs(an-bn):
        return False
    else:
        return True





def gensixfil(p,persize,totalsize):
    validsize=0
    invalidsize=0
    size=0
    repetition=0
    a,b,c,d,e,f=p
    allselection=set()
    while True:
        an=random.choice(range(1,persize+1))
        bn=random.choice(range(1,persize+1))
        while an==bn:
            bn=random.choice(range(1,persize+1))
        cn=random.choice(range(1,persize+1))
        while cn==an or cn==bn:
            cn=random.choice(range(1,persize+1))
        dn=random.choice(range(1,persize+1))
        while dn==cn or dn==bn or dn==an:
            dn=random.choice(range(1,persize+1))
        en=random.choice(range(1,persize+1))
        while en==dn or en==cn or en==bn or en==an:
            en=random.choice(range(1,persize+1))
        fn=random.choice(range(1,persize+1))
        while fn==en or fn==dn or fn==cn or fn==bn or fn==an:
            fn=random.choice(range(1,persize+1))
        filename=''
        filename+=tupletostr(a,an)+'_'
        filename+=tupletostr(b,bn)+'_'
        filename+=tupletostr(c,cn)+'_'
        filename+=tupletostr(d,dn)+'_'
        filename+=tupletostr(e,en)+'_'
        filename+=tupletostr(f,fn)
        dictkey=str(an)+"_"+str(bn)+"_"+str(cn)+"_"+str(dn)+"_"+str(en)+"_"+str(fn)
        if not dictkey in allselection:
            allselection.add(dictkey)
            size+=1
            if validdis(a,an,b,bn) and validdis(a,an,c,cn) and validdis(a,an,d,dn) and validdis(a,an,e,en) and validdis(a,an,f,fn) \
                and validdis(b,bn,c,cn) and validdis(b,bn,d,dn) and validdis(b,bn,e,en) and validdis(b,bn,f,fn)\
                    and validdis(c,cn,d,dn) and validdis(c,cn,e,en) and validdis(c,cn,f,fn)\
                         and validdis(d,dn,e,en) and validdis(d,dn,f,fn) and validdis(e,en,f,fn):
                with open('snake/snake'+filename+'.csv','w') as filewt:
                    filewt.write(tupletostr2(a,an)+'\n')
                    filewt.write(tupletostr2(b,bn)+'\n')
                    filewt.write(tupletostr2(c,cn)+'\n')
                    filewt.write(tupletostr2(d,dn)+'\n') 
                    filewt.write(tupletostr2(e,en)+'\n')                          
                    filewt.write(tupletostr2(f,fn))
                validsize+=1
            else :
                #print('invalid dist',a,an,b,bn,c,cn,d,dn)
                with open('snakeinvalid/snake'+filename+'.csv','w') as filewt:
                    filewt.write(tupletostr2(a,an)+'\n')
                    filewt.write(tupletostr2(b,bn)+'\n')
                    filewt.write(tupletostr2(c,cn)+'\n')
                    filewt.write(tupletostr2(d,dn)+'\n')                        
                    filewt.write(tupletostr2(e,en)+'\n')                          
                    filewt.write(tupletostr2(f,fn))
                invalidsize+=1
        else:
            print('repeat: ',dictkey)
            repetition+=1
        if validsize==totalsize:
            break
        	
    print(str(a).replace(', ','-'),str(b).replace(', ','-'),str(c).replace(', ','-'),str(d).replace(', ','-'),str(e).replace(', ','-'),str(f).replace(', ','-'),',',size,',',validsize,',',invalidsize,',',repetition) 
    

#genfourfil(((10, 1), (10, 5), (10, 7), (10, 9)),5)
#find 10 groups of combinations of 4 positions
samp=random.sample(comb,k=10)

#for each position in the combination, assign a value from 1 to len^2. Repeat 100 times.
#in total, there are 10*100 different assignments. 
for s in samp:
    gensixfil(s,SIZE_BOARD*SIZE_BOARD,100)




exit()


def genfivefil(p,persize,totalsize):
    validsize=0
    invalidsize=0
    size=0
    repetition=0
    a,b,c,d,e=p
    allselection=set()
    while True:
        an=random.choice(range(1,persize+1))
        bn=random.choice(range(1,persize+1))
        while an==bn:
            bn=random.choice(range(1,persize+1))
        cn=random.choice(range(1,persize+1))
        while cn==an or cn==bn:
            cn=random.choice(range(1,persize+1))
        dn=random.choice(range(1,persize+1))
        while dn==cn or dn==bn or dn==an:
            dn=random.choice(range(1,persize+1))
        en=random.choice(range(1,persize+1))
        while en==dn or en==cn or en==bn or en==an:
            en=random.choice(range(1,persize+1))
        filename=''
        filename+=tupletostr(a,an)+'_'
        filename+=tupletostr(b,bn)+'_'
        filename+=tupletostr(c,cn)+'_'
        filename+=tupletostr(d,dn)+'_'
        filename+=tupletostr(e,en)
        dictkey=str(an)+"_"+str(bn)+"_"+str(cn)+"_"+str(dn)+"_"+str(en)
        if not dictkey in allselection:
            allselection.add(dictkey)
            size+=1
            if validdis(a,an,b,bn) and validdis(a,an,c,cn) and validdis(a,an,d,dn) and validdis(a,an,e,en) \
                and validdis(b,bn,c,cn) and validdis(b,bn,d,dn) and validdis(b,bn,e,en) \
                    and validdis(c,cn,d,dn) and validdis(c,cn,e,en) and validdis(d,dn,e,en):
                with open('snake/snake'+filename+'.csv','w') as filewt:
                    filewt.write(tupletostr2(a,an)+'\n')
                    filewt.write(tupletostr2(b,bn)+'\n')
                    filewt.write(tupletostr2(c,cn)+'\n')
                    filewt.write(tupletostr2(d,dn)+'\n')                        
                    filewt.write(tupletostr2(e,en))
                validsize+=1
            else :
                #print('invalid dist',a,an,b,bn,c,cn,d,dn)
                with open('snakeinvalid/snake'+filename+'.csv','w') as filewt:
                    filewt.write(tupletostr2(a,an)+'\n')
                    filewt.write(tupletostr2(b,bn)+'\n')
                    filewt.write(tupletostr2(c,cn)+'\n')
                    filewt.write(tupletostr2(d,dn)+'\n')                        
                    filewt.write(tupletostr2(e,en))
                invalidsize+=1
        else:
            print('repeat: ',dictkey)
            repetition+=1
        if validsize==totalsize:
            break
        	
    print(str(a).replace(', ','-'),str(b).replace(', ','-'),str(c).replace(', ','-'),str(d).replace(', ','-'),str(e).replace(', ','-'),',',size,',',validsize,',',invalidsize,',',repetition) 
    

#genfourfil(((10, 1), (10, 5), (10, 7), (10, 9)),5)
#find 10 groups of combinations of 4 positions
samp=random.sample(comb,k=10)

#for each position in the combination, assign a value from 1 to len^2. Repeat 100 times.
#in total, there are 10*100 different assignments. 
for s in samp:
    genfivefil(s,SIZE_BOARD*SIZE_BOARD,100)




exit()





def genfourfil(p,persize,totalsize):
    validsize=0
    invalidsize=0
    size=0
    repetition=0
    a,b,c,d=p
    allselection=set()
    while True:
        an=random.choice(range(1,persize+1))
        bn=random.choice(range(1,persize+1))
        while an==bn:
            bn=random.choice(range(1,persize+1))
        cn=random.choice(range(1,persize+1))
        while cn==an or cn==bn:
            cn=random.choice(range(1,persize+1))
        dn=random.choice(range(1,persize+1))
        while dn==cn or dn==bn or dn==an:
            dn=random.choice(range(1,persize+1))
        filename=''
        filename+=tupletostr(a,an)+'_'
        filename+=tupletostr(b,bn)+'_'
        filename+=tupletostr(c,cn)+'_'
        filename+=tupletostr(d,dn)
        dictkey=str(an)+"_"+str(bn)+"_"+str(cn)+"_"+str(dn)
        if not dictkey in allselection:
            allselection.add(dictkey)
            size+=1
            if validdis(a,an,b,bn) and validdis(a,an,c,cn) and validdis(a,an,d,dn) and validdis(b,bn,c,cn) and validdis(b,bn,d,dn) and validdis(c,cn,d,dn) :
                with open('snake/snake'+filename+'.csv','w') as filewt:
                    filewt.write(tupletostr2(a,an)+'\n')
                    filewt.write(tupletostr2(b,bn)+'\n')
                    filewt.write(tupletostr2(c,cn)+'\n')
                    filewt.write(tupletostr2(d,dn))
                validsize+=1
            else :
                #print('invalid dist',a,an,b,bn,c,cn,d,dn)
                with open('snakeinvalid/snake'+filename+'.csv','w') as filewt:
                    filewt.write(tupletostr2(a,an)+'\n')
                    filewt.write(tupletostr2(b,bn)+'\n')
                    filewt.write(tupletostr2(c,cn)+'\n')
                    filewt.write(tupletostr2(d,dn))
                invalidsize+=1
        else:
            print('repeat: ',dictkey)
            repetition+=1
        if validsize==totalsize:
            break
        	
    print(str(a).replace(', ','-'),str(b).replace(', ','-'),str(c).replace(', ','-'),str(d).replace(', ','-'),',',size,',',validsize,',',invalidsize,',',repetition) 
    

#genfourfil(((10, 1), (10, 5), (10, 7), (10, 9)),5)
#find 10 groups of combinations of 4 positions
samp=random.sample(comb,k=10)

#for each position in the combination, assign a value from 1 to len^2. Repeat 100 times.
#in total, there are 10*100 different assignments. 
for s in samp:
    genfourfil(s,SIZE_BOARD*SIZE_BOARD,100)

