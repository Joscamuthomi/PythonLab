# Interactive quiz generator with garading system

questions= (
    "Which of the following is not an input device?:",
    "What is meant by the term RAM",
    "Which is the largest planet in the solar system",
    "Abreviation of system development lifecyle",
    "Which of the following is not part of software development process",
    )

options= (
    ("A. keyboard", "B. monitor", "C. mouse", "D. stylus pen"),
    ("A. Radom access memory", "B. Radomised sw aplication", "C. read only memory ", "D. read and write to folder"),
    ("A. venus", "B. jupiter", "C. satun", "D. neptune"),
    ("A. SDL", "B. SDC", "C. SDLC", "D. none of the above"),
    ("A. initialitaon", "B. analysis", "C. design", "D. exiperimentation")
    )

answers = ("B", "A", "B", "C", "D")

quiz_number = 0

score = 0



for question in questions:
    print("___________________________________")
    print(question)
    for option in options[quiz_number]:
        print(option)
        
    guess = input("Enter your guess: "). upper()
    if guess == answers[quiz_number]:
        print("correct answer!")
        score += 1
        
    else:
        print(f"Incorrect! {answers[quiz_number]} is the correct answer")  
    quiz_number += 1
        
marks = score/5 * 100 
 
 
if 70 <= marks <= 100:
    grade = "A"
    comment = "Exelent!!"
    
elif 60 <= marks <= 69:
    grade = "B"
    comment = "Good keep it up!"
    
elif 50 <= marks <= 59:
    grade = "C"
    comment = "Fair trial"
    
elif 40 <= marks <= 49:
    grade = "D"
    comment = "poor work"
    
    
else:
    grade = "E"
    comment="Poor work"
     

print(f"your grade is {grade}, {comment}")
