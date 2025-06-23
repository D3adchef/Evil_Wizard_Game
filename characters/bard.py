import random
from characters.base import Character  # Make sure base.py exists in characters folder

class Bard(Character):
    def __init__(self, name):
        super().__init__(name, health=90, attack_power=20)
        self.intelligence = 40
        self.agility = 35
        self.max_health = 90
        self.blocking = False
        self.evading = False

    def attack(self, opponent):
        damage = random.randint(15, 25)
        opponent.health -= damage
        print(f"{self.name} strums a sonic chord at {opponent.name} for {damage} damage!")

    def heal(self):
        heal_amount = 15
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} plays a calming note and heals for {heal_amount} HP. Current HP: {self.health}/{self.max_health}")

    def musical_strike(self, opponent):
        damage = self.attack_power + 5
        opponent.health -= damage
        print(f"{self.name} plays a piercing solo! {opponent.name} takes {damage} damage!")

    def sleepy_song(self, opponent):
        chance = random.random()
        if chance < 0.5:
            opponent.evading = True
            print(f"{self.name} plays a dreamy lullaby... {opponent.name} looks drowsy and may miss their next attack!")
        else:
            print(f"{self.name} plays a sleepy tune, but {opponent.name} resists the effect!")

    def display_stats(self):
        print(f"\n🎼 {self.name}'s Stats:")
        print(f"Class: Bard")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Agility: {self.agility}\n")
