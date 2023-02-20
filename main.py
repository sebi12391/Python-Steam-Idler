import os
import steam.client

games = [440] #right now only testing Team Fortress 2
username = input("Please Enter your username: ")
password = input("Please Enter your password: ")

os.system("title Python-Steam-Idler")
client = steam.client.SteamClient()
client.cli_login(username, password)
os.system("cls")
print(f"Idling account {username} with games {games}")
client.games_played(games)
client.run_forever()

