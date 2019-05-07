import os

path = os.path.join(os.path.expanduser("~"), "amaindola")
os.chdir(path)
print(os.getcwd())

# Read the PDF File
from PyPDF2 import PdfFileReader

file = os.path.join(path, "test.pdf")
pdf = PdfFileReader(file)

# Print pdf Info
text = pdf.getPage(3).extractText()
print(text)

from sys import version
print(version)
