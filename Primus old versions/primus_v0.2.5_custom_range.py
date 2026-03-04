
import pymem
import pymem.process
import time

# === PRIMUS v0.2.5 CUSTOM DIFFICULTY TEST ===

class PrimusEngine:
    def __init__(self):
        self.difficulty_level = 3
        self.aggression_score = 0
        self.last_speed = 0

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

    def analyze_speed(self, speed):
        delta = abs(speed - self.last_speed)
        if speed > 110:
            self.aggression_score += 1
        elif delta > 30:
            self.aggression_score += 1
        else:
            self.aggression_score = max(0, self.aggression_score - 0.5)

        self.aggression_score = min(10, self.aggression_score)
        self.last_speed = speed

    def update_difficulty(self):
        if self.aggression_score >= 3:
            self.difficulty_level = min(20, self.difficulty_level + 1)
            self.aggression_score = 0
        elif self.aggression_score == 0 and self.difficulty_level > 1:
            self.difficulty_level -= 1

    def display_status(self, speed):
        print(f"Speed: {speed:.2f} MPH | Difficulty: {self.difficulty_level} / 20 | Aggression Score: {self.aggression_score} / 10")

    def run(self):
        print("PRIMUS v0.2.5 - CUSTOM DDA TEST STARTED...")
        try:
            while True:
                speed = self.read_speed()
                self.analyze_speed(speed)
                self.update_difficulty()
                self.display_status(speed)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down PRIMUS v0.2.5")

if __name__ == "__main__":
    engine = PrimusEngine()
    engine.run()
