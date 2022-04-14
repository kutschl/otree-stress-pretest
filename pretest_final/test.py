
import random
d = {
     "a": "ACAT",
    "b": "ACTG",
     "c": "ACCC"
 }
print(d)
shuffled = list(d.values())
random.shuffle(shuffled)
a = dict(zip(d, shuffled))
print(a)
