with open("books/frankenstein.txt") as f:
    file_contents = f.read()
#Header Info
    print('--- Begin report of books/frankenstein.txt ---')
#Word Count of Book
    print(len(file_contents.split()),"words found in this document")

#Line Break
    print()
#Empty variables used for following steps
    lower_file_contents = file_contents.lower()
    sorted_alphabet = {}
#dictionary for alphabet
    alphabet: dict[str, int] = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
#split words into list of characters
    for key in lower_file_contents:
        if key in alphabet:
            alphabet[key] += 1

#dictionary to sorted lists
    sorted_list = sorted(alphabet.items(),key=lambda x:x[1],reverse=True)
    sorted_dictionary = dict(sorted_list)

#returns value from letter
    def get_letter(letter):
        for key, value in sorted_dictionary.items():
            if letter == key:
                return value
        
#Format words
    for i in sorted_dictionary:
        print("The",i ,"character was found ",get_letter(i),"times")

#Ender Info
    print("--- End report ---")

    
 