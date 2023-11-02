import streamlit as st
import openai




# Customize the page configuration (including the favicon)
st.set_page_config(
    page_title="Political Bias Detection App",
    page_icon="📜"
)



api_key = st.text_area("Enter an OpenAI API key:", "")

# Set your OpenAI API key
openai.api_key = api_key

# Streamlit app header with a more prominent title and subtitle 
st.title("Political Bias Detection App")
st.subheader("Analyze and Detect Political Bias in Text")

# Input text box for the user with a label
user_input = st.text_area("Enter a text:", "")

# Create a button for users to trigger the analysis
if st.button("Analyze"):
    if user_input:
        # Use GPT-3 to analyze the user input
        prompt = "Is this text '" + user_input + "' politically biased in the context of the Israeli and Palestain conflict and who does it favor? and elaborate on how to get a better well-rounded view of the issue"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Display GPT-3 response in a styled box
        gpt3_response = response.choices[0].message.content
        st.info("Analysis Result:")
        st.write(gpt3_response)
    else:
        st.warning("Please enter some text for analysis.")

# Add a footer with your API key information and a link to OpenAI
st.markdown("---")


