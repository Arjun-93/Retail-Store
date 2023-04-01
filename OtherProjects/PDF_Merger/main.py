import PyPDF2
import PyPDF2 as pdf
pdfFiles = ["IE_lab4.pdf", "IE_lab5.pdf", "IE_lab6.pdf"]
merger = pdf.PdfMerger()

for filename in pdfFiles:
    pdfFiles = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFiles)
    merger.append(pdfReader)
pdfFiles.close()
merger.write('merged.pdf')