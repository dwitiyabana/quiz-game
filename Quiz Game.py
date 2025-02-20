# General Knowledge Quiz Game
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "2. How many continents are there on Earth?",
        "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
        "answer": "C"
    },
    {
        "question": "3. What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "4. Who invented the light bulb?",
        "options": ["A) Albert Einstein", "B) Isaac Newton", "C) Thomas Edison", "D) Nikola Tesla"],
        "answer": "C"
    },
    {
        "question": "5. What is the national animal of India?",
        "options": ["A) Elephant", "B) Lion", "C) Tiger", "D) Peacock"],
        "answer": "C"
    },
    {
        "question": "6. How many sides does a hexagon have?",
        "options": ["A) 4", "B) 5", "C) 6", "D) 8"],
        "answer": "C"
    },
    {
        "question": "7. What is the currency of Japan?",
        "options": ["A) Yen", "B) Won", "C) Ringgit", "D) Dollar"],
        "answer": "A"
    },
    {
        "question": "8. Which planet is known as the 'Red Planet'?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "9. Who wrote the national anthem of India?",
        "options": ["A) Rabindranath Tagore", "B) Mahatma Gandhi", "C) Subhash Chandra Bose", "D) Sarojini Naidu"],
        "answer": "A"
    },
    {
        "question": "10. What is the longest river in the world?",
        "options": ["A) Amazon River", "B) Nile River", "C) Ganges River", "D) Yangtze River"],
        "answer": "B"
    },
    {
        "question": "11. How many players are there in a cricket team?",
        "options": ["A) 9", "B) 10", "C) 11", "D) 12"],
        "answer": "C"
    },
    {
        "question": "12. What is the smallest prime number?",
        "options": ["A) 0", "B) 1", "C) 2", "D) 3"],
        "answer": "C"
    },
    {
        "question": "13. Which gas do plants absorb from the air?",
        "options": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
        "answer": "C"
    },
    {
        "question": "14. What is the hardest natural substance on Earth?",
        "options": ["A) Gold", "B) Diamond", "C) Iron", "D) Platinum"],
        "answer": "B"
    }
]
# Initialize score
score = 0

# Loop through each question
for q in questions:
    print("\n" + q["question"])  # Display question
    for option in q["options"]:
        print(option)  # Display answer choices

    # Get user input
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    # Check if the answer is correct
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1  # Increase score
    else:
        print(f"❌ Wrong! The correct answer is {q['answer']}")

# Show final score
print(f"\n🎉 You got {score} out of {len(questions)} correct!")