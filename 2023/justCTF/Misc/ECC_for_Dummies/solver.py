import random
from sandbox import evaluate
import ast

CARD_COUNT = 5

cards = [bool(random.getrandbits(1)) for _ in range(CARD_COUNT)]
print(cards)
question = "cards"
value = evaluate(cards, question)
print(value)