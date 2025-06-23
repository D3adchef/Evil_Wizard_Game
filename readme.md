# 🧙‍♂️ Evil Wizard - Terminal Battle Game

A text-based Python game where you choose a hero and face off against the Dark Wizard in a turn-based battle! Built using object-oriented programming, this game features quirky characters, unique special abilities, and randomized enemy behavior.

## 🎮 How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/D3adchef/Evil-Wizard_game.git
   cd Evil-Wizard_game

2. Run the game:

bash
python main.py

3. Follow the prompts to:

Choose your character class: Bard, Jester, Beastmaster, or Butcher

Use attacks, special abilities, heal, block, or view stats

Survive and defeat the Evil Wizard!

🧠 Character Classes
Class	Description
Bard	Agile and intelligent. Can strike musically or lull enemies to sleep.
Jester	Unpredictable and clever. Jokes hurt, and props may stun!
Beastmaster	Balanced fighter. Summons Thelma (raccoon) and Louise (opossum). Louise may confuse enemies.
Butcher	High health and attack. Uses cleavers and spices to inflict pain or weaken foes.

🧙 Enemy Behavior
The Dark Wizard now chooses actions randomly:

Casts powerful spells: fireball, lightning, or curse

May regenerate health

Can be stunned or confused by player abilities

🗂️ Project Structure
Evil-Wizard_game/
├── characters/
│   ├── base.py
│   ├── bard.py
│   ├── jester.py
│   ├── beastmaster.py
│   └── butcher.py
├── battle/
│   └── battle.py
├── utils/
│   └── preview_stats.py
├── wizard.py
├── main.py
└── README.md

✅ Features
Four custom character classes

Turn-based combat system

Block and evade mechanics

Confusion and stun effects

Colorful combat descriptions

Fully modular and expandable

✍️ Author
Created by D3adchef