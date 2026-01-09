import streamlit as st
import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import YoutubeVideoSearchTool


st.set_page_config(page_title="AI Video to Blog Converter", page_icon="📝")

st.title("🤖 CrewAI: YouTube Video to Blog Post")
st.markdown("Enter a YouTube video URL and a topic, and let the AI agents generate a comprehensive blog post for you.")

with st.sidebar:
    st.header("Settings")
    
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    
    model_name = st.selectbox("Select Model", ["gpt-4o", "gpt-4-turbo", "gpt-5.1"], index=0)

    st.divider()
    st.info("Ensure the video has captions/transcript available.")

topic = st.text_input("Enter the Blog Topic:")
video_url = st.text_input("Enter YouTube Video URL:")

def run_crew(api_key, topic, video_url):
    
    os.environ["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_MODEL_NAME"] = model_name

    # Tools included
    
    yt_tool = YoutubeVideoSearchTool(youtube_video_url=video_url)

    # Agents Section
    blog_researcher = Agent(
        role='Blog Researcher from Youtube Videos',
        goal=f'Get the relevant video transcription and insights for the topic {topic} from the provided video',
        verbose=True,
        memory=True,
        backstory=(
           "Expert in analyzing video content to extract key technical details and insights."
        ),
        tools=[yt_tool],
        allow_delegation=True
    )

    blog_writer = Agent(
        role='Blog Writer',
        goal=f'Narrate compelling tech stories about the video {topic} from YT video',
        verbose=True,
        memory=True,
        backstory=(
            "With a flair for simplifying complex topics, you craft "
            "engaging narratives that captivate and educate."
        ),
        tools=[yt_tool],
        allow_delegation=False
    )

    # Tasks Section
    research_task = Task(
        description=(
            f"Analyze the provided video on the topic {topic}. "
            "Extract key technical details, explanations, and insights from the video transcript."
        ),
        expected_output=f'A comprehensive 3 paragraphs long report based on the {topic} of video content.',
        tools=[yt_tool],
        agent=blog_researcher,
    )

    write_task = Task(
        description=(
            f"Using the research provided, create a blog post about {topic}."
        ),
        expected_output=f'Summarize the info from the video on the topic {topic} and create the content for the blog',
        tools=[yt_tool],
        agent=blog_writer,
        async_execution=False,
        output_file='blog-post.md' 
    )

    # Crew
    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        memory=True,
        cache=True,
        max_rpm=100,
        share_crew=True
    )

    result = crew.kickoff(inputs={'topic': topic})
    return result

if st.button("Generate Blog Post"):
    if not api_key:
        st.error("Please enter your OpenAI API Key in the sidebar.")
    elif not video_url:
        st.error("Please provide a YouTube URL.")
    else:
        with st.spinner("Agents are working..."):
            try:
    
                result = run_crew(api_key, topic, video_url)
                
                st.success("Blog Post Generated Successfully!")
                
                st.subheader("📝 Generated Blog Content")
                st.markdown(result)
                
                st.download_button(
                    label="Download Blog Post",
                    data=str(result),
                    file_name="blog_post.md",
                    mime="text/markdown"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")