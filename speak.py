import pyttsx3 as sx

class Voicing:
  def sayText(text):
    a = sx.init();
    a.say(text=text)
    a.runAndWait()