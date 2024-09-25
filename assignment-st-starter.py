# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8')

# show the title
st.title("Titanic App by Jiao Ma")

# read csv and show the dataframe
train = pd.read_csv("train.csv")
st.dataframe(train)

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

classes = [1, 2, 3]
for i, pclass in enumerate(classes):
    class_data = train[train['Pclass'] == pclass]['Fare']
    axes[i].boxplot(class_data, vert=True)
    
    axes[i].set_title(f'PClass = {pclass}', loc='center', y=-0.2, pad=20)
    axes[i].set_xticks([1])
    axes[i].set_xticklabels(['Fare'])
    
    if i == 0:
        axes[i].set_ylabel('Fare')

st.pyplot(fig)
