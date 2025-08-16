from prompts import SYSPROMPTS

class SummaryService:
    def __init__(self, llm) -> None:
        self.llm  = llm
        
    def generate(self, content) -> str:
        print("Generating Summary")
        messages = [
                ("system", SYSPROMPTS["summary"]),
                ("human", content)
                ]
        summary =  self.llm.invoke(messages)
        return summary.content
