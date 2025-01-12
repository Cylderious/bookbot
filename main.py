def word_count(text):
    wcount = len(text.split())
    return wcount

def count_characters(text):
    char_counts = {}
    for char in text.lower(): 
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def print_counts(word_count, char_count):
    print(f"Word count: {word_count}")
    print(f"Character counts: {char_count}")

def char_counts_report(char_counts):
    sorted_char_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)
    print("\n".join(f"{char} was used {count} times" for char, count in sorted_char_counts))

def main():
    file_path = "books/frankenstein.txt"
    with open(file_path, "r") as f:  
        file_contents = f.read()
    
    wcount = word_count(file_contents)
    counts = count_characters(file_contents)
    
    print_counts(wcount, counts) 
    
    print("\nDetailed Character Count Report:")
    char_counts_report(counts) 
    
if __name__ == "__main__":
    main()