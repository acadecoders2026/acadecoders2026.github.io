### GENERATOR CORE
### Core system program. Generates unique tokens and stores them in /stash.
### Win by generating 100 tokens before the other team.
### Tokens cannot be copied, counterfeited or deleted.
### This generator script will always be running, but there may be flaws that
### slow its efficiency or block it's production. Fix them, and you may win
### this war.
import sys
import os
import time

sys.path.append("../../game_files/")
sys.path.append("../services/")

import scanner
import gamestate

team = None

log_file = ".."

TEAM = "red" ## "blue"
team_dir = ".."

def init():
    print("start generator program")
    if TEAM == "red":
        print("red team boot sequence start")
        gamestate.log("red team boot sequence start", TEAM)
    if TEAM == "blue":
        print("blue team boot sequence start")
        gamestate.log("blue team boot sequence start", TEAM)



def main():
    system_health_check()

def initiate_scan():
    pass

def initiate_collection():
    pass

def fabricate_token():
    pass

def verify_token():
    pass

def stash_token():
    pass

def system_health_check():
    ### check temporary files
    tmp_files = os.scandir(team_dir + "/tmp")
    for file in tmp:
        pass



print(__name__)
print(gamestate.running)


if __name__ == "__main__":
    init()
    while gamestate.running:
        time.sleep(1)
        print("tick")
        main()
