# Wagner-Fischer-Distance

A simple Python spell checker using the **Wagner–Fischer dynamic programming algorithm** to compute the **Levenshtein (edit) distance** between words.  
It suggests the 5 closest matches for a given word and displays the **DP table** for the best match in a clean **Tkinter GUI**.

# What’s Used

Tkinter – GUI interface
Dynamic Programming – Wagner–Fischer algorithm
Dictionary file (dict.txt) – English word list for spell suggestions

# About the Algorithm

The Wagner–Fischer algorithm calculates the minimum number of operations (insertions, deletions, substitutions) to transform one string into another.
Each cell in the DP table represents the edit cost for converting prefixes of two words.
The final cell gives the edit distance — smaller values mean more similar words.

# Example
setlled → settled → distance = 1  
(Delete one extra 'l')

<img width="664" height="718" alt="image" src="https://github.com/user-attachments/assets/f2f1d4a2-434c-41ff-8f6e-312be7588daa" />
