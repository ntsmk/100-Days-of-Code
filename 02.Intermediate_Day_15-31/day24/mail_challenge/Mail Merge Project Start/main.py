#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

text_list = []
old_text = open(r"Input\Letters\starting_letter.txt", "r")
text = ''.join(old_text.readlines())
names = open(r"Input\Names\invited_names.txt", "r")
names_text = names.readlines()

for i in range(len(names_text)):
    new_text = text.replace("[name]",names_text[i])
    text_list.append(new_text)

for i in range(len(names_text)):
    with open(f"Output/ReadyToSend/letter{i}.txt", mode="w") as file:
        file.write(text_list[i])

