import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
@st.cache
def load_data():
    # Load your dataset here
    df = pd.read_csv('Electric_Vehicle_Population_Data.csv')
    return df

# Main function to run the app
def main():
    # Set page title
    st.title('Exploratory Data Analysis App')

    # Load the data
    df = load_data()

    # Display the dataset
    st.subheader('Electric Vehicle Dataset')
    st.write(df)

    # Sidebar for feature selection
    st.sidebar.title('Feature Selection')
    selected_features = st.sidebar.multiselect('Select Features', df.columns)

    # Display summary statistics
    if selected_features:
        st.subheader('Summary Statistics')
        st.write(df[selected_features].describe())

    # Display histograms
    if selected_features:
        st.subheader('Histograms')
        for feature in selected_features:
            plt.figure(figsize=(8, 6))
            sns.histplot(data=df, x=feature, kde=True)
            plt.title(f'Histogram of {feature}')
            st.pyplot()

    # Display counts and pie charts for categorical columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        st.subheader(f'Counts of {column}')
        st.write(df[column].value_counts())
        if len(df[column].unique()) <= 10:
            st.subheader(f'Pie Chart of {column}')
            fig, ax = plt.subplots()
            ax.pie(df[column].value_counts(), labels=df[column].value_counts().index, autopct='%1.1f%%')
            st.pyplot(fig)

# Run the app
if __name__ == '__main__':
    main()
