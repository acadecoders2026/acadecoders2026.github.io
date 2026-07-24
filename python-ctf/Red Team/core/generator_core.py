### GENERATOR CORE
### Core system program. Generates unique tokens and stores them in /stash.
### Win by generating 100 tokens before the other team.
### Tokens cannot be copied, counterfeited or deleted.
### This generator script will always be running, but there may be flaws that
### slow its efficiency or block it's production. Fix them, and you may win
### this war.
import sys
import os
from time import sleep
import time
import hashlib
import random
import uuid

sys.path.append("../..")

import gamestate

sys.path.append(gamestate.red_team_dir + "/services/")
sys.path.append(gamestate.red_team_dir + "/modules/")
sys.path.append(gamestate.red_team_dir +"/data/")

import scanner

def nosleep(x):
    pass

DEBUG = True

if DEBUG:
    sleep = nosleep

TEAM = "red" ## "blue"
team_dir = gamestate.red_team_dir

token_words = []
good_modules = []

flags = []
generated = []

score = 0

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

    token_words = initiate_collection()

    fabricate_token(token_words)


def initiate_collection():
    ### Collect random words to use when generating random tokens
    word_bank = os.scandir(team_dir + "/tmp")

def fabricate_token(words):
    print("fabricate_token")
    ### Token Phrase Synthesis
    ## Each token is created from a collection of 10 words.
    ## These words must be processed by modules in order to be prepared for token generation.
    ## the more modules are functional, the more tokens can be generated.

    flags_file = open(team_dir + "/data/PLACE YOUR FLAGS HERE.txt", 'r')
    flags_file.readline()

    for line in flags_file:
        if not line in flags:
            if len(line):
                flags.append(line)



    hashstr = ""


    new_token = open(team_dir + "/stash/" + str(random.randint(1111,9999)) + ".token", 'a+')

    if len(flags):
        for i in flags:
            if i in generated:
                pass
            else:
                gamestate.log("Generating Point Token", TEAM)
                print("gen")
                sleep(1)
                tohash = i.encode("utf-8")
                new_token.write(hashlib.sha256(tohash).hexdigest())
                generated.append(i)

                sep()
    else:
        gamestate.log("No Flags to generate", TEAM)
        sep()


    stash_files = os.scandir(team_dir + "/stash")
    count = 0
    for file in stash_files:
        if ".token" in file.name:
            count +=1

    score = count

    gamestate.log(f"YOU HAVE SCORED {score} FLAGS.", TEAM)
    time.sleep(5)
    sep()

    new_token.close()


def sep(x=1):
    gamestate.log("\n"*x, TEAM)
    sleep(2)

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
        sleep(1)
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
            sleep(8)
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
                        codetext = mod.read()
                        code = compile(codetext, file.path, 'exec')
                        exec(code)
                        gamestate.log(f"Module {file.name} OK!", TEAM)
                        good_modules.append(globals()[file.name.split('.')[0]])
                        sep()
                        break
                except Exception as e:
                    gamestate.log(f"WARNING! {file.name} Module failed to execute:\n{e}", TEAM)
                    gamestate.log("Trying again... ", TEAM)
                    sep()
                    sleep(4)

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
        sleep(1)
        loop()
        print("tick")
