with open("dorian.txt", "r") as file:
    list = file.read().split("\n")
all_letters = []
all_words = []
letters = {0, 1, 2}
letters.clear()
words = {1, 2}
words.clear()
clean_word = str()
l_dict = {}
wn_dict = {}
wl_dict = {}
for lines in list:
    lines = lines.lower().split()
    for word in lines:
        all_words.append(word)
        for letter in word:
                all_letters.append(letter)
                letters.add(letter)
for i in range(len(all_words)):
    for j in range(len(all_words[i])):
        if ((ord(all_words[i][j]) >= 97 and ord(all_words[i][j]) <= 122) or
                (ord(all_words[i][j]) >= 48 and ord(all_words[i][j]) <= 57) or all_words[i][j] == '-'):
            clean_word += all_words[i][j]
    all_words[i] = clean_word
    clean_word = str()
    words.add(all_words[i])
for i in letters:
    if all_letters.count(i) in l_dict:
        l_dict[all_letters.count(i)] += ("', '"+i)
    else:
        l_dict[all_letters.count(i)] = i
print("Letters statistics:\n\n- 5 most common letters/chars:")
x = 0
for i in reversed(sorted(l_dict)):
    x += 1
    print(f"-char '{l_dict[i]}' founded {i} times")
    if x == 5:
        break
print("\n- 5 least common letters/chars:")
x = 0
for i in sorted(l_dict):
    x += 1
    print(f"- char '{l_dict[i]}' founded {i} times")
    if x == 5:
        break
for i in words:
    if all_words.count(i) in wn_dict:
        wn_dict[all_words.count(i)] += ("', '"+i)
    else:
        wn_dict[all_words.count(i)] = i
    if len(i) in wl_dict:
        wl_dict[len(i)] += ("', '" + i)
    else:
        wl_dict[len(i)] = i
print(f"\nWords statistics:\n\n- number of unique words {len(words)}\n\n- 5 most common words:")
x = 0
for i in reversed(sorted(wn_dict)):
    x += 1
    print(f"- word '{wn_dict[i]}' founded {i} times")
    if x == 5:
        break
print("\n-the longest words:")
x = 0
for i in reversed(sorted(wl_dict)):
    x += 1
    print(f"- words of length '{i}' are {wl_dict[i]}")
    if x == 5:
        break