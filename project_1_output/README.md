# Chat Assistant Documentation

## Overview
This Chat Assistant is a web application that allows users to interact with a language model through a chat interface. It is built using a FastAPI backend and a JavaScript frontend.

## Features
- Continuous conversation with the LLM.
- User can choose different LLMs.
- Displays conversation history similar to ChatGPT.
- Deployable on Render.com.

## Installation Instructions
### Prerequisites
- Python 3.7+
- Node.js
- FastAPI
- LiteLLM

### Backend Setup
1. Clone the repository.
2. Navigate to the backend directory.
3. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
4. Run the server:
   ```bash
   uvicorn server:app --reload
   ```

### Frontend Setup
1. Navigate to the frontend directory.
2. Open `index.html` in a web browser.

## Usage
- Open the frontend in your browser.
- Type your message in the input box and press enter.
- The assistant will respond based on the selected LLM.

## Deployment
1. Create an account on Render.com.
2. Follow the instructions to deploy a FastAPI application.
3. Ensure your application is publicly accessible.

## Extensions
- Text file uploads for prompt context.
- Image file uploads for multimodal LLMs.
- Side-by-side LLM response comparison.

## License
This project is licensed under the MIT License.