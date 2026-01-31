import streamlit as st
import difflib
import random
import string

st.set_page_config(page_title="Hospital Chatbot", page_icon="🤖")

st.title("🏥 Hospital FAQ Chatbot")
st.write("Ask me questions about hospital services")

# FAQ Data
faqs = {
    "what are hospital timings": "Our hospital is open 24/7.",
    "how can i book an appointment": "You can book an appointment by calling or through our website.",
    "what is the emergency number": "Our emergency number is 123-456-789.",
    "do you have ambulance service": "Yes, we provide 24/7 ambulance service.",
    "what departments do you have": "We have Cardiology, Neurology, Pediatrics, Orthopedics, and General Medicine.",
    "what are visiting hours": "Visiting hours are from 4 PM to 8 PM.",
    "do you accept insurance": "Yes, we accept most major insurance plans.",
    "where is the hospital located": "We are located at Main City Road, near Central Park.",
    "do you have pharmacy": "Yes, our pharmacy is open 24/7.",
    "can i get lab tests here": "Yes, we offer all major laboratory tests.",
    "do you have icu": "Yes, we have a fully equipped ICU.",
    "is parking available": "Yes, free parking is available.",
    "do you have female doctors": "Yes, we have experienced female doctors.",
    "do you provide maternity services": "Yes, we provide full maternity care."
}

thanks_responses = [
    "You're welcome! I'm always here to help 😊",
    "My pleasure! Let me know if you need anything else 💙",
    "Glad I could help! Stay healthy 🌸"
]

greeting_responses = [
    "Hello! Welcome to our hospital support chatbot. How can I assist you today? 😊",
    "Hi there! I'm here to help you with hospital-related queries.",
    "Hey! How can I help you today?"
]

def get_best_match(user_question):
    questions = list(faqs.keys())
    matches = difflib.get_close_matches(user_question, questions, n=1, cutoff=0.4)
    return matches[0] if matches else None

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['text']}")
    else:
        st.markdown(f"**Bot:** {msg['text']}")

user_input = st.chat_input("Type your question...")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})

    user_text = user_input.lower().translate(str.maketrans("", "", string.punctuation))
    greetings = ["hi", "hello", "hey", "hii", "hy"]

    if user_text in greetings:
        response = random.choice(greeting_responses)
    elif user_text in ["thanks", "thank you", "ok thanks", "okay thanks", "thx", "ok"]:
        response = random.choice(thanks_responses)
    else:
        match = get_best_match(user_text)
        if match:
            response = faqs[match]
        else:
            response = "Sorry, I couldn't understand that."

    st.session_state.messages.append({"role": "bot", "text": response})
    st.rerun()


