---
title: "Vision Aid: Smart Glasses"
excerpt: Assisting visually impaired individuals in real-time navigation through object detection and audio feedback, integrating deep learning models and decision-making algorithms for enhanced mobility and safety.
collection: portfolio
---
<!-- [Link to Github Repo](https://github.com/abuba8) -->

<p> The entire system architecture that consists of three major components: object detection, sound detection and decision making. The outputs of both detection models will be passed on to a decision maker which communications a proper decision to the user via text-to-speech module.
I was responsible of working on computer vision, decision-making and system integration part, so we'll discuss only that part here. </p>
<p>Developed a system integrating computer vision and decision-making components, leveraging technologies such as pre-trained YOLOv5 for object detection to ensure real-time obstacle avoidance and hazard detection. Led the collection and preprocessing of video data from multiple sources, including real-time footage captured via Zed mini cameras, and processed this data for training deep learning models. Contributed to deployment of LLMs and optimized models to run efficiently on NVIDIA Jetson Nano. Achieved significant accuracy in object detection and sound localization tasks, surpassing 85%.</p>
- Tools: Python, PyTorch, YOLOv5, SSD, NVIDIA Jetson Nano, Threading, QR Code Scanner, Ultralytics

<h2>Object Detector</h2>
<h3>Data Description</h3>
<p>Data collection involved two primary sources. The first source entailed video footage
captured by our team members along predefined paths, wherein they wore glasses
equipped with the Zed mini camera to record the video. The second source comprised a
curated dataset obtained from the internet.</p>
<p>
During the preprocessing stage, frames were extracted from the video footage at
a rate of 20 frames per second. Subsequently, the data was cleaned by removing any
blurred images or other unclean data. The annotation process involved manually identifying
objects within each frame, drawing bounding boxes around the objects, and assigning
corresponding labels. Following annotation, data augmentation techniques, including flipping, shearing,
and rotation, were applied using the Roboflow website.
Our final dataset encompassed eight classes: Person, Elevator, Stairs, Door, Garbage Container, Wet Floor Sign, Backpack, and Chair.</p>

<h2>Network Details</h2>
<p>This study uses and compares one-stage detectors like SSD and YOLOv5. The general
architecture works as follows:
Initially, we used an open-source custom dataset for pre-trained CNN models that
will act as a backbone network. Afterwards, we fine-tune the pre-trained weights on our
specific dataset to adapt it to our use cases and object classes.</p>
<p>These detectors are capable of detecting and classifying the required objects in the
predefined routes on campus. They can assist the visually impaired by conveying
information about the following classes: door, Chair, Backpack, Stairs, Elevator, Garbage
Container, Wet Floor Sign, and Person. By using these models, real-time feedback can
be provided to visually impaired individuals, helping them make informed decisions
about their surroundings and navigate across the campus.</p>
<p>In this project, different variants of YOLO and SSD were fine-tuned on a custom
dataset containing five classes. The hyperparameters used for training all the models
include an image size of 400 for YOLO and 512 for SSD, batch size of 4, and 25 training
epochs. The hyperparameters were kept consistent across all the object detectors for comparison purposes of different types of single-shot detectors, ensuring a fair performance
evaluation of each model.</p>

<h2>Decision Maker</h2>
<p>The decision-making module determines the action produced after processing the audio
and video. Therefore, this should occur simultaneously. Decisions include providing
navigation instructions, directing the user to obtain more visual information, instructing
the user how to avoid obstacles, and instructing the user to proceed with caution due to
hazards.</p>
<h3>QR Codes</h3>
<p>To facilitate navigation for visually impaired individuals on our campus, we have
strategically placed multiple QR codes along the predefined paths. These codes provide
visual cues to the user with essential information about their current whereabouts and
assist in deciding their next course of action. Additionally, the QR codes help detect and
identify landmarks along the paths.</p>
<h3>Decision Maker - Finite State Machine</h3>
<p>To give informed decision-making and provide appropriate guidance to visually impaired users, we have proposed a finite state machine which integrates a detailed set
of rules and conditions. The finite state machine will act as a central decision-making
component, taking multiple factors into account, such as object detection, distance estimation, environmental conditions, audio threats.</p>