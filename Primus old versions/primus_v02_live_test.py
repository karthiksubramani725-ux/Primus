# primus_v02_live_test.py

import pymem
import pymem.process
import time

# === PRIMUS v0.2 LIVE COP CONTROL TEST ===

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

        # TEMP Cop Speed Control (dynamic live RAM address found manually)
        # This is NOT static and may change between sessions
        self.cop1_address = 0x0E84FCE4  # Cop 1 movement control

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
        self.last_speed = speed

    def update_difficulty(self):
        if self.aggression_score >= 3:
            self.difficulty_level = min(5, self.difficulty_level + 1)
            self.aggression_score = 0
        elif self.aggression_score == 0 and self.difficulty_level > 1:
            self.difficulty_level -= 1

    def control_cop_ai(self):
        # Adjust this cop's movement control based on difficulty
        try:
            if self.difficulty_level <= 2:
                self.pm.write_float(self.cop1_address, 0.0)  # Immobilize
            elif self.difficulty_level == 3:
                self.pm.write_float(self.cop1_address, 50.0)  # Medium mobility
            else:
                self.pm.write_float(self.cop1_address, 150.0)  # Full aggression
        except:
            print("⚠️ Cop address not writable this session.")

    def display_status(self, speed):
        print(f"Speed: {speed:.2f} MPH | Difficulty: {self.difficulty_level} | Aggression Score: {self.aggression_score}")

    def run(self):
        print("PRIMUS v0.2 TEMP LIVE COP CONTROL TEST STARTED...")
        try:
            while True:
                speed = self.read_speed()
                self.analyze_speed(speed)
                self.update_difficulty()
                self.control_cop_ai()
                self.display_status(speed)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down PRIMUS v0.2")

if __name__ == "__main__":
    engine = PrimusEngine()
    engine.run()
