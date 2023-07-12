import requests
import pandas as pd

respostas = []

with open('arquivo.txt', 'r') as arquivo:
    for linha in arquivo:
        ca = linha.strip()
        try:
            xyz = requests.get(f'https://projeto-ca-api.rj.r.appspot.com/api/ca/{ca}')
            
            resp = xyz.json()
            respostas.append(resp)
            print(f"CA: {resp['CA']}  |  Equipamento: {resp['Equipamento']}  |  Situacao: {resp['Situacao']}  |  Validade: {resp['Validade']}")
        except:
            print(f'ERRO CA --> {ca}')

df = pd.DataFrame(respostas)

colunas = ['CA', 'Equipamento', 'Situacao', 'Validade']

df[colunas].to_excel('respostas.xlsx', index=False)