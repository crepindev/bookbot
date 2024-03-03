def main():
    with open("books/frankenstein.txt") as f:   
        file_contents = f.read()
        
    words = file_contents.split()
    word_count = len(words)
    
    letters = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0
    }
    lowered_file_contents = file_contents.lower()
    letter_dict_list = []
    for c in letters:
        letter_count = lowered_file_contents.count(c)
        letters[c] = letter_count
        letter_dict_list.append({"name" : c, "num" : letter_count})
        lowered_file_contents.replace(c,"") #remove this character from file_contents
        #the above line should make the code faster (???)

    def sort_on(dict):
        return dict["num"]

    letter_dict_list.sort(reverse=True,key=sort_on)
    
    report_letter_str = ""
    for letter_dict in letter_dict_list:
        c = letter_dict["name"]
        n = letter_dict["num"]
        s = f"The '{c}' character was found {n} times\n"
        report_letter_str += s

    report = f"""--- bookbot report on frankenstein.txt ---\n
    {word_count} words were found in the document \n
    \n
    {report_letter_str}
    --- end report ---
    """
    print(report)

main()