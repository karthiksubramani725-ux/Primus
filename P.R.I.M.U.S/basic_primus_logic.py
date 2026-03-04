# Simple example: Primus AI logic for adjusting enemy difficulty
player_accuracy = 0.92

if player_accuracy > 0.9:
    enemy_difficulty = "Hard"
else:
    enemy_difficulty = "Normal"

print(f"Enemy difficulty set to: {enemy_difficulty}")