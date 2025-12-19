def word_count(text):
    text = text or ""
    return len(text.split()) 

def char_count(text):
    char_counts = {}
    text = text.lower()
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def dict_to_list(char_counts):
    count_list = []
    for char, count in char_counts.items():
        count_list.append({"char": char, "num": count})
    return count_list

def sort_by(char_count):
    return char_count["num"]

def sort_counts(count_list):
    count_list.sort(reverse=True, key=sort_by)
    return count_list

def print_list(sorted_list):
    for item in sorted_list:
        char, count = item["char"], item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
