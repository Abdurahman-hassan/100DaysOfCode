from art import logo

isCont = True

bidDict = {}
print(logo + "\n welcome to the secret action program.")


def highestBidder(bidderDict):
    maxBid = 0
    for bider in bidderDict:
        amount = bidderDict[bider]
        if amount > maxBid:
            maxBid = amount
            winner = bider # the key name
    print(f"The winner is {winner} with  {maxBid} bid.")


while isCont:

    name = input("what is your name?:")
    bid = int(input("what is your bid?:"))
    askToContOrstop = input("are they any other bidders yes to cont and no to stop").lower()

    bidDict[name] = bid

    if askToContOrstop == "no":
        isCont = False
        highestBidder(bidDict)
