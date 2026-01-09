# 🤖 CrewAI Video-to-Blog 

[![Live Demo](https://img.shields.io/badge/Demo-Live%20App-blueviolet?style=for-the-badge&logo=streamlit)](https://crewai-youtube-to-blog.streamlit.app/)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Agentic_Framework-crimson?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green?style=for-the-badge&logo=openai&logoColor=white)

##  Overview

This project leverages **Multi-Agent Orchestration** to automate the process of content creation. It uses **CrewAI** to deploy autonomous AI agents that "watch" YouTube videos, extract key insights, and transform them into comprehensive, engaging blog posts.

Instead of manually taking notes and drafting, this tool employs a **Researcher Agent** to analyze video transcripts and a **Writer Agent** to craft professional narratives, all accessible through a clean **Streamlit** interface.

---

##  Key Features

* **Autonomous Research:** The **Researcher Agent** extracts transcripts and technical details from any YouTube URL using `YoutubeVideoSearchTool`.
* **Intelligent Drafting:** The **Writer Agent** takes raw research and converts it into a structured, 3-paragraph blog post.
* **Custom Topic Focus:** Users can guide the agents to focus on specific angles (e.g., "Technical Implementation" vs. "General Overview").
* **Model Flexibility:** Seamlessly switch between **GPT-4o**, **GPT-4-Turbo**, and other OpenAI models directly from the sidebar.
* **Instant Export:** Generate and download the final blog post as a Markdown (`.md`) file with one click.

---

##  Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | [Streamlit](https://streamlit.io/) | Interactive web UI for input and real-time feedback. |
| **Orchestration** | [CrewAI](https://crewai.com/) | Managing agent roles, goals, and sequential task execution. |
| **LLM Provider** | [OpenAI API](https://openai.com/) | Powering the intelligence of the agents (GPT-4o). |
| **Tools** | `YoutubeVideoSearchTool` | Semantic search and transcript extraction from video URLs. |


---

##  How It Works

1.  **Configuration:** The user enters their OpenAI API Key and selects a model (e.g., `gpt-4o`) via the sidebar.
2.  **Input:** The user provides a **YouTube Video URL** and a specific **Blog Topic**.
3.  **Agent 1 (The Researcher):** 
    * *Role:* Uses the `YoutubeVideoSearchTool` to scrape the video's content.
    * *Goal:* Extract relevant quotes, technical explanations, and timestamps.
4.  **Agent 2 (The Writer):** 
    * *Role:* Receives the structured data from the Researcher.
    * *Goal:* Writes a compelling narrative, ensuring the tone matches the requested topic.
5.  **Output:** The final blog post is displayed in Markdown format and made available for download.

---

##  Installation & Setup

**Prerequisites:** Python 3.10+



1.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**
    ```bash
    streamlit run app.py
    ```

3.  **Usage:**
    * Enter your OpenAI API Key in the sidebar.
    * Paste a YouTube link.
    * Click **Generate Blog Post**.
      
> **Note:** Ensure the YouTube video you select has captions/transcripts enabled for the tool to work correctly.
---

##  Screenshots

![App Screenshot](assets/demo.png)
[Click here for demo (PDF)](assets/demo.pdf)

[Click here for demo of backend process (PDF)](assets/demo1.pdf)

---

**Built with ❤️ using CrewAI & Streamlit**
