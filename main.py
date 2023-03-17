import numpy as np
from PIL import Image
from Algorithms import Algorithms

# A dictionary that maps the user's choice to the name of the algorithm
algorithms_map = {"1": "thresholding", "2": "Error_diffusion_dithering", "3": "Ordered_dithering",
                  "4": "Pattern_dithering", "5": "Exit"}


# The function that shows the menu and returns the user's choice
def show_menu():
    print("Choose the algorithm you want to use:")
    print("1. Thresholding")
    print("2. Error diffusion dithering")
    print("3. Ordered dithering")
    print("4. Pattern dithering")
    print("5. Exit")
    # Get the user's choice
    algo_key = input()
    # Check if the input is valid
    if algo_key.isdigit() and 1 <= int(algo_key) <= 5:
        # Convert the input to an integer and return it
        print("You chose: " + algorithms_map[algo_key])
        return int(algo_key)
    else:
        # If the input is not valid, print an error message and show the menu again
        print("Invalid input. Please enter a number from 1 to 5.")
        return show_menu()


# The main function
def main():
    # Get the path of the image
    img_path = input("Enter the path of the image: ")
    # Create an instance of the Algorithms class
    algo = Algorithms(img_path)
    # Show the menu and get the user's choice
    while True:
        # Get the user's choice
        algo_key = show_menu()
        if algo_key == 5:
            break
        else:
            # Get the name of the algorithm from the map
            algo_name = algorithms_map[str(algo_key)]
            # Call the algorithm
            getattr(algo, algo_name)()
            print("Done and saved.")
            # Ask the user if they want to check another algorithm
            check_again = input("Do you want to check another algorithm? (y/n): ")
            # If the user doesn't want to check another algorithm, break the loop
            if check_again == "n":
                break


# Call the main function
if __name__ == "__main__":
    main()
