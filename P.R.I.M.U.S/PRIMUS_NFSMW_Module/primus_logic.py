# primus_logic.py
# Simulated logic for Primus observing reckless driving

# Placeholder values
offroad_time = 12  # seconds
player_speed = 180  # km/h

print("PRIMUS MODULE STARTED")

if offroad_time > 10 and player_speed > 150:
    print("Primus: Reckless driving detected. Increase police presence.")
    with open("primus_action.txt", "w") as f:
        f.write("Action: Increase Heat Level, Add More Cops\n")
else:
    print("Primus: Normal driving. No changes triggered.")
