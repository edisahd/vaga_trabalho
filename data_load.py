import pandas as pd
import requests

df = pd.read_csv('ofertas.csv', sep=';', encoding='utf-8')

errs = []

for r in df.index:
    d = {
        'doc_id': df.loc[r, 'doc_id'],
        'employer_name': df.loc[r, 'employer_name'],
        'date_posted': df.loc[r, 'date_posted'],
        'employment_type': df.loc[r, 'employment_type'],
        'location': df.loc[r, 'location'],
        'title': df.loc[r, 'title'],
        'description': df.loc[r, 'description']
    }
    res = requests.post('http://127.0.0.1:8000/api/vacancy/', data=d)
    print(res)
    if(res.status_code != 201):
        errs.append((d, res.text))