import random
from characters.base import Character  # ✅ Add the correct import

class Beastmaster(Character):
    def __init__(self, name):
        super().__init__(name, health=115, attack_power=23)
        self.max_health = 115
        self.thelma_ready = True
        self.louise_ready = True
        self.blocking = False
        self.evading = False

    def attack(self, opponent):
        damage = random.randint(18, 26)
        opponent.health -= damage
        print(f"{self.name} strikes {opponent.name} with a beast whip for {damage} damage!")

    def heal(self):
        heal_amount = 15
        self.health = min(self.health + heal_amount, self.max_health)
        print(f"{self.name} takes a breath and heals for {heal_amount} HP. Current HP: {self.health}/{self.max_health}")

    def thelma_attack(self, opponent):
        if self.thelma_ready:
            damage = random.randint(15, 25)
            opponent.health -= damage
            self.thelma_ready = False
            print(f"Thelma the raccoon dashes out and bites {opponent.name} for {damage} damage!")
        else:
            print("Thelma is hiding and needs to rest!")

    def louise_surprise(self, opponent):
        if self.louise_ready:
            damage = random.randint(10, 20)
            opponent.health -= damage
            self.louise_ready = False
            print(f"Louise the opossum plays dead and tail-whips {opponent.name} for {damage} damage!")

            # Confusion chance
            if hasattr(opponent, 'confused'):
                if random.random() < 0.4:
                    opponent.confused = True
                    print(f"{opponent.name} looks dazed and confused from the tail whip!")
        else:
            print("Louise has vanished into the mist...")

    def call_of_the_wild(self):
        self.thelma_ready = True
        self.louise_ready = True
        print(f"{self.name} whistles into the trees... Thelma and Louise are ready to strike again!")

    def display_stats(self):
        print(f"\n🐾 {self.name}'s Stats:")
        print(f"Class: Beastmaster")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Companions: Thelma (raccoon), Louise (opossum)\n")
