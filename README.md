# 🌊 Ocean Escapes — Life Below Water (Pygame Arcade Game)

**Ocean Escapes** (*Life Below Water*) is a 2D arcade shooter game built in **Python** using **Pygame**. Set underwater, your mission is to pilot a submersible craft at the bottom of the screen and shoot descending ocean trash before it reaches the seabed—while avoiding hitting marine life (fish)!

---

## 📂 Repository Structure

```text
Ocean-Escapes/
├── competition_game.py   # Main Pygame arcade game loop, collision detection, and scoring
├── background.png        # Underwater background artwork (800x600)
├── player.png            # Player submersible sprite
├── trash.png             # Ocean trash target sprite (+1 score)
├── fish.png              # Marine life sprite (-1 score penalty if hit!)
├── bullet.png            # Projectile sprite
├── laser.wav             # Projectile firing sound effect
├── explosion.wav         # Target hit sound effect
└── README.md             # Game instructions and documentation
```

---

## 🎮 Controls & Gameplay Rules

| Key | Action |
| :--- | :--- |
| `←` (Left Arrow) | Move craft left |
| `→` (Right Arrow) | Move craft right |
| `Spacebar` | Fire laser projectile |

### Scoring System
- **Hit Ocean Trash (`trash.png`)**: **+1 Point**
- **Hit a Fish (`fish.png`)**: **-1 Point** (Protect marine life!)
- **Game Over**: Triggered if ocean trash descends all the way to your craft's vertical level.

---

## 🚀 How to Play

1. **Clone the repository**:
   ```bash
   git clone https://github.com/sparsh0106/Ocean-Escapes.git
   cd Ocean-Escapes
   ```

2. **Install Pygame**:
   ```bash
   pip install pygame
   ```

3. **Launch the game**:
   ```bash
   python competition_game.py
   ```

---

## 👤 Author

**Sparsh Agarwal** — [GitHub](https://github.com/sparsh0106) · [LinkedIn](https://www.linkedin.com/in/sparsh-agarwal-4b443b304/)
