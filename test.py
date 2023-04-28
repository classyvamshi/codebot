!pip install openai
import streamlit as st
import openai


openai.api_key = "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"
# Define the conversation flow
conversation = {
    "hello": "Hello! I'm a chatbot here to help you learn about water conservation. What would you like to know?",
    "why is water conservation important": "Water conservation is important because it helps to preserve one of our most valuable resources. By using less water, we can ensure that there will be enough to meet the needs of future generations.",
    "how can I conserve water": "There are many ways to conserve water, such as taking shorter showers, fixing leaks, and using water-efficient appliances. Would you like more information on any of these topics?",
    "shorter showers": "Taking shorter showers is a great way to save water. The average shower uses about 2.5 gallons of water per minute, so cutting your shower time by just a few minutes can add up to significant savings over time.",
    "fixing leaks": "Fixing leaks is another important way to conserve water. Even a small leak can waste hundreds of gallons of water over time, so it's important to fix leaks as soon as you notice them.",
    "water-efficient appliances": "Using water-efficient appliances is another great way to conserve water. Look for appliances with the WaterSense label, which means they meet strict water efficiency standards set by the Environmental Protection Agency.",
    "no": "Okay, let me know if you have any other questions!",
    "thanks": "You're welcome! Remember to always be mindful of your water usage and to look for ways to conserve whenever possible."
}

# Define the chatbot function
def chat():
    st.title("Water Conservation Chatbot")
    st.sidebar.title("Menu")
    st.sidebar.write("Type your message in the box below and press enter to send it.")
    message = st.sidebar.text_input("You", "")
user_input = st.text_input("You:", key="input")
    if user_input:
        message(f"You: {user_input}", is_user=True)
        random_number = random.randint(0, 100)
        message(
            f"Bot: Hi there! I think You Lucky Number is {random_number}", is_user=False
        )
