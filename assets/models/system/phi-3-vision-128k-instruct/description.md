## Model Summary

Phi-3 Vision is a lightweight, state-of-the-art open multimodal model built upon datasets which include - synthetic data and filtered publicly available websites - with a focus on very high-quality, reasoning dense data both on text and vision.  The model belongs to the Phi-3 model family, and the multimodal version comes with 128K context length (in tokens) it can support. The model underwent a rigorous enhancement process, incorporating both supervised fine-tuning and direct preference optimization to ensure precise instruction adherence and robust safety measures.

Resources and Technical Documentation:

+ [Phi-3 Microsoft Blog](https://aka.ms/phi3blog-april)
+ [Phi-3 Technical Report](https://aka.ms/phi3-tech-report)

## Training

### Model

* Architecture: Phi-3-Vision-128K-Instruct has 4.2B parameters and contains image encoder, connector, projector, and Phi-3 Mini language model.
* Inputs: Text and Image. It’s best suited for prompts using the chat format. 
* Context length: 128K tokens
* GPUs: 512 H100-80G
* Training time: 1.5 days
* Training data: 500B vision and text tokens
* Outputs: Generated text in response to the input
* Dates: Our models were trained between February and April 2024
* Status: This is a static model trained on an offline text dataset with cutoff date Mar 15, 2024. Future versions of the tuned models may be released as we improve models.
* Release Type: Open weight release
* Release dates: The model weight is released on May 21, 2024.

### Datasets

Our training data includes a wide variety of sources, and is a combination of

1) publicly available documents filtered rigorously for quality, selected high-quality educational data and code;
2) selected high-quality image-text interleave;
3) newly created synthetic, “textbook-like” data for the purpose of teaching math, coding, common sense reasoning, general knowledge of the world (science, daily activities, theory of mind, etc.), newly created image data, e.g., chart/table/diagram/slides;
4) high quality chat format supervised data covering various topics to reflect human preferences on different aspects such as instruct-following, truthfulness, honesty and helpfulness.

The data collection process involved sourcing information from publicly available documents, with a meticulous approach to filtering out undesirable documents and images. To safeguard privacy, we carefully filtered various image and text data sources to remove or scrub any potentially personal data from the training data.

More details can be found in the [Phi-3 Technical Report](https://aka.ms/phi3-tech-report).

## Benchmarks

To understand the capabilities, we compare Phi-3 Vision-128K-Instruct with a set of models over a variety of zero-shot benchmarks using our internal benchmark platform.

|Benchmark|Phi-3 Vision-128K-In1|LlaVA-1.6 Vicuna-7B|QWEN-VL Chat|Llama3-Llava-Next-8B|Claude-3 Haiku|Gemini 1.0 Pro V|GPT-4V-Turbo|
|---------|---------------------|------------------|------------|--------------------|--------------|----------------|------------|
|MMMU|40.4|34.2|39.0|36.4|40.7|42.0|55.5| 
|MMBench|80.5|76.3|75.8|79.4|62.4|80.0|86.1|
|ScienceQA|90.8|70.6|67.2|73.7|72.0|79.7|75.7|
|MathVista|44.5|31.5|29.4|34.8|33.2|35.0|47.5|
|InterGPS|38.1|20.5|22.3|24.6|32.1|28.6|41.0|
|AI2D|76.7|63.1|59.8|66.9|60.3|62.8|74.7|
|ChartQA|81.4|55.0|50.9|65.8|59.3|58.0|62.3|
|TextVQA|70.9|64.6|59.4|55.7|62.7|64.7|68.1|
|POPE|85.8|87.2|82.6|87.0|74.4|84.2|83.7|

## Intended Uses

**Primary use cases**

The model is intended for broad commercial and research use in English. The model provides uses for general purpose AI systems and applications with visual and text input capabilities which require

1) memory/compute constrained environments;
2) latency bound scenarios;
3) general image understanding;
4) OCR;
5) chart and table understanding.

The model is designed to accelerate research on efficient language and multimodal models, for use as a building block for generative AI powered features.

**Use case considerations**

The model is not specifically designed or evaluated for all downstream purposes. Developers should consider common limitations of language models as they select use cases, and evaluate and mitigate for accuracy, safety, and fairness before using within a specific downstream use case, particularly for high-risk scenarios.
Developers should be aware of and adhere to applicable laws or regulations (including privacy, trade compliance laws, etc.) that are relevant to their use case.

Nothing contained in this Model Card should be interpreted as or deemed a restriction or modification to the license the model is released under.

## Responsible AI Considerations

Like other models, the Phi family of models can potentially behave in ways that are unfair, unreliable, or offensive. Some of the limiting behaviors to be aware of include:

+ Quality of Service: The Phi models are trained primarily on English text. Languages other than English will experience worse performance English language varieties with less representation in the training data might experience worse performance than standard American English.
+ Representation of Harms & Perpetuation of Stereotypes: These models can over- or under-represent groups of people, erase representation of some groups, or reinforce demeaning or negative stereotypes. Despite safety post-training, these limitations may still be present due to differing levels of representation of different groups or prevalence of examples of negative stereotypes in training data that reflect real-world patterns and societal biases.  
+ Inappropriate or Offensive Content: These models may produce other types of inappropriate or offensive content, which may make it inappropriate to deploy for sensitive contexts without additional mitigations that are specific to the use case.  
+ Information Reliability: Language models can generate nonsensical content or fabricate content that might sound reasonable but is inaccurate or outdated.
+ Limited Scope for Code: Majority of Phi-3 training data is based in Python and use common packages such as "typing, math, random, collections, datetime, itertools". If the model generates Python scripts that utilize other packages or scripts in other languages, we strongly recommend users manually verify all API uses.

Developers should apply responsible AI best practices and are responsible for ensuring that a specific use case complies with relevant laws and regulations (e.g. privacy, trade, etc.). Important areas for consideration include:  

+ Allocation: Models may not be suitable for scenarios that could have consequential impact on legal status or the allocation of resources or life opportunities (ex: housing, employment, credit, etc.) without further assessments and additional debiasing techniques.
+ High-Risk Scenarios: Developers should assess suitability of using models in high-risk scenarios where unfair, unreliable or offensive outputs might be extremely costly or lead to harm. This includes providing advice in sensitive or expert domains where accuracy and reliability are critical (ex: legal or health advice). Additional safeguards should be implemented at the application level according to the deployment context.
+ Misinformation: Models may produce inaccurate information. Developers should follow transparency best practices and inform end-users they are interacting with an AI system. At the application level, developers can build feedback mechanisms and pipelines to ground responses in use-case specific, contextual information, a technique known as Retrieval Augmented Generation (RAG).
+ Generation of Harmful Content: Developers should assess outputs for their context and use available safety classifiers or custom solutions appropriate for their use case.
+ Misuse: Other forms of misuse such as fraud, spam, or malware production may be possible, and developers should ensure that their applications do not violate applicable laws and regulations.
+ Identification of individuals: models with vision capabilities may have the potential to uniquely identify individuals in images. Safety post-training steers the model to refuse such requests, but developers should consider and implement, as appropriate, additional mitigations or user consent flows as required in their respective jurisdiction, (e.g., building measures to blur faces in image inputs before processing).

## Inference Samples

Inference type|Python sample (Notebook)|CLI with YAML
|--|--|--|
Real time|<a href="https://aka.ms/azureml-infer-sdk-image-text-to-text-generation" target="_blank">image-text-to-text-generation-online-endpoint.ipynb</a>|<a href="https://aka.ms/azureml-infer-cli-image-text-to-text-generation" target="_blank">image-text-to-text-generation-online-endpoint.sh</a>

## Sample inputs and outputs (for real-time inference)

Phi-3-vision model only supports single image per conversation. Specifically, please refer to below grid:
 
|    |Single-turn|Multi-turn conversation|
|------------|------------|------------|
|Single Image|Yes|Yes|
|Multiple Images|No|No|

### Sample Input

```json
{
  "input_data": {
    "input_string": [
      {
        "role": "user",
        "content": [
          {
            "type": "image_url",
            "image_url": {
              "url": "https://www.ilankelman.org/stopsigns/australia.jpg"
            }
          },
          {
            "type": "text",
            "text": "What is shown in this image? Be extremely detailed and specific."
          }
        ]
      }
    ],
    "parameters": { "temperature": 0.7, "max_new_tokens": 2048 }
  }
}
```

### Sample Output

```json
{
  "output": " The image captures a vibrant street scene. Dominating the left side of the image is a red stop sign, standing on a white pole. Adjacent to the stop sign, a white lion statue adds a touch of symbolism to the scene. \n\nThe background is filled with colorful buildings, including a red one and a yellow one, adding a lively atmosphere to the scene. The blue sky overhead and a clear white road underneath it complete the picture. \n\nAdding to the cultural context, there are Chinese characters visible in the background, suggesting the presence of a Chinese influence in this location. The overall scene is a blend of urban life and cultural elements."

}
```

## Software

* [PyTorch](https://github.com/pytorch/pytorch)
* [Transformers](https://github.com/huggingface/transformers)
* [Flash-Attention](https://github.com/HazyResearch/flash-attention)

## Hardware
Note that by default, the Phi-3-Vision-128K model uses flash attention, which requires certain types of GPU hardware to run. We have tested on the following GPU types:
* NVIDIA A100
* NVIDIA A6000
* NVIDIA H100

## License

The model is licensed under the MIT license.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft’s Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks). Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party’s policies.
