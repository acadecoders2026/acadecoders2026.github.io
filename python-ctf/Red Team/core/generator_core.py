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
import hashlib

sys.path.append("../..")

import scanner
import gamestate

sys.path.append(gamestate.red_team_dir + "/services/")
sys.path.append(gamestate.red_team_dir + "/modules/")
sys.path.append(gamestate.red_team_dir +"/data/")


TEAM = "red" ## "blue"
team_dir = gamestate.red_team_dir

def init():
    print("start generator program")
    if TEAM == "red":
        print("red team boot sequence start")
        gamestate.log("red team boot sequence start", TEAM)
        sep()

    if TEAM == "blue":
        print("blue team boot sequence start")
        gamestate.log("blue team boot sequence start", TEAM)
        sep()




def loop():
    system_health_check()

    initiate_collection()

    fabricate_token()
    stash_token()


def initiate_collection():
    ### Collect random words to use when generating random keys
    word_bank = os.scandir(team_dir + "/tmp")

def fabricate_token():
    ### Token Phrase Synthesis
    ## Each token is created from a
    pass


def stash_token():
    pass

def sep(x=1):
    gamestate.log("\n"*x, TEAM)
    time.sleep(2)

def system_health_check():
    pcount = 0
    print("health check")
    gamestate.log("Starting system health check", TEAM)
    sep()
    ### check temporary files
    tmp_files = os.scandir(team_dir + "/tmp")
    count = 0
    for file in tmp_files:
        gamestate.log("Searching cache...", TEAM)
        time.sleep(1)
        gamestate.log("Found temporary file " + file.name, TEAM)
        count += 1

    if count > 10:
        gamestate.log("Many temporary files found. Please clear directory /tmp to speed up generator function.", TEAM)
        sep()
    gamestate.log("Completed tmp check.", TEAM)

    sep(2)

    pcount += count

    ### check stash storage
    stash_files = os.scandir(team_dir + "/stash")
    count = 0
    for file in stash_files:
        gamestate.log("Searching tokens stash...", TEAM)

        if not ".token" in file.name:
            gamestate.log(f"Found unknown file {file.name} in stash, deleting...", TEAM)
            time.sleep(8)
            count += 1

        if count:
            gamestate.log("Please remove unknown files from /stash to improve efficiency. /stash should only contain .token files.", TEAM)
            sep()

    gamestate.log("Completed tokens stash check.", TEAM)

    sep(2)

    pcount += count


    ### checking module security
    module_files = os.scandir(team_dir + "/modules")
    count = 0
    for file in module_files:
        gamestate.log("Searching moudle files...", TEAM)

        if ".py" in file.name:
            for i in range(3):
                try:
                    with open(file.path, "r") as mod:
                        code = compile(mod.read(), file.path, 'exec')
                        exec(code)
                        gamestate.log(f"Module {file.name} OK!", TEAM)
                        sep()
                        break
                except Exception as e:
                    gamestate.log(f"WARNING! {file.name} Module failed to execute:\n{e}", TEAM)
                    gamestate.log("Trying again... ", TEAM)
                    sep()
                    time.sleep(4)

                    if i == 1:
                        count += 1




    gamestate.log("Completed module check", TEAM)

    pcount += count


    sep(2)

    gamestate.log(f"Completed system health check, found {pcount} problems", TEAM)

    sep()



print(__name__)
print(gamestate.running)


if __name__ == "__main__":
    init()
    while gamestate.running:
        time.sleep(1)
        loop()
        print("tick")
