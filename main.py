import PyPDF2
import os

# criando um objeto
merger = PyPDF2.PdfMerger()

lista_pdfs = os.listdir('pdfs_para_mesclar')

for pdf in lista_pdfs:
  if '.pdf' in pdf:
    merger.append(f'pdfs_para_mesclar/{pdf}')

merger.write('pdfs_mesclados.pdf')
