title = 'Welcome to Rock Paper Scissors'
divider = '--**************--'

print(title.center(80))
print(divider.center(85))
import random

def play_rock_paper_scissors():
    print('Welcome to Rock Paper Scissors')

    while True:
        user = input("Please choose 'r' for rock, 's' for scissors, 'p' for paper: ").lower()
        if user in ['r', 'p', 's']:
            break
        else:
            print('Invalid choice, please try again\n')

    computer = random.choice(['r', 'p', 's'])
    print(f"Computer chose: {computer}")

    if user == computer:
        print('You tied!')
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        print('You won!')
    else:
        print('You lost!')

def main():
    print('Welcome to games! Press 1 to play Rock Paper Scissors\n')

    while True:
        try:
            n = int(input('Answer: '))
            if n != 1:
                print('Wrong Input. Please enter 1 to play Rock Paper Scissors\n')
                continue
            
            while True:
                play_rock_paper_scissors()
                
                request = input('Do you want to play again? (y/n): ').lower()
                if request in ['no', 'n']:
                    break
            break
        except ValueError:
            print('Please enter a valid number\n')
            continue

if __name__ == "__main__":
    main()
