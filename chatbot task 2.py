faq = {
    "what is ai": "AI means Artificial Intelligence.",
    "what is python": "Python is a programming language.",
    "who are you": "I am a chatbot."
}

question = input("Ask a question: ").lower()

if question in faq:
    print(faq[question])
else:
    print("Sorry, I don't know.")