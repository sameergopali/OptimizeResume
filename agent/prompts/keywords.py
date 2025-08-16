SYSPROMPTS = {}
INPUTPROMPTS={}

SYSPROMPTS["keyword"]="""You are an expert HR analyst. Your task is to carefully analyze the job description text provided below and extract keywords for years of experience, list of technical skills and soft skills.
Instructions:
Identify Years of experience: Include the only the numbers and the relevant symbol/word representing years
Identify Technical Keywords: These include programming languages, software, tools, platforms, frameworks, methodologies (like Agile or Scrum), and specific technical processes.
Identify Soft Skills Keywords: These are interpersonal abilities, character traits, communication styles, and work habits (e.g., communication, teamwork, problem-solving, detail-oriented).
Extract Exactly: Pull the kOutput should be in json format in format. The keys should be named experience, technical, and softskilleywords exactly as they appear in the text. Do not rephrase, shorten, or change them in any way.
Format:{format}
"""


skills = "Python, Java, Golang, JavaScript, TypeScript, React, Go, Mockery, Buf, Kafka, Krakend, Protobuf, gRPC, Grafana, OpenTelemetry, AWS,  Redis,  FastMCP, React, Flask, Python, Presidio, Pytorch, Transformers, SpaCy, Postgres, Tailwind, Spring Boot, Spring MVC, Spring Cloud, JUnit4, Swagger, Eureka, ElasticSearch, MySql, Prometheus, Microservices, NumPy, Pandas, Scikit-learn, Pytorch, MLFlow, Java, SpringBoot, AWS, DynamoDB, Kubernetes, Lucene, Jinja, ZeroMQ, MongoDB, Linux, Redis, Flask, Bash, Zookeeper, Docker, Kafka, MySQL, Nginx, Rsyslog, OpenVPN, nxlog"

SYSPROMPTS["summary"]="""
You are writing a professional summary for a resume that is keyword-optimized for ATS while remaining truthful and engaging. Use the following instructions carefully:
Identify the technical and soft skills keywords that are important for job descripton in the input.
Use the exact keywords for technical and soft skills from the input list wherever they match the skill from the known  list. 
If a synonym or variation appears in input, use the exact keyword from the input to maximize ATS matching, while keeping the text accurate and natural.
Do not include any domain-specific names, algorithms from the input. 
If any critical skills like programming language, framework, or tool in the input is not in the known skills list, include it using phrases like “actively learning,” “eager to develop expertise in,” to ensure truthful keyword coverage.
Keep tone professional, energetic, and recruiter-friendly, without bullet points.
Nautrally weave soft skills from the input in the summary, without forcing them.
Make sure all keywords appear exactly as in the provided input description rather than known skills list, and fit it in naturally. 
Maintain a professional, energetic, and recruiter-friendly tone. Avoid bullet points.
Write as plain text format, DO NOT use markdown syntax.
Keep the summary 2-4 sentences, grammatically correct, and smooth to read.
Where possible, rephrase sentences to include additional known skills  without sounding forced.

Known skills list: Python(expert), Java(intermediate), Golang/GO(expert), JavaScript(intermediate), TypeScript, React, Mockery, Buf, Kafka, Krakend, Protobuf, gRPC, Grafana, OpenTelemetry, Loki, AWS, DynamoDB, Rollbar, Redis, Langgraph, FastMCP, React, Flask, Presidio, Pytorch, Transformers, SpaCy, Postgres, Tailwind, Spring Boot, Spring MVC, Spring Cloud, JUnit4, Swagger, Node.js, Eureka, ElasticSearch, MySql, Prometheus, Microservices, Gradle, TestContainers, Jfrog Artifactory, NumPy, Pandas, Scikit-learn, PySpark, MLFlow, Kubernetes, Lucene, Jinja, ZeroMQ, MongoDB, ZFS, Linux, Bash, Zookeeper, Docker, ExtJS, Jenkins, Nginx, Rsyslog, OpenVPN, CI/CD, Github Actions, AI agents, LLM, langchain, langgraph, data-pipelines, observability, ingest, normalize, containerization, system design, event-driven, Agile, Jira, Confluence


Template to Fill / Rephrase:

Software Engineer(change to full stack or backend or senior according to input description ) with {match required experience in the input list, default and max upto “5+ years”, don't use range like(1-3)} of experience building AI-driven, scalable systems. I have experience in cloud-native applications, microservices, and real-time data systems, specializing in backend development, API design, cloud infrastructure (AWS, Docker{, other matched cloud/infra skills}), and CI/CD automation using Github Actions{, other matched CI/CD tools}. I bring experience in frontend development with React{, other matched frontend frameworks/languages if applicable}, and in ML systems using {matched ML/data skills: PyTorch, Transformers, SpaCy, NumPy, Pandas, Scikit-learn, PySpark, MLFlow, etc. if applicable}. I am  {3-4 soft skills}, (Now this is optional) I am {phrases like “actively learning” or “developing expertise in”} {any additional technologies from that did not match} to continuously improve { according to tool selected, eg observability, frontend, ml/ai etc} 
"""

INPUTPROMPTS["summary"]="""
The job description has following requirement:
Experience: {experince}
Target skills/keywords (list of keywords to optimize for, some may not be in my existing skills)
{target_skill}
Soft skills (list of qualities)
{soft_skil}
"""