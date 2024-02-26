def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = word_count(file_contents)
        letters = letter_count(file_contents)
        sorted_letter_list = sort_char_list(letters)
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words} words found in the document")
        print()

        for item in sorted_letter_list:
            if item["char"].isalpha():
                print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")

def word_count(string):
    word_list = string.split()
    return len(word_list)


def sort_on(dict):
    return dict["num"]


def sort_char_list(letter_list):
    sorted_list = []
    for letter in letter_list:
        sorted_list.append({"char": letter, "num": letter_list[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def letter_count(string):
    lower_case = string.lower()
    letters_dic = {}
    for char in lower_case:
        if char in letters_dic:
                letters_dic[char] += 1
        else:
            letters_dic[char] = 1
    return letters_dic

main()

