def count_vowels(word):
    vowels = "aeiouyAEIOUY"
    return sum(1 for char in word if char in vowels)


file_path = "/Users/haseebtahir/Downloads/lab_data/pg2701.txt"
with open(file_path, "r", encoding="utf-8") as file:
    lines_array = file.readlines()


start_counting = False
vowel_count = 0
word_count = 0

for line in lines_array:
    if "CHAPTER 1. Loomings." in line:
        start_counting = True
        continue

    if start_counting: 
        words = line.split()
        for word in words:
            clean_word = ''.join(filter(str.isalpha, word))  
            if clean_word:
                vowel_count += count_vowels(clean_word)
                word_count += 1

average_vowels = vowel_count / word_count if word_count > 0 else 0
print(f"Average number of vowels per word: {average_vowels:.2f}")
