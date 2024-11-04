from flask import Flask, request, jsonify
from scraper import scrape
from keyword_processor import extract_keywords, categorize_topics, generate_questions
from utils import classify_users

app = Flask(__name__)

@app.route('/scrape-content', methods=['POST'])
def scrape_content():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    content = scrape(url)
    if content is None:
        return jsonify({'error': 'Error scraping content'}), 500
    
    keywords = extract_keywords(content)
    topic_scores = categorize_topics(keywords)
    return jsonify({'keywords': keywords[:10], 'topics': topic_scores})

@app.route('/generate-questions', methods=['POST'])
def generate_questions_route():
    data = request.get_json()
    topic_scores = data.get('topics')
    
    if not topic_scores:
        return jsonify({'error': 'Topic scores are required'}), 400
    
    questions = generate_questions(topic_scores)
    return jsonify({'questions': questions})

@app.route('/classify-interest', methods=['POST'])
def classify_interest():
    data = request.get_json()
    responses = data['responses']

    if not responses:
        return jsonify({'error': 'Responses are required'}), 400
    
    classification = classify_users(responses)
    return jsonify({'classification': classification})

if __name__ == '__main__':
    app.run(debug=True)
