import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
engine.say("中文测试")
engine.runAndWait()