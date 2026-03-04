
import pymem
import time
import random

class Primus:
    def __init__(self, process_name="speed.exe"):
        self.pm = pymem.Pymem(process_name)
        self.speed_address = 0x00000000  # Replace with your correct speed pointer
        self.difficulty_level = 1
        self.aggression_score = 0
        self.max_difficulty = 20
        self.max_aggression = 10

    def read_speed(self):
        try:
            return self.pm.read_float(self.speed_address)
        except:
            return 0.0

    def calculate_aggression(self, speed):
        if speed > 140:
            self.aggression_score = min(self.max_aggression, self.aggression_score + 1)
        elif speed < 60:
            self.aggression_score = max(0, self.aggression_score - 1)
        return self.aggression_score

    def update_difficulty(self):
        if self.aggression_score >= 7:
            self.difficulty_level = min(self.max_difficulty, self.difficulty_level + 2)
        elif self.aggression_score >= 4:
            self.difficulty_level = min(self.max_difficulty, self.difficulty_level + 1)
        elif self.aggression_score <= 1:
            self.difficulty_level = max(1, self.difficulty_level - 1)
        return self.difficulty_level

    def run(self):
        print("PRIMUS v0.2 - Adaptive AI Engine Started")
        while True:
            speed = self.read_speed()
            aggression = self.calculate_aggression(speed)
            difficulty = self.update_difficulty()

            print(f"Speed: {speed:.2f} MPH | Aggression: {aggression} / {self.max_aggression} | Difficulty: {difficulty} / {self.max_difficulty}")
            time.sleep(1)

if __name__ == "__main__":
    primus = Primus()
    primus.run()
