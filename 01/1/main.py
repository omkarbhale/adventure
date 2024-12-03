import heapq

def main():
    heap1 = []
    heap2 = []

    with open("../input.txt") as f:
        while True:
            line = list(map(int, f.readline().strip().split()))
            if len(line) == 0: break
            heapq.heappush(heap1, line[0])
            heapq.heappush(heap2, line[1])

    distance = 0
    while len(heap1) > 0:
        increment = abs(heapq.heappop(heap1) - heapq.heappop(heap2))
        print(f"  +{increment}")
        distance += increment
    
    print(f"={distance}")
    
if __name__ == '__main__':
    main()