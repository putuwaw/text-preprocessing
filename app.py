import streamlit as st
from preprocessing import preprocess

st.header("Text Preprocessing")
st.write('''
            Text preprocessing is the process of transforming text into clean format by 
            converting text to lowercase, removing numbers, removing punctuation, tokenizing, removing stopwords, and stemming.
        ''')

text_area = st.empty()

text = text_area.text_area(
    'Text:', "The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil.",
    help="Write or paste your English text here.")
if (st.button("Clear")):
    text_area.text_area("Text:")

options = st.multiselect(
    'Steps:',
    ['Lowercase', 'Number removal', 'Punctuation removal',
        'Tokenization', 'Stopword removal', 'Stemming'],
    ['Lowercase', 'Number removal', 'Punctuation removal',
        'Tokenization', 'Stopword removal', 'Stemming'],
    help="Steps are applied in the order they are selected."
)

if st.button("Preprocess"):
    st.write("Result:")
    st.code(preprocess(options, text))
