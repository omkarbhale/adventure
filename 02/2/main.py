# returns true if triplet is safe
# second return value is true if they are safe after removing middle value
def triplet_safe(a, b, c, increasing):
    is_safe = None
    if increasing:
        is_safe = c > b and b > a and c - b <= 3 and b - a <= 3
    else:
        is_safe = a > b and b > c and a - b <= 3 and b - c <= 3
    
    if is_safe:
        return is_safe, None
    
    if increasing:
        return is_safe, c > a and c - a <= 3
    else:
        return is_safe, a > c and a - c <= 3
    

def safe(levels, increasing, tolerated=False):
    if levels[2] == 2:
        pass
    if len(levels) == 1: return True
    if levels[0] == levels[1]: return False

    # increasing = levels[1] > levels[0]

    if len(levels) == 3: return triplet_safe(levels[0], levels[1], levels[2], increasing)[0] or triplet_safe(levels[0], levels[1], levels[2], increasing)[1]

    # While loop because standard for-loop doesn't let me increment iterator
    i = -1
    while i + 1 < len(levels) - 2:
        i += 1
        a = levels[i]
        b = levels[i + 1]
        c = levels[i + 2]

        is_safe, is_safe_tolerated = triplet_safe(a, b, c, increasing)
        if is_safe: continue

        if not tolerated and is_safe_tolerated:
            tolerated = True
            i += 1
            continue
        
        return False
    return True

def main():
    safe_count = 0
    with open("../input.txt") as f:
        while True:
            levels = list(map(int, f.readline().strip().split()))
            if len(levels) == 0: break

            if safe(levels, True) or safe(levels[1:], True, tolerated=True) or safe(levels[:-1], True, tolerated=True) or safe(levels, False) or safe(levels[1:], False, tolerated=True) or safe(levels[:-1], False, tolerated=True):
                print('- Safe')
                safe_count += 1
            else:
                print('- Unsafe')

        print(safe_count)

if __name__ == '__main__':
    main()