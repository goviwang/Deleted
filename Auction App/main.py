from art import logo
from about import info
from about import pick_greet
from clear import clear
from time import sleep

print(logo, end= "\n")

def find_highest_bid():
    highest_bid= 0
    winner= ""
    for bidder in submitted_bids:
        bid_amount= submitted_bids[bidder] # This is used to collect all the bid amount into an list.
        if bid_amount > highest_bid:
            highest_bid= bid_amount # This is used to find the maximum amount in the list of bids.
            winner= bidder
    print(f"\nThe winner is {winner} with a bid of ${highest_bid}".title())

submitted_bids= {} # For each time the loop run, it will add the a key value pair of 'name' : 'amount'

end_auction = False
while end_auction == False:
    
    name=  input("What Is Your Name: ")
    clear()
    print(logo)
    sleep(.3)
    amount=  int( input(f"\n{pick_greet} {name.title()},\n\nPlease Enter Your Bid Amount In USD $"))  
    clear()
    print(logo)
    submitted_bids[name]= amount # This will all the program to update the dictionary each time the loop runs.


    add_bidders= input( "\nType 'yes' add someone else or Type 'no' show the winner:\n")
    
    if add_bidders.lower() == "no": # This will end the loop and show the highest bid.
        clear()
        print(logo, end= "\n")
        print("PLEASE WAIT . . .")
        sleep(3)
        clear()
        print(logo, end= "\n")
        find_highest_bid()
        sleep(6.9)
        end_auction= True
    elif add_bidders.lower() == "yes": # This will clear the resent terminal log and restart the loop.
        clear()
        print(logo, end= "\n")
    else: # This will provide you with more information on these type of auction.
        clear()
        print(logo)
        sleep(0.9)
        print(info)
        sleep(15)
        clear()
        print(logo, end= "\n")

