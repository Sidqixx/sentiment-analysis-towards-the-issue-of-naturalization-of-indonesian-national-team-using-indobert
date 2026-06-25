import streamlit as st
import pandas as pd
import os

st.title("Manual Tweet Labeling App")
st.write("Label each tweet as Positive, Neutral, or Negative.")

DATA_PATH = "../filter_raw/filter_opinion.csv"  
SAVE_PATH = "hasil_manual.csv"  

# ====== Load Data ======
df = pd.read_csv(DATA_PATH)

# ====== Load or create labeled file ======
if os.path.exists(SAVE_PATH) and os.path.getsize(SAVE_PATH) > 0:
    labeled_df = pd.read_csv(SAVE_PATH)
else:
    labeled_df = df.copy()
    labeled_df["label"] = None

# ====== Find Next Unlabeled Row ======
unlabeled_rows = labeled_df[labeled_df["label"].isna()]

if len(unlabeled_rows) == 0:
    st.success("All tweets have been labeled! 🎉")
    st.dataframe(labeled_df)
else:
    current_index = unlabeled_rows.index[0]
    tweet_text = labeled_df.loc[current_index, "clean_text"]

    st.subheader(f"Tweet #{current_index + 1}")
    st.write(tweet_text)

    st.write("### Choose Label:")
    col1, col2 = st.columns(2)

    if col1.button("Op"):
        labeled_df.loc[current_index, "label"] = "Op"
        labeled_df.to_csv(SAVE_PATH, index=False)
        st.rerun()

    if col2.button("Inf"):
        labeled_df.loc[current_index, "label"] = "Inf"
        labeled_df.to_csv(SAVE_PATH, index=False)
        st.rerun()

    progress = (len(labeled_df) - len(unlabeled_rows)) / len(labeled_df)
    st.progress(progress)
    st.write(f"Progress: {round(progress * 100, 2)}%")
