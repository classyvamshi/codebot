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
     st.header("Water usage in the world")
    
     st.subheader("Water is essential for life and is a limited resource, with only 2.5% of the world's water being freshwater.
According to the United Nations, 2.2 billion people lack access to safe drinking water and 4.2 billion people lack access to safely managed sanitation services.
Agriculture accounts for the largest share of global water usage, with irrigation accounting for approximately 70% of all freshwater withdrawals.
Industrial water usage accounts for approximately 20% of global freshwater withdrawals.
Domestic water usage accounts for approximately 10% of global freshwater withdrawals.
The world's population is projected to reach 9.7 billion by 2050, which will put further strain on already scarce water resources.
Climate change is exacerbating water scarcity in many regions, with droughts and water stress becoming more common.
The United Nations has declared 2021-2030 as the "Decade of Water Action" in an effort to raise awareness about water scarcity and promote sustainable water management practices.
Approximately one-third of the world's population already lives in water-stressed areas, and this number is expected to increase in the coming decades.
Water scarcity is not just a problem in developing countries; many developed countries also face water scarcity issues, particularly in arid and semi-arid regions.
The world's largest groundwater reserves, such as the Ogallala Aquifer in the United States, are being depleted at an unsustainable rate.
The use of water-efficient technologies, such as drip irrigation and low-flow toilets, can help to reduce water usage in agriculture and households.
Water recycling and reuse can also help to conserve water resources, particularly in industrial and urban settings.
In many regions, the privatization of water resources has led to inequitable distribution and increased water prices for the poor.
Effective water governance and management, including the participation of all stakeholders, is critical to ensuring sustainable and equitable water use for all.")

# Define conversation logic
def conservation_chatbot(msg):
    # Convert input message to lowercase
    msg = msg.lower()

    # Define conservation-related keywords
    water_keywords = ["water", "conservation", "save", "usage", "waste"]
    plant_keywords = ["plants", "garden", "landscaping", "irrigation"]
    shower_keywords = ["shower", "bath", "faucet"]
    percent_keywords = ["percentage"]

    # Check for relevant keywords in message and respond accordingly
    if any(word in msg for word in water_keywords):
        response = "Here are some water conservation tips: \n\n- Fix leaky faucets \n- Take shorter showers \n- Water your lawn in the morning or evening \n- Install a low-flow toilet"
    elif any(word in msg for word in plant_keywords):
        response = "Consider planting drought-resistant plants or installing a drip irrigation system to conserve water in your garden."
    elif any(word in msg for word in shower_keywords):
        response = "Taking shorter showers and turning off the water while you soap up can save a lot of water over time."
    elif any(word in msg for word in percent_keywords):
        response = "The world water percentage is 71%."
    else:
        response = "I'm sorry, I'm not sure how to help with that. Please ask me about water conservation!"

    return response

# Set up conversation interface
user_input = st.text_input("You:", "")
if user_input:
    bot_response = conservation_chatbot(user_input)
    st.text_area("Bot:", bot_response)
