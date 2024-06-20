from crewai import Crew, Process
from nagents import news_researcher, news_writer
from ntasks import write_task, research_task

## Form the tech focus crew with some enhanced configuration

crew=Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

## Starting the task execution process with enhanced feedback 

result=crew.kickoff(inputs={"topic":"AI in healthcare"})
print(result)