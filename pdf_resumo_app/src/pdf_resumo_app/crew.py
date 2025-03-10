from crewai import Agent, Crew, Task
from crewai.project import CrewBase, agent, crew, task
from pdf_resumo_app.tools.pdf_text_reader import PdfTextExtractionTool

@CrewBase
class ResumidorPdfs():
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	
	pdfReader = PdfTextExtractionTool(result_as_answer=True)

	@agent
	def pdf_reader_agent(self) -> Agent:
		return Agent(
			config = self.agents_config['pdf_reader_agent'], 
			verbose = True,
		)

	@agent
	def analyzer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['analyzer_agent'],
			verbose=True,
		)
	
	@agent
	def summarizer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['summarizer_agent'],
			verbose=True,
		)
	
	@agent
	def blogger_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['blogger_agent'],
			verbose=True,
		)
	

	@task
	def read_pdf_task(self) -> Task:
		return Task(
			config=self.tasks_config['read_pdf_task'],
			tools = [self.pdfReader]
		)

	@task
	def analyze_task(self) -> Task:
		return Task(
			config=self.tasks_config['analyze_task'],
			context=[self.read_pdf_task()]
		)
	
	@task
	def summarize_task(self) -> Task:
		return Task(
			config=self.tasks_config['summarize_task'],
			context=[self.analyze_task()]
		)
	
	@task
	def blog_format_task(self) -> Task:
		return Task(
			config=self.tasks_config['blog_format_task'],
			context=[self.summarize_task()],
			output_file="data/outputs/{file_name}.md"
		)
	

	@crew
	def crew(self) -> Crew:
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			verbose=True
		)