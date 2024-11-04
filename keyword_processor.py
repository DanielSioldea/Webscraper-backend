# This module processes the scraped content and extracts keywords, generates questions, and categorizes topics.

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
import random
from questions import topics

# Load the spaCy English language model
processor = spacy.load('en_core_web_sm')

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
    return random.sample(questions, min(10, len(questions)))