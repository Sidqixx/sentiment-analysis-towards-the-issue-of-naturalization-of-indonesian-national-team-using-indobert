import streamlit as st
import pandas as pd
import os

st.title("Manual Tweet Labeling App")
st.write("Label each tweet as Positive, Neutral, or Negative.")

DATA_PATH = "../splitting/train.csv"  
SAVE_PATH = "train_labeled.csv"  

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
    tweet_text = labeled_df.loc[current_index, "cleaned_text"]

    st.subheader(f"Tweet #{current_index + 1}")
    st.write(tweet_text)

    st.write("### Choose Label:")
    col1, col2, col3 = st.columns(3)

    if col1.button("Positive"):
        labeled_df.loc[current_index, "label"] = "2"
        labeled_df.to_csv(SAVE_PATH, index=False)
        st.rerun()

    if col2.button("Neutral"):
        labeled_df.loc[current_index, "label"] = "1"
        labeled_df.to_csv(SAVE_PATH, index=False)
        st.rerun()

    if col3.button("Negative"):
        labeled_df.loc[current_index, "label"] = "0"
        labeled_df.to_csv(SAVE_PATH, index=False)
        st.rerun()

    progress = (len(labeled_df) - len(unlabeled_rows)) / len(labeled_df)
    st.progress(progress)
    st.write(f"Progress: {round(progress * 100, 2)}%")
