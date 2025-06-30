sentence = input('Please input sentence:').strip()

if sentence:
    print(f"So'zlar soni: {len(sentence.split())}")
else:
    print("Siz matn kiritmadingiz.")