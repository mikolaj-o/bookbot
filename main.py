
def main(low_case_text):
    character_dict = {}
    i = 0
    for character in low_case_text:
        

        if character in character_dict and character.isalpha():
            character_dict[character] += 1 
        elif character.isalpha():
            character_dict[character] = 1 
        
    return character_dict
        

def contents():
        with open("books/frankenstein.txt") as f:
            file_contents = f.read()
            return file_contents

def word_count(file_contents):
        words = file_contents.split()
        words_count = len(words)  
        return words_count

def lower_case_contents(file_contents):
        low_case_text = file_contents.lower()
        return low_case_text


def make_dict_list(dict):
      book_dict_list = []
      dict_items = dict.items()
      for record in dict_items:
            a = record[0]
            b = record[1]
            value = {"letter": f"{a}", "num": b}
            book_dict_list.append(value)
      return book_dict_list

def sort_on(dict):
      return dict["num"]

def printer_wiadomosci(words_counter, input_list):
      print(f"--- Begin report of books/frankenstein.txt ---\n{words_counter} words found in the document")
      for input in input_list:
            ch = input["letter"]
            nb = input["num"]
            print(f"The '{ch}' character was found {nb} times")
      print("--- End report ---")


contents_of_the_file = contents()

number_of_words = word_count(contents_of_the_file)

y = lower_case_contents(contents_of_the_file)

char_dict = main(y)

listofdict = make_dict_list(char_dict)

listofdict.sort(reverse=True, key=sort_on)

printer_wiadomosci(number_of_words, listofdict)

