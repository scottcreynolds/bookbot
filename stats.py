def read_file(file):
    with open(file) as f:
        return f.read()

def sort_key(dict):
    return dict["count"]

def sort_character_counts(counts):
    sorted = []
    for c in counts:
        if c.isalpha():
            sorted.append({"char": c, "count": counts[c]})
    sorted.sort(key=sort_key, reverse=True)
    return sorted

def get_character_counts(file):
    counts = {}
    text = read_file(file)
    for c in text:
        char = c.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_num_words(file):
    file_contents = read_file(file)
    return len(file_contents.split())

def generate_report(file):
    words = get_num_words(file)
    counts = get_character_counts(file)
    sorted_counts = sort_character_counts(counts)
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {file}\n" 
    report += "----------- Word Count ----------\n"
    report += f"Found {words} total words\n"
    report += "--------- Character Count -------\n"
    for c in sorted_counts:
        report += f"{c['char']}: {c['count']}\n"
    return report