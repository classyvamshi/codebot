


import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Define function to generate OpenAI response
def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# Define Streamlit app
def main():
    # Set page title and description
    st.set_page_config(page_title="Water Conservation Chatbot", page_icon=":droplet:", layout="wide")
    st.title("Water Conservation Chatbot")
    st.markdown("Ask me questions about water conservation!")

    # Create text input box for user input
    user_input = st.text_input("You:", "")

    # Generate response using OpenAI when user inputs text
    if user_input:
        prompt = f"User: {user_input}\nBot:"
        response = generate_response(prompt)
        st.text_area("Bot:", value=response, height=200)

if _name_ == "_main_":
    main()
