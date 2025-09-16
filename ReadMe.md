# ⌨️ Key War – Typing Game

Key War is a fast-paced typing game built with **Python** and **Pygame**.  
Defeat enemies by typing words before they reach you, track your **Words Per Minute (WPM)**, and improve your typing skills with fun visuals!

---

## 🚀 Features
- 🎮 **Engaging Gameplay** – Enemies drop words, and you must type them quickly to destroy them.  
- 📊 **Typing Stats** – Real-time **WPM** and **Accuracy** calculation.  
- 💖 **Lives System** – Lose a life when you miss words.  
- 🌊 **Animated Text Effects** – Wave/water-style animated titles.  
- 🖼️ **Custom Graphics** – Pixel-art ships, backgrounds, and UI elements.  
- 🎶 (Optional) Sound effects and music support.  

---
## 🛠️ Tech Stack

* Python 3.10+
* Pygame
* Custom assets (fonts, pixel-art, sounds)

[---

## 📷 Screenshots
![](data\screenshots\1.png)

![](data\screenshots\2.png)

![](data\screenshots\3.png)

---

## ⚙️ Installation

1. Clone this repository:
```bash
   git clone https://github.com/yourusername/key-war.git
   cd key-war
```

2. Clone this repository:
```
pip install -r requirements.txt
```

3. Run the game:
```
python main.py
```
---
## 🎯 How to Play

* Words appear on the screen attached to enemies.
* Start typing:

   -  The first correct key locks onto a word.
    
    - Keep typing until the word is completed.
    
    - The enemy is destroyed when the word is finished.
* If an enemy reaches you before you finish typing, you lose a life.
* The game ends when you lose all lives.
---
## 📊 Typing Analysis

The game tracks:

* WPM (Words Per Minute) – based on total characters typed / 5, adjusted by time in minutes.

* Accuracy – (Correctly typed words ÷ Total words attempted) × 100.
---
## 🧩 Future Improvements

* Multiplayer / online leaderboard
* More enemy types and word categories
* Power-ups and boss fights
* Advanced stats dashboard

---
## 🙌 Contribution

**Pull requests are welcome!**

Feel free to open issues for bugs, feature requests, or improvements.