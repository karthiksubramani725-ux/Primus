# primus_v01_cheatengine.py (MPH-TUNED)

import pymem
import pymem.process
import time

# === PRIMUS + CHEAT ENGINE LIVE READER (MPH FIX) ===

class PrimusEngine:
    def __init__(self):
        self.difficulty_level = 0  # Starts at none
        self.aggression_score = 0
        self.last_speed = 0

        # Attach to game
        self.pm = pymem.Pymem("speed.exe")
        self.base_address = pymem.process.module_from_name(self.pm.process_handle, "speed.exe").lpBaseOfDll
        self.speed_offset = 0x514798  # Float address confirmed via CE

    def read_speed(self):
        address = self.base_address + self.speed_offset
        try:
            speed = self.pm.read_float(address)
        except:
            speed = 0.0
        return speed

    def analyze_speed(self, speed):
        delta = abs(speed - self.last_speed)

        # MPH-TUNED THRESHOLDS
        if speed > 90:  # Aggressive driving threshold in MPH (~140 KMH)
            self.aggression_score += 1
        elif delta > 30:  # Hard acceleration or braking
            self.aggression_score += 1

        self.last_speed = speed

    def update_difficulty(self):
        if self.aggression_score >= 3:
            self.difficulty_level = min(5, self.difficulty_level + 1)
            self.aggression_score = 0
        elif self.aggression_score == 0 and self.difficulty_level > 1:
            self.difficulty_level -= 1

    def display_status(self, speed):
        print(f"Speed (MPH): {speed:.2f} | Difficulty: {self.difficulty_level} | Aggression Score: {self.aggression_score}")

    def run(self):
        print("Primus v0.1 Cheat Engine Integration (MPH Tuned) Started...\n")
        try:
            while True:
                speed = self.read_speed()
                self.analyze_speed(speed)
                self.update_difficulty()
                self.display_status(speed)
                time.sleep(1)  # 1 second interval
        except KeyboardInterrupt:
            print("Shutting down Primus.")

if __name__ == "__main__":
    engine = PrimusEngine()
    engine.run()
