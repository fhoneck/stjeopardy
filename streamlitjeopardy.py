import pandas as pd
import streamlit as st
import random
#import session_state
from streamlit import caching

try:
    @st.cache(allow_output_mutation=True)
    def get_data():
        return []

    @st.cache(allow_output_mutation=True)
    def right():
        return []

    @st.cache(allow_output_mutation=True)
    def wrong():
        return []

    j = pd.read_table("master_season1-36.tsv")
    r = get_data()

    if st.button("Show Correct Question & New Answer"):
        get_data().append(random.randint(0,len(j)))
    st.markdown("**Answer:**")
    st.title(j.iloc[r[len(r)-1]]["category"] + " | $" + str(j.iloc[r[len(r)-1]]["value"]))
    st.header(j.iloc[r[len(r)-1]]["answer"])
    st.markdown("*Air Date: " + j.iloc[r[len(r)-1]]["air_date"] + "*")
    st.header(" ")
    st.header(" ")
    st.markdown("**Last Answer:**")
    st.write(j.iloc[r[len(r)-2]]["answer"])
    st.success(j.iloc[r[len(r)-2]]["question"])
    if st.button("Got it"):
        right().append(1)
    if st.button("Missed it"):
        wrong().append(1)
    a = len(right())
    b = len(wrong())
    try:
        st.write("Accuracy: " + str(round(a*100/(a+b),1)) + "%   |   " + str(a) + "/ " + str(a+b))
        if st.button("Clear Results (Then Click Refresh)"):
            caching.clear_cache()
    except:
        pass    
except:
    get_data().append(random.randint(0,len(j)))
    st.title(j.iloc[r[len(r)-1]]["category"] + " | $" + str(j.iloc[r[len(r)-1]]["value"]))
    st.header(j.iloc[r[len(r)-1]]["answer"])
    st.markdown("*Air Date: " + j.iloc[r[len(r)-1]]["air_date"] + "*")
    