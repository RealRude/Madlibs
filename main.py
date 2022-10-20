# Madlibs 12 Beginner Python Projects - Coding Course https://www.youtube.com/watch?v=8ext9G7xspg

print("")

#defines nouns
nouns = ("dog", "person", "student", "actress", "country", "politician", "language")

#imports file with a tuple of verbs
exec(open("./verbs.py").read())

#reads an "adjectives" text file into list
with open('adjectives', "r") as f:
    adjectives = f.read().splitlines()

#picks a random element from each
import random
r_noun = random.choice(nouns)
r_verb = random.choice(verbs)
r_adjective = random.choice(adjectives)

#import sys
#sys.exit("Stopped.")
#print(r_noun)
#print(r_verb)
#print(r_adjective)

madlibs = "She showed me how best to " + r_verb + " this absolutely " + r_adjective + " " + r_noun + ". I had the time of my life."
print(madlibs)

endprint = "\n\n>>>|END OF PROGRAM|<<<"
print(endprint)


