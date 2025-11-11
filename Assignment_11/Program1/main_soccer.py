from soccer_player import Goalkeeper, Defender, Midfielder, Forward
def main():
    squad = [
        Goalkeeper("Casillas") 
        , Defender("Walker")
        , Defender("Maldini")
        , Defender("Puyol")
        , Defender("Cancelo")
        , Midfielder("Kevin De Bruyne")
        , Midfielder("Rodri")
        , Midfielder("Zidane")
        , Forward("Lionel Messi")
        , Forward("Cristiano Ronaldo")
        , Forward("Neymar Jr")
    ]

    print("My Favorite XI Soccer Team Lineup and Play Styles:\n")

    for player in squad:
        print(player.play_style())
if __name__ == "__main__":
    main()
