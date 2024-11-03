# use_virtual_pet.py

from src.virtualpet.pet import VirtualPet

def main():
    # Create a new virtual pet instance
    pet_name = input("What would you like to name your pet? ")
    pet = VirtualPet(pet_name)

    # Loop to interact with your pet
    while pet.active:
        action = input(
            "\nWhat would you like to do with your pet? "
            "(Options: feed/play/take shower/check status/sleep/wake up/exit): "
        ).strip().lower()

        if action == "feed":
            pet.feed_pet()
        elif action == "play":
            sub_action = input("Choose how to play with your pet (hug/pet/kiss): ").strip().lower()
            if sub_action in ['hug', 'pet', 'kiss']:
                pet.play_with_pet(sub_action)
            else:
                print("Invalid play action. Please choose hug, pet, or kiss.")
        elif action == "take shower":
            pet.take_shower()
        elif action == "check status":
            pet._display_status()
        elif action == "sleep":
            pet.is_sleeping = True
            print(f"{pet.name} is now sleeping.")
        elif action == "wake up":
            pet.is_sleeping = False
            print(f"{pet.name} is awake now.")
        elif action == "exit":
            pet.exit()
        else:
            print("Invalid action. Please choose a valid action.")

if __name__ == "__main__":
    main()
