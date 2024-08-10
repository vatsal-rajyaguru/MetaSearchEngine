import csv
import re

x = open("output-york07-ga-03.txt",'rt',encoding='cp949')
y = open("output-york07-ga-02.txt",'rt',encoding='cp949')
z = open("output-york07-ga-03.txt",'rt',encoding='cp949')

topics = []
docid =[]
rank =[]
okapii =[]
offset =[]
bytess =[]
tagid = []



for line in x:
    t1 = line.split()
    topics.append(t1[0])
    docid.append(t1[1])
    rank.append(t1[2])
    okapii.append(t1[3])
    offset.append(t1[4])
    bytess.append(t1[5])
    tagid.append(t1[6])

#for line in y:
#    t2 = line.split()
#    topics.append(t2[0])
#    docid.append(t2[1])
#    rank.append(t2[2])
#    okapii.append(t2[3])
#    offset.append(t2[4])
#    bytess.append(t2[5])
#    tagid.append(t2[6])

#for line in z:
#    t3 = line.split()
#    topics.append(t3[0])
#    docid.append(t3[1])
#    rank.append(t3[2])
#    okapii.append(t3[3])
#    offset.append(t3[4])
#    bytess.append(t3[5])
#    tagid.append(t3[6])    


#print(topics[0]+","+docid[0]+","+rank[0]+","+okapii[0]+","+offset[0]+","+bytess[0]+","+tagid[0])


with open("output-york07-ga-03.csv", "w", newline="") as f:
    fieldnames = ["Topic","DocID","Rank","Okapi","Offset","Bytes","TagID"]
    thewriter = csv.DictWriter(f,fieldnames=fieldnames)
    thewriter.writeheader()
    for i in range(0,len(topics)):
        thewriter.writerow({"Topic" : topics[i],"DocID" : docid[i],"Rank" : rank[i],"Okapi" : okapii[i],"Offset" : offset[i],"Bytes" : bytess[i],"TagID" : tagid[i]})