# example of for loop on dictionary 
india = {
    "Sanju Samson": 3,
    "Abhishek Sharma": 69,
    "Ishan Kishan": 37,
    "Shreyas Iyer": 1,
    "Tilak Varma": 28,
    "Naman Dhir": 10,
    "Nitish Kumar Reddy": 21,
    "Axar Patel": 20,
    "Arshdeep Singh": 11,
    "Prince Yadav": 13,
    "Mayank Yadav": 0
}

#findout sum 
sum = 0
for key in india:
    # print(key,end=' ')
    sum = sum + india[key]

print(sum)

#count no of players who score 0 runs 
#count no of players who score >50 runs 
#count no of players who score <10 runs 
