import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from langchain_community.chat_models import ChatOpenAI
import warnings
from scripts.tools.reader_tool import PDFExtractorTool

# Warning control
warnings.filterwarnings('ignore')

# Load the .env file
load_dotenv()

# Get the OpenAI API key from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    # Directories for input (PDFs) and output (summaries)
    input_dir = "data/pdfs"
    output_dir = "data/outputs"

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Initialize the OpenAI model
    llm = ChatOpenAI(
        model_name="gpt-4",
        temperature=0.7,
        openai_api_key=OPENAI_API_KEY
    )

    # Initialize the PDF extraction tool
    pdf_tool = PDFExtractorTool()

    # Define agents
    pdf_reader_agent = Agent(
        role="Senior PDF Reader and Extractor",
        goal="Read and extract the raw text from a PDF file.",
        backstory="You are a professional that excels in getting brute text from PDF files, keeping the file's content integrity.",
        verbose=True,
        llm=llm,
        tools=[pdf_tool]
    )

    analyzer_agent = Agent(
        role="Senior Text Analyst",
        goal="Identify important information from the given text.",
        backstory="You are a professional that excels in analyzing texts and extracting their most important information while keeping the content's integrity.",
        llm=llm
    )

    summarizer_agent = Agent(
        role="Senior Copywriter",
        goal="Create short and coherent summaries from the given text.",
        backstory="You are a professional that excels in summarizing texts, ensuring that the summaries are concise and maintain coherence.",
        llm=llm
    )

    blogger_agent = Agent(
        role="Senior Blog Writer",
        goal="Format the received summary in a blog post style, including title, subheadings, and conclusion.",
        backstory="You are a professional that excels in formatting content for blog posts.",
        llm=llm
    )

    # Define tasks
    read_pdf_task = Task(
        description="Extract text from the given PDF.",
        expected_output="Return the raw text extracted from the PDF.",
        agent=pdf_reader_agent
    )

    analysis_task = Task(
        description="Identify and extract the most relevant information from the text received.",
        expected_output="A text containing the most relevant parts of the given text in natural language.",
        agent=analyzer_agent,
        context=[read_pdf_task]
    )

    summarize_task = Task(
        description="Summarize the received text in a way that keeps it cohesive while making it as concise as possible.",
        expected_output="A summarized text created from the given text in natural language.",
        agent=summarizer_agent,
        context=[analysis_task]
    )

    blog_format_task = Task(
        description="Format the given summary to match the style of a blog post.",
        expected_output="A text formatted in markdown that includes a relevant title and well-structured subheadings to organize the content.",
        agent=blogger_agent,
        context=[summarize_task]
    )

    # Create the Crew with a sequential execution process
    crew = Crew(
        agents=[pdf_reader_agent, analyzer_agent, summarizer_agent, blogger_agent],
        tasks=[read_pdf_task, analysis_task, summarize_task, blog_format_task],
        process="sequential"
    )

    # Iterate over the PDFs in the input directory and process them
    for pdf_file in os.listdir(input_dir):
        if pdf_file.endswith(".pdf"):
            pdf_path = os.path.abspath(os.path.join(input_dir, pdf_file))
            output_path = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}_summary.txt")

            print(f"\n📄 Processing: {pdf_file} at path: {pdf_path}")

            # Start the workflow
            try:
                result = crew.kickoff(inputs={"pdf_path": pdf_path})
            except Exception as e:
                print(f"❌ Error processing {pdf_file}: {e}")
                continue

            # Save the result to an output file
            with open(output_path, 'w', encoding="utf-8") as f:
                f.write(str(result))  # Convert CrewOutput to string
            print(f"✅ Processed and saved summary for {pdf_file} to {output_path}")

if __name__ == "__main__":
    main()