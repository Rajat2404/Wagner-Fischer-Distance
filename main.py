from Fisher_wanger import load_dictionary, spell_check

if __name__ == "__main__":
    dictionary = load_dictionary("dict.txt")
    word = input("Enter a word to check: ")
    suggestions = spell_check(word, dictionary)
    print(f"\nTop suggestions for '{word}':")
    for w, d in suggestions:
        print(f"{w} (Distance: {d})")
