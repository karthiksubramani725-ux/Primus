
import pymem
import pymem.process
import time
import random

# === PRIMUS v0.2.7 - Debugged Live Influence Version ===

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

        # Writable memory offsets
        self.heat_offset = 0x5231A8
        self.cop_spawn_flag = 0x67B92C
        self.ai_rubberband = 0x58F930

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
            if speed > 110:
                self.aggression_score += 0.5
            if delta > 20:
                self.aggression_score += 1
            else:
                self.aggression_score -= 0.25

        self.aggression_score = max(0, min(10, self.aggression_score))

    def update_difficulty(self):
        base = int(self.aggression_score * 2)
        fluctuation = random.randint(0, 2)
        self.difficulty_level = min(20, base + fluctuation)

    def update_game_parameters(self):
        try:
            # Confirm game influence by hardcoding max chaos
            self.pm.write_int(self.heat_offset, 5)
            self.pm.write_uchar(self.cop_spawn_flag, 1)
            self.pm.write_float(self.ai_rubberband, 2.5)

            # Debug log to confirm real writes
            print(f"[PRIMUS WRITE] Heat: 5, Cop Spawn: 1, AI Multiplier: 2.5")

        except Exception as e:
            print(f"[PRIMUS ERROR] Memory write failed: {e}")

    def display_status(self, speed):
        print(f"Speed: {speed:.2f} MPH | Aggression: {self.aggression_score:.2f} / 10 | Difficulty: {self.difficulty_level} / 20")

    def run(self):
        print("PRIMUS v0.2.7 - Debug Live Influence Mode Active")
        try:
            while True:
                speed = self.read_speed()
                self.update_aggression_score(speed)
                self.update_difficulty()
                self.update_game_parameters()
                self.display_status(speed)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Shutting down PRIMUS v0.2.7")

if __name__ == "__main__":
    engine = PrimusEngine()
    engine.run()
