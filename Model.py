import random
def last_hand_out(bag,surplus):
    mean   = surplus/2
    value  = random.uniform(-1/4*mean,2*mean)
    if value < 0:
        value = 0.01
    bag.append(value)
    bag.append(surplus-value)

def hand_out(bag,surplus,n):
    mean   = surplus/(n-len(bag))
    value  = random.uniform(-1/4*mean,9/4*mean)
    if value < 0:
        value = 0.01
    bag.append(value)
    
def weixin_red_envelope(money,n):
    bag    = []
    surplus= money
    while len(bag) < n-2:
        hand_out(bag,surplus,n)
        surplus=surplus-bag[len(bag)-1]
    last_hand_out(bag,surplus)
    print(bag)
