#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"Input\Letters\starting_letter.txt", "r") as old_text: # open starting letter as read mode
    text = ''.join(old_text.readlines()) # converting list into str
with open(r"Input\Names\invited_names.txt", "r") as names: # open name list as read mode
    names_text = names.readlines() # this is already list

for i in range(len(names_text)):
    new_text = text.replace("[name]",names_text[i]) # replace each names with [name] blank
    with open(f"Output/ReadyToSend/letter{i}.txt", mode="w") as file: # creates each letters txt file
        file.write(new_text) # writing new text already replaced

