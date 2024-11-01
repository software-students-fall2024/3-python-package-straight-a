from typing import Literal
import random
import time

class VirtualPet: 
    _HAPPINESS_EMOJIS = {
        range(1, 3): "૮₍ •᎔•₎ა",
        range(3, 5): "૮₍ • - •₎ა",
        range(5, 7): "૮₍ •ᴗ•₎ა",
        range(7, 9): "૮₍ ˶>ᴗ<˶₎ა",
        range(9, 11): "૮₍ ˊᗜˋ₎ა♡"
    }
    _SLEEP_EMOJI = "૮₍ っ ̫-₎ა  ૮ ᴗ͈ˬᴗ͈ ౭౭౭ა"
    _DIRTY_EMOJI = "৩৩৩૮₍ ๑ᵒᯅᵒ๑₎ა೨೨"

    def __init__(self, name: str):
        self.name = name
        self.happiness = 10
        self.cleanness = 10
        self.is_sleeping = False
        self.dirty_command_count = 0
        self.active = True

    def _get_emoji(self) -> str:
        if self.is_sleeping:
            return self._SLEEP_EMOJI
        if self.cleanness < 3:
            return self._DIRTY_EMOJI
        
        for happiness_range, emoji in self._HAPPINESS_EMOJIS.items():
            if self.happiness in happiness_range:
                return emoji
        return self._HAPPINESS_EMOJIS[range(1, 3)]
    
    def _check_cleanness(self):
        if self.cleanness < 3:
            self.dirty_command_count += 1
            if self.dirty_command_count >= 5:
                self.happiness = max(1, self.happiness - 1)
                print(f"Warning: You need to give {self.name} a shower!")
        else:
            self.dirty_command_count = 0
    
    def _display_status(self):
        print(f"\n{self._get_emoji()}")
        print(f"Current Happiness Level: {self.happiness}, Cleanness Level: {self.cleanness}")
    
    ###
    def feed_pet(self):
        if self.is_sleeping:
            print(f"{self.name} is sleeping!")
            return
        
        self.happiness = min(10, self.happiness + 1)
        self.cleanness = max(1, self.cleanness - 2)
        self._check_cleanness()
        self._display_status()

    ###
    def exit(self):
        self.active = False
        print(f"Goodbye, {self.name}! Thanks for the memories!")

    ###
    def restart(self):
        self.happiness = 10
        self.cleanness = 10
        self.is_sleeping = False
        self.dirty_command_count = 0
        self.active = True
        print(f"{self.name} has been restarted to default!")
        self._display_status()

    ###
    def take_shower(self):
        self.cleanness = 10
        self.dirty_command_count = 0
        print(f"{self.name} has taken a shower and is now clean!")
        self._display_status()

    def pet_sleep(self):
        print(f"{self.name} is going to sleep...")
        self.is_sleeping = True 
        sleep_time = random.randint(20, 25) 
        time.sleep(sleep_time)
        self.is_sleeping = False 
        print(f"{self.name} has already woke up after {sleep_time} seconds of sleep!")
