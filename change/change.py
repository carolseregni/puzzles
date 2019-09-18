def find_fewest_coins(coins, target):
    
    numberofcoins=len(coins)
    coins=sorted(coins, reverse=True)
    target_remaining=target
    n=[]
    for i in range(0,numberofcoins, 1):
        n = [n + [target_remaining//coins[i]]]
        target_remaining=target_remaining%coins[i]

    return(n)

print(find_fewest_coins([5, 10, 20, 2], 57))
