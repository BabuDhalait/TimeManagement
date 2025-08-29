# word_character_counter.py
text = input("Enter your text: ")

characters = len(text)
words = len(text.split())
sentences = text.count(".") + text.count("!") + text.count("?")

print("✅ Analysis:")
print(f"Characters (with spaces): {characters}")
print(f"Words: {words}")
print(f"Sentences: {sentences}")
