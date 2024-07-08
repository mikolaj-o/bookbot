
def main(low_case_text):
    character_dict = {}
    for character in low_case_text:
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

z = contents()

y = lower_case_contents(z)

x = main(y)

print(y)
print(x)
