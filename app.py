import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT Plus DALL-E")

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size",["1024x1024","512x512","256x256"])
    submit = st.form_submit_button("Submit")

if submit and user_input:
    command = "Imagine the detail appeareance of the input. Response it shortly around 20 words."
    
    command = command+user_input
    
    with st.spinner("Waiting for ChatGPT"):
        gpt_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=command,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )    
        
        prompt = gpt_response.choices[0].text
        
        st.write(prompt)
    
    with st.spinner("Waiting for ChatGPT"):
        dalle_response =  openai.Image.create(
            prompt = prompt,
            size= size
        )
    
    st.image(dalle_response["data"][0]["url"])