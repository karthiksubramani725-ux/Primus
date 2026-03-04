import pymem
import pymem.process
import time
import random
import shutil
import os

# === PRIMUS v0.2.7 - Aggression + Profile Swapping ===

class PrimusEngine:
    def __init__(self):
        self.difficulty_level = 3
        self.aggression_score = 0
        self.speed_history = []

        # Memory Setup
        self.pm = pymem.Pymem("speed.exe")
        self.base_address = pymem.process.module_from_name(self.pm.process_handle, "speed.exe").lpBaseOfDll
        self.speed_offset = 0x514798

        # Profile Setup
        self.profile_dir = "D:/PrimusMW/Profiles/"
        self.game_dir = "D:/Games/NFS_MW_Backup_PrePRIMUS/GLOBAL/"
        self.target_file = os.path.join(self.game_dir, "GLOBALB.BUN")
        self.last_profile_applied = None

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

    def determine_profile(self):
        if self.difficulty_level < 8:
            return "easy.vlt"
        elif self.difficulty_level < 15:
            return "medium.vlt"
        else:
            return "brutal.vlt"

    def apply_profile(self, profile):
        if profile == self.last_profile_applied:
            return
        src = os.path.join(self.profile_dir, profile)
        try:
            shutil.copyfile(src, self.target_file)
            print(f"[PRIMUS] Applied profile: {profile}")
            self.last_profile_applied = profile
        except Exception as e:
            print(f"[ERROR] Could not apply profile {profile}: {e}")

    def display_status(self, speed):
        print(f"Speed: {speed:.2f} MPH | Aggression: {self.aggression_score:.2f} / 10 | Difficulty: {self.difficulty_level} / 20")

    def run(self):
        print("PRIMUS v0.2.7 - Profile Linking Enabled")
        try:
            while True:
                speed = self.read_speed()
                self.update_aggression_score(speed)
                self.update_difficulty()
                profile = self.determine_profile()
                self.apply_profile(profile)
                self.display_status(speed)
                time.sleep(5)
        except KeyboardInterrupt:
            print("Shutting down PRIMUS v0.2.7")

if __name__ == "__main__":
    engine = PrimusEngine()
    engine.run()