from libraries.libraries import *
from process.dataGeneration import *
from process.apriori import *
from process.fp import *

def main():
    while True:
        print("\n1. Load SpeedMart_99 data")
        print("2. Run Apriori Algorithm")
        print("3. Run FP Growth Algorithm")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            # Load SpeedMart_99 data
            basketData.generatingData()
        elif choice == '2':
            # Run Apriori Algorithm
            aPriori.algorithm()
        elif choice == '3':
            # Run FP Growth Algorithm
            fP.algorithm()
        elif choice == '4':
            # Exit the program
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()