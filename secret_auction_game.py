import time

def countdown(t):
     print("The dors are closed. The auction will began in 30 seconds...")
     while t:
         mins, secs = divmod(t, 60)
         timeformat = '{:02d}:{:02d}'.format(mins, secs)
         print(timeformat, end="\n")
         time.sleep(1)
         t -= 1

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

if __name__ == '__main__':
    countdown(5)
    bids = {}
    bidding_finished = False
    while not bidding_finished:
        name = input("What is your name?: ")
        price = int(input("What is your bid?: $"))
        bids[name] = price
        should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
        if should_continue == "no":
            bidding_finished = True
            find_highest_bidder(bids)
