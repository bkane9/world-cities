import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df= pd.read_csv('worldcities.csv')

st.title('Major Cities of the World- Brendan Kane')

pop_filter=st.sidebar.slider('Choose minimum population(in millions)',0,40,15)#min max and default

capital_filter=st.sidebar.multiselect('capital filter',df.capital.unique(),df.capital.unique())#options, default

form=st.sidebar.form('country-form')
country_filter=form.text_input('Enter Country Name','ALL')
form.form_submit_button('Apply')

#population filter
df=df[df.population>pop_filter]

#filter by capital
df=df[df.capital.isin(capital_filter)]

#country filter
if country_filter!='ALL':
    df= df[df.country==country_filter]


st.map(df)

st.write(df[['city','country','population',]])

pop_sum=df.groupby('country').sum()['population']
fig, ax =plt.subplots(figsize=(20,5))
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)