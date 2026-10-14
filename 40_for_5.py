# example of for loop on string 
#count words, letters 
line = "the easylearn academy 105, eva surbhi opp waghawadi road, bhavnagar - 36001" #21
word  = 1
count = 0
for letter in line:
    # print(letter)
    if letter == ' ':
        word+=1
    count+=1

print(f"no of words = {word} no of letters = {count}")

#count symbols 
#count digits