import random as r

""""""
#*This is a Slot Machine Game developed in Python. The game allows players to deposit money, choose the number of lines to bet on, and place bets. The slot machine generates random symbols, and players can win based on matching symbols across the chosen lines. The game continues until the player decides to stop playing.It was developed as a project to practice Python programming skills, including functions, loops, and user input handling.
"By Nqubeko Shange"
""""""

MAX_LINES:int = 3
MAX_BET:int = 10000

ROWS: int = 3
COLS: int = 3

SYMBOLS_COUNT: dict = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
    "E": 10
}

def check_winnings(columns: list, lines: int, bet: float, values: dict) -> tuple: #this function will handle the checking of winnings based on the slot machine spin
    winnings: float = 0
    winning_lines: list = []
    
    for line in range(lines):
        symbol: str = columns[0][line]
        
        for column in columns:
            symbol_to_check: str = column[line]
            if symbol != symbol_to_check:
                break
            
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    
    return winnings, winning_lines

def get_slot_machine_spin(rows: int, cols: int, symbols: dict) -> list: #this function will handle the generation of the slot machine spin
    all_symbols: list = []
    
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    
    columns: list = []
    
    for _ in range(cols):
        column: list = []
        current_symbols: list = all_symbols[:]
        for _ in range(rows):
            value: str = r.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
            
        columns.append(column)
    
    return columns

def print_slot_machine(columns: list) -> None: #this function will handle the printing of the slot machine
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
                
        print()

def deposit() -> float: #this function will handle the deposit input from the user
    while True:
        try:
            amount: float = float(input("What would you like to deposit?: $")) 
            
            if amount <= 0:
                print("Please enter a positive amount.")
            else:
                return amount
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_number_of_lines(): #this function will handle the number of lines input from the user
    while True:
        try:
            lines: int = int(input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?: "))
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Please enter a number between 1 and " + str(MAX_LINES) + ".")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            
def get_bet(balance: float, lines: int) -> float: #this function will handle the bet input from the user
    while True:
        try:
            bet: float = float(input("What would you like to bet on each line?: $"))
            total_bet: float = bet * lines
            
            if bet <= 0:
                print("Please enter a positive amount.")
            elif total_bet > balance:
                print(f"You do not have enough balance to make that bet. Your current balance is: ${balance:.2f}")
            else:
                return bet
            
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            
def game(balance: float) -> float:
    print(f"\nCurrent balance: ${balance:.2f}")

    lines: int = get_number_of_lines()
    bet: float = get_bet(balance, lines)

    total_bet: float = bet * lines

    slot_machine: list = get_slot_machine_spin(
        ROWS, COLS, SYMBOLS_COUNT
    )

    print("\nSlot Machine:")
    print_slot_machine(slot_machine)

    winnings, winning_lines = check_winnings(
        slot_machine, lines, bet, SYMBOLS_COUNT
    )

    print(f"\nTotal bet: ${total_bet:.2f}")
    print(f"You won ${winnings:.2f}.")

    if winning_lines:
        print(f"Winning lines: {winning_lines}")
    else:
        print("No winning lines this round.")

    return winnings - total_bet

def statistics(balance: float, total_bet: float, total_winnings: float) -> None: #this function will handle the statistics of the game
    print(f"\nGame Statistics:")
    print(f"Total amount bet: ${total_bet:.2f}")
    print(f"Total amount won: ${total_winnings:.2f}")
    print(f"Net gain/loss: ${balance:.2f}")

def main(): #this function will handle the main game loop
    print("Welcome to the Slot Machine!")
    balance: float = deposit()
    while True:
        net_change: float = game(balance)
        balance += net_change
        print(f"Your current balance is: ${balance:.2f}")
        
        if balance <= 0:
            print("You have run out of money. Game over!")
            break
        
        play_again: str = input("Do you want to play again? (y/n): ").lower()
            
        if play_again.lower() == 'y':
            continue
        elif play_again.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
            continue
            
    statistics(balance, total_bet, total_winnings)
    print(f"You left the game with a balance of: ${balance:.2f}")
    print("Thank you for playing!")
    
if __name__ == "__main__":
    main()
    