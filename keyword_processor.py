# This module processes the scraped content and extracts keywords, generates questions, and categorizes topics.

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import random

# Load the spaCy English language model
processor = spacy.load('en_core_web_sm')

topics = {
    "technology": {
        "keywords": ["AI", "machine learning", "software", "technology", "computing"],
        "questions": [
            {"question": "How interested are you in AI advancements?", "options": ["Not interested", "Somewhat interested", "Very interested"]},
            {"question": "How likely are you to follow news about software development?", "options": ["Not likely", "Somewhat likely", "Very likely"]},
            {"question": "How much do you follow trends in computing?", "options": ["Not at all", "Occasionally", "Often"]}
            ]
        },
    "health": {
        "keywords": ["health", "medicine", "wellness", "fitness", "nutrition"],
        "questions": [
            {"question": "How often do you read about health topics?", "options": ["Rarely", "Sometimes", "Frequently"]},
            {"question": "How interested are you in fitness and wellness?", "options": ["Not interested", "Somewhat interested", "Very interested"]},
            {"question": "How likely are you to explore new nutrition trends?", "options": ["Not likely", "Somewhat likely", "Very likely"]}
            ]
        },
    "business": {
        "keywords": ["finance", "business", "economics", "marketing", "sales"],
        "questions": [
            {"question": "How interested are you in business trends?", "options": ["Not interested", "Somewhat interested", "Very interested"]},
            {"question": "Do you keep up with financial news?", "options": ["No", "Sometimes", "Yes"]},
            {"question": "How much do you read about marketing and sales strategies?", "options": ["Rarely", "Occasionally", "Often"]}
            ]
        }
    }

# Define a function to extract keywords from the text
def extract_keywords(text):
    # Process the text using spaCy
    doc = processor(text)    

    # Extract noun chunks as keywords
    keywords = [chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text.split()) > 1] 
    return keywords

# Function to categorize topics based on keywords
def categorize_topics(keywords):
    # Define a list of topics and their keywords

    topic_scores = {topic: 0 for topic in topics}
    for topic, data in topics.items():
        if any(keyword in data["keywords"] for keyword in keywords):
            topic_scores[topic] += 1
    return topic_scores if any(topic_scores.values()) else ["Other"]

# Function to generate questions based on keywords
def generate_questions(topic_scores):

    # Initialize an empty list to store the generated questions
    questions = []

    for topic, score in topic_scores.items():
        if score > 0:
            questions.extend(topics[topic]["questions"])
    return random.sample(questions, min(5, len(questions)))