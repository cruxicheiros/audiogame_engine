from pydub import AudioSegment, effects
from pydub.playback import play
from os import path
from math import hypot, fabs, asin, sin, degrees

class AudioSource:
    def __init__(self, x, y, sound_bank={}):
        self.x = x
        self.y = y

        self.sound_bank = sound_bank
        
    def LoadSound(self, filenames, name):
        self.soundslist = []
        
        for i in filenames:
            file_path = path.dirname(path.abspath(__file__)) + "\\sfx\\" + i
            self.wave_obj = AudioSegment.from_file(file_path, format="wav")
            
            self.soundslist.append(self.wave_obj)
        


        self.sound_bank[name] = self.soundslist

    def PlaySound(self, soundlist, listener):
        xdist = self.x - listener.x
        ydist = self.y - listener.y
        hdist = hypot(fabs(xdist), fabs(ydist))
        
        if ydist > 0:
            sound = soundlist[1]
            print('negative')
        else:
            sound = soundlist[0]

        vol_sound = effects.low_pass_filter(sound - hdist, 10000 / hdist)
        
        
        if hdist != 0:
            print(degrees(asin((xdist * sin(90)) / hdist)))
            print('x:' + str(xdist))
            print('hyp:' + str(hdist))
            panned_sound = vol_sound.pan(degrees(asin((xdist * sin(90)) / hdist)) / 90)
            play(panned_sound)
        else:
            play(vol_sound)
            

        
class Listener:
    def __init__(self, x, y):
        self.x = x
        self.y = y


