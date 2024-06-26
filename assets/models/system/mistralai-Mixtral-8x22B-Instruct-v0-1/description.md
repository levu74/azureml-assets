The Mixtral-8x22B-Instruct-v0.1 Large Language Model (LLM) is an instruct fine-tuned version of the [Mixtral-8x22B-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-v0.1).


# Inference samples

Inference type|Python sample (Notebook)|CLI with YAML
|--|--|--|
Real time|<a href="https://aka.ms/azureml-infer-online-sdk-text-generation-dolly" target="_blank">text-generation-online-endpoint.ipynb</a>|<a href="https://aka.ms/azureml-infer-online-cli-text-generation-dolly" target="_blank">text-generation-online-endpoint.sh</a>


# Sample inputs and outputs

### Sample input
```json
{
    "input_data": {
        "input_string": [
            {
                "role": "user",
                "content": "I am going to Paris, what should I see?"
            },
            {
                "role": "assistant",
                "content": "Paris, the capital of France, is known for its stunning architecture, art museums, historical landmarks, and romantic atmosphere. Here are some of the top attractions to see in Paris:\n\n1. The Eiffel Tower: The iconic Eiffel Tower is one of the most recognizable landmarks in the world and offers breathtaking views of the city.\n2. The Louvre Museum: The Louvre is one of the world's largest and most famous museums, housing an impressive collection of art and artifacts, including the Mona Lisa.\n3. Notre-Dame Cathedral: This beautiful cathedral is one of the most famous landmarks in Paris and is known for its Gothic architecture and stunning stained glass windows.\n\nThese are just a few of the many attractions that Paris has to offer. With so much to see and do, it's no wonder that Paris is one of the most popular tourist destinations in the world."
            },
            {
                "role": "user",
                "content": "What is so great about #1?"
            }
        ],
        "parameters": {
            "temperature": 0.6,
            "top_p": 0.9,
            "do_sample": true,
            "max_new_tokens": 200,
            "return_full_text": true
        }
    }
}
```

### Sample output
```json
{
  "output": " The Eiffel Tower is one of the most iconic landmarks in the world and is considered a symbol of Paris and France. Here are a few reasons why the Eiffel Tower is so great:\n\n1. Iconic design: The Eiffel Tower is known for its unique and distinctive design, which has made it one of the most recognizable landmarks in the world.\n2. Stunning views: The Eiffel Tower offers breathtaking views of the city of Paris from its observation decks. Visitors can see many of the city's famous landmarks, including the Louvre Museum, Notre-Dame Cathedral, and the Arc de Triomphe.\n3. Historical significance: The Eiffel Tower was built in 1889 for the World's Fair and was the tallest structure in the world at the time. It has since become a symbol of French culture and history.\n4. Romantic atmosphere"
}
```
