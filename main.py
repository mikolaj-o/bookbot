
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

# kod pomiedzy komentarzami do skonczenia

def make_dict_list(dict):
      book_dict_list = []
      for record in dict:
            
# kod pomiedzy komentarzami do skonczenia            
      

z = contents()

y = lower_case_contents(z)

char_dict = main(y)

# print(y)
print(char_dict)
