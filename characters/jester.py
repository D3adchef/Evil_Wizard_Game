import random
from characters.base import Character  # ✅ Import base class

class Jester(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=22)
        self.intelligence = 35
        self.agility = 30
        self.max_health = 110
        self.blocking = False
        self.evading = False

    def attack(self, opponent):
        damage = random.randint(15, 25)
        opponent.health -= damage
        print(f"{self.name} tells a side-splitting joke to {opponent.name}, causing {damage} damage!")

    def heal(self):
        heal_amount = 15
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} juggles flaming torches and restores {heal_amount} HP! Current HP: {self.health}/{self.max_health}")

    def joke_strike(self, opponent):
        damage = self.attack_power + 5
        opponent.health -= damage
        print(f"{self.name} delivers a killer pun! {opponent.name} takes {damage} damage!")

    def prop_strike(self, opponent):
        damage = random.randint(15, 25)
        opponent.health -= damage
        print(f"{self.name} slaps {opponent.name} with a rubber chicken! {opponent.name} takes {damage} damage!")

        # Attempt to stun the opponent (e.g., the wizard)
        if hasattr(opponent, 'stunned'):
            if random.random() < 0.4:
                opponent.stunned = True
                print(f"{opponent.name} is stunned and may lose their next turn!")

    def display_stats(self):
        print(f"\n🤡 {self.name}'s Stats:")
        print(f"Class: Jester")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Agility: {self.agility}\n")
