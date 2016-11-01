# Project: *BigBook*
*by Team Goodnight Moon*

#### Team Members
- Clayton Petty
- Dalton Harris  
- Chris Foy
- Wes Moncrief

#### Project Goal
To create a tool for aggregating and presenting focused, directed, and relevant information to end users, people, customers, and clients, and the world.

### What is the need? Who wants or benefits?
Scenario, picture this: You're a college student. You have a final tomorrow. You have not once attended class. You are not familiar with your professors name. You visit TAMU's Howdy portal and find the course name and syllabus. At this point, you need to learn all of the relevant information from the entire semester. Good thing there's *BigBook*. You quickly and efficiently upload said syllabus into *BigBook* via *BigBook's* friendly and intuitive UI/UX. BigBook performs analysis on said syllabus and outputs a BigBook of the length of your choosing containing all of the information needed to pass said course. Boom, you graduate.

**** BigBook is not responsible for any failed semesters.   
We avidly and vigorously support the following motto as our 4.0 and Go Tutor once said:
***You can always retake a class, but you can never relive a party.***

In Layman's terms, the purpose of this project is to identify and aggregate related information requested by a client and present it in a helpful format.

### What data (or datasets)?
*BigBook* will take advantage of Wikipedia's vast quantity of knowledge, facts, and truths. All 14 gigabytes. As a stretch goal, it will also incorporate additional sources of knowledge, i.e. news, research, etc.

### What is your "data science" toolkit? You should list specific tools / packages you will use.
In order to identify, categorize, and present information, the following tools will be integrated into *BigBook*:  
- LDA analysis
    - This will allow *BigBook* to identify related topics
- Web Scraping analysis of Wikipedia link structure
    - This will allow *BigBook* to further identify related topics and access them
- Keyword extraction algorithms to identify important topics
- Graph-based ranking models to identify key sentences and information and Extraction-based summarization
    - This will allow for the summarization and aggregation of information that will be included in the requested *BigBook*
- Actual tools we know we might use:
    - Scrapy
    - LDA implementation

### Incremental Steps to Completion
1. Given a word, find related topics
    - via LDA, web scraping, etc.
2. Given a topic, find related articles
3. Given an article, summarize article appropriately
4. Aggregate summarized articles, and output result
5. Add fine-tuning aspects for clients
6. Build out web application to support above processes
7. Allow for more complicated inputs (entire documents instead of a single topic)

### Preliminary sketch of what you hope to find.
What we hope to produce is a product that can do the following:
- Input a topic or series of topics
- Output a useful and relevant summarization of all related information
    - Allow user to fine-tune content of *BigBook*
        - Length of *BigBook*
        - Type of information included
            - News, history, usage, etc.
        - Obscurity levels/depth of information
        - Language of resulting *BigBook*
