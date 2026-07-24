import os
print("loaded gamestate")

running = True

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

red_team_dir = ROOT_DIR + "/Red Team"
blue_team_dir = ROOT_DIR + "/Blue Team"



def log(text, team):
    if team == "red":
        path = red_team_dir + "/logs/log.txt"
        with open(path, "a+") as logfile:
            logfile.write(text + "\n")
    if team == "blue":
        path = blue_team_dir + "/logs/log.txt"
        with open(path, "a+") as logfile:
            logfile.write(text + "\n")



print(ROOT_DIR)

