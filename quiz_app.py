# =============================
#   QUIZ APP by Vinitha
# =============================

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["A. Earth", "B. Venus", "C. Mercury", "D. Mars"],
        "answer": "C"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Process Unit", "B. Computer Personal Unit", 
                    "C. Central Processing Unit", "D. Core Processing Unit"],
        "answer": "C"
    },
    {
        "question": "Which language is used for AI/ML?",
        "options": ["A. Java", "B. Python", "C. C++", "D. PHP"],
        "answer": "B"
    },
    {
        "question": "How many bytes are in 1 Kilobyte?",
        "options": ["A. 100", "B. 512", "C. 1024", "D. 2048"],
        "answer": "C"
    }
]

# =============================
#   GAME STARTS HERE
# =============================

print("=" * 40)
print("       WELCOME TO THE QUIZ APP!       ")
print("=" * 40)

name = input("Enter your name: ")
print(f"\nHello {name}! Let's start the quiz.")
print("Choose the correct option (A/B/C/D)\n")

score = 0
total = len(questions)

for i, q in enumerate(questions):
    print(f"Question {i+1}: {q['question']}")
    for option in q['options']:
        print(" ", option)
    
    user_answer = input("Your answer: ").upper().strip()
    
    if user_answer == q['answer']:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer was: {q['answer']}\n")

# =============================
#   FINAL RESULT
# =============================

print("=" * 40)
print(f"Quiz Complete! {name}'s Results:")
print(f"Score: {score} / {total}")

percentage = (score / total) * 100

if percentage == 100:
    print("🏆 Perfect Score! Outstanding!")
elif percentage >= 80:
    print("🥇 Excellent! Great job!")
elif percentage >= 60:
    print("🥈 Good! Keep practicing!")
elif percentage >= 40:
    print("🥉 Not bad! Study more!")
else:
    print("📚 Keep learning! You'll do better!")

print("=" * 40)