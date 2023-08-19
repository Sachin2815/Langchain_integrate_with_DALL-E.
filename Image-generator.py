key = "sk-W9fKkXZYsgYKZF83Yvvxxxxxxxxxxxx"

from langchain.llms import OpenAI
import os
from skimage import io
import cv2
myllm = OpenAI(
    model = 'text-davinci-003',
    temperature=1,
    openai_api_key=key
)
os.environ['OPENAI_API_KEY'] = key
from langchain.agents import load_tools
from langchain.agents import initialize_agent

tools = load_tools(['dalle-image-generator'])

agent = initialize_agent(tools, llm =myllm, agent="zero-shot-react-description", verbose=True)
output = agent.run("The Busking girl")
