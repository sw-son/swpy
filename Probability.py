import random

def random_kid():
    return random_choice(["boy"],["girl"])
    
both_girls = 0
either_girl = 0
older_girl = 0

random.seed(0)

for _ in range(10000):
    younger = random_kid()
    older = random_kid()
    
    if older == "girl"
        older_girl += 1
    if younger == "girl" and older == "girl" :
        both_girls += 1
    if younger == "girl" or older == "girl" :
        either_girl += 1
       
print "P(both|older):", both_girls / older_girl
print "P(both|either):", both_girls / either_girl
