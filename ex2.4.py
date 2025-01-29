import timeit

def count_vowels(word):
    vowels = "aeiouyAEIOUY"
    return sum(1 for char in word if char in vowels)

def average_vowels_per_word():
    file_path = "/Users/haseebtahir/Downloads/lab_data/pg2701.txt"
    with open(file_path, 'r', encoding="utf-8") as file:
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

    if word_count == 0:
        return 0  

    average_vowels = vowel_count / word_count
    return average_vowels


time_taken = timeit.timeit('average_vowels_per_word()', globals=globals(), number=100)


average_time = time_taken / 100
print(f"Average time to compute the average number of vowels (over 100 runs): {average_time:.6f} seconds")
