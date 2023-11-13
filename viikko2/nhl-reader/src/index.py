import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        if player.nationality == "FIN":
            players.append(player)
    # https://www.freecodecamp.org/news/python-sort-how-to-sort-a-list-in-python/
    # Mallista otettu
    players.sort(key=lambda player: player.goals, reverse=True)

    #print("Oliot:")
    print("Players from FIN\n")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
