# Chat Assistant Documentation

## Overview
This project is a Chat Assistant built using FastAPI for the backend and a JavaScript frontend. It allows users to interact with a selected LLM in a continuous conversation format.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/robot-coder/ChatAssistant.git
   cd ChatAssistant
   ```
2. Install the required dependencies:
   ```bash
   pip install fastapi uvicorn
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```
4. Open your browser and navigate to `http://localhost:8000` to access the Chat Assistant.

## Deployment
The Chat Assistant will be deployed on Render.com. Link to the deployed site will be added here once available.

## API Key
A new OpenRouter.ai API Key will be created for public availability with a spending limit.

## Features
- Continuous conversation with LLM
- LLM selection

## Extensions
- Text and image file uploads (to be implemented)
- Side-by-side LLM response comparison (to be implemented)