from gtts import gTTS
from io import BytesIO

language = 'en'
#tld = 'com.au'
mp3_fp = BytesIO()

mytext = input("Enter your text: ")

myobj = gTTS(text=mytext, lang=language)
  
# Saving the converted audio in a mp3 file named
# welcome 
#cd /Documents/Uni
myobj.save("test.mp3")
myobj.write_to_fp(mp3_fp)