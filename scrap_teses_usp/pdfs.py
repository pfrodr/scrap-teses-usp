import fitz
import os


for root, dirs, files in os.walk("/mnt/d/downloads/"):
    for file in files:
        if file.endswith(".pdf"):
            arquivo_pdf = os.path.join(root, file)
            # print(arquivo_pdf)
            text = ''

            with fitz.open(arquivo_pdf) as doc:
                for page in doc:
                    text+= page.getText()
            try:
                with open(root + file + '.txt', "w") as stream:
                    print('processando ' + arquivo_pdf)
                    stream.truncate()
                    print(text, file=stream)
            except:
                with open('erros.txt', "w") as erros:
                    print('erro ' + arquivo_pdf)
                    print(arquivo_pdf, file=erros)