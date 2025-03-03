from stats import count_words, count_characters
import sys
def main():
    if len(sys.argv) < 2:        
        print("Useage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============")
        file = sys.argv[1]
        print("Analyzing book found at " + file)
        with open(file) as f:
            file_contents = f.read()
            print("----------- Word Count ----------")
            print("Found " + str(count_words(file_contents)) + " total words")
            print("--------- Character Count -------")
            list_for_report = count_characters(file_contents)
            for c in range(0,len(list_for_report)):
                character = list_for_report[c]["char"]
                if character.isalpha():
                    print(list_for_report[c]["char"] + ": " + str(list_for_report[c]["num"]))
            print("============= END ===============")
main()