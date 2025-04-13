# crew.py
from crewai import Crew
from agents import (
    IndustryResearchAgent, 
    MarketStandardsAnalysisAgent,
    UseCaseGenerationAgent,
    ResourceCollectionAgent,
    ProposalSynthesisAgent
)
from tasks import AIUseCaseGenerationTasks
from tools import WebSearchTool, DatasetSearchTool

class AIUseCaseGenerationCrew:
    def __init__(self, llm):
        self.llm = llm
        self.web_search_tool = WebSearchTool()
        self.dataset_search_tool = DatasetSearchTool()
        
        # Initialize agents
        self.industry_research_agent = IndustryResearchAgent(llm=self.llm)
        self.industry_research_agent.add_tool(self.web_search_tool)
        
        self.market_standards_agent = MarketStandardsAnalysisAgent(llm=self.llm)
        self.market_standards_agent.add_tool(self.web_search_tool)
        
        self.use_case_generation_agent = UseCaseGenerationAgent(llm=self.llm)
        
        self.resource_collection_agent = ResourceCollectionAgent(llm=self.llm)
        self.resource_collection_agent.add_tool(self.web_search_tool)
        self.resource_collection_agent.add_tool(self.dataset_search_tool)
        
        self.proposal_synthesis_agent = ProposalSynthesisAgent(llm=self.llm)
        
        # Initialize tasks
        self.tasks = AIUseCaseGenerationTasks()
    
    def run(self, company_name=None, industry=None):
        # Create tasks
        industry_research_task = self.tasks.industry_research_task(
            agent=self.industry_research_agent,
            company_name=company_name,
            industry=industry
        )
        
        market_standards_task = self.tasks.market_standards_analysis_task(
            agent=self.market_standards_agent,
            industry_research_output="{industry_research_task_output}"
        )
        
        use_case_generation_task = self.tasks.use_case_generation_task(
            agent=self.use_case_generation_agent,
            industry_research_output="{industry_research_task_output}",
            market_standards_output="{market_standards_task_output}"
        )
        
        resource_collection_task = self.tasks.resource_collection_task(
            agent=self.resource_collection_agent,
            use_cases_output="{use_case_generation_task_output}"
        )
        
        proposal_synthesis_task = self.tasks.proposal_synthesis_task(
            agent=self.proposal_synthesis_agent,
            industry_research_output="{industry_research_task_output}",
            market_standards_output="{market_standards_task_output}",
            use_cases_output="{use_case_generation_task_output}",
            resources_output="{resource_collection_task_output}"
        )
        
        # Create and run the crew
        crew = Crew(
            agents=[
                self.industry_research_agent,
                self.market_standards_agent,
                self.use_case_generation_agent,
                self.resource_collection_agent,
                self.proposal_synthesis_agent
            ],
            tasks=[
                industry_research_task,
                market_standards_task,
                use_case_generation_task,
                resource_collection_task,
                proposal_synthesis_task
            ],
            verbose=2
        )
        
        result = crew.kickoff()
        return result
