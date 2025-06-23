import random
from characters.bard import Bard
from characters.jester import Jester
from characters.beastmaster import Beastmaster
from characters.butcher import Butcher

def battle(player, wizard):
    print("\n🌑 The battle begins!\n")

    while player.health > 0 and wizard.health > 0:
        print(f"--- {player.name}'s Turn ---")
        print("1. Attack")
        print("2. Use Special Ability")
        print("3. Heal")
        print("4. Block/Evade")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)

        elif choice == '2':
            print("\nChoose a special ability:")
            if isinstance(player, Bard):
                print("1. Musical Strike")
                print("2. Sleepy Song")
                ability = input("Select ability: ")
                if ability == '1':
                    player.musical_strike(wizard)
                elif ability == '2':
                    player.sleepy_song(wizard)
                else:
                    print("Invalid ability.")

            elif isinstance(player, Jester):
                print("1. Joke Strike")
                print("2. Prop Strike")
                ability = input("Select ability: ")
                if ability == '1':
                    player.joke_strike(wizard)
                elif ability == '2':
                    player.prop_strike(wizard)
                else:
                    print("Invalid ability.")

            elif isinstance(player, Beastmaster):
                print("1. Thelma Attack")
                print("2. Louise Surprise")
                print("3. Call of the Wild (reset both)")
                ability = input("Select ability: ")
                if ability == '1':
                    player.thelma_attack(wizard)
                elif ability == '2':
                    player.louise_surprise(wizard)
                elif ability == '3':
                    player.call_of_the_wild()
                else:
                    print("Invalid ability.")

            elif isinstance(player, Butcher):
                print("1. Cleaver Strike")
                print("2. Spice Mix")
                ability = input("Select ability: ")
                if ability == '1':
                    player.cleaver_strike(wizard)
                elif ability == '2':
                    player.spice_mix(wizard)
                else:
                    print("Invalid ability.")

        elif choice == '3':
            player.heal()

        elif choice == '4':
            if isinstance(player, Butcher):
                player.blocking = True
                print(f"{player.name} braces for impact and prepares to block!")
            elif isinstance(player, (Bard, Beastmaster)):
                player.evading = True
                print(f"{player.name} prepares to evade the next attack!")
            elif isinstance(player, Jester):
                if random.random() < 0.5:
                    player.evading = True
                    print(f"{player.name} tumbles away from the next attack!")
                else:
                    player.blocking = True
                    print(f"{player.name} throws up a goofy defense!")

        elif choice == '5':
            player.display_stats()
            wizard.display_stats()
            continue  # Skip wizard turn when viewing stats

        else:
            print("Invalid choice. Try again.")
            continue

        # Wizard's Turn
        if wizard.health > 0:
            print(f"\n--- {wizard.name}'s Turn ---")
            wizard.take_turn(player)

        if player.health <= 0:
            print(f"\n💀 {player.name} has been defeated! Evil wins... for now.")
            break

    if wizard.health <= 0:
        print(f"\n🎉 {wizard.name} has been defeated by {player.name}! You win!")
