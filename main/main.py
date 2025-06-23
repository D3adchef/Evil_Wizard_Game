import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from characters.bard import Bard
from characters.jester import Jester
from characters.beastmaster import Beastmaster
from characters.butcher import Butcher
from wizard.EvilWizard import EvilWizard
from battle import battle
from utils.preview_stats import preview_stats

def create_character():
    print("Choose your character class:")
    print("1. Bard 🎼")
    print("2. Jester 🤡")
    print("3. Beastmaster 🐾")
    print("4. Butcher 🔪")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Bard(name)
    elif class_choice == '2':
        return Jester(name)
    elif class_choice == '3':
        return Beastmaster(name)
    elif class_choice == '4':
        return Butcher(name)
    else:
        print("Invalid choice. Defaulting to Bard.")
        return Bard(name)

def main():
    player = create_character()
    wizard = EvilWizard()
    
    print("\n📝 Previewing Stats Before Battle:")
    preview_stats(player, wizard)

    battle(player, wizard)

if __name__ == "__main__":
    main()
