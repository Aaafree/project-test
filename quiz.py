print("*************")
print("welcome to the quiz game!!!")
print("**************")

questions=("How many elements are in the periodic table?:",
            "What is the tallest mountain in the world?:",
            "Who was the first President of the United States?:",
            "What are the primary colors?:",
            "What does WWW stand for?:",
            "Who was the first man to walk on the moon?:",    
            "What is the world's largest desert?:",
            "What is the longest river in the world?:",
            "How many stars are there on the flag of China?:",
            "What year did women get the right to vote in the United States?:",
            "which annimal lay the largest egg?:",
            "when did resoulation pass?:",
            "what is most abundant gas in Earth 's atmosphere?:",
            "How many bones are in the human body?:",
            "Which planet in the solar is the hottest?:",
            "How many legs does a spider usually have?:",
            "What is the main ingredient in chocolate?:",
            "What is a group of crows called?:",
            "What is the capital city of Italy?:",
            "what year was Facebook founded?:")


options=(("A.116","B.117","C.118","D.119"),
         ("A.K2","B.Mount Everest","c.Mount Kilimanjaro","D.Denali"),
         ("A.Thomas Jefferson","B.Benjamin Franklin","C.Abraham Lincoln","D.George Washington"),
         ("A.Yellow-Blue-Red","B.Yellow-Orang-Green","C.Orange-Purple-Green","D.Blue-Green-Yellow"),
         ("A.World Wide Web","B. World Web Warriors","C. Wide World Web","D.Web Wide World"),
         ("A.John Glenn","B.Yuri Gagarin","C.Buzz Aldrin","D.Neil Armstrong"),
         ("A.Mojave","B.Siberian Desert","C.Sahara","D.Antarctic Desert"),
         ("A.Amazon River","B.Nile River","C.Yangtze River","D.Mississippi River"),
         ("A.1","B.3","C.5","D.7"), 
         ("A.1920","B.1930","C.1940","D. 1950"),
         ("A.whale","B.crocodile","C.elephant","D.ostrich"),
         ("A.1997","B.1192","C.1930","D.1940"),
         ("A.nitrogen","B.oxygen","C.carbondioxide","D.hydrogen"),
         ("A.206","B.204","C.207","D.208"),
         ("A.mercury","B.venus","C.earth","D.mars"),
         ("A.Fourb","B.Six","C.Eight","D.Ten"),
         ("A.Sugar","B.Milk","C.Cocoa Beans","D.Wheat"),
         ("A.pack","B.A flock","C.A murder","D.A caw"),
         ("A.Milan","B.Venice","C.Florence","D.Rome"),
         ("A.2000","B.2004","C.2009","D.2010"))


answers=("C","B","D","A","A","D","D","C","D","B","D","D","A","A","B","C","C","C","D","B",)
guesses=[]
score=0
question_num=0

for question in questions:
    print("_ _ _ _ _ _ _ _ _ _ _")
    print(question)
    for option in options [question_num]:
        print(option)

    guess=input("Enter(A,B,C,D):").upper()
    guesses.append(guess) 
 
    if guess==answers[question_num]:
        score+=1
        print("correct!")
    else:   
        print("incorrect!")
        print(f"{answers[question_num]} is the correct answer") 
       
       
    question_num+=1    


print("_ _ _ _ _ _ _ _ _ _ _")
print("    RESULTS    ")
print("_ _ _ _ _ _ _ _ _ _ _")    

print("answers:",end="")
for answer in answers:
    print(answer,end="")
print()

print("guesses:",end="")
for guess in guesses:
    print(guess,end="")
print()
 

print(f"you have given{score} correct answer")
print(f"yourscoreis{(score/len(questions))*100}%")

#calculate the grades
grade=(score/len(questions))*100
if grade >=90:
    print("Grade:A+")
elif grade >=80:
    print("Grade:A")
elif grade >=70:
    print("Grade:B")
elif grade >=60:
    print("Grade:C")
elif grade >=50:
    print("Grade:D")
else:
    print("sorry you are fail")        