# import library
import pyttsx3
import PyPDF2
 
# intializing pyttsx3
speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', rate+50)

pdfReader = PyPDF2.PdfFileReader(open('Book.pdf', 'rb'))
for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.save_to_file(text, 'Audio.mp3')
    speaker.runAndWait()
    speaker.stop()
