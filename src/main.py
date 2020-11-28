from query import query
from index import buildIndex

indexPath = '../files/invertedIndex.json'
dataPath = '../example/'

[invertedIndex, totalTweets, allTweets] = buildIndex(indexPath, dataPath)

inputText = str(input("Ingrese keywords: "))
k = int(input("Ingrese cantidad de tweets a recuperar: "))

result = query(inputText, k, invertedIndex, totalTweets)

count = 1
for i in result:
    print('[', count, '] ➥', i)
    count += 1

print()
lookFor = int(input('¿Que tweet desea visualizar? '))

while lookFor >= count:
    print('Indice invalido')
    lookFor = int(input('¿Que tweet desea visualizar?'))

print()
print(allTweets[int(result[lookFor - 1][0])])
