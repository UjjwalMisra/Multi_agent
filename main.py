# main.py
import os
import argparse
from crew import AIUseCaseGenerationCrew
from langchain.chat_models import ChatOpenAI

def main():
    parser = argparse.ArgumentParser(description="AI Use Case Generation System")
    parser.add_argument("--company", type=str, help="Name of the company to research", default=None)
    parser.add_argument("--industry", type=str, help="Industry to research if company not specified", default=None)
    args = parser.parse_args()
    
    if not args.company and not args.industry:
        print("Error: You must specify either a company name or an industry.")
        return
    
    # Initialize LLM
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    
    # Create and run the crew
    crew = AIUseCaseGenerationCrew(llm=llm)
    result = crew.run(company_name=args.company, industry=args.industry)
    
    # Save the result to a file
    with open("ai_use_case_proposal.md", "w") as f:
        f.write(result)
    
    print(f"AI Use Case Proposal has been generated and saved to ai_use_case_proposal.md")

if __name__ == "__main__":
    main()
