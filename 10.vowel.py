def vowels(text):
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count
input = "Hello World  Shajeena"
print("Number of vowels:", vowels(input))
