import vlc # type: ignore
from time import sleep
import os

folder_path = "D:/02_Python/Python_Journey/Notes/26_OOPS/Music Player/"

instance = vlc.Instance()
file_list = os.listdir(folder_path)

print("Enter the name of the music you want to play : ")
print("==================================== Music List ==========================================")
i = 1

for file in file_list:
    if not file.endswith('py'):
        print(f"{i}: {file}")
        i+=1

music_name = input("Enter the songs name : ")
music_path = os.path.join(folder_path, music_name)

if not os.path.exists:
    print(f"{music_name} does not exist")
    exit()

player = instance.media_player_new(music_path)
player.play()


sleep(0.5)
print(f"{player.get_length() / (1000 * 60):.2f} minutes")

print(f"Playing {music_name}: ")
print("p - pause")
print("s - stop")
print("c - contiue")



while True:
    print(f"\r{player.get_position() * 100:.2f} %", end = "", flush=True)
    inp = input()
    if inp == 'p':
        player.pause()
        print("The music has been paused")
    elif inp == 's':
        player.stop()
        print("The music has been stopped")
        break
    elif inp == 'c':
        player.play()
        print("Playing the music again")

# try:
#     print("Music Playing")
#     while True:
#         sleep(1)

# except KeyboardInterrupt:
#     player.stop()
#     print("Music Stopped")

