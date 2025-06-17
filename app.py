import streamlit as st
import openai

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="AI Job Interview Assistant")
st.title("🎤 AI Job Interview Assistant")

job_title = st.text_input("Enter the job title you're applying for:")

if st.button("Generate Interview Questions") and job_title:
    with st.spinner("Thinking..."):
        prompt = f"Give me 5 common interview questions for a {job_title} role."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        questions = response.choices[0].message.content
        st.write("### 🔹 Interview Questions:")
        st.markdown(questions)

    if st.button("Suggest Answers"):
        prompt_answers = f"Give sample answers for these 5 interview questions for a {job_title} role."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt_answers}],
            temperature=0.7,
        )
        answers = response.choices[0].message.content
        st.write("### 🧠 Suggested Answers:")
        st.markdown(answers)
