from functions import *


words = [
    "merry christmas",
    "happy easter",
    "welcome home",
    "welcome back",
    "happy birthday",
    "congratulations",
    "beth and howard",
    "ross family",
    "its a girl",
    "its a boy",
    "kk and hector",
    "katy and anthony",
    "home sweet home"
]

for word in words:
    createBlocksRec(word, blocks)

print("Adding first batch...")

lettersUsed()

optimize(words)


words2 = [
    "home sweet home",
    "happy fourth",
    "happy new year",
    "a time for thanks",
    "starry nights",
    "happy halloween",
    "arizona",
    "arizona home",
    "st patricks day",
    "st pattys day"
]

print("\nAdding second batch...")

addWords(words2, words)

optimize(words)

print("\nBlocks:")
pprint(blocks)

lettersUsed()

# Uncomment line below to test specific
# words or phrases to see if they can be
# made with the blocks
#userCanWrite()
