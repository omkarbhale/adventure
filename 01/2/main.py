def main():
    locations1 = []
    locations2 = []
    freq2 = {} # Frequency of location IDs in second list

    
    with open("../input.txt") as f:
        while True:
            line = list(map(int, f.readline().strip().split()))
            if len(line) == 0: break
            locations1.append(line[0])
            locations2.append(line[1])
    
    for id in locations2:
        freq2[id] = freq2.get(id, 0) + 1

    similarity = 0
    for id in locations1:
        print(f"  +{id * freq2.get(id, 0)}")
        similarity += id * freq2.get(id, 0)    

    print(f"={similarity}")

if __name__ == "__main__":
    main()