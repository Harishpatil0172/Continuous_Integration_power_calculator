def calculate_powers(number):
    square = number ** 2
    cube = number ** 3
    fifth_power = number ** 5
    return square, cube, fifth_power

if __name__ == "__main__":
    try:
        number = float(input("Enter a number: "))
        square, cube, fifth_power = calculate_powers(number)
        print(f"Square: {square}")
        print(f"Cube: {cube}")
        print(f"Fifth Power: {fifth_power}")
    except ValueError:
        print("Please enter a valid number.")