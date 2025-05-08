# Chat Assistant Documentation

## Overview
This Chat Assistant is a simple implementation of a conversational AI using FastAPI for the backend and a JavaScript frontend. The assistant allows users to interact with different language models and maintain a continuous conversation.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/robot-coder/ChatAssistant.git
   cd ChatAssistant
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
2. Open `index.html` in your browser to access the Chat Assistant.
3. Interact with the assistant by typing your messages and selecting the desired language model.

## Features
- Continuous conversation
- User selection of language models
- Basic styling and user interface

## Deployment
This Chat Assistant can be deployed on Render.com. Follow their documentation for deployment instructions.

## Extensions
- Text file uploads to add to the prompt context.
- Image file uploads for multimodal LLMs.
- Side-by-side LLM response comparison.

## License
This project is licensed under the MIT License.