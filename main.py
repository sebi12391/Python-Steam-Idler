import os
import sys
import getopt
import steam.client

def login_no_args():
    os.system("title Python-Steam-Idler")
    client = steam.client.SteamClient()
    if client.relogin_available:
        client.relogin()
    else:
        print(f"Please Enter Your Username and Password")
        user = input("Username: ")
        passw = input("Password: ")
        client.cli_login(user, passw)
    os.system("cls")
    print("Successfully Logged In!")
    return client


def login_args(user, passw):
    os.system("title Python-Steam-Idler")
    client = steam.client.SteamClient()
    if client.relogin_available:
        client.relogin()
    else:
        print(f"For Account: {user}")
        client.cli_login(user, passw)
    os.system("cls")
    print("Successfully Logged In!")
    return client


def play_games(client, game_list):
    print(f"Idling account {client.username} with games {game_list}")
    client.games_played(game_list)
    client.run_forever()


username = ""
password = ""
games = []

try:
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "u:p:g:")
except:
    print("Argument setup has failed.")

for opt, arg in opts:
    if opt in ['-u']:
        username = arg
    elif opt in ['-p']:
        password = arg
    elif opt in ['-g']:
        games = arg.replace(" ", "").split(',')


if username == "" and password == "" and games == []:
    print("No Arguments Given, Manual Login Required")
    steam_client = login_no_args()
    print("Please Input the list of games you want to idle, by ID, seperated by commas [E.G. \"440, 654231\"]")
    games = input("Games: ")
    play_games(steam_client, games)

try:
    steam_client = login_args(username, password)
except:
    print("Failure during login process")

play_games(steam_client, games)
