prop="nu are elev exemplu util usor restaurang gata"
sir=prop.split()
print(sir)
n=len(sir)
lung=[0 for i in range(n)]
succ=[-1 for i in range(n)]
d_lit={}
#lit=[-1 for i in range(ord('z')-ord('a')+1)]
lung[n-1]=1
prima_litera=sir[n-1][0]
d_lit[prima_litera]=n-1
for i in range(n-2,-1,-1):
    print(d_lit)
    lung[i]=1
    ult_litera=sir[i][-1]
    prima_litera=sir[i][0]
    #lung[i]=1+lung[d_lit[ult_litera]]
    if ult_litera in d_lit:
        lung[i]=1+lung[d_lit[ult_litera]]
        succ[i]=d_lit[ult_litera]
    #actualizam d_lit[prima_litera]
    if prima_litera not in d_lit:
        d_lit[prima_litera]=i
    if lung[i]>lung[d_lit[prima_litera]]:
        d_lit[prima_litera]=i
print(d_lit)
print(lung)
print(succ)

lung_max=0
index=0
for i in range(n):
    if(lung_max<lung[i]):
        lung_max=lung[i]
        index=i

while index!=-1:
    print(sir[index],end=" ")
    index=succ[index]