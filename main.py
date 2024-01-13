import streamlit as st 
import pandas as pd

with st.echo():
    st.title("Getting Stated Streamlit")
    st.write("test")

    st.markdown("## my markdown")

    code = '''def hello():
        print("Hello, Streamlit!")'''

    run = st.button("show code!")
    if run:
        st.code(code, language='python')

    cols = st.columns(2)
    with cols[0]:
        age = st.number_input("input your age")
        st.markdown(f"Your age is {age}")

    with cols[1]:
        # st.markdown("NLP task")
        text = st.text_input("input y text")
        st.markdown(f"{text}")

    df = pd.DataFrame({
        'first column': [1,2,3,4],
        'second column': [10,20,30,40]
    })

    st.dataframe(df)

    show = st.button("show chart!")
    if show:
        st.line_chart(df, x='first column',y='second column')
