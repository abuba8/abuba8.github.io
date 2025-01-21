---
title: "Classification of Fake Job Description using ResNet and BiLSTM"
excerpt: A hybrid model leveraging ResNet and BiLSTM architectures to detect fraudulent job descriptions with an F1 score of 98.25%.
collection: portfolio
---
<!-- [Link to Github Repo](https://github.com/abuba8) -->

<p>This project aims to address the challenge of detecting fraudulent job descriptions by developing a hybrid model that combines the strengths of ResNet and BiLSTM for feature extraction and classification. Extensive preprocessing and multi-category feature integration contributed to achieving a high classification accuracy of 98.25% F1 score.</p>
- Tools: Python, TensorFlow, Sklearn, NLTK
- Github: [Link to Github Repo](https://github.com/abuba8/classification-fake-job-description)

<h2>Data Collection and Preprocessing</h2>
<h3>1. Data Preparation</h3> 
<p>Textual job description data was collected and extensively preprocessed to remove noise such as redundant characters, stop words, and irrelevant formatting. The dataset included multiple categories of features, including job title, company name, description text, and metadata.</p> 

<h3>2. Feature Engineering</h3> 
<p>Text embeddings were generated using word tokenization and vectorization techniques. Features were enriched with contextual information to enhance model learning. Data cleaning and feature integration ensured robust input representations for model training.</p>

<h2>Model Development and Training</h2>
<h3>1. Hybrid ResNet and BiLSTM Model</h3> 
<p>The hybrid model was designed to extract both spatial and temporal features:</p>

- **ResNet Component:** Extracted hierarchical features from text embeddings using residual blocks, ensuring deep feature representation. 
- **BiLSTM Component:** Captured sequential dependencies and contextual relationships in the text. 

<p>The outputs from ResNet and BiLSTM were concatenated and passed through a dense layer for final classification.</p> 
<h3>2. Training and Optimization</h3> 
<p>The model was trained using TensorFlow with optimized hyperparameters, including learning rate and dropout, to mitigate overfitting. Cross-entropy loss was used to evaluate performance during training.</p>

<h2>Results and Evaluation</h2>
<h3>1. Performance Metrics</h3> 
<p>The hybrid model achieved an impressive F1 score of 98.25% in detecting fraudulent job descriptions, outperforming traditional models and other baselines. Key performance metrics demonstrated the model’s robustness in identifying fraudulent postings accurately.</p> 
<h3>2. Comparative Analysis</h3> 
<p>The hybrid approach was compared to individual ResNet and BiLSTM models, showcasing significant improvements in precision, recall, and F1 scores due to the complementary feature extraction mechanisms.</p>