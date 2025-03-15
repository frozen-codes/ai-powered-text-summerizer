# AI-Powered Text Summarizer

A web-based application that uses DeepSeek AI to generate concise summaries of long texts. Built with Python, Gradio, and the DeepSeek API.

## Features

- Simple and intuitive web interface
- Real-time text summarization
- Bullet-point format summaries
- Built on DeepSeek's powerful language model

## Prerequisites

- Python 3.x
- Ollama with DeepSeek model installed locally

## Installation

1. Clone the repository:
```bash
git clone https://github.com/frozen-codes/ai-powered-text-summerizer.git
cd ai-powered-text-summerizer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Make sure Ollama is running with DeepSeek model

## Usage

1. Start the application:
```bash
python text_summarizer.py
```

2. Open your web browser and navigate to `http://localhost:7860`

3. Enter your text in the input box and click submit to get a summarized version

## How it Works

The application uses:
- Gradio for the web interface
- DeepSeek AI model through Ollama for text summarization
- Requests library for API communication

## API Configuration

The application connects to a local Ollama instance at `http://localhost:11434/api/generate`. Make sure Ollama is running with the DeepSeek model before starting the application.

## Contributing

Feel free to open issues or submit pull requests to improve the application.

## License

This project is open source and available under the MIT License.
