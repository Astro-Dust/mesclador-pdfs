import PyPDF2
import os

# criando um objeto
merger = PyPDF2.PdfMerger()

path_pdfs = 'pdfs_para_mesclar'

lista_pdfs = os.listdir('pdfs_para_mesclar')

# ordenando os arquivos por data (mais antiga para mais nova)
lista_pdfs_ordenada = sorted(os.listdir(path_pdfs), key=lambda x: os.path.getmtime(os.path.join(path_pdfs, x)))

for pdf in lista_pdfs_ordenada:
  if '.pdf' in pdf:
    merger.append(f'{path_pdfs}/{pdf}')
