import random

print("--- DICE SIMULATOR ---")

num_dice = int(input("Enter number of dice: "))
num_rolls = int(input("Enter number of rolls: "))

if num_dice <= 0 or num_rolls <= 0:
    print("Please enter positive numbers.")
else:
    frequency = {i: 0 for i in range(1, 7)}

    for roll in range(1, num_rolls + 1):
        results = []

        for dice in range(num_dice):
            result = random.randint(1, 6)
            results.append(result)
            frequency[result] += 1

        print("Roll", roll, ":", results)

    print("\n--- FACE FREQUENCY ---")

    for face, count in frequency.items():
        print(face, "appeared", count, "times")

    total = num_dice * num_rolls

    print("\nTotal dice outcomes:", total)

    print("\n--- OBSERVED PROBABILITY ---")

    for face, count in frequency.items():
        probability = count / total
        print(face, ":", round(probability, 3))
