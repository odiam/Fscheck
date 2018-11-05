# This script provides a random directory tree
#
# Usage: python random_tree_dir.py


import random
import os

def ranstring():
    import random
    r = random.randint(50, 999)
    res = ""
    for x in range(r):
        res += chr(random.randint(1, 26) + 96)
    return res


for x in range(0, random.randint(10, 30)):
    os.makedirs("dir"+str(x))

for x in os.listdir():
    if x == "random_tree_dir.py": continue
    for y in range(0, random.randint(10, 100)):
        with open(os.getcwd()+"/"+x+"/"+"f"+str(y), "w") as f:
            f.write( ranstring() )
