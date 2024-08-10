import pandas as pd
from sklearn import preprocessing
import numpy as np
import concurrent.futures
from tkinter import *





#Creating a dataframe for each resultset

search1 = pd.read_csv("output-york07-ga-01.csv")
search2 = pd.read_csv("output-york07-ga-02.csv")
search3 = pd.read_csv("output-york07-ga-03.csv")

search1["CombSum"]= " "
search2["CombSum"]= " "
search3["CombSum"]= " "

#Normalized the rank column across all three resultsets
column = 'Rank'
search1[column] = (search1[column] - search1[column].min()) / (search1[column].max() - search1[column].min())


search2[column] = (search2[column] - search2[column].min()) / (search2[column].max() - search2[column].min())


search3[column] = (search3[column] - search3[column].min()) / (search3[column].max() - search3[column].min())




# Creating a dataframe for the querired topic from searchengine 1
Topic = []
DocID  = []
Rank = []
Okapi = []
Offset = []
Bytes = []
TagID = []
for i in range(len(search1.index)):
   if(search1.Topic[i] == 235):
       Topic.append(search1.Topic[i])
       DocID.append(search1.DocID[i])
       Rank.append(search1.Rank[i])
       Okapi.append(search1.Okapi[i])
       Offset.append(search1.Offset[i])
       Bytes.append(search1.Bytes[i])
       TagID.append(search1.TagID[i])

sd1 = {'Topic' :Topic,
       'DocID' :DocID,
       'Rank' :Rank,
       'Okapi' :Okapi,
       'Offset' :Offset,
       'Bytes' :Bytes,
       'TagID' :TagID}

df1 = pd.DataFrame(sd1)





# Creating a dataframe for the querired topic from searchengine 2
Topic2 = []
DocID2  = []
Rank2 = []
Okapi2 = []
Offset2 = []
Bytes2 = []
TagID2 = []
for j in range(len(search2.index)):
   if(search2.Topic[j] == 235):
       Topic2.append(search2.Topic[j])
       DocID2.append(search2.DocID[j])
       Rank2.append(search2.Rank[j])
       Okapi2.append(search2.Okapi[j])
       Offset2.append(search2.Offset[j])
       Bytes2.append(search2.Bytes[j])
       TagID2.append(search2.TagID[j])

sd2 = {'Topic' :Topic2,
       'DocID' :DocID2,
       'Rank' :Rank2,
       'Okapi' :Okapi2,
       'Offset' :Offset2,
       'Bytes' :Bytes2,
       'TagID' :TagID2}

df2 = pd.DataFrame(sd2)



# Creating a dataframe for the querired topic from searchengine 3
Topic3 = []
DocID3  = []
Rank3 = []
Okapi3 = []
Offset3 = []
Bytes3 = []
TagID3 = []

for i in range(len(search3.index)):
   if(search3.Topic[i] == 235):
       Topic3.append(search3.Topic[i])
       DocID3.append(search3.DocID[i])
       Rank3.append(search3.Rank[i])
       Okapi3.append(search3.Okapi[i])
       Offset3.append(search3.Offset[i])
       Bytes3.append(search3.Bytes[i])
       TagID3.append(search3.TagID[i])

sd3 = {'Topic' :Topic3,
       'DocID' :DocID3,
       'Rank' :Rank3,
       'Okapi' :Okapi3,
       'Offset' :Offset3,
       'Bytes' :Bytes3,
       'TagID' :TagID3}


df3 = pd.DataFrame(sd3)



# For each document combining the ranking from each search engine by the combSum method

#summ = 0
#for i in range(len(df1.index)):
    #for j in range(len(df2.index)):
        #for g in range(len(df3.index)):
            #if (df1.DocID[i] == df2.DocID[j] and df2.DocID[j] == df3.DocID[g]):
                #summ = df1.Rank[i] + df2.Rank[j] + df3.Rank[g]
                #df1[i,"Combsum"] = summ
                #df2[j,"Combsum"] = summ
                #df3[g,"Combsum"] = summ
                #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            #else:
                #print(i,j,g)




# Results that match the query across three search engines
df1.to_csv('df1.csv')
df2.to_csv('df2.csv')
df3.to_csv('df3.csv')






#Combining the search results from 3 different search engines
final = pd.concat([df1, df2, df3])
final.to_csv('final.csv')

  



#Sorting the okapi scores for each document from greatest to least
SortedList = final.sort_values('Okapi', ascending=False)
SortedList.to_csv('sorted.csv')

#Printing the top 1000 results based on the okapi score for each query
SortedList.head(1000).to_csv('final1000.csv')
