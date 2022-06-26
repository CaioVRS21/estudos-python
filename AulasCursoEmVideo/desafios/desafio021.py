import vlc
import time

p = vlc.MediaPlayer("BB _ Q Band - On the beat(MP3_320K).mp3")
p.play()
time.sleep(60)
p.stop()

