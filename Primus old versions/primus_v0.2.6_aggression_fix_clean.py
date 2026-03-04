
import pymem
import pymem.process
import time
import random

# === PRIMUS v0.2.6 - Aggression Fix & Cleaned Up ===

class PrimusEngine:
    def __init__(self):
        self.difficulty_level = 3
        self.aggression_score = 0
        self.speed_history = []

        # Attach to NFS MW
        self.pm = pymem.Pymem("speed.exe")
        self.base_address = pymem.process.module_from_name(self.pm.process_handle, "speed.exe").lpBaseOfDll

        # Player speed (read only)
        self.speed_offset = 0x514798

    def read_speed(self):
        try:
            speed = self.pm.read_float(self.base_address + self.speed_offset)
        except:
            speed = 0.0
        return speed

    def update_aggression_score(self, speed):
        if len(self.speed_history) > 10:
            self.speed_history.pop(0)
        self.speed_history.append(speed)

        if len(self.speed_history) >= 2:
            delta = abs(self.speed_history[-1] - self.speed_history[-2])
            if speed > 110 or delta > 20:
                self.aggression_score += 1
            else:
                self.aggression_score -= 0.25

        self.aggression_score = max(0, min(10, self.aggression_score))

    def update_difficulty(self):
        base = int(self.aggression_score * 2)
        fluctuation = random.randint(0, 2)
        self.difficulty_level = min(20, base + fluctuation)

    def display_status(self, speed):
        print(f"Speed: {speed:.2f} MPH | Aggression: {self.aggression_score:.2f} / 10 | Difficulty: {self.difficulty_level} / 20")

    def run(self):
        print("PRIMUS v0.2.6 - Aggression Fix Applied")
        try:
            while True:
                speed = self.read_speed()
                self.update_aggression_score(speed)
                self.update_difficulty()
                self.display_status(speed)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down PRIMUS v0.2.6")

if __name__ == "__main__":
    engine = PrimusEngine()
    engine.run()
