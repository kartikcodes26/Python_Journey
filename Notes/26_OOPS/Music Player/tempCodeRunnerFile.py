import vlc
from time import sleep

instance = vlc.Instance()
player = instance.media_player_new('Music.mp3')
player.play()
sleep(0.5)
print(player.get_length() / (1000 * 60))