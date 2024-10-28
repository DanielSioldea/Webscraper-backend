# Interest Classifier Based on Webscraper Data

## This application takes a website URL as an input, scraping its contents for relevant keywords on related topics (currently: Technology, health, and business topics). Once the keywords are scraped a list of 5 questions is generated based on the topics. The user is presented with 3 options for answsers, and then a classification is made on how interested the user is with the related topics
### Currently this is only the backend code for this project. To run this code as is please follow the steps below:

1. Install and open HTTPie Desktop: https://httpie.io/
2. Clone the repository: >git clone https://github.com/DanielSioldea/Webscraper-backend
3. Install requirements: >pip install -r requirements.txt
4. Install spaCy's NLP module: >python -m spacy download en_core_web_sm
5. Start the Flask server: >python app.py
6. In HTTPie desktop change the dropdown before the URL to: POST
7. Add a JSON text file to the Body tab containing your website URL: >{"url: "https://www.example.com"}
8. Paste the server URL into the URL bar, followed by /scrape-content: >http://127.0.0.1:5000/scrape-content
9. Press send and observe results
