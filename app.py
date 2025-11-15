from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import sqlite3
import google.generativeai as genai



genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('models/gemini-1.5-pro')
    response = model.generate_content(prompt + [question])
    return response.text

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

prompt = [
    "You are an expert AI assistant specializing in converting natural language questions into SQL queries.",
    "The SQL database is named STUDENT and contains the following columns:",
    "**NAME** (VARCHAR), **CLASS** (VARCHAR), **SECTION** (VARCHAR), **MARKS** (INT)",
    "Follow these guidelines when generating SQL queries:",
    "1. Ensure the output contains only the SQL query — do not include explanations, formatting, or markdown.",
    "2. Use proper SQL syntax while maintaining accuracy and efficiency.",
    "3. If the query involves filtering, apply appropriate WHERE clauses.",
    "4. If an aggregation is required (counting records, averaging values), use SQL functions.",
    "#### Examples",
    "*Question*: \"How many student records are present?\"",
    "**SQL Query**: SELECT COUNT(*) FROM STUDENT;",
    "*Question*: \"List all students in the Data Science class.\"",
    "**SQL Query**: SELECT * FROM STUDENT WHERE CLASS = \"Data Science\";"
]

st.set_page_config(page_title="SQL Query Generator | Edureka")
st.markdown("Your AI-Powered SQL generator")
st.markdown("Ask questions here to generate the sql queries")

question = st.text_input("Enter your query in english", key="imput")


submit = st.button("Generate SQL Query")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is") 
    for row in  response:
        print(row)
        st.header(row)

    


