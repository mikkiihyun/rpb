def main():
    print("Let's implement division. Type two numbers for x and y.")

    x = int(input("x > "))
    y = int(input("y > "))

    result = divide(x, y)
    if result is not None:
        print(f"{x} / {y} = {result}")
def add(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        print("Error: cannot divide by zero.")
        return None
    return x / y

if __name__ == "__main__":
    main()