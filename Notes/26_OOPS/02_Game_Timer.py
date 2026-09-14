import time
from time import sleep

class game:
    started = False
    start_time = None
    end_time = None
    start_numeric = None
    end_numeroc = None
    player_count = 0
    alive_count = 0

    # No player can be created after the game has been started
    def __init__(self, p_name):
        if game.started:
            print(f"The game has already been started at {self.start_time}")
            return

        self.player_name = p_name
        self.alive = True
        game.alive_count += 1
        self.death_time = None
        game.player_count += 1

    def die(self):
        if not self.alive:
            print("The player is already dead")
            return
        self.alive = False
        self.death_time = time.ctime()
        game.alive_count -= 1
        print(f"Player {self.player_name} has died at {self.death_time}")

    @classmethod
    def start(cls):
        if cls.player_count == 0:
            print("No players joined. Cannot start")
            return
        if cls.started:
            print(f"The game has already been started")
            return
        cls.start_numeric = time.time()
        cls.started = True
        cls.start_time = time.ctime()
        print(f"The game has been started at {cls.start_time}")

    @classmethod
    def end(cls):
        if not cls.started:
            print(f"The game has not started or already ended")
            return
        cls.started = False
        cls.end_time = time.ctime()
        cls.end_numeric = time.time()
        duration = cls.end_numeric - cls.start_numeric
        print(f"The game ended with {cls.alive_count} players alive")
        print(f"Duration :{duration:.2f}")


p1 = game("Kartik")
p2 = game("Vivobook")
p1.die()

game.start()
sleep(2)
p2.die()
game.end()
