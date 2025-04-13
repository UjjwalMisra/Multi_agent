# tasks.py
from crewai import Task

class AIUseCaseGenerationTasks:
    def industry_research_task(self, agent, company_name=None, industry=None):
        if company_name:
            task_description = f"""Research {company_name} to understand its business model, 
            key offerings, market position, and strategic focus areas.
            
            1. Research the company's history, mission, and values
            2. Identify the company's main products or services
            3. Analyze the company's market position and competitors
            4. Determine the company's strategic focus areas (e.g., operations, supply chain, customer experience)
            5. Identify any existing AI/ML initiatives or digital transformation efforts
            
            Compile your findings into a comprehensive report that will serve as the foundation
            for identifying relevant AI use cases.
            """
        else:
            task_description = f"""Research the {industry} industry to understand its structure, 
            key players, business models, and strategic focus areas.
            
            1. Research the industry's structure, size, and growth trends
            2. Identify the major players and their business models
            3. Analyze common challenges and opportunities in the industry
            4. Determine typical strategic focus areas in this industry
            5. Identify any existing AI/ML adoption trends in the industry
            
            Compile your findings into a comprehensive report that will serve as the foundation
            for identifying relevant AI use cases.
            """
        
        return Task(
            description=task_description,
            agent=agent,
            expected_output="A detailed analysis report of the company or industry"
        )
    
    def market_standards_analysis_task(self, agent, industry_research_output):
        return Task(
            description=f"""Analyze industry trends and standards related to AI, ML, and automation
            within the sector based on the industry research provided.
            
            Use the following industry research as context:
            {industry_research_output}
            
            Your analysis should include:
            1. Current state of AI/ML adoption in the industry
            2. Common AI use cases already being implemented by industry leaders
            3. Emerging AI trends that are gaining traction
            4. Industry-specific standards or best practices for AI implementation
            5. Potential gaps or opportunities for AI innovation
            
            Provide specific examples and references where possible.
            """,
            agent=agent,
            expected_output="An analysis of AI/ML industry standards and adoption trends"
        )
    
    def use_case_generation_task(self, agent, industry_research_output, market_standards_output):
        return Task(
            description=f"""Generate relevant use cases where the company or industry can leverage 
            GenAI, LLMs, and ML technologies based on the research and analysis provided.
            
            Use the following as context:
            Industry Research: {industry_research_output}
            Market Standards Analysis: {market_standards_output}
            
            For each use case, provide:
            1. A clear title and description
            2. The specific business problem it addresses
            3. The expected benefits (operational efficiency, customer satisfaction, cost reduction, etc.)
            4. The type of AI/ML technology required (e.g., GenAI, computer vision, NLP, predictive analytics)
            5. Implementation complexity (Low, Medium, High)
            6. Potential ROI (Low, Medium, High)
            
            Generate at least 10 use cases, ensuring they are relevant to the company's
            or industry's specific needs and strategic focus areas.
            """,
            agent=agent,
            expected_output="A list of at least 10 relevant AI/GenAI use cases with detailed descriptions"
        )
    
    def resource_collection_task(self, agent, use_cases_output):
        return Task(
            description=f"""Find relevant datasets, tools, frameworks, and resources for implementing
            the proposed AI use cases.
            
            Use Cases: {use_cases_output}
            
            For each use case, identify:
            1. Relevant datasets available on platforms like Kaggle, HuggingFace, and GitHub
            2. Suitable AI/ML frameworks or libraries
            3. Research papers, tutorials, or guides that could be helpful
            4. Pre-trained models that could be leveraged
            
            For each resource, provide:
            - Name or title
            - Link (URL)
            - Brief description of how it relates to the use case
            - Any usage considerations or limitations
            
            Compile your findings into a structured resource list organized by use case.
            """,
            agent=agent,
            expected_output="A comprehensive list of resources for implementing each use case"
        )
    
    def proposal_synthesis_task(self, agent, industry_research_output, market_standards_output, use_cases_output, resources_output):
        return Task(
            description=f"""Create a comprehensive final proposal that presents the top AI use cases
            for the company or industry, based on all previous research and analysis.
            
            Use the following as context:
            Industry Research: {industry_research_output}
            Market Standards Analysis: {market_standards_output}
            Use Cases: {use_cases_output}
            Resources: {resources_output}
            
            Your proposal should include:
            1. Executive Summary
            2. Industry/Company Overview
            3. AI Landscape in the Industry
            4. Top 5 Recommended AI Use Cases (prioritized based on impact and feasibility)
            5. Implementation Considerations for Each Use Case
            6. Required Resources (with clickable links)
            7. Next Steps and Timeline
            
            Format the proposal in a professional, well-structured manner suitable for presentation
            to executives. Make sure all resource links are properly formatted and clickable.
            """,
            agent=agent,
            expected_output="A comprehensive AI use case proposal document"
        )
