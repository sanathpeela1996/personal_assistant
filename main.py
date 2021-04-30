
import pyaudio
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
wake_up_word = "alexa"

# to change voice cmds
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)


# rate = engine.getProperty('rate')
# print (rate)
# engine.setProperty('rate', 200)

def  talk(cmd):
    engine.say(cmd)
    engine.runAndWait()


def take_cmd():
    try:
        with sr.Microphone() as source:
            print("Please wait. Calibrating microphone...")
            # listen for 5 seconds and create the ambient noise energy level
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening ...")
            voice = listener.listen(source, phrase_time_limit=3)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if wake_up_word in cmd:
               cmd = cmd.replace(wake_up_word,"")
               print(cmd)
               #talk(cmd)
            else:
                print("Not a command for me ")
                return ""
            return cmd
    except Exception as e:
        # talk("I am sorry, could you repeat that")
        # print("exception", str(e))
        return ""


def run_alexa():
    cmd = take_cmd()
    while cmd == "":
        cmd = take_cmd()
    print(cmd)
    if 'play' in cmd:
        content =  cmd.replace("play","")
        talk("Playing "+ content)
        print(content)
        pywhatkit.playonyt(content)
    elif 'time' in cmd:
        time =datetime.datetime.utcnow().strftime('%H:%M:%S')
        print(time)
        talk("Current time is "+time)
    # elif "utc " in cmd:
    #     time =datetime.datetime.utcnow().strftime('%H:%M:%S')
    #     print(time)
    #     talk("Current UTC  time is "+time)
    elif "chrome" in cmd and "open" in cmd:
        cmd =cmd.replace("open","")
        talk("opening"+cmd)
        os.system("open /Applications/Google\ Chrome.app")
    elif "pychram" in cmd and "open" in cmd:
        cmd = cmd.replace("open", "")
        talk("opening" + cmd)
        os.system("open /Applications/PyCharm\ CE.app")
    elif "slack" in cmd and "open" in cmd:
        cmd = cmd.replace("open", "")
        talk("opening" + cmd)
        os.system("open /Applications/Slack.app")
    elif "iterm" in cmd and "open" in cmd:
        cmd = cmd.replace("open", "")
        talk("opening" + cmd)
        os.system("open /Applications/iterm.app")
    elif "calculator" in cmd and "open" in cmd:
        cmd = cmd.replace("open", "")
        talk("opening" + cmd)
        os.system("open /Applications/Calculator.app")
    else:
        talk("I am not sure I understand, could you repeat that.")



while True:
    run_alexa()