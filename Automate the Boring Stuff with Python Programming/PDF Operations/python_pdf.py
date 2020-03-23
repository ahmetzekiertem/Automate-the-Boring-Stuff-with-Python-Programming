import PyPDF2
import os

#extracting and combining pff files


os.chdir("/Users/mac/Desktop")

pdfFile = open('lmu_data.pdf','rb')

reader = PyPDF2.PdfFileReader(pdfFile)

reader.numPages

page = reader.getPage(0)

print(page.extractText())


for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())


pdf_2file = open('lmu_data.pdf','rb')
pdf_5file = open('lmu_data.pdf','rb')


reader1 = PyPDF2.PdfFileReader(pdf_5file)
reader2 = PyPDF2.PdfFileReader(pdf_2file)

writer = PyPDF2.PdfFileWriter()


for i in range(reader1.numPages):
    page = reader1.getPage(i)
    writer.addPage(page)

for i in range(reader2.numPages):
    page = reader2.getPage(i)
    writer.addPage(page)

outputfile = open("combinedpdf.pdf","wb")

writer.write(outputfile)
