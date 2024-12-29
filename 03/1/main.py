import re

regex = r"mul\((\d{1,3}),(\d{1,3})\)"

def main():
    with open("../input.txt") as f:
        memory = f.read(-1)
        matches = re.finditer(regex, memory)
        result = 0
        for match in matches:
            num1 = match.group(1)
            num2 = match.group(2)
            print(f"  +{int(num1) * int(num2)}")
            result += int(num1) * int(num2)
        print(f"={result}")
    pass

if __name__ == "__main__":
    main()