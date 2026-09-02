import os
import time
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel, Field

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")
client=Groq(api_key=my_api_key)
model="llama-3.3-70b-versatile"

job_Description="""
Job Description Summary
Overview
• The Decision Management program enables intelligent decision based products through streaming analytics with the ability to govern these decisions and manage their outcomes with business agility.
• This program leverages business rules & AI engines, a streaming big data cluster, an in memory data grids, APIs, & UIs to deliver real time decisions at global scale
• This person will be responsible for mentoring the team as well as stay hands on.

We are looking for a Senior Software Developer to join our DMP team in Pune office

• Are you a strong technical programmer with experience working on high performance applications?
• Are you a excited about getting a 360 degree view of the coding world - writing code to develop a piece of code as well as write code to test it?
• Are you passionate about making a difference in this world?
• Do you want to be part of a team which helps prevent fraud on every Mastercard transaction in this world?

Role
• Design and implement application logic in Java.
• Write code to do unit testing, integration testing and functional testing.
• Manage your own time while collaborating with teammates to accomplish project goals
• Participate in all the scrum ceremonies.
• Apply best development practices to write well designed, maintainable, testable, scalable, and secure code.

Essential Knowledge/Experience
• Strong programming skills with deep knowledge of Java(>8 version).
• Strong knowledge in DSA and design patterns.
• Strong knowledge in Cloud/micro-services.
• Strong knowledge on code coverage tools (Sonar) and Application Security tools like Blackduck and Checkmarx.
• Strong knowledge of Spring, Spring boot and other frameworks.
• Strong knowledge on Source Code Management (SCM) or Version Control like Bitbucket, Github
• Good knowledge of unit testing and mocking frameworks like junit, mockito or easymock.
• Good knowledge of SQL and experience working with Oracle.
• Good problem diagnostic and creative problem solving skills.
• Good knowledge on scripting like shell, python, groovy.
• Good knowledge on Observability, Application Performance Monitoring (APM) like Splunk, Dynatrace
• Experience working with high performance applications.
• Experience in working in Agile Methodology.
• Experience using project and program management tools such as Jira, Confluence
• Exposure/ Knowledge in cloud - AWS
• Good knowledge on functional and non-fucntional requirements.
• Experience with Dockers, Kubernetes etc.
• Experience on Build and configuration Tools like Maven, Gradle, Jenkins
• Strong organizational skills; able to manage multiple tasks within the constraints and timelines determined by business needs.


Desirable Skills:

• Experience working with AI Models
• Experience with testing frameworks like Rest Assure, Selenium with web driver etc
• Experience with IBM ILOG/ODM and Pivotal Gemfire Grid.
• Experience with Angular."""


