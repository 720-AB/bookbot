def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):

    char_count = {}

    text = text.lower()

    for char in text:

        if char in char_count:

            char_count[char] += 1

        else:

            char_count[char] = 1

    return char_count

def get_sorted_char_list(char_dict):

    char_list = []

    for char, count in char_dict.items():
        char_info = {"char": char, "num": count}
        char_list.append(char_info)



    char_list.sort(key=lambda x: x["num"], reverse=True)


    return char_list




