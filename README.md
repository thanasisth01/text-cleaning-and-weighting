# 🧹 Text Preprocessing and Feature Extraction in Python

This project implements a **text preprocessing pipeline** for preparing a training dataset of documents for further machine learning or natural language processing tasks.

The core goal is to convert each article or document into a meaningful set of **important words**, based on frequency, significance, or other weighting strategies.

---

## 📚 Project Description

The project takes a set of **training documents** and processes them to extract the most relevant words per document. Each document is then represented as a list of its **top-k weighted terms**.

---

## 🧪 Preprocessing Steps

The preprocessing phase includes the following:

1. **Header Removal**  
   - Strips out metadata or titles that do not contribute to the document’s content.

2. **Punctuation Removal**  
   - Removes punctuation marks and non-alphanumeric symbols.

3. **Stopword Removal**  
   - Removes common function words (e.g., *the*, *is*, *and*) that do not carry semantic meaning.

4. **Optional: Stemming or Lemmatization**  
   - Reduces words to their root forms (e.g., *running* → *run*).

5. **Optional: Lowercasing**  
   - Converts all words to lowercase to avoid duplicates due to case differences.

---

## 📊 Weighting Methods

Each word in a document is assigned a **weight** based on one of the following methods:

- **Term Frequency (TF)** – Counts how many times a word appears in the document.
- **TF-IDF (Term Frequency-Inverse Document Frequency)** – Weighs words based on their importance in the document and rarity across the dataset.
- **Raw Count** – Simple number of occurrences.

---

## 🔍 Feature Selection

After computing weights:

- For each document, the **top-k words** (e.g., top 20) are selected based on their weight.
- These top-k words form the final representation of the document.

---

## 📂 Folder Structure

