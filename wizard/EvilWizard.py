import random
from characters.base import Character

class EvilWizard(Character):
    def __init__(self, name="The Dark Wizard"):
        super().__init__(name, health=150, attack_power=15)
        self.max_health = 150
        self.confused = False  # NEW: Track confusion

    def regenerate(self):
        regen_amount = 5
        self.health = min(self.health + regen_amount, self.max_health)
        print(f"{self.name} absorbs dark energy and regenerates {regen_amount} HP! Current HP: {self.health}/{self.max_health}")

    def cast_spell(self, player):
        spell = random.choice(["fireball", "lightning", "curse"])

        if spell == "fireball":
            damage = random.randint(10, 25)
            print(f"{self.name} hurls a Fireball!")
        elif spell == "lightning":
            damage = random.randint(15, 20)
            print(f"{self.name} summons a bolt of Lightning!")
        else:  # Curse
            damage = random.randint(5, 30)
            print(f"{self.name} whispers a terrifying Curse!")

        # Check for block or evade on player
        if player.blocking:
            damage = damage // 2
            print(f"{player.name} blocks part of the damage! Reduced to {damage}.")
            player.blocking = False
        elif player.evading:
            if random.random() < 0.4:
                damage = 0
                print(f"{player.name} evades the spell completely!")
            else:
                print(f"{player.name} tries to dodge but fails!")
            player.evading = False

        player.health -= damage
        print(f"{player.name} takes {damage} damage!\n")

    def take_turn(self, player):
        # Check for confusion first
        if self.confused:
            if random.random() < 0.5:
                print(f"{self.name} looks disoriented and fails to act!\n")
                self.confused = False
                return
            else:
                print(f"{self.name} shakes off the confusion!\n")
                self.confused = False

        # Choose action randomly
        action = random.choice(["attack", "heal"])

        if action == "attack":
            self.cast_spell(player)
        else:
            self.regenerate()

    def display_stats(self):
        print(f"\n🧙 {self.name}'s Stats:")
        print(f"Class: Evil Wizard")
        print(f"Health: {self.health}/{self.max_health}")
        print(f"Attack Power: {self.attack_power}")
        print(f"Abilities: Fireball, Lightning, Curse\n")
