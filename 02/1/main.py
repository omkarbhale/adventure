def safe(levels):
    if len(levels) == 1: return True
    if levels[0] == levels[1]: return False

    increasing = levels[1] > levels[0]
    for i in range(len(levels) - 1):
        if increasing and levels[i] >= levels[i + 1]: return False
        if not increasing and levels[i + 1] >= levels[i]: return False
        if abs(levels[i] - levels[i + 1]) > 3: return False
    return True

def main():
    safe_count = 0
    with open("../input.txt") as f:
        while True:
            levels = list(map(int, f.readline().strip().split()))
            if len(levels) == 0: break

            if safe(levels):
                print('- Safe')
                safe_count += 1
            else:
                print('- Unsafe')

        print(safe_count)

if __name__ == '__main__':
    main()