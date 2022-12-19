import pandas as pd
import streamlit as st
import plotly.express as px

from math import floor

st.set_page_config(
    page_title = "Reading Log", 
    page_icon = ":fire:",
    layout="wide")

df = pd.read_csv('log.csv')

source_df = df.groupby(df['Book Source'])['Book Source'].count().reset_index(name="count")
genre_df = df.groupby(df['Genre'])['Genre'].count().reset_index(name="count")
format_df = df.groupby(df['Book Type'])['Book Type'].count().reset_index(name="count")

# Title
st.title(":closed_book: 2022 Reading Log Review")
st.markdown("##")

# BANs
total_books = df["Title"].count()
total_pages = df["Pages"].sum()
avg_rating = round(df["Rating"].mean(),1)
avg_star_rating = ":star:" * int(floor(avg_rating))

left_col, middle_col, right_col = st.columns(3, gap="small")

with left_col:
    st.subheader("# Books :books:")
    st.subheader(total_books)
with middle_col:
    st.subheader("# Pages :page_facing_up:")
    st.subheader(total_pages)
with right_col:
    st.subheader("Average Rating :star:")
    st.subheader(f"{avg_rating} {avg_star_rating}")

st.markdown("---")

# Rating Bar Chart
fig = px.bar(data_frame = df, y = df["Title"], x = df["Rating"], orientation = 'h', hover_data=["Author(s)","Review"])
fig.update_layout(
    hoverlabel=dict(font_size=20, align="left"), 
    font=dict(size=16))
st.plotly_chart(fig, use_container_width= True)

st.markdown("---")

# Donut Charts
fig_l = px.pie(source_df, values="count", names="Book Source", title='Where do I get books?', hole = 0.5)
fig_m = px.pie(genre_df, values="count", names="Genre", title='Fact or Fiction', hole = 0.5)
fig_r = px.pie(format_df, values="count", names="Book Type", title='Physical vs Electronic', hole = 0.5)

col1, col2, col3 = st.columns(3,gap="small")

with col1:
    st.plotly_chart(fig_l, use_container_width=True)
with col2:
    st.plotly_chart(fig_m, use_container_width=True)
with col3:
    st.plotly_chart(fig_r, use_container_width=True)
