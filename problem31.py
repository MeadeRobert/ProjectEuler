coins = [1, 2, 5, 10, 20, 50, 100, 200]
coins = [1, 5, 10, 25]
coins = coins[::-1]
# print(coins)

path = dict(zip(coins, [0 for i in range(0, len(coins))]))
sum = 0
value = 100
# print(value)  
while value - sum > 0:
    for c in coins:
        # print(c, (value - sum) % c)
        if (value - sum) % c == 0 and value - sum > 0:
            path[c] += 1
            sum += c
print(path)
# print(path.keys())

all_paths = []
def coin_paths(value, path):
    num_paths = 0
    for c1 in coins:
        if c1 in path.keys() and path[c1] > 0:
            for c2 in coins:
                if c1 % c2 == 0 and c1 != c2 and c2 in path.keys():
                    # print(c1, c2)
                    new_path = path.copy()
                    new_path[c1] -= 1
                    new_path[c2] += c1 / c2
                    num_paths += 1
                    print(new_path)
                    if new_path not in all_paths:
                        all_paths.append(new_path)
                    num_paths += coin_paths(value, new_path)
                        
        elif c1 in path.keys():
            del path[c1]
    return len(all_paths)
        
print(coin_paths(value, path))
                        

