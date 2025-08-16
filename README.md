# KeyWordMatcher

A FastAPI-based application that automatically generates keyword-optimized resume summaries using AI. The application analyzes job descriptions, extracts relevant keywords, and generates professional summaries that are optimized for Applicant Tracking Systems (ATS) while maintaining truthfulness and readability.


## 📋 Prerequisites

- Python 3.12+
- Docker and Docker Compose
- Google Gemini API key
- LaTeX distribution (handled automatically in Docker)

## 🛠️ Setup

### Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd KeyWordMatcher
   ```

2. **Set up environment variables**
   ```bash
   cd agent
   cp .env.example .env  # if .env.example exists
   # Edit .env and add your Google API key:
   # GOOGLE_API_KEY=your_api_key_here
   ```

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

## Usage
Install the chrome extension and use it to send the page contents to server and generate resume


---

**Note**: This application requires a valid Google Gemini API key to function. Ensure you have proper API access and billing set up before use.
