import streamlit as s
import random
import copy

#  Initialize session state variables
if "score" not in s.session_state:
    s.session_state.score = 0
if "q_no" not in s.session_state:  
    s.session_state.q_no = 0
if "answered" not in s.session_state:
    s.session_state.answered = False
if "balloon_shown" not in s.session_state:
    s.session_state.balloon_shown= False
if "quiz_over" not in s.session_state:
    s.session_state.quiz_over= False


# Titles and subheadings
s.title("⚡ BitQuest ⚡")
s.subheader('Can you get all 5 correct?')
s.markdown("Test your tech knowledge!")

# Quiz Questions 
qns = [
    {
        "question": "Which company developed the Windows operating system?",
        "options": ["Apple", "Microsoft", "IBM"],
        "answer": "Microsoft"
    },
    {
        "question": "Which language is mainly used for building Android apps?",
        "options": ["Java", "C#", "PHP"],
        "answer": "Java"
    },
    {
        "question": "Who is the founder of Linux?",
        "options": ["Linus Torvalds", "Bill Gates", "Ken Thompson"],
        "answer": "Linus Torvalds"
    },
    {
        "question": "Which markup language is used to structure web pages?",
        "options": ["HTML", "Python", "CSS"],
        "answer": "HTML"
    },
    {
        "question": "Which company created the JavaScript language?",
        "options": ["Netscape", "Microsoft", "Sun Microsystems"],
        "answer": "Netscape"
    }
]

#Shuffling questions
if "shuffled_qn" not in s.session_state:
    s.session_state.shuffled_qn= copy.deepcopy(qns)
    random.shuffle(s.session_state.shuffled_qn)
    for q in s.session_state.shuffled_qn:
        random. shuffle(q["options"]) #shuffling options
questions= s.session_state.shuffled_qn #final shuffled list of qns


# At quiz not over condition
if s.session_state.q_no < len(questions): 
    if s.session_state.q_no> 0:
        s.progress((s.session_state.q_no+1)/len(questions)) #progress bar

    q = questions[s.session_state.q_no]
    s.subheader(f"Q{s.session_state.q_no+1}: {q['question']}") #displaying qn
    choice = s.radio("Choose one:", q["options"], disabled= s.session_state.answered)

    if s.session_state.answered== False: #before answering qn
        if s.button("Submit",disabled= s.session_state.answered):
            s.session_state.answered = True #after answering

            #Feedback 
            if choice == q["answer"]:
                s.success(" Correct!")  
                s.session_state.score += 1
            else:
                s.error(f" Wrong! Correct answer: {q['answer']}")

            

    if s.session_state.answered :
        if s.session_state.q_no < len(questions) - 1: #except last qn
            if s.button("Next Question"):
                s.session_state.q_no += 1
                s.session_state.answered = False
                s.rerun()
        else: #for last qn
            if s.session_state.quiz_over==False and s.button('Finish Quiz'):
                s.session_state.quiz_over= True

                s.success(f" Quiz Finished! Your Score: {s.session_state.score}/{len(questions)}")

                if s.session_state.balloon_shown== False: #displaying balloons
                    s.balloons()

            if s.session_state.quiz_over: #if finish button is pressed
                if s.button("Play Again"):
                    s.session_state.q_no = 0 
                    s.session_state.score = 0
                    s.session_state.answered = False
                    s.session_state.quiz_over= False
                    if "shuffled_qn" in s.session_state:
                        del s.session_state['shuffled_qn']
                    s.rerun()