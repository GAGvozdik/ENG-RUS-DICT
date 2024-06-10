

import PyPDF2

# creating a pdf reader object
reader = PyPDF2.PdfReader('eng-rus-susch.pdf')

# print the number of pages in pdf file
print(len(reader.pages))

# print the text of the first page
page = reader.pages[7].extract_text()
alpENG = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNMI'
alpRUS = 'йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'



sPage = page.split('\n')

# print(sPage)


enRuWords = []

oneWord = ''
enWord = ''
ruWord = ''
ruSPage = ' '


for i in range(len(sPage)):

    if '' in sPage[i]:

        enRuWords.append((enWord, ruWord))

        oneStr = sPage[i].split(' ')

        enWord = oneStr[0]
        # ruWord = oneStr[1]

        # print(enWord)

    else:
        ruWord += sPage[i]
        ruWord = ''

for i in enRuWords:
    print(i)
