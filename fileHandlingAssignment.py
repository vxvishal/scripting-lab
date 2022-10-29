#read stocks.txt and print the contents
theFile = open("stocks.txt", "r")
fileRead = theFile.read()
print(fileRead)
theFile.close()
