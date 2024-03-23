import random
from collections import defaultdict

tokens = ["I", "try", "to", "learn", "something", "new", "every", "day"]

graph = defaultdict(list)

graph["word"].append("hello")

print(graph["word"])

for i, token in enumerate(tokens):
    print(i, token)

print(random.choice(tokens))
