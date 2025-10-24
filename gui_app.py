# gui_app.py
import tkinter as tk
from tkinter import ttk, messagebox
from Fisher_wanger import load_dictionary, spell_check, wagner_fischer_table

# Load dictionary once at startup
dictionary = load_dictionary("dict.txt")

def check_word():
    word = entry.get().strip().lower()
    if not word:
        messagebox.showwarning("Input Required", "Please enter a word!")
        return

    results = spell_check(word, dictionary, top_k=5)

    # Clear previous output
    for widget in output_frame.winfo_children():
        widget.destroy()

    # Display top suggestions
    tk.Label(output_frame, text="Top 5 Suggestions:", font=("Arial", 12, "bold")).pack(anchor="w")

    for i, (w, d) in enumerate(results, start=1):
        tk.Label(output_frame, text=f"{i}. {w} (Distance: {d})", font=("Arial", 11)).pack(anchor="w")

    # Show DP table for the top match
    best_word = results[0][0]
    dp, dist = wagner_fischer_table(word, best_word)

    tk.Label(output_frame, text=f"\nDP Table for '{word}' → '{best_word}' (Distance: {dist}):",
             font=("Arial", 12, "bold")).pack(anchor="w")

    table_box = tk.Text(output_frame, width=70, height=15, font=("Consolas", 10))
    table_box.pack()
    table_box.insert("end", format_dp_table(word, best_word, dp))
    table_box.config(state="disabled")

def format_dp_table(s1, s2, dp):
    """Nicely formats DP matrix for display."""
    s1 = " " + s1
    s2 = " " + s2
    header = "    " + "  ".join(s1) + "\n"
    lines = [header]
    for j in range(len(s2)):
        row = [s2[j]] + [str(dp[j][i]) for i in range(len(s1))]
        lines.append("  ".join(row))
    return "\n".join(lines)

# GUI layout
root = tk.Tk()
root.title("Wagner–Fischer Spell Checker")

frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Enter a word:", font=("Arial", 12)).pack(anchor="w")
entry = ttk.Entry(frame, width=40)
entry.pack(anchor="w", pady=5)

ttk.Button(frame, text="Check Spelling", command=check_word).pack(pady=10)

output_frame = ttk.Frame(frame)
output_frame.pack(fill="both", expand=True)

root.mainloop()
