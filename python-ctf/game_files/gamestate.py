print("loaded gamestate")

running = True

red_team_dir = "../Red Team"
blue_team_dir = "../Blue Team"

def log(text, team):
    if team == 'red':
        path = red_team_dir + "/logs/log.txt"
        with open(path, "a") as logfile:
            logfile.write(text + "\n")
    if team == 'blue':
        path = blue_team_dir + "/logs/log.txt"
        with open(path, "a") as logfile:
            logfile.write(text + "\n")
