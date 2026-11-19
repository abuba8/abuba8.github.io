from flask import Flask, render_template, request, jsonify, abort

app = Flask(__name__)

# Newest first. "link" is optional.
NEWS = [
    {
        "date": "Sep 2026",
        "text": "Paper \u201cYour Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric\u201d accepted at BlackboxNLP 2026 @ EMNLP 2026 (Budapest).",
        "link": "https://aclanthology.org/2026.blackboxnlp-1.40.pdf",
    },
    {
        "date": "Jun 2026",
        "text": "Paper \u201cSafety-Prioritised Multimodal Navigation for Edge Smart Glasses with Constrained On-Device Language Models\u201d presented at the 11th International Digital Public Health Conference (DPH 2026, Barcelona).",
        "link": "https://ieeexplore.ieee.org/document/11650519",
    },
    {
        "date": "Apr 2026",
        "text": "Joined EY as a Software Engineer.",
    },
    {
        "date": "Apr 2026",
        "text": "Admitted to the Ph.D. in Computer Science at Arizona State University and the M.S. in Computer Science at Georgia Tech.",
    },
]

PUBLICATIONS = [
    {
        "slug": "in-context-label-bias",
        "title": "Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric",
        "venue": "Empirical Methods in Natural Language Processing (EMNLP), 9th BlackBoxNLP Workshop",
        "authors": "Abdullah Ahmad, Ahmed J.O. Ahmed, Luca Citi",
        "year": "2026",
        "abstract": """
        LLM-as-judge has become a standard way to
        score open-ended model outputs, yet the judge
        is itself a frozen language model steered by
        a few in-context examples, and such models
        are known to absorb the label balance of their
        demonstrations rather than treat them as neutral illustrations. We ask whether this label
        bias reaches an LLM judge used inside a multimodal (video question answering) evaluation
        pipeline, and what form it takes. Using a
        fully frozen generator–judge pipeline, we hold
        the generated answers fixed and vary only the
        Yes/No balance of the judge’s few-shot exam-
        ples across four demonstration sets, validating
        each verdict against a two-annotator human
        consensus on 200 examples per dataset. The
        judge’s acceptance rate stays close to human
        consensus when its examples are balanced or
        skewed toward rejection, but jumps sharply—
        by about 30 points on NExT-QA and 20 on
        MSVD-QA, with a strongly one-sided error
        profile—when the examples are skewed to-
        ward acceptance; the opposite skew produces
        no matching drop. The bias is therefore one-
        directional. A separate five-draw analysis
        shows that results from a single example draw
        are unreliable, varying by up to 18 points—
        more than any difference between prompting
        conditions. We conclude that demonstration
        label bias in an LLM judge is a directional,
        inflation-only failure mode that can fabricate
        apparent benchmark gains but not losses, and
        that it is cheaply avoided by balancing the
        judge’s examples and reporting results averaged over several draws.
        """,
        "link": "https://aclanthology.org/2026.blackboxnlp-1.40.pdf",
        "code": "https://github.com/abuba8/When-Few-Shot-Hurts",
    },
    {
        "slug": "smart-vision-glasses",
        "title": "Safety-Prioritised Multimodal Navigation for Edge Smart Glasses with Constrained On-Device Language Models",
        "venue": "International Digital Public Health Conference, 2nd International Workshop on Architecture-Based IoT and Artificial Intelligence",
        "authors": "Sefki Kolozali, Abdullah Ahmad, Alireza Kalantarhormozi, Ali Radwan, Ahmed J.O. Ahmed, Soran Ghaderi, Mustafa Mustafa, Vishwanathan Mohan, Klaus McDonald-Maier",
        "year": "2026",
        "abstract": """
        AI-enabled assistive navigation for visually impaired
        individuals must satisfy strict safety, latency, and computational
        constraints on wearable edge platforms. This paper presents a
        safety-prioritised multimodal navigation framework implemented
        on a fully custom-designed and 3D-printed smart glasses platform
        integrated with an NVIDIA Jetson Orin Nano edge computing
        module. The system combines lightweight visual object detection,
        binaural audio localisation, and QR-based contextual cues with
        constrained small-scale large language model (LLM) reasoning.
        A deterministic finite state machine (FSM) enforces a hazard-
        first decision hierarchy, ensuring that safety-critical detections
        override contextual navigational suggestions while maintaining
        real-time operation entirely on-device.
        Experimental results demonstrate 99% audio event recognition
        accuracy and up to 90.1% precision 85.9% recall for object
        detection under edge constraints. The 0.5B parameter LLM
        achieves approximately 2.1 seconds inference latency on the
        Jetson Orin Nano. The integrated system was validated through a
        structured 9-minute 45-second indoor navigation trial involving
        dynamic and static obstacles, during which no unsafe actions
        occurred. These findings show that compact multimodal models,
        when embedded within a deterministic safety hierarchy and
        deployed on dedicated edge hardware, enable reliable real-time
        assistive navigation without reliance on cloud infrastructure.
        """,
        "link": "https://ieeexplore.ieee.org/document/11650519",
    },
]

PROJECTS = [
    {
        "slug": "self-driving",
        "name": "Self Driving",
        "initials": "SD",
        "blurb": "Self-Driving Perception Stack — Real-Time CV Pipeline",
        "year": "2025",
        "stack": ["PyTorch", "YOLO", "MiDaS", "ONNX", "ByteTrack/DeepSORT"],
        "github": "https://github.com/abuba8",
        "description": [
            "Unified perception pipeline combining YOLOv8 object detection, YOLOv8-seg/ENet lane segmentation (fine-tuned on CULane), MiDaS monocular depth estimation, and traffic sign classification. ",
            "Per-frame JSON output (objects, lanes, depth map) for downstream planning/control; ONNX export for efficient inference; ByteTrack/DeepSORT multi-object tracking. ",
        ],
    },
    {
        "slug": "long-vid-qa",
        "name": "Long VidQA",
        "initials": "LVQA",
        "blurb": "LongVidQA — Long-Video Q&A + Highlights Engine",
        "year": "2025",
        "stack": ["Python", "Whisper", "shot-based chuking", "CLIP", "FAISS", "cross-encoder reranking", "Distillation", "FASTAPI"],
        "github": "https://github.com/abuba8/LongVidQA",
        "description": [
            "Built a multimodal Q&A engine for 2–4h videos delivering timestamped answers, auto-chapters, and highlight reels.",
            "Retrieval stack: Whisper transcription + shot-based chunking, CLIP/SigLIP frame embeddings, FAISS ANN search, cross-encoder reranking.", 
            "Model efficiency: distilled teacher model to a 0.5B INT4 student, 63% latency reduction, 71% cost reduction.", 
        ],
    },
]

CONTACT = {
    "email": "abdullah.ahmad.ac@gmail.com",
    # "twitter": "https://twitter.com/johndoe",
    "github": "https://github.com/abuba8",
    "linkedin": "https://linkedin.com/in/abuba8",
    # "scholar": "https://scholar.google.com",
}


def find(items, slug):
    return next((x for x in items if x["slug"] == slug), None)


HEADLINE = "Building data & training systems for multimodal foundation models · Open to research collaborations"

STATUS = {"label": "Available for research collaborations", "kind": "open"}

RESEARCH = {
    "paragraph": (
        "My research sits at the intersection of multimodal representation learning and the data systems "
        "that make modern foundation models possible. I'm interested in how the structure of pretraining data "
        "shapes what a model learns, how we can build training pipelines that scale gracefully without large "
        "compute budgets, and how to evaluate cross-modal understanding in ways that go beyond benchmark accuracy. "
        "Increasingly I'm drawn to the messy, infrastructural questions — data curation, deduplication, "
        "pretraining recipes — because that's where the real leverage lives. "
        "A lot of what draws me to this side of ML is the same thing I like about my day job: the unglamorous " 
        "infrastructure work where most of the real progress quietly happens."
    ),
    "areas": [
        "Multimodal representation learning (vision, language, audio)",
        "Data-centric ML and pretraining corpus design",
        "Efficient training and inference at small-to-medium scale",
        "Evaluation methodology for foundation models",
        "Open-source research tooling",
    ],
    # "highlights": [
    #     "Established a new Pareto frontier between modality coverage and downstream performance, matching SOTA at one-third the training tokens (ICLR 2025).",
    #     # "Showed that distribution-shift robustness in vision-language models is largely a data composition problem, not a training-time one (CVPR 2024).",
    #     # "Released open-source training and evaluation toolkits used by research labs at three universities.",
    # ],
}


@app.route("/")
def home():
    return render_template(
        "index.html",
        news=NEWS,
        publications=PUBLICATIONS,
        projects=PROJECTS,
        contact=CONTACT,
        headline=HEADLINE,
        status=STATUS,
        research=RESEARCH,
    )


@app.route("/cv")
def cv():
    return render_template("cv.html", contact=CONTACT)


@app.route("/publications/<slug>")
def publication_detail(slug):
    pub = find(PUBLICATIONS, slug)
    if not pub:
        abort(404)
    return render_template("publication.html", pub=pub, contact=CONTACT)


@app.route("/projects/<slug>")
def project_detail(slug):
    project = find(PROJECTS, slug)
    if not project:
        abort(404)
    return render_template("project.html", project=project, contact=CONTACT)


@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = (request.json or {}).get("email", "")
    return jsonify({"ok": True, "email": email})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
