import pandas as pd
import requests
import tabula


def pdf_para_excel(caminho_arquivo):
    tabelas = tabula.read_pdf(caminho_arquivo,pages='all')#você pode escolher o index da pagina do pdf que você quiser 
    excel_cobimado = pd.DataFrame()
    for tabela in tabelas :
        excel = tabela.copy()
        excel_cobimado = pd.concat ([excel_cobimado ,excel],ignore_index=False)
    return excel_cobimado

caminho_arquivo = 'caminho seu arquivo'#você tem que mudar isso 

excel_combinado2 = pdf_para_excel(caminho_arquivo)

excel_combinado2.to_excel('arquivos-saida.xlsx',index=True )# e isso
