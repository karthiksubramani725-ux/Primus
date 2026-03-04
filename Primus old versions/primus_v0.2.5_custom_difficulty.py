
import pymem
import time
import random

class Primus:
    def __init__(self):
        self.pm = pymem.Pymem("speed.exe")
        self.speed_address = 0x000000  # Replace with actual pointer address
        self.difficulty_level = 1
        self.aggression_score = 0
        self.speed_history = []

    def read_speed(self):
        try:
            speed = self.pm.read_float(self.speed_address)
            return speed
        except:
            return 0.0

    def update_aggression_score(self, speed):
        if len(self.speed_history) > 10:
            self.speed_history.pop(0)
        self.speed_history.append(speed)

        # If sudden spikes or high speed, increase aggression
        if len(self.speed_history) >= 2:
            delta = self.speed_history[-1] - self.speed_history[-2]
            if delta > 10 or speed > 120:
                self.aggression_score += 1
            else:
                self.aggression_score = max(0, self.aggression_score - 0.5)

        self.aggression_score = min(10, max(0, self.aggression_score))

    def calculate_difficulty(self):
        base = int(self.aggression_score * 2)
        random_fluctuation = random.randint(0, 2)
        self.difficulty_level = min(20, base + random_fluctuation)

    def display_stats(self, speed):
        print(f"Speed: {speed:.2f} MPH | Aggression: {self.aggression_score:.1f} / 10 | Difficulty: {self.difficulty_level} / 20")

    def run(self):
        print("PRIMUS v0.2.5 - Real-Time DDA Engine Running...")
        while True:
            speed = self.read_speed()
            self.update_aggression_score(speed)
            self.calculate_difficulty()
            self.display_stats(speed)
            time.sleep(1)

if __name__ == "__main__":
    primus = Primus()
    primus.run()
