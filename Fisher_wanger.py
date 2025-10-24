# Fisher_wanger.py
def load_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]


def wagner_fischer_table(s1, s2):
    """Returns both the DP table and the edit distance."""
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0] * (len_s1 + 1) for _ in range(len_s2 + 1)]

    for i in range(len_s1 + 1):
        dp[0][i] = i
    for j in range(len_s2 + 1):
        dp[j][0] = j

    for j in range(1, len_s2 + 1):
        for i in range(1, len_s1 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[j][i] = dp[j - 1][i - 1]
            else:
                dp[j][i] = min(
                    dp[j - 1][i] + 1,    # deletion
                    dp[j][i - 1] + 1,    # insertion
                    dp[j - 1][i - 1] + 1 # substitution
                )
    return dp, dp[len_s2][len_s1]


def wagner_fischer(s1, s2):
    """Returns only the distance (fast version)."""
    _, dist = wagner_fischer_table(s1, s2)
    return dist


def spell_check(word, dictionary, top_k=5):
    """Find top k closest words from dictionary."""
    results = [(w, wagner_fischer(word, w)) for w in dictionary]
    results.sort(key=lambda x: x[1])
    return results[:top_k]
