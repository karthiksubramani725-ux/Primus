# Simulated driving behavior tracker
player_speed = 180
offroad_time = 30  # seconds

if offroad_time > 20:
    spawn_police = True
    print("Primus: Dispatching police units due to reckless driving.")
else:
    spawn_police = False