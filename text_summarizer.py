import requests
from gradio.blocks import Blocks
from gradio.components import Textbox

# DeepSeek API Endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

def summarize_text(text):
    """
    Uses DeepSeek AI to summarize a given text.
    """
    payload = {
        "model": "deepseek-coder",
        "prompt": f"Summarize the following text in **3 bullet points**:\n\n{text}",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        if response.status_code == 200:
            return response.json().get("response", "No summary generated.")
        else:
            return f"Error: {response.text}"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama server. Make sure it's running at localhost:11434"

# Create interface using Blocks API
with Blocks(title="AI-Powered Text Summarizer", description="Enter a long text and get a concise summary in bullet points.") as demo:
    input_text = Textbox(label="Input Text", lines=10, placeholder="Enter text to summarize...")
    output_text = Textbox(label="Summary")
    input_text.change(fn=summarize_text, inputs=input_text, outputs=output_text)

if __name__ == "__main__":
    print("Starting Gradio interface...")
    demo.launch(server_port=7860)
