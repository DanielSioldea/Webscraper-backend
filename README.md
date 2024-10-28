# Interest Classifier Based on Webscraper Data

## This application takes a website URL as an input, scraping its contents for relevant keywords on related topics (currently: Technology, health, and business topics). Once the keywords are scraped a list of 5 questions is generated based on the topics. The user is presented with 3 options for answsers, and then a classification is made on how interested the user is with the related topics
### Currently this is only the backend code for this project. To run this code as is please follow the steps below:

1. Install and open HTTPie Desktop: https://httpie.io/
2. Clone the repository:
```
git clone https://github.com/DanielSioldea/Webscraper-backend
```
4. Install requirements:
```
pip install -r requirements.txt
```
5. Install spaCy's NLP module:
```
python -m spacy download en_core_web_sm
```
6. Start the Flask server:
```
python app.py
```
7. In HTTPie desktop change the dropdown before the URL to: POST
8. Add a JSON text file to the Body tab containing your website URL:
```
{
"url": "https://www.example.com"
}
```
9. Paste the server URL into the URL bar, followed by /scrape-content:
```
http://127.0.0.1:5000/scrape-content
```
10. Press send and observe results
11. In the same tab or a new one, change the URL to include: /generate-questions:
```
http://127.0.0.1:5000/generate-questions
```
12. Create another JSON text file in the Body and populate it with the topics that were scraped as follows:
```
{
  "topics": {"technology": X, "business": Y, "health": Z}
}
```
13. Press send and view the questions and possible responses
14. Follow the same steps changing the URL to include: /classify-interest:
```
http://127.0.0.1:5000/classify-interest
```
15. Create another JSON text file and populate it with the following format:
```
{
"responses":
  {"technology_1": "#",
  "technology_2": "#",
  "technology_n": "#",
  "business_1": "#",
  .....}
}
```
16. Press send and observe classification results
