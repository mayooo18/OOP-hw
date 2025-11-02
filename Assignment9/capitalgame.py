import random
def capital_dict():
    return{
        "Alabame": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "florida": "Tallahassee",
        "Georgia": "Atlanta",
        "illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "new york": "Albany",
        "texas" : "Austin"
    }

def ask_one(state_to_capital):
    state = random.choice(list(state_to_capital.keys()))
    answer = input(f"What is the capital of {state}? ")
    return state, answer

def check_answer(state,answer,state_to_capital):
   if answer == "":
        return "skipped"
   if answer.lower() == state_to_capital[state].lower():
        return "correct"
   
   return "wrong" 


def main():
    states_to_capitals = capital_dict()

    asked = 0
    correct = 0
    wrong = 0
    skipped = 0

    while True: 
        state , answer = ask_one(states_to_capitals)
        

        if answer.lower() == "q":
            print("Goodbye!")
            break

        result = check_answer(state, answer, states_to_capitals)

        if result == "correct":
            print("Correct!")
            correct += 1

        elif result == "wrong":
            print(f"Wrong! The capital of {state} is {states_to_capitals[state]}.")
            wrong += 1

        else:
            print(f"Skipped! The capital of {state} is {states_to_capitals[state]}.")
            skipped += 1
        
        asked += 1
        print("enter q to quit")

    print(f"Total questions answered: {asked}")
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"Skipped: {skipped}")

if __name__ == "__main__":
    main()