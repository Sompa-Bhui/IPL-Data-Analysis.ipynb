import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("IPL Data Analysis Dashboard")

# Upload file
uploaded_file = st.file_uploader("Upload your IPL dataset (CSV)", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview", df.head())

    # Example: Total matches per team
    team_wins = df['winner'].value_counts()
    st.write("### Total Wins by Team")
    st.bar_chart(team_wins)

    # Example: Toss decision impact
    toss_decision = df['toss_decision'].value_counts()
    st.write("### Toss Decision Count")
    st.bar_chart(toss_decision)

    # Example: Win by runs distribution
    st.write("### Distribution of Win by Runs")
    fig, ax = plt.subplots()
    sns.histplot(df['win_by_runs'], kde=True, ax=ax)
    st.pyplot(fig)
