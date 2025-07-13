#  Breakout Game 

This is a custom-built **Breakout-style arcade game** created using **Python** and **Pygame**, with several exciting features such as sound effects, a live timer, hearts (lives), power-ups, and a simple GUI-based gameplay.

---

##  Game Overview

The goal of the game is to break all the blocks using a bouncing ball while preventing the ball from falling by controlling the paddle. You lose a life when the ball falls and win the game when all blocks are broken.

---

##  Features

-  **Sound Effects**  
  - Paddle/Block collision  
  - Gaining and losing lives  
  - Win and Game Over effects

-  **Live Timer**  
  - Displays real-time gameplay duration (MM:SS)

-  **Lives System**  
  - Player starts with 3 hearts  
  - Loses 1 life when the ball falls  
  - Game Over when all hearts are lost

-  **Power-Ups (Hearts)**  
  - Random chance to drop a heart when breaking a block  
  - Catch it with the paddle to gain 1 extra life (up to 3 max)

-  **Block Difficulty Levels**  
  - Top two rows require two hits to break  
  - Bottom rows break with one hit

-  **Click to Start / Restart**  
  - User can click to start the game or restart after Game Over or winning

---

##  Controls

- **Left / Right Arrow Keys**: Move the paddle  
- **Mouse Click**: Start or restart the game

---

##  Required Assets

Place these files in the same directory as the script:

- `heart.png` — Heart image used to display remaining lives  
- `gain_life.mp3` — Sound for collecting a heart  
- `win.mp3` — Sound when all blocks are cleared  
- `lose_life.mp3` — Sound for losing a life  
- `lose_life_final.mp3` — Sound for final life lost (Game Over)  
- `paddle_hit.mp3` — Sound for paddle and block collision

---

##  How to Run

### 1. Install Pygame
```bash
pip install pygame
```

### 2. Run the game
```bash
python breakout.py
```

---

##  Game Screen Elements

- **Top Left**: Lives displayed as heart icons  
- **Top Right**: Timer in MM:SS format  
- **Center**: Game messages ("Click to Start", "Game Over", etc.)  
- **Blocks**: Vary in strength (1 or 2 hits)

---

## Project Structure

```
breakout_game/
│
├── breakout.py             # Main game script
├── heart.png               # Heart image for lives
├── gain_life.mp3           # Sound: extra life
├── win.mp3                 # Sound: win
├── lose_life.mp3           # Sound: lose one life
├── lose_life_final.mp3     # Sound: game over
├── paddle_hit.mp3          # Sound: paddle/block collision
└── README.md               # Project documentation
```

---

##  Notes

- Game window size: **600x600**
- Make sure all image and sound files are named exactly as expected
- Sound volume can be adjusted inside the code if needed

---

##  Future Ideas (Optional)

- Add more power-ups (like speed boost, multi-ball)
- Implement a level system or scoring
- Add background music
- Make the game mobile-compatible using Kivy or another framework

