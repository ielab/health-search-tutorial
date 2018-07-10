# The Health Search Tutorial

Welcome to the homepage for The Health Search Tutorial - a full day on all things Information Retrieval for the Health domain.

Quick links:
* SIGIR 2018 [tutorial slides](https://github.com/ielab/health-search-tutorial/tree/master/slides)
* SIGIR 2018 [hands-on worksheet](https://github.com/ielab/health-search-tutorial/tree/master/hands-on)

## Intended Audience

Researchers of all levels seeking to understand the challenges, tasks and recent developments in information retrieval related to health, be it consumer-oriented search, clinician search, or biomedical search.

No prior knowledge in health search is required, making this tutorial ideal for those unfamiliar with this domain. 

The tutorial is also suitable for those familiar with health search as they will acquire insights from hands-on sessions. 

The tutorial will also provide an analysis of the successes and failures of current techniques, and an outline of the opportunities for IR research in the health domain.

## Motivation & Overview

With modern medicine increasingly reliant on information technology, the demand for IR systems that search medical content has grown significantly. The increasing need to retrieve medical advice (by both consumers and clinicians), and the adoption of electronic medical records are two factors driving the demand for health search. IR research has much to offer here by developing new tools and techniques specific to this domain.

The range of health information available - from electronic medical records, to medical literature, to health advice on the web - all leads to complex requirements that often require novel solutions to these different problems.

The key challenge in health search is how to bridge the *sematic gap*: the mismatch between the raw data and the way a human being interprets it. Although particularly prevalent in health search, the semantic gap problem is found in all domains; advances in health search can thus advance the whole field. 

Key challenges include:

* How to leverage semantics and domain-knowledge resources for a better representation of documents and information need.
* What characterises relevance, in particular how topicality is complemented by other dimensions of relevance (understandability, authoritativeness, etc.).
* How bias and time pressure affects perception of relevance and decisions.
* How these influences the search process and evaluation.

## Objectives of the Tutorial

The main aims of HS2018 will be to:

* Summarise the basics of search in the health domain;
* Present the different end user requirements for multiple user groups interested in health search, including tasks;
* Provide an overview of the current use of IR techniques in the health domain;
* Provide a hands-on introduction to domain-specific tools which can be exploited in health search;
* Present resources and campaigns for evaluation in health search, including novel evaluation approaches;
* Present challenges and opportunities for further research in the health domain and discuss how these could be met. 

This knowledge will allow IR researchers to identify promising ways of applying their work to the health domain, allowing them to contribute to a domain of rapidly growing importance.


## Format and Schedule

### Session 1: Background & Theory

#### Introduction to the health domain and to the tutorial

The tutorial begins with an introduction to IR in health, giving an overview of the topics that will be covered in the tutorial and why they are important.

*Duration: 15m*

#### Types of health information

Health information comes in a myriad of forms.  is section covers the characteristics of di erent types of health information sources important for health search.  ese range from patient-based information (e.g., electronic health records), knowledge-based information (e.g., scienti c papers), through to consumer-based information (e.g., patient forums on the web). Also included are sources of domain knowledge such as medical ontologies, terminologies and classi cation systems, all of which are playing an increasingly important role in state-of-the-art IR systems.

*Duration: 30m*

#### End users and tasks
An analysis of the end user (from consumer to clinician) characteristics and tasks in health search is presented. Some groups of end users are addressed, and the information needs and search tasks they undertake are described. For example, the group of ``physicians'' can be divided into groups ranging from general practitioners operating from individual practices who require practice-oriented secondary literature, through specialists in a medical domain who wish to access more specialised works in this domain, to research physicians who have an interest in the primary literature. 

*Duration: 45m*


### Session 2: Techniques and methods

#### Methods in health search

This section covers the state-of-the-art in health search, summarising the most important research methods and results in this area with respect to the different tasks discussed in the previous session and highlighting common trends across tasks. 
 
This session will cover methods across different health search tasks, including: query expansion and reformulation, use of domain knowledge and inference mechanisms, learning to rank and other learning methods, task-based information, and specifically handling clinical text. We provide examples of health search systems already in use and lessons that can be drawn from their use.


*Duration: 90m*

### Session 3: Practical

#### Use of clinical NLP tools for medical IR: Hands-on session on tools for medical IR

The clinical informatics and clinical natural language processing community have developed a number of tools for extracting clinical information free text. For example, statistical and dictionary-based named entity recognition systems have been developed to identify medical entities; algorithms have been developed to extract associations, relationships and contexts and to enhance textual content with semantic information.

This part of the tutorial presents an overview of such techniques, providing a hands-on demonstration of how these tools work. In addition, the tutorial provides an outlook at how these tools have been used in the literature or can be integrated to enhance information representation and the whole information retrieval process.

**All details for the hands on session are at:**

[https://github.com/ielab/health-search-tutorial/tree/master/hands-on](https://github.com/ielab/health-search-tutorial/tree/master/hands-on).


*Duration: 90m*

### Session 4: Evaluation and future directions

#### Evaluation

The tasks and challenges in evaluating health search are covered in this section. Evaluation that considers multiple dimensions of relevance (topicality, reliability, understandability, bias) is presented.  We touch on new frameworks to evaluate systems based on task completion rather than relevance. Evaluation campaigns and resources in this domain are presented, including TREC Medical Records Track, TREC Clinical Decision Support Track, CLEF eHealth (consumer health search and as of 2018 search systems for the compilation of systematic reviews), i2b2 Shared Task Challenges, ALTA Shared Task (Query-based summarisation for evidence-based medicine), clinical trial retrieval, and the use of ICD coded data as an automated relevance judgement mechanism.


*Duration: 50m*

#### Open challenges for health search and conclusions (including discussion)

There are many open problems in health search which are fertile ground for information retrieval (IR) research. Examples include: 

* searching for "similar" anonymised patient records or "similar" medical images within a hospital to assist in diagnosis or treatment; 
* linking treatment guidelines to patient records based on their content; 
* searching within a patient record to obtain an overview of someones medical history. This part of the tutorial briefly presents some of the areas of medicine and consumer-health experience that have a potential to be improved through the use of IR techniques, leading to a discussion with the participants on meeting these challenges.

*Duration: 40m*

## Presenters Bios

### Guido Zuccon

Guido is a lecturer within the School of Electrical Engineering and Computing Science at the Queensland University of Technology. His research interests include formal models of search and evaluation methods, in particular applied to health search. 
Guido has actively contributed to the areas of document ranking, search result diversification, formal models, and evaluation. Guido is the IR Task leader for the CLEF eHealth Evaluation Lab, a shared-task that aims to evaluate systems for consumer health search. He has already presented tutorials at SIGIR 2015, CIKM 2016 and ICTIR 2016 on formal models of search.

Guido received a Ph.D. in Computing Science from the University of Glasgow in 2012. Before joining the Queensland University of Technology as a lecturer in 2014, he was a postdoctoral research fellow at the CSIRO, Australia, working on health search technology at intersection of academic research and applied research with real customers.

### Bevan Koopman
Bevan is a Research Scientist at the Australian e-Health Research Centre, part of the Commonwealth Science and Industrial Research Organisation (CSIRO), based in Brisbane, Australia. He leads projects dedicated to health search, that is the research and development of novel search engine technology to improve access, retrieval and analysis of different health data. He is working on search engines for electronic patient records and search engines for evidence-based medicine. This work is done at intersection of academic research and applied research with real customers. 

He received a PhD from the Queensland University of Technology in 2014 with a thesis titled *Semantic search as inference: applications in health informatics* and holds a visiting researcher position at that university. He also spent a number of years in industry and will therefore provide both an academic and commercial expertise to this tutorial.


## Type of support materials to be supplied to attendees

The tutorial will include:

* Slides and the corresponding hand-outs
* An annotated bibliography of important works in health search
* A virtual machine distribution and/or Git repository containing software and example programs that will be demonstrated in the hands-on session.
