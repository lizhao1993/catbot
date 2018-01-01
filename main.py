from chatterbot import ChatBot
import pyttsx3
import simpleaudio as sa


def greeting():
    welcome_message = "Hello, I am the chatbot, Catbot! What's your name?"
    return welcome_message

def is_goodbye(user_input):
    goodbyes = ["bye", "goodbye", "farewell", "Goodbye", "Bye", "Goodbye", "GOODBYE", "BYE"]
    for goodbye in goodbyes:
        if goodbye in user_input:
            return True
    return False

def response(user_input, catbot):
    if is_goodbye(user_input):
        return ""
    else:
        return str(catbot.get_response(user_input))

def to_voice(message, engine):
    print(message)
    engine.say(message)
    engine.runAndWait()

def main():
    engine = pyttsx3.init()
    catbot = ChatBot(
    "catbot",
    storage_adapter="chatterbot.storage.MongoDatabaseAdapter")
    to_voice(greeting(), engine)
    user_name = input()
    if user_name == "BOYFRIENDCAT 3000":
        wave_obj = sa.WaveObject.from_wave_file("robot.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        to_voice("BOYFRIENDCAT MODE ACTIVATED", engine)
    else:
        to_voice(response("", catbot), engine)
    while True:
        reponse_message = response(input(), catbot)
        if reponse_message:
            to_voice(reponse_message, engine)
        else:
            to_voice("Goodbye " + user_name + "!", engine)
            exit()

if __name__ == "__main__":
    main()


# Sound from http://soundbible.com/1317-Sci-Fi-Robot.html
# Title: Sci Fi Robot>
# About: Sound of a classic sci-fi robot computing data. youll know what i mean when you hear it. requested by bob jackson
# Uploaded: 01.17.10 | License: Attribution 3.0 | Recorded by Mike Koenig | File Size: 730 KB | Downloads: 42477