import streamlit as st

# Set up greeting message
st.sidebar.title("Water Conservation Chatbot")
st.sidebar.write("Enter a message to start a conversation with the chatbot")
st.sidebar.title("Menu")
options = [
    "Displaying Text",
    "Data Elements",
    "Media Elements",
    "Interactive Input Elements",
    "Chart Elements",
    "Progress and Status Elements",
    "StreamlitChat",
]
choice = st.sidebar.radio("Select an option", options)
if choice == "Displaying Text":
    # Define variables for water consumption
daily_consumption = 8  # in cups
weekly_consumption = 56  # in cups
monthly_consumption = 240  # in cups

# Define a dictionary to store water consumption by day of the week
weekly_data = {'Monday': 10, 'Tuesday': 8, 'Wednesday': 6, 'Thursday': 7, 'Friday': 5, 'Saturday': 10, 'Sunday': 10}

# Define a list to store monthly water consumption data by day
monthly_data = [8, 10, 12, 9, 6, 8, 11, 10, 8, 10, 12, 9, 6, 8, 11, 10, 8, 10, 12, 9, 6, 8, 11, 10, 8, 10, 12, 9, 6, 8, 11]

# Print the data
print("Daily consumption:", daily_consumption, "cups")
print("Weekly consumption:", weekly_consumption, "cups")
print("Monthly consumption:", monthly_consumption, "cups")
print("Weekly consumption data:", weekly_data)
print("Monthly consumption data:", monthly_data)

# Define conversation logic
def conservation_chatbot(msg):
    # Convert input message to lowercase
    msg = msg.lower()

    # Define conservation-related keywords
    water_keywords = ["water", "conservation", "save", "usage", "waste"]
    plant_keywords = ["plants", "garden", "landscaping", "irrigation"]
    shower_keywords = ["shower", "bath", "faucet"]

    # Check for relevant keywords in message and respond accordingly
    if any(word in msg for word in water_keywords):
        response = "Here are some water conservation tips: \n\n- Fix leaky faucets \n- Take shorter showers \n- Water your lawn in the morning or evening \n- Install a low-flow toilet"
    elif any(word in msg for word in plant_keywords):
        response = "Consider planting drought-resistant plants or installing a drip irrigation system to conserve water in your garden."
    elif any(word in msg for word in shower_keywords):
        response = "Taking shorter showers and turning off the water while you soap up can save a lot of water over time."
    else:
        response = "I'm sorry, I'm not sure how to help with that. Please ask me about water conservation!"

    return response

# Set up conversation interface
user_input = st.text_input("You:", "")
if user_input:
    bot_response = conservation_chatbot(user_input)
    st.text_area("Bot:", bot_response)
