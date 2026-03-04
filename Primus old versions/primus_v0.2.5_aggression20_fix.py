
import pymem
import pymem.process
import time
import random

# === PRIMUS v0.2.5 CUSTOMIZED AGGRESSION + DIFFICULTY ===

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

        # TEMP Cop Speed Control (optional)
        self.cop1_address = 0x0E84FCE4

    def read_speed(self):
        try:
            speed = self.pm.read_float(self.base_address + self.speed_offset)
        except:
            speed = 0.0
        return speed

    def analyze_speed(self, speed):
        delta = abs(speed - self.last_speed)
        if speed > 110 or delta > 25:
            self.aggression_score += 1
        else:
            self.aggression_score = max(0, self.aggression_score - 0.5)

        self.aggression_score = min(10, self.aggression_score)
        self.last_speed = speed

    def update_difficulty(self):
        if self.aggression_score >= 3:
            increase = int(self.aggression_score * 1.5) + random.randint(0, 2)
            self.difficulty_level = min(20, self.difficulty_level + increase)
            self.aggression_score = 0
        elif self.aggression_score == 0 and self.difficulty_level > 1:
            self.difficulty_level -= 1

    def control_cop_ai(self):
        try:
            if self.difficulty_level <= 5:
                self.pm.write_float(self.cop1_address, 0.0)
            elif self.difficulty_level <= 10:
                self.pm.write_float(self.cop1_address, 50.0)
            else:
                self.pm.write_float(self.cop1_address, 150.0)
        except:
            print("Cop address not writable this session.")

    def display_status(self, speed):
        print(f"Speed: {speed:.2f} MPH | Difficulty: {self.difficulty_level} / 20 | Aggression Score: {self.aggression_score:.1f} / 10")

    def run(self):
        print("PRIMUS v0.2.5 - Live AI Test Running...")
        try:
            while True:
                speed = self.read_speed()
                self.analyze_speed(speed)
                self.update_difficulty()
                self.control_cop_ai()
                self.display_status(speed)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down PRIMUS v0.2.5")

if __name__ == "__main__":
    engine = PrimusEngine()
    engine.run()
