import pickle

import streamlit as st
tfidf=pickle.load(open('vectorizer (2).pkl', 'rb'))
model=pickle.load(open('model (2).pkl', 'rb'))




chatwords={
    "AFAIK": "As Far As I Know",
    "ASAP": "As Soon As Possible" ,
    "BRB": "Be Right Back",
    "BTW": "By The Way",
    "DM": "Direct Message",
    "FOMO": "Fear of Missing Out",
    "FYI": "For Your Information",
    "GG": "Good Game",
    "GN":"good night",
    "GR8": "Great",
    "GTG": "Got To Go",
    "HBD": "Happy Birthday",
    "ICYMI": "In Case You Missed It",
    "IDK": "I Don't Know",
    "IMO": "In My Opinion",
    "JK": "Just Kidding",
    "LOL": "Laughing Out Loud",
    "LMK": "Let Me Know",
    "NP": "No Problem",
    "NVM": "Never Mind",
    "OMG": "Oh My God",
    "ROFL": "Rolling On the Floor Laughing",
    "TTYL": "Talk To You Later",
    "TYT": "Take Your Time",
    "WYD": "What You Doing",
    "YOLO": "You Only Live Once",
    "YT": "YouTube",
    "404": "Not Found (Internet Error)",
    "IMHO": "In My Humble Opinion",
    "LMAO": "Laughing My Ass Off",
    "BFF": "Best Friends Forever"
}





from nltk.stem.snowball import SnowballStemmer
snowball_stemmer=SnowballStemmer(language='english')
import nltk
nltk.download('punkt')
import string
punct=string.punctuation
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

def transformation(text):
    text = nltk.word_tokenize(text)

    a=[]
    for i in text:
        if i not in punct:
            a.append(i)
    text = a[:]
    b=[]
    for w in text:
        if w.upper() in chatwords:
            b.append(chatwords[w.upper()])
        else:
            b.append(w)
    text=b[:]
    c=[]
    for i in text:
        if i not in stopwords.words('english'):
            c.append(i)
    text=c[:]
    d=[]
    for w in text:
        d.append(snowball_stemmer.stem(w))
    text=d[:]
    e=[]
    for i in text:
        e.append(i.lower())
    text=e[:]
    return " ".join(e)




st.title("Spam Detection")
input_sms=st.text_input('enter the msg')

if st.button('Predict'):
    transform_sms=transformation(input_sms)

    vector_input=tfidf.transform([transform_sms])

    result=model.predict(vector_input)

    if result!=1:
        st.header('Not Spam')
    else:
        st.header('Spam')


