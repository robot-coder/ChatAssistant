# Chat Assistant Documentation

## Overview
This documentation provides an overview of the Chat Assistant project, detailing the front-end and back-end components, how they interact, and instructions for deployment.

## Front-End Development
The front-end is developed using HTML and JavaScript. It provides a user interface for interacting with the Chat Assistant. Users can input messages, view conversation history, and select different LLMs.

### Key Features
- Continuous conversation display similar to ChatGPT.
- User selection of LLM.

## Back-End Development
The back-end is built using Python's FastAPI framework. It handles requests from the front-end, processes user inputs, and interacts with the LiteLLM for generating responses.

### Key Features
- Maintains a message array for continuous conversation.
- Integrates with LiteLLM to make calls to the selected LLM.

## Deployment Instructions
1. Deploy the back-end FastAPI server on Render.com.
2. Ensure the front-end is hosted and linked to the back-end.
3. Update the Lab02 repo README with the link to the deployed Chat Assistant.

## Extensions (if implemented)
- Text file uploads to add context to prompts.
- Image file uploads for multimodal LLMs.
- Side-by-side comparison of LLM responses.

## Conclusion
This Chat Assistant project demonstrates the integration of front-end and back-end technologies to create an interactive AI assistant. The project can be extended with additional features as needed.