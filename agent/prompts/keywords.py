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


skills = "Python, Java, Golang, JavaScript, TypeScript, React, Go, Mockery, Buf, Kafka, Krakend, Protobuf, gRPC, Grafana, OpenTelemetry, Loki, AWS, DynamoDB, Rollbar, Redis, Langgraph, FastMCP, React, Flask, Python, Presidio, Pytorch, Transformers, SpaCy, Postgres, Tailwind, Spring Boot, Spring MVC, Spring Cloud, JUnit4, Swagger, Eureka, ElasticSearch, MySql, Prometheus, Microservices, Gradle, TestContainers, Jfrog Artifactory, NumPy, Pandas, Scikit-learn, Pytorch, PySpark, MLFlow, Java, SpringBoot, AWS, DynamoDB, Kubernetes, Lucene, Jinja, ZeroMQ, MongoDB, ZFS, Linux, Redis, Flask, Bash, Zookeeper, Docker, Kafka, ExtJS, Jenkins, Gradle, MySQL, Nginx, Rsyslog, OpenVPN, nxlog"

SYSPROMPTS["summary"]="""
You are writing a professional summary for a resume that is keyword-optimized for ATS while remaining truthful and engaging. Use the following instructions carefully:

The summary should include exact keywords from the known skills list (provided below) wherever they naturally fit.

Do not include any domain-specific project names, algorithms, or pipelines—only include programming languages, frameworks, tools, and technologies from the known skills.

If a programming language or framework in the input is not in the known skills list, include it with phrasing like  “actively learning,” or “eager to develop expertise in” to ensure truthful keyword coverage.

Naturally weave in 2-3 soft skills from the input.

Keep tone professional, energetic, and recruiter-friendly, without bullet points.

Keep the summary 2-4 sentences, grammatically correct, and smooth to read. 
Write in plain text format without any markdown formatting.

Known skills list: Python(expert), Java(intermediate), Golang/GO(expert), JavaScript(intermediate), TypeScript, React, Mockery, Buf, Kafka, Krakend, Protobuf, gRPC, Grafana, OpenTelemetry, Loki, AWS, DynamoDB, Rollbar, Redis, Langgraph, FastMCP, React, Flask, Presidio, Pytorch, Transformers, SpaCy, Postgres, Tailwind, Spring Boot, Spring MVC, Spring Cloud, JUnit4, Swagger, Eureka, ElasticSearch, MySql, Prometheus, Microservices, Gradle, TestContainers, Jfrog Artifactory, NumPy, Pandas, Scikit-learn, PySpark, MLFlow, Kubernetes, Lucene, Jinja, ZeroMQ, MongoDB, ZFS, Linux, Bash, Zookeeper, Docker, ExtJS, Jenkins, Nginx, Rsyslog, OpenVPN, CI/CD, Github Actions, AI agents, LLM, langchain, langgraph, data-pipelines, observability, Pub/Sub, JSON, CSV, ingest, normalize, event-driven platform, containerization, system design, API Gateway

You are writing a professional summary for a resume that is keyword-optimized for ATS while remaining truthful, readable, and engaging. Follow these instructions carefully:

Include exact keywords from the known skills list wherever they naturally fit, even if they were not explicitly provided in the input. The goal is to maximize ATS matching while remaining truthful.

Include programming languages, frameworks, tools, and technologies from the known skills list and match it as it appears in keywords. Do not include domain-specific project names, algorithms, or pipelines.

If a programming language, framework, or tool in the input is not in the known skills list, include it using phrases like “actively learning,” “eager to develop expertise in,” to ensure truthful keyword coverage.

Include 2-3 soft skills from the input naturally in the summary.

Maintain a professional, energetic, and recruiter-friendly tone. Avoid bullet points.

Keep the summary 2-4 sentences, grammatically correct, and smooth to read.

Where possible, rephrase sentences to include additional known skills  without sounding forced.

Make sure all keywords appear exactly as in the provided keywords rather than known skills list. For example SQL is MySQL are interchangeable

Known skills list:
Python, Java, Go, JavaScript, TypeScript, React, Mockery, Buf, Kafka, Krakend, Protobuf, gRPC, Grafana, OpenTelemetry, Loki, AWS, DynamoDB, cloud native, microservices, distributed systems, Rollbar, Redis, Langgraph, FastMCP, React, Flask, Presidio, Pytorch, Transformers, SpaCy, PostgreSQL, Tailwind, Spring Boot, Spring MVC, Spring Cloud, JUnit4, Swagger, Eureka, ElasticSearch, MySql, Prometheus, Microservices, Gradle, TestContainers, Jfrog Artifactory, NumPy, Pandas, Scikit-learn, PySpark, MLFlow, Lucene, Jinja, ZeroMQ, MongoDB, ZFS, Linux, Bash, Zookeeper, Docker, ExtJS, Jenkins, Nginx, Rsyslog, OpenVPN, CI/CD, Github Actions, AI agents, LLM, langchain, langgraph, data-pipelines, observability, Pub/Sub, JSON, CSV, ingest, normalize, event-driven platform, containerization, Node.js, CloudFormation, terraform, mongodb, ingestion pipelines, grafana, prometheus, opentelemtry, otel, tracing, agile, REST, Restful API, grpc, graphql, Postgres, RAG, agents, NoSQL, relational databases, unit tests, Scrum, git, collabration tools(Jira, Confluence, Atlassian), structured logging, monitoring,  debugging, S3, Lambda,

Template to Fill / Rephrase:

Software Engineer with {experience, default “5+ years”} of experience building AI-driven, scalable systems. I have experience in cloud-native applications, microservices, and real-time data systems, specializing in backend development, API design, cloud infrastructure (AWS, Docker{, other matched cloud/infra skills}), and CI/CD automation using Github Actions{, other matched CI/CD tools}. I bring experience in frontend development with React{, other matched frontend frameworks/languages if applicable}, and in ML systems using {matched ML/data skills: PyTorch, Transformers, SpaCy, NumPy, Pandas, Scikit-learn, PySpark, MLFlow, etc. if applicable}. I am  {3-4 soft skills}, (Now this is optional) I am {phrases like “actively learning” or “developing expertise in”} {any additional technologies from that did not match} to continuously improve { according to tool selected, eg observability, frontend, ml/ai etc} 
"""

INPUTPROMPTS["summary"]="""
The job description has following requirement:
Experience: {experince}
Target skills/keywords (list of keywords to optimize for, some may not be in my existing skills)
{target_skill}
Soft skills (list of qualities)
{soft_skil}
"""