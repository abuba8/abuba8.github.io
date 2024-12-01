---
title: "Video Question Answering using Deep Learning"
excerpt: "I explored VideoQA systems, investigating the generalization capabilities of LLaVA model using zero-shot instruction tuning. Additionally, used Llama 3 & 3.1 as performance metric to compare the similarity between generated and original sentences."
collection: portfolio
---
<!-- [Link to Github Repo](https://github.com/abuba8) -->

<p> Let's dive deep into the major components of this study, providing a comprehensive 
overview of our approaches explored for the video question-answering task. 
Beginning with a detailed description of the Next-QA dataset used, followed by an
in-depth explanation of the data preprocessing steps that include data reformatting, uniform
and optical flow frame extraction, resizing, and feature extraction using CLIP and LLM tokenized features.</p> 

<h2>Leveraging the power of LLMs and using Single Modalities for VideoQA (Approach A: MCQ)</h2>
<p>The first approach introduces an innovative pipeline that combines frame captioning using LLAVA with LLM-based question answering 
for multiple-choice questions. The frames are extracted and captioned using the LLAVA model and then 
fed into different state-of-the-art LLMs to predict the correct answers for multiple-choice-based questions. </p>

<p>This approach itself is very unique and represents a novel, innovative method for tackling
VideoQA tasks by primarily leveraging a single modality (textual information) derived from
video content; from this approach, we can realize the capabilities and power of large language
models in understanding and reasoning about visual content through textual descriptions.</p>

<p>VideoQA pipeline using frame captioning with LLAVA and LLM-based Question
Answering. Respective captions for video frames are extracted using LLAVA, and then
carefully crafted prompts along with captions are passed to an LLM to generate an output. 
For this approach, powerful state-of-the-art LLMs like Mistral 7B, LLaMA 2, LLaMA 3, and
LLaMA 3.1 were used which allows for a comparative analysis of their performance on this
task</p>

<h2>VidInstructQA</h2>
<p>Secondly, VidInstructQA, a zero-shot prompt-based instruction tuning approach will be explored that
utilizes carefully crafted instruction-based prompts to guide the LLAVA model in generating accurate 
answers for open-ended questions. The generated answers, along with the original answers are then 
evaluated based on BERT similarity score, Cosine similarity, and a strong LLM (LLAMA-3.1) as an evaluator. 
Where, the LLAMA model asses the similarities providing a novel way to gauge the effectiveness of the approach.
