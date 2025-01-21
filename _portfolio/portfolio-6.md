---
title: "Hybrid Residual-Inception based Network for ECG Classification"
excerpt: A novel deep learning architecture leveraging residual and inception modules for robust classification of ECG abnormalities into 27 classes.
collection: portfolio
---
<!-- [Link to Github Repo](https://github.com/abuba8) -->

<p>This project introduces a hybrid residual-inception-based deep learning network to classify ECG signals into 27 abnormality classes using multi-frequency signals (257 Hz to 1 kHz) and demographic features like age and sex. The model demonstrated state-of-the-art performance with a Kaggle competition score of 50.87% and was optimized for heart disease detection using PhysioNet datasets.</p> 
<p>Combining 1D convolutional layers, residual blocks, and inception modules, the architecture extracts high-level and low-level features in parallel, overcoming challenges like vanishing gradients and high variance in ECG data. Optimized data preprocessing and network design enabled effective classification with diverse datasets, showcasing the potential for real-world medical applications.</p>
- Tools: Python, TensorFlow, Seaborn, ECG Plot
- Github: [Link to Github Repo](https://github.com/abuba8/Inception-Residual-Based-Cardiac-Abnormalities-Classification)


<h2>Network Architecture and Methodology</h2>

<h3>1. Feature Extraction</h3> 
<p>The network begins with 1D convolutional layers with 512 filters (5×5 kernel size) and ReLU activation to extract high-level features. Batch normalization layers stabilize training, while a 1D max pooling layer reduces input dimensions while preserving key features.</p> 

<h3>2. Residual Block</h3> 
<p>The residual block uses three stacks of 1D convolutional layers (filters: 128, 128, 256; kernel size: 1×1) followed by batch normalization and leaky ReLU activation (α=0.01). A skip connection with a 1D convolutional layer (256 filters) preserves weights and mitigates the vanishing gradient problem.</p> 

<h3>3. Inception Block</h3> 
<p>The inception module extracts multi-scale features by combining 1D convolutional layers with kernel sizes 1, 3, and 5, each with 64 filters. These parallel layers are followed by batch normalization and leaky ReLU activation, capturing diverse patterns in the ECG data.</p> 

<h3>4. Convolutional Blocks</h3> 
<p>Three additional convolutional blocks enhance feature extraction: - Block 1: 128 filters (5×5 kernel), instance normalization, parametric ReLU, dropout (20%), and 1D max pooling (2×2). - Block 2: 256 filters (11×11 kernel), similar layers as Block 1. - Block 3: 512 filters (21×21 kernel), omitting the max pooling layer to retain spatial information.</p> 

<h3>5. Classification Layer</h3> 
<p>The final layers include 1D max pooling, global average pooling, and flattening. A dense layer connects these features for multi-class classification.</p>

<h2>Results and Performance</h2>
<h3>Evaluation Metrics</h3> 
<p>The hybrid residual-inception network achieved a Kaggle competition score of 50.87%, ranking third in the challenge. Metrics such as precision, recall, and F1 score demonstrated the model’s effectiveness in distinguishing ECG abnormalities across 27 classes.</p> 

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 16px;
    text-align: left;
  }

  table th, table td {
    border: 1px solid #ddd;
    padding: 10px;
  }

  table th {
    background-color: #f4f4f4;
    font-weight: bold;
  }

  table tr:nth-child(even) {
    background-color: #f9f9f9;
  }

  table tr:hover {
    background-color: #f1f1f1;
  }

  .table-container {
    margin-top: 20px;
    font-family: Arial, sans-serif;
  }
</style>

<div class="table-container">
  <table>
    <thead>
      <tr>
        <th>Model</th>
        <th>Test Scores - Kaggle</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Simple ANN</td>
        <td>18.5</td>
      </tr>
      <tr>
        <td>LeNet</td>
        <td>15.7</td>
      </tr>
      <tr>
        <td>AlexNet</td>
        <td>33.8</td>
      </tr>
      <tr>
        <td>VGG-16</td>
        <td>34.9</td>
      </tr>
      <tr>
        <td>ResNet-50</td>
        <td>35.1</td>
      </tr>
      <tr>
        <td>Inception</td>
        <td>40.6</td>
      </tr>
      <tr>
        <td>Inception-Residual</td>
        <td>50.87</td>
      </tr>
    </tbody>
  </table>
</div>
