def count_words(file_contents):
    num_words = len(file_contents.split())
    return num_words

def count_characters(file_contents):
    char_dict = {}
    file_contests_lowercase = file_contents.lower()

    for char in file_contests_lowercase:
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] = 1
    sorted_list = sort_dict(char_dict)
    return sorted_list

def sort_on(dict):
    return dict["num"]

def sort_dict(dict):
    list_for_report = []
    for char in dict:
        list_for_report.append({"char": char, "num": dict[char]})
    list_for_report.sort(reverse=True, key=sort_on)
    
    return list_for_report
    

    