#!/home/bard/miniconda3/envs/kaldi/bin/python

from vosk import Model, KaldiRecognizer
import os

if not os.path.exists("model-en"):
    print ("Please download the model from https://github.com/alphacep/kaldi-android-demo/releases and unpack as 'model-en' in the current folder.")
    exit (1)

import pyaudio

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

model = Model("model-en")
rec = KaldiRecognizer(model, 16000)

while True:
    data = stream.read(2000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        #print(rec.Result())
        # I commented out this line and added the 3 lines below
        myResult = rec.Result()
        myList = myResult.split("text")
        print(myList[1])
    # I commented out everything below
    #else:
    #    print(rec.PartialResult())
    #    print("two")

#print(rec.FinalResult())
