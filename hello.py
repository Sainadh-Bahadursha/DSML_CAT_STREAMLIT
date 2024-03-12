import streamlit as st

# To create a header with some heading --> st.header,
# divider parameter creates a dividing line with some colours like 'rainbow'
st.header('This is my first web app!', divider='rainbow')

# to create another header with a word with blue colour and to insert emoji with sunglasses
st.header('_Streamlit_ is :blue[cool] :sunglasses:')

# to insert a code block in python language
code = '''def Cat():
    print("Hello, Cat!")'''
st.code(code, language='python')

# To insert a check box
cat = st.checkbox('I agree with you')

# if anyone checked the box, it is True ---> Great will be printed, st.write is like print
if cat:
    st.write('Great!')