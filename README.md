# Express.js Application Generator 🚀

CLI tool that generates single-file Express.js applications with MongoDB integration.

## Features 🛠️

- Express.js server setup
- MongoDB/Mongoose integration
- Swagger UI documentation
- CORS enabled
- Optional authentication
- Single-file output

## Requirements 📋

- Python 3.6+
- GPT-4 Mini API access
- Required packages: `langchain`, `openai`

## Installation ⚙️

```bash
pip install langchain openai
export OPENAI_API_KEY='your-api-key'
```

## Usage 💻

```bash
python app.py
```

Follow the prompts to specify:
- API endpoints
- Authentication requirements

Output will be saved as `express_app.js`

## Architecture 🏗️

- Uses LangChain for LLM interaction
- GPT-4 Mini for code generation
- Template-based prompt engineering
- File I/O for code output

## Limitations ⚠️

- Single file output only
- Basic authentication options
- Requires manual dependency installation
- No custom middleware support
