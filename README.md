# AI-Powered Fact Checker

A modern web application that leverages the Perplexity AI API to fact-check text content and claims. Built with FastAPI and a beautiful dark-mode UI, this tool helps users verify information and get reliable sources.

![Fact Checker Demo](demo.gif)

## Features

### Core Functionality

- ✅ Real-time fact-checking of text content
- 🔍 Detailed analysis of claims and statements
- 📚 Source verification with citations
- 🎯 Accuracy rating on a scale of 1-10
- 🌐 Access to up-to-date information (weekly recency filter)

### User Interface

- 🌙 Modern dark mode interface
- 💫 Smooth animations and transitions
- ⚡ Real-time response display
- 🔗 Clickable source citations
- 📱 Fully responsive design
- ⌛ Beautiful loading animations

### Technical Features

- 🚀 Fast and efficient API responses
- 🛡️ Error handling with informative messages
- 🎨 DaisyUI and Tailwind CSS for styling
- 📊 Anime.js for smooth animations
- 🔒 Secure API key handling
- 🖥️ Clean code architecture

## ❤️ Support & Get 400+ AI Projects

This is one of 400+ fascinating projects in my collection! [Support me on Patreon](https://www.patreon.com/c/echohive42/membership) to get:

- 🎯 Access to 400+ AI projects (and growing daily!)
  - Including advanced projects like [2 Agent Real-time voice template with turn taking](https://www.patreon.com/posts/2-agent-real-you-118330397)
- 📥 Full source code & detailed explanations
- 📚 1000x Cursor Course
- 🎓 Live coding sessions & AMAs
- 💬 1-on-1 consultations (higher tiers)
- 🎁 Exclusive discounts on AI tools & platforms (up to $180 value)

## Setup

### Prerequisites

- Python 3.7+
- Perplexity API key

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fact-checker.git
cd fact-checker
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your environment variable for the Perplexity API key:

```bash
# Windows
set PERPLEXITY_API_KEY=your_api_key_here

# Linux/Mac
export PERPLEXITY_API_KEY=your_api_key_here
```

### Running the Application

1. Start the server:

```bash
python main.py
```

2. Open your browser and navigate to:

```
http://127.0.0.1:8000
```

## Usage

1. Enter or paste the text you want to fact-check into the text area
2. Click the "Check Facts" button
3. Wait for the analysis to complete
4. Review the detailed fact-check results
5. Check the provided sources through the citation links

## Technical Details

### API Configuration

- Model: llama-3.1-sonar-large-128k-online
- Temperature: 0.2 (for focused, consistent responses)
- Top P: 0.9
- Search Recency: Weekly updates
- Frequency Penalty: 1 (for diverse responses)

### Project Structure

```
fact-checker/
├── main.py              # FastAPI application entry point
├── config.py            # Configuration and environment variables
├── requirements.txt     # Project dependencies
├── README.md           # Documentation
├── services/
│   └── perplexity_service.py  # Perplexity API integration
└── templates/
    └── index.html      # Web interface
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- UI components from [DaisyUI](https://daisyui.com/)
- Animations powered by [Anime.js](https://animejs.com/)
- AI capabilities by [Perplexity AI](https://perplexity.ai/)
