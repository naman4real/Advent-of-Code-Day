from collections import defaultdict

f = open("temp.txt", "r")
read = [i.strip() for i in f.readlines()]

d={}
letterDict = defaultdict(int)
counter = defaultdict(int)
template=read[0]
for r in read[2:]:
    t=r.split(' -> ')
    d[t[0]]=t[1]
letterDict[template[0]]+=1
for i in range(1,len(template)):
    counter[template[i-1]+template[i]]+=1
    letterDict[template[i]]+=1
steps=0
while steps<40:
    tempCounter = defaultdict(int)
    for k,v in counter.items():
        res = d[k]
        tempCounter[k[0]+res]+=v
        tempCounter[res+k[1]]+=v
        letterDict[res]+=v
    counter=tempCounter
    steps+=1
print(letterDict)

ans=[]
for k,v in letterDict.items():
    ans.append(v)
ans.sort()
print(ans[-1]-ans[0])
