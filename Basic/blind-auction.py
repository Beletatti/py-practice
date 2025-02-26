import os

def clear_screen():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bid():
    name = input("Qual é o seu nome? ")
    while True:
        try:
            bid = float(input("Qual é o seu lance? R$"))
            break
        except ValueError:
            print("Por favor, insira um valor numérico válido.")
    return name, bid

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    return winner, highest_bid

def main():
    bids = {}
    bidding_finished = False

    while not bidding_finished:
        name, bid = get_bid()
        bids[name] = bid
        clear_screen()
        while True:
            should_continue = input("Há mais alguém que deseja dar um lance? Digite 'sim' ou 'não': ").lower()
            if should_continue in ['sim', 'não']:
                break
            else:
                print("Por favor, digite 'sim' ou 'não'.")
        if should_continue == 'não':
            bidding_finished = True

    winner, highest_bid = find_highest_bidder(bids)
    print(f"O vencedor é {winner} com um lance de R${highest_bid:.2f}")

if __name__ == "__main__":
    main()