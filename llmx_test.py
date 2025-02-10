from llmx import  llm, TextGenerationConfig
import os

text_gen = llm(
provider="openai",
api_type="azure",
azure_endpoint="",#os.environ["AZURE_OPENAI_BASE"],
api_key="",#os.environ["AZURE_OPENAI_API_KEY"],
api_version="",
)

textgen_config = TextGenerationConfig(
    n=1,  # Number of responses generated
    temperature=0.0,  # Make the model deterministic
    model="",  # Model to be used
    use_cache=True,  # Use caching for faster generation
    top_p=0.1,  # Limit the next-token selection to a highly probable subset
    top_k=1,  # Consider only the most likely next word
)

messages = [
    {"role": "system", "content": "You are a helpful assistant that can explain concepts clearly to a 6 year old child."},
    {"role": "user", "content": "What is  gravity?"}
]

openai_response = text_gen.generate(messages, config=textgen_config)
print(openai_response.text[0].content)
