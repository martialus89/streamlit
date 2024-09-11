import streamlit as st
import pandas as pd
from io import StringIO
import numpy as np
import matplotlib.pyplot as plt

uploaded_file = st.file_uploader("Choose a file",type=['csv'] )
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file,sep=';')
    st.write(dataframe)
 

  
    user_selection = st.selectbox('Select une variable',list(dataframe.columns.values))
    st.write(dataframe[user_selection].value_counts())
    

    # Exemple pour la variable 'Ever_Married' (autopct='%1.1f%%')
    plt.figure(figsize=(8, 8))
    st.pyplot(dataframe[user_selection].value_counts().plot.pie(autopct='%1.1f%%',colors=['skyblue', 'lightcoral'], startangle=90))
        # dataframe[user_selection].value_counts().plot.pie(autopct='%1.1f%%',colors=['skyblue', 'lightcoral'], startangle=90, labels=['Homme', 'Femme'])
    # plt.title('Répartition de l\'État Matrimonial')
    # plt.legend()
    # plt.show()

    # st.pyplot(fig1)


# import streamlit as st
# import matplotlib.pyplot as plt
# import numpy as np

# arr = np.random.normal(1, 1, size=100)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)

# st.pyplot(fig)

