import pyttsx3
import PyPDF2

book = open('Chapter 6.pdf', 'rb')

speaker = pyttsx3.init()
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

print(pages)

for num in range(0, 12):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
