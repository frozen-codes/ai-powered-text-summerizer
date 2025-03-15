# AI-Powered Text Summarizer

A modern web application that uses DeepSeek R1 to generate concise bullet-point summaries from long text. Built with FastAPI and a clean, responsive user interface.

## Features

- Clean and modern user interface
- Real-time text summarization using DeepSeek R1
- Bullet-point format summaries
- Responsive design that works on all devices
- Shows both summary and original text for easy comparison

## Prerequisites

- Python 3.8 or higher
- Ollama with DeepSeek R1 model installed and running
- pip (Python package manager)

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

3. Make sure Ollama is running with DeepSeek R1 model:
```bash
ollama run deepseek-r1
```

## Usage

1. Start the application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:7860
```

3. Enter your text in the input field and click "Generate Summary" to get a concise bullet-point summary.

## Project Structure

- `app.py`: FastAPI application with route handlers
- `text_summarizer.py`: Core text summarization logic
- `templates/`: HTML templates for the web interface
- `requirements.txt`: Project dependencies

## License

This project is open source and available under the MIT License.
