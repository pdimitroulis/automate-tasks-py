#Remove \n from an input text


myFile = open('removeCHL.txt','r')
text = myFile.read()
text = text.replace('\n',' ')
text = text.replace('  ',' ') #in case there was a space before \n

myFile = open('removeCHL.txt','w')
myFile.write(text)
