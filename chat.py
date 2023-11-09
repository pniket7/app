import openai
import streamlit as st
from utils import ChatSession

def main():
    st.title('Financial Bank Advisor Chatbot')

    # Load the OpenAI API key from Streamlit secrets
    openai.api_key = st.secrets["api_key"]

    # Initialize the AdvisorGPT. (Move this outside of the button click handler)
    sessionAdvisor = ChatSession(gpt_name='Advisor')

    # Instruct GPT to become a financial advisor.
    sessionAdvisor.inject(
        line="You are a financial advisor at a bank. Start the conversation by inquiring about the user's financial goals. If the user mentions a specific financial goal or issue, acknowledge it and offer to help. Be attentive to the user's needs and goals. ",
        role="user"
    )
    sessionAdvisor.inject(line="Ok.", role="assistant")

    # Create a Streamlit text input for user input with a unique key
    user_input = st.text_input("User:", key="user_input")

    # Create a Streamlit button with a unique key to send a message
    if st.button("Send", key="send_button"):
        # Update the chat session with the user's input
        sessionAdvisor.chat(user_input=user_input, verbose=False)

    # Get the chat history, which includes the chatbot's responses
    chat_history = sessionAdvisor.messages

    # Display the conversation history, including previous questions and answers
    for message in chat_history:
        role = message['role']
        content = message['content']
        st.markdown(f'**{role.capitalize()}:** {content}', unsafe_allow_html=True)

    # Add a "New Chat" button to start a new conversation
    if st.button("New Chat"):
        # Clear the chat history to start a new conversation
        sessionAdvisor.clear()

    # Add an "Exit Chat" button to exit the current conversation
    if st.button("Exit Chat"):
        st.write("You have exited the current conversation.")
        st.stop()  # This stops the Streamlit app

if __name__ == "__main__":
    main()
