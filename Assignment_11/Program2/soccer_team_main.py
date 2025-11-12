from soccer_team import Goalkeeper, Defender, Midfielder, Forward


def display_menu():
    print("\n--- Soccer Team Menu ---")
    print("1. Add a new Player")
    print("2. View all Players")
    print("3. Show Player Playstyles")
    print("4. Delete a Player")
    print("5. Exit")


def main():
    team = []

    while True:
        display_menu()
        choice = input("Select an option (1-5): ")

        if choice == '1':
            name = input("enter player's name: ")
            print("Select position:")
            print("1. Goalkeeper, 2. Defender, 3. Midfielder, 4. Forward")
            pos_choice = input("Enter position number (1-4): ")

            if pos_choice == '1':
                player = Goalkeeper(name, "Goalkeeper")

            elif pos_choice == '2':
                player = Defender(name, "Defender")

            elif pos_choice == '3':
                player = Midfielder(name, "Midfielder")
            
            elif pos_choice == '4':
                player = Forward(name, "Forward")

            else:
                print("Invalid position choice.")
                continue

            team.append(player)
            print(f"{name} added to the team as a {player.position}.")

        elif choice == '2':
            if not team:
                print("No players in the team.")
            else:
                print("\nTeam Players:")
                for player in team:
                    print(f"- {player.name} ({player.position})")

        elif choice == '3':
            if not team:
                print("No players in the team.")
            else:
                print("\nPlayer Playstyles:")
                for player in team:
                    print(player.playstyle())
        
        elif choice == '4':
            name = input("Enter the name of the player to delete: ")
            for player in team:
                if player.name == name:
                    team.remove(player)
                    print(f"{name} has been removed from the team.")
                    break
            else:
                print(f"No player named {name} found in the team.")
    
        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")
    
if __name__ == "__main__":
    main()