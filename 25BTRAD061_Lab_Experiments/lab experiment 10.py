# Frequency Counter Using Dictionaries

sentence = input("Enter a sentence: ")

words = sentence.lower().split()

frequency = {}

for word in words:
    word = word.strip(".,!?;:\"'()[]{}")

    if word != "":
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

print("\n--- WORD FREQUENCY COUNTER ---")

for word, count in frequency.items():
    print(word, ":", count)

print("\nTotal words:", sum(frequency.values()))
print("Unique words:", len(frequency))
