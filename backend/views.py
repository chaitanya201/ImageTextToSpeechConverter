from django.shortcuts import render
import pyttsx3 as tts

# Image to Speech Converter.
import easyocr as itt

def showText(request):
    if request.method == 'POST':

        image = request.FILES['img1'].read()

        reader = itt.Reader(['en'])
        textFromImage = ""
        ttsObj = tts.init()
        ttsObj.setProperty("rate", 178)
        out = reader.readtext(image)
        for result in out:
            textFromImage += result[1] + " "
        print(textFromImage)
        ttsObj.say(textFromImage)
        ttsObj.runAndWait()
        return render(request, 'home.html', {'text': textFromImage})


def home(request):
    return render(request, 'home.html', {'text':""})

