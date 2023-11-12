def karp_rabin(pattern, text):
    # Define prime number for hash calculation
    prime = 101

    # Calculate hash for the pattern and the initial window in the text
    pattern_hash = 0
    text_hash = 0
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash * 256 + ord(pattern[i])) % prime
        text_hash = (text_hash * 256 + ord(text[i])) % prime

    # Slide the window through the text and check for matches
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash and pattern == text[i:i+len(pattern)]:
            print("Pattern found at index", i)

        # Update the hash for the next window
        if i < len(text) - len(pattern):
            text_hash = (256 * (text_hash - ord(text[i]) * (256**(len(pattern) - 1))) + ord(text[i + len(pattern)])) % prime
            text_hash = (text_hash + prime) % prime

# Example usage
text = "ABABCABABABCABABCABABABCABABABC"
pattern = "ABABC"
karp_rabin(pattern, text)
