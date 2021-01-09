import fitz
import os


arquivo_pdf = '/mnt/d/downloads/2017ME_HeiderAndrade.pdf'
# print(arquivo_pdf)
text = ''

with fitz.open(arquivo_pdf) as doc:
    for page in doc:
        text+= page.getText()
try:
    with open('/mnt/d/downloads/2017ME_HeiderAndrade.pdf.txt', "w") as stream:
        print('processando ' + arquivo_pdf)
        print(text, file=stream)
except:
    with open('erros.txt', "w") as erros:
        print('erro ' + arquivo_pdf)
        print(arquivo_pdf, file=erros)