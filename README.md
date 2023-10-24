# NLP-Project
Team Project for Natural Language Processing
---
### Link to Presentation
https://www.canva.com/design/DAFyGuVUN5I/sN2GX_yOhQ40j9Y2Axkm1Q/edit?utm_content=DAFyGuVUN5I&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
---
### Initial Goals
- Can we accurately determine the primary coding language used based on only the test in a github readme?
- Do those key words change when looking at different languages?
---
### Findings
- Words like 'api', and 'data' appear more often when the primary language is Python
- Java and Typescript both have 'use' frequently
- C has has heavy usage of the word 'component'
---
### Next Steps
- Perform further ngram analysis to determine if pairings of words further affect predictive strength
- Apply analysis to more repositories to validate model accuracy
---
## Project Description
### Utilizing classification machine learning algorithms and natural language processing in order to predict programming language using 101 readme files from Github repositories. This project contains acquisition through web scraping using Python, preparation in order to explore, exploratory analysis of the data, statistical testing of categorical variables, and classification modeling to predict language.
---
## Project Goals
- Predict programming language
- Apply natural language processing techniques to wrangle and explore data
---
## Initial Hypotheses
- Our initial assumption is that we would not be able to predict language based off of natural language from readme files with high accuracy.
- We thought different readme authors would write in unique enough ways to waive any similarities across files.
---
## Data Dictionary
| Feature | Definition | 
| :- | :- |
| Title | Name of github repository readme was pulled from |
| Readme | Content of readme pulled |
| Lemmatized | Cleaned content of readme |
| <font color='red'>Language</font> | The Primary language used in readme to be predicted |
| Encoded columns | Each column indicates if a readme either omits a word (0), or contains it (1) |
---
## Steps to Reproduce
- Clone the repository
- Use the wrangle file to acquire and cache the data
- Reproduce code in project notebook for final results
