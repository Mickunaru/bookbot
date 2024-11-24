def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(file_contents)

def count_words(text):
    return len(text.split())

def count_char_in_dict(text):
    dict = {}
    for char in text.lower():
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1
    return dict

def print_report(text):
    word_count = count_words(text)
    dict = count_char_in_dict(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for key, count in dict.items():
        print(f"The '{key}' character was found {count} times")
    print("--- End report ---")
   
main()