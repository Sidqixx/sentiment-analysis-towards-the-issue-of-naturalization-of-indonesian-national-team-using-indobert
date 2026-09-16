# Public Sentiment Analysis of the Naturalization of Indonesian National Team Players on X Using IndoBERT

> **Project ID:** project-06
> **Category:** Natural Language Processing
> **Subcategory:** Sentiment Analysis
> **Project Type:** Individual Project — Undergraduate Thesis
> **Status:** Completed

## 📌 Overview

This project analyzes public sentiment toward the **naturalization of Indonesian National Team players** using Indonesian-language posts collected from **X (formerly Twitter)** between **2021 and 2025**.

The study applies **IndoBERT (`indobert-large-p1`)** for three-class sentiment classification:

* **Negative**
* **Neutral**
* **Positive**

A key focus of this research is the comparison of three different annotation strategies:

1. Manual Labeling
2. Pseudo Labeling
3. Hybrid Manual-Pseudo Labeling

The resulting models are evaluated using Accuracy, Precision, Recall, Macro-F1, and Confusion Matrix analysis.

---

## 🎯 Problem & Objective

The naturalization of football players has generated various discussions among Indonesian social media users, ranging from arguments about strengthening the national team to concerns about the long-term development of Indonesian players.

This project aims to:

* Analyze public sentiment surrounding the naturalization of Indonesian National Team players.
* Develop a sentiment classification model using IndoBERT.
* Compare different annotation strategies for sentiment classification.
* Identify sentiment patterns and discussion themes through N-gram analysis.
* Examine how public sentiment changes across the 2021–2025 observation period.

---

## 📊 Dataset

### Data Source

Posts were collected from **X (Twitter)** using keyword-based searches through **TwitterAPI.io**.

| Attribute          | Details                     |
| ------------------ | --------------------------- |
| Source             | X (Twitter)                 |
| Collection Tool    | TwitterAPI.io               |
| Language           | Indonesian                  |
| Observation Period | 2021–2025                   |
| Initial Collection | 6,800 tweets                |
| Final Dataset      | 2,000 tweets                |
| Target Classes     | Negative, Neutral, Positive |

### Data Filtering

The initial dataset contained a substantial amount of content that was not suitable for sentiment analysis.

Manual filtering was performed to remove:

* Irrelevant posts
* News-related content
* Spam
* Bot-related posts
* Other content outside the research scope

This resulted in a final dataset of **2,000 relevant posts** for subsequent analysis and modeling.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **Hugging Face Transformers**
* **IndoBERT**
* **TwitterAPI.io**
* **Jupyter Notebook**
* **Google Colab**

---

## 🔬 Methodology

The overall research workflow consists of the following stages:

```text
X (Twitter) Data Collection
          ↓
Keyword-Based Search
          ↓
Manual Data Filtering
          ↓
Text Preprocessing
          ↓
Train / Validation / Test Split
          ↓
┌─────────────────────────────────────┐
│        Annotation Strategies        │
│                                     │
│  1. Manual Labeling                 │
│  2. Pseudo Labeling                 │
│  3. Hybrid Manual-Pseudo Labeling   │
└─────────────────────────────────────┘
          ↓
IndoBERT Fine-Tuning
          ↓
Class Imbalance Handling
          ↓
Model Evaluation
          ↓
N-gram Analysis + Sentiment Trends
```

### 1. Data Collection

Tweets were collected using keyword-based searches related to the naturalization of Indonesian National Team players.

### 2. Data Filtering

Collected posts were manually reviewed to remove irrelevant content, including news, spam, bot-related posts, and other posts outside the research scope.

### 3. Text Preprocessing

The remaining Indonesian-language text was prepared for model training through preprocessing steps appropriate for the dataset.

### 4. Data Splitting

The dataset was divided into:

* Training set
* Validation set
* Test set

### 5. Annotation Strategies

Three annotation approaches were investigated.

#### Manual Labeling

Tweets were manually assigned to one of the three sentiment classes:

* Negative
* Neutral
* Positive

#### Pseudo Labeling

A labeling approach was used to generate additional sentiment labels based on model-assisted predictions.

#### Hybrid Manual-Pseudo Labeling

Manual and pseudo-labeled data were combined to construct the training data used for the hybrid experiment.

### 6. IndoBERT Fine-Tuning

The **IndoBERT Large (`indobert-large-p1`)** model was fine-tuned for three-class Indonesian sentiment classification.

### 7. Class Imbalance Handling

Class weights were incorporated during training to reduce the effect of imbalanced sentiment classes.

Additional training techniques included:

* Dropout
* Early stopping

### 8. Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* Macro-F1 Score
* Confusion Matrix

Macro-F1 was particularly considered to evaluate performance across sentiment classes while accounting for differences in class distribution.

### 9. N-gram Analysis

N-gram analysis was performed to identify frequently occurring word combinations associated with different sentiment categories.

### 10. Sentiment Trend Analysis

Sentiment distributions were analyzed across the **2021–2025** observation period to identify changes in public sentiment over time.

---

## 📈 Model Results

The three annotation strategies produced the following results:

| Annotation Strategy  | Accuracy | Macro-F1 |
| -------------------- | -------: | -------: |
| Manual Labeling      |     0.71 |     0.66 |
| Pseudo Labeling      |     0.65 |     0.61 |
| Hybrid Manual-Pseudo | **0.73** | **0.70** |

The Hybrid Manual-Pseudo strategy achieved the highest reported performance among the three approaches, reaching **0.73 Accuracy** and **0.70 Macro-F1**.

### Evaluation Metrics

The evaluation considered multiple classification metrics rather than relying solely on accuracy:

* **Accuracy** — overall proportion of correctly classified posts.
* **Precision** — proportion of predicted instances that were correctly assigned to a class.
* **Recall** — proportion of actual instances correctly identified by the model.
* **Macro-F1** — average F1-score across sentiment classes.
* **Confusion Matrix** — detailed view of classification performance across the three sentiment categories.

---

## 💡 Key Findings

### Sentiment Classification

The experiments showed different performance levels depending on the annotation strategy.

The reported results were:

* Manual Labeling: **0.71 Accuracy / 0.66 Macro-F1**
* Pseudo Labeling: **0.65 Accuracy / 0.61 Macro-F1**
* Hybrid Manual-Pseudo: **0.73 Accuracy / 0.70 Macro-F1**

The Hybrid Manual-Pseudo approach produced the highest performance in this experiment.

### Discussion Themes

N-gram analysis revealed different discussion patterns across sentiment categories.

Negative discussions were associated with concerns regarding **long-term youth development and the potential impact of naturalization on the development of local players**.

Positive discussions included arguments related to **strengthening the Indonesian National Team through the addition of naturalized players**.

### Sentiment Trends

Across the **2021–2025** observation period, negative sentiment represented a substantial portion of the observed discussions and reached its highest level in **2025**.

These trends provide an overview of how sentiment surrounding the naturalization issue varied throughout the observation period.

---
### Demo

No Streamlit, Tableau, or interactive demo was developed for this project.

---

## ⚠️ Limitations

Several limitations should be considered when interpreting the results:

* The final dataset consists of **2,000 posts** after manual filtering.
* Data collection relies on keyword-based searches, which may not capture every relevant discussion.
* Manual filtering and annotation can introduce subjective judgment.
* Pseudo labeling may propagate errors from the labeling process into the training data.
* The analysis represents discussions observed on X and should not be interpreted as a direct representation of the opinion of the entire Indonesian population.
* Sentiment classification does not necessarily capture the full context, sarcasm, or nuanced opinions expressed in social media posts.

---

## 👤 Role

**Team Research Project — Undergraduate Thesis**

Responsibilities included:

* Research design
* Data collection
* Data filtering
* Data preprocessing
* Annotation strategy design
* Model development
* IndoBERT fine-tuning
* Model evaluation
* Sentiment analysis
* N-gram analysis
* Sentiment trend analysis
* Research documentation

---

## 📌 Summary

This project investigates public sentiment toward the naturalization of Indonesian National Team players using Indonesian-language posts from X between **2021 and 2025**.

By comparing **Manual, Pseudo, and Hybrid Manual-Pseudo annotation strategies**, the study evaluates how different approaches affect IndoBERT-based sentiment classification.

The Hybrid Manual-Pseudo approach achieved the highest reported performance in the experiment, with **0.73 Accuracy and 0.70 Macro-F1**.

Beyond classification, N-gram and temporal sentiment analyses were conducted to provide additional insight into the themes and evolution of public discussions surrounding player naturalization.
