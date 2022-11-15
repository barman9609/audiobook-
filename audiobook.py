from cgitb import text
from http.cookies import BaseCookie
import pyttsx3
import PyPDF2

book = open('ab.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages= pdfReader.numPages
print(pages)

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)
for num in range(7,pages):
    page= pdfReader.getPage(num)
    text = page.extract_text()
    speaker.say(text)
    speaker.runAndWait()