import streamlit as st

st.write("""
# Multiplication of 2 Numbers 

""")
#Get Input


def user_input_features():
    
    val_a = st.number_input("a")
    val_b = st.number_input("b")

    data = {'a':val_a, 'b': val_b}
    return data

df = user_input_features()

if type(df['a']) != float:
    df['a'] = float(df['a'])
if type(df['b']) != float:
    df['b'] = float(df['b'])

st.subheader('Product')
st.write(str(float(df['a'] * df['b'])))

