---
title: "Video Question Answering using Deep Learning"
excerpt: Enabling machines to answer complex questions about videos by integrating temporal reasoning, multimodal fusion, and advanced video-language models for state-of-the-art accuracy.
collection: portfolio
---
<!-- [Link to Github Repo](https://github.com/abuba8) -->

<p>Implemented innovative data preprocessing techniques, such as uniform sampling and optical flow extraction to optimize the extraction of relevant frames, ensuring efficient processing and accurate feature representation. Explored chain-of-thought few shot instruction-tuning methods and fine-tuning of Video Language Models and Large Language Models for VideoQA tasks, achieving 72% accuracy, surpassing state-of-the-art models. Conducted comprehensive evaluations using metrics like cosine similarity, BERT score, and advanced LLM-based similarity evaluation, leading to significant advancements in VideoQA systems.</p>

- Tools: Python, PyTorch, HuggingFace, LlaMa, LLaVa, Clip, Mistral, Clip-VIT, LoRA, QLoRA, Zero-shot, Prompt Engineering

<h2>Approach 1: Proposed Architecture</h2>
<p> A new approach was proposed that contains pre-trained backbones. The system leverages the Mistral-7B language model as a textual encoder and CLIP model for
visual-language understanding. There are two main pre-trained models being used in this approach, the Mistral-7B
language model which is used for natural language understanding and generation, and the
CLIP (Contrastive Language-Image Pretraining) model, specifically vit-base-patch16-224
variant which is used for extracting visual features from video frames. </p>
<p>Mistral-7B model is a large language model specifically designed for tasks involving lan-
guage generation and understanding, with billions of parameters the model has strong ca-
pabilities to reason and generate accurate responses based on input text on open-ended
questions. The model in our approach is leveraged to generate answers based on the combined inputs of visual data and textual data from questions, making it an integral part of the proposed architecture.</p>
<p>The CLIP (Contrastive Language-Image Pretraining) model is designed to bridge the
gap between visual and textual data, the model is pre-trained on a vast amount of image-
text pairs and has shown promising results in understanding and associating images with
its textual descriptions. For our approach, this block plays a vital role in extracting high-
dimensional visual features from video frames.</p>
<p>The first block of the architecture contains an STC Connector, which stands for spatio-
temporal connector and is designed to process the temporal sequences of visual features.
The block contains temporal downsampling via pooling layers, convolutional layers to capture
temporal dependencies in the video frame, and a multi-layer perceptron acting as a projector
for the visual features to convert them into the desired dimensional space.
Then Input combiner block is responsible for the fusion of multi-modal data that combines
visual and textual features into a single feature space, projecting them using linear layers
and concatenating them.</p>
<p>For this approach, the aim is to finetune the pre-trained models and train the STC
and Fusion block. Cross-Entropy loss function and AdamW optimizer are employed with a
learning rate scheduler.</p>

<h2>Approach 2: Modified LLaVA</h2>
<p>Explored the impact of altering a state-of-the-art Video Language Model
(VLM) by replacing its existing language model block with a stronger, more powerful lan-
guage model like LLAMA-3.1 that has a larger vocabulary and embedding size which can
enhance the model’s overall performance in VideoQA tasks.
LLAMA 3.1 theoretically could lead to improved understanding and generation capa-
bilities for our task of complex video-based queries. This alongside, a strong backbone
like LLAVA-Next that is capable of extracting meaningful temporal features from the video
frames, this fusion should be robust for multi-modal tasks.</p>
<p>After integrating the new language model, the vision resampler component critical for
processing video frames was repositioned, which was adjusted and placed in the correct po-
sition of the architecture. This adjustment is necessary to maintain the LLAVA architecture
pipeline, ensuring the visual features are correctly fused with the textual understanding ca-
pabilities of the LLAMA-3.1 model. Moreover, the multi-modal projector that aligns the
visual and language embeddings, is adjusted to the correct dimensions that are capable with
LLAMA-3.1.</p>

<h2>Approach 3: Leveraging the power of LLMs and using Single Modalities for VideoQA</h2>
<p>This approach itself is very unique and represents a novel, innovative method for tackling
VideoQA tasks by primarily leveraging a single modality (textual information) derived from
video content; from this approach, we can realize the capabilities and power of large language
models in understanding and reasoning about visual content through textual descriptions.</p>
<h3>Frame Captioning with LLAVA</h3>
<p>To achieve a good performance, we require captions from video frames which is a crucial
step. To extract captions, a power multimodal model like LLAVA (Large Language and
Vision Assistant) was used that combines the power of LLaMA (text encoder) and CLIP
(vision encoder).
LLAVA was pre-trained on a large dataset for visual description and then further in-
struction tuned. This allows the model to leverage the broad knowledge base of LLaMA,
allowing it to describe objects, actions, and scenes in a way that aligns well with human un-
derstanding. This model excels at understanding visual content and translating it to natural
language descriptions and bridges the gap between visual and textual modalities. Unlike
simpler image captioning models, LLAVA can generate detailed, context-aware descriptions
that capture subtle aspects of the visual scenes.
By extracting frames from each video and generating captions for each, we create a textual
summary of the video’s content. This approach allows us to capture key visual information
across the video’s timeline without the need to process the entire video sequence.</p>
<h3>LLM-based Question Answering</h3>
<p>In this approach, various large language models were used and compared to answer multiple-
choice questions from generated captions along with the question and a carefully crafted negative & few-shot instruction tuning prompts. </p>
<p>Transforming VideoQA into a text-only task by converting visual information to captions
allows us to leverage the full power of the state-of-the-art language models. The use of
carefully crafted prompts and instructions helps guide the LLM in understanding the task
of using frame captions and questions to generate an answer (choose from the given option).
For this approach, powerful state-of-the-art LLMs like Mistral 7B, LLaMA 2, LLaMA 3, and
LLaMA 3.1 were used which allows for a comparative analysis of their performance on this
task.
These large language models have good understanding capabilities but each of them has
its strengths:</p>
- Mistral 7B: Known for its efficiency and strong performance despite its relatively
smaller size.
- LLaMA 2: A significant improvement over the original LLaMA, with enhanced instruction-
following capabilities.
- LLaMA 3 and 3.1: The latest iterations with further improvements in language under-
standing and generation.

<h2>VidInstructQA: Zero-shot Prompt-Based Instruction Tuning</h2>
<p>In this approach, cutting-edge state-of-the-art models were used in a unique way to tackle
a video question-answering system without the need for task-specific training. Leveraged
the power of VLMs, LLMs, and instruction tuning capabilities which was a significant step
towards a more flexible and adaptable AI system capable of handling complex multi-modal
tasks. So, we used the powers of LLAVA-Next to understand and generate an answer for
open-ended questions from video frames which will later be evaluated by a Llama-3 model
if the generated answer is similar to the original one.</p>
<p>Can share more details upon request.</p>