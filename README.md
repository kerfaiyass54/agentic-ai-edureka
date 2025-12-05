# Edureka agentic AI

## 🚀 Overview
Welcome to this project*, an AI-powered SQL query generator that leverages the power of Google's Generative AI to convert natural language questions into SQL queries. This project is designed to help developers and data analysts quickly and accurately generate SQL queries from plain English questions, making data retrieval more efficient and accessible.

### Key Features
- **AI-Powered Query Generation**: Utilizes Google's Generative AI to convert natural language questions into SQL queries.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive user experience.
- **SQL Database Integration**: Supports SQLite for seamless data retrieval and manipulation.
- **Customizable Prompts**: Allows for customization of AI prompts to fit specific use cases.

### Who This Project Is For
- Data analysts and developers looking to streamline SQL query generation.
- Anyone interested in leveraging AI to automate repetitive tasks.
- Educators and students learning about AI and SQL integration.

## ✨ Features
- 🔍 **Natural Language to SQL Conversion**: Convert English questions into SQL queries using AI.
- 📊 **SQL Database Integration**: Connect to SQLite databases for data retrieval.
- 🛠️ **Customizable Prompts**: Tailor AI prompts to fit specific requirements.
- 🌟 **User-Friendly Interface**: Easy to use with Streamlit.

## 🛠️ Tech Stack
- **Programming Language**: Python
- **Frameworks and Libraries**:
  - Streamlit: For building the web interface.
  - Google Generative AI: For AI-powered query generation.
  - Python-Dotenv: For managing environment variables.
  - SQLite: For database operations.
- **System Requirements**: Python 3.8 or later, SQLite 3.30 or later.

## 📦 Installation

### Prerequisites
- Python 3.8 or later
- SQLite 3.30 or later

### Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agentic-ai-edureka.git
   cd agentic-ai-edureka
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your Google API key:
     ```env
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

### Alternative Installation Methods
- **Docker**: You can use Docker to containerize the application. A Dockerfile is included in the repository.
  ```bash
  docker build -t agentic-ai-edureka .
  docker run -p 8501:8501 agentic-ai-edureka
  ```


## 🔧 Configuration
- **Environment Variables**: Set your Google API key in a `.env` file.
- **Configuration Files**: Modify `app.py` to customize prompts and database connections.

## 🤝 Contributing
We welcome contributions! Here's how you can get involved:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, concise messages.
4. Push your branch to your fork.
5. Open a pull request.

### Development Setup
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Code Style Guidelines
- Follow PEP 8 style guidelines.
- Use meaningful variable and function names.
- Add comments to explain complex logic.

### Pull Request Process
1. Ensure your code is well-tested.
2. Write clear and concise commit messages.
3. Address any feedback from the maintainers.



**Additional Guidelines:**
- Use modern markdown features (badges, collapsible sections, etc.).
- Include practical, working code examples.
- Make it visually appealing with appropriate emojis.
- Ensure all code snippets are syntactically correct for Python.
- Include relevant badges (build status, version, license, etc.).
- Make installation instructions copy-pasteable.
- Focus on clarity and developer experience.
