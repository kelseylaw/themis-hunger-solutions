import TextToMP3
import PlayMP3

class TextToSpeech:
    def textToSpeech(self, text, file):
        record = TextToMP3.TextToMP3()
        record.convertToMp3("{}".format(text), "{}".format(file))

        play = PlayMP3.PlayMP3()
        play.playMP3("{}".format(file))
