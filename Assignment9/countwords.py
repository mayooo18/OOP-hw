import string   

def fix_word(word):
    return word.strip(string.punctuation).lower()

def count_words(filename):
    wordcount = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                fixed_word = fix_word(word)
                if fixed_word:
                    if fixed_word in wordcount:
                        wordcount[fixed_word] += 1
                    else:
                        wordcount[fixed_word] = 1
    return wordcount

def main():
    print("=== Count Words ===")
    filename = input("Enter the name of the file to read: ")

    try:
        counts = count_words(filename)
    except FileNotFoundError:
        print("File not found. Try again.")
        return

    unique_words = set(counts.keys())

    print(f"\nTotal unique words: {len(unique_words)}")
    print("Sample of words:")
    for word in sorted(list(unique_words))[:20]:
        print(word + ":", counts[word])

if __name__ == "__main__":  
    main()
