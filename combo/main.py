# Made by Skj0nes-2
import itertools as it; import re; import os
char = input("Characters: "); digits = int(input("Digit Count: "))
l = [list(char)]; l = [element for element in l for _ in range(int(digits))]; c = list(it.product(*l)); iter = 1
with open('combo.txt', 'w') as file:
    file.write('combinations'.upper())
for item in c:
    combo = re.sub('[' + re.escape("'(), ") + ']', '', str(item))
    combo = f"\n{iter}: {combo}"
    with open('combo.txt', 'a') as file:
        file.write(combo)
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
    except:
        pass
    print(f"Generated Combo {iter}")
    iter = iter + 1
