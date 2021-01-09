from __future__ import unicode_literals 
import os
import re




for root, dirs, files in os.walk("/mnt/d/downloads/teses.usp.br/"):
    for file in files:
        if file.endswith(".php"):
            arquivo = os.path.join(root, file)

            # arquivo_enc = arquivo.decode('utf-8', 'ignore')


            with open(arquivo, 'r', encoding="utf8", errors='ignore') as f:
                contents = f.read()

            links = re.findall('("\/teses\/disponiveis\/.{1,}pdf")', contents)
            
            if links != []:
                links = 'https://www.teses.usp.br' + links[0].replace('"','')
                print(links)
