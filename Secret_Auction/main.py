import art
print(art.logo)
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
bids = {}
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bidder = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of ${highest_bidder}")


continue_bidding = True
while continue_bidding:
    name = input("What is Your Name? : ")
    price = int(input("What is your Bid? : $"))
    bids[name] = price
    should_continue = input("Is there any other Bidders? Type 'yes' or 'no': \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("\n"*100)


# TODO-4: Compare bids in dictionary


