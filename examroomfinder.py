import streamlit as st
import pandas as pd
st.title("Exam Room Finder")
#loading excel file
import pandas as pd
df = pd.read_excel("excel data.xlsx")
roll_no=st.text_input("Roll Number")
if st.button("Find Room"):
    student=df[df["Roll No"].astype(str).str.upper()
               ==roll_no.upper()]
    if not student.empty:
        st.success("Exam Details Found")
        st.write("Student Details")
        st.write(f"Name :{student.iloc[0]['Student Name']}")
        st.write(f"Roll No :{student.iloc[0]['Roll No']}")
        st.write(f"Exam Date :{student.iloc[0]['Exam Date']}")
        st.write(f"Room No :{student.iloc[0]['Room No']}")
        st.write(f"Building:{student.iloc[0]['Building']}")
    else:
        st.error("Roll no not found")
        
                