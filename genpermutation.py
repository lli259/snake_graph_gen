import itertools
import random
boundings=[]
for i in range(1,12):
    boundings.append((1,i))
    boundings.append((11,i))

for i in range(2,11):
    boundings.append((i,1))
    boundings.append((i,11))

#print(len(boundings))
#boundings=[1,2,3,4,5]
boundings=sorted(boundings)
comb=list(itertools.combinations(boundings,4))
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
samp=random.sample(comb,k=10)
for s in samp:
    genfourfil(s,100,100)

