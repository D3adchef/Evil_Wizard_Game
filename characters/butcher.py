import random
from characters.base import Character  # ✅ Import the base class

class Butcher(Character):
    def __init__(self, name):
        super().__init__(name, health=130, attack_power=28)
        self.intelligence = 20
        self.agility = 22
        self.max_health = 130
        self.blocking = False
        self.evading = False

    def attack(self, opponent):
        damage = random.randint(20, 28)
        opponent.health -= damage
        print(f"{self.name} swings a meat tenderizer at {opponent.name} for {damage} damage!")

    def heal(self):
        heal_amount = 10
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} eats raw chicken and restores {heal_amount} HP! Current HP: {self.health}/{self.max_health}")

    def cleaver_strike(self, opponent):
        damage = random.randint(20, 35)
        opponent.health -= damage
        print(f"{self.name} hacks at {opponent.name} with a cleaver for {damage} damage!")

    def spice_mix(self, opponent):
        effect = random.choice(["burn", "slow", "weaken"])

        if effect == "burn":
            damage = 10
            opponent.health -= damage
            print(f"{self.name} hurls ghost pepper powder! {opponent.name} is burned for {damage} damage!")

        elif effect == "slow":
            print(f"{self.name} throws calming herbs! {opponent.name} looks sluggish... but shrugs it off.")

        elif effect == "weaken":
            original_power = opponent.attack_power
            opponent.attack_power = max(1, opponent.attack_power - 5)
            reduced = original_power - opponent.attack_power
            print(f"{self.name} tosses sour spice mix! {opponent.name}'s attack power drops by {reduced}!")

    def display_stats(self):
        print(f"\n🔪 {self.name}'s Stats:")
        print(f"Class: Butcher")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Intelligence: {self.intelligence}")
        print(f"Agility: {self.agility}\n")

