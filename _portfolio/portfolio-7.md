---
title: "Sentiment Analysis of Pakistani Public regarding Covid Vaccines"
excerpt: A data-driven sentiment analysis leveraging fine-tuned BERT to uncover public opinions on COVID-19 vaccines in Pakistan.
collection: portfolio
---

<p>This project focuses on understanding the sentiment of the Pakistani public regarding COVID-19 vaccines. By scraping and labeling over 10,000 tweets with geographic filtering using the Twitter API, a fine-tuned BERT model was employed for multi-class sentiment analysis. The model achieved an impressive F1 score of 95.62%, with the sentiment distribution revealing 42% neutral, 41% positive, and 17% negative sentiments. The insights derived from the analysis can inform policymakers in public health campaigns.</p>
- Tools: Python, TensorFlow, HuggingFace, Sklearn, NLTK, Web Scraping, Seaborn, Plotly
- Github: [Link to Github Repo](https://github.com/abuba8/Sentiment-Analysis-on-Climate-Change-using-Twitter-Feed )

<h2>Data Collection and Preprocessing</h2>
<h3>1. Data Scraping and Labeling</h3> 
<p>Using the Twitter API, tweets were collected with geographic filters targeting the Pakistani public. Over 10,000 tweets were scraped, ensuring coverage of diverse opinions on COVID-19 vaccines. The data was manually labeled into three sentiment categories: positive, neutral, and negative.</p> 

<h3>2. Preprocessing Steps</h3> 
<p>Textual data was cleaned and tokenized using NLTK to remove noise such as stop words, emojis, and special characters. Linguistic patterns and token frequencies were analyzed to prepare the dataset for modeling.</p>

<h2>Model Development and Training</h2>
<h3>1. Fine-Tuning BERT</h3> 
<p>The BERT model was fine-tuned for multi-class sentiment analysis using HuggingFace’s transformers library. Optimized hyperparameters, such as learning rate and batch size, were used to achieve high classification accuracy. The fine-tuned model outperformed baseline models with an F1 score of 95.62%.</p> 
<h3>2. Comparative Analysis of Models</h3> 
<p>Several models were evaluated to benchmark performance: - Simple ANN: 18.5 - LeNet: 15.7 - AlexNet: 33.8 - VGG-16: 34.9 - ResNet-50: 35.1 - Inception: 40.6 - Inception-Residual: 50.87 (best baseline performance).</p>

<h2>Insights and Visualization</h2>
<h3>1. Sentiment Distribution</h3> 
<p>Analysis revealed the following sentiment proportions in the dataset: - Neutral: 42% - Positive: 41% - Negative: 17%</p> 
<h3>2. Visualization</h3> 
<p>Data was visualized using Seaborn and Plotly, providing interactive dashboards for better understanding. Key linguistic insights, such as word clouds and sentiment trends, highlighted areas for potential intervention.</p>