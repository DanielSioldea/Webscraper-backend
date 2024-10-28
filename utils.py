# Helper function for processing user responses and categorizing them

def classify_users(responses):
    
    topic_scores = {'technology': 0, 'health': 0, 'business': 0}

    for question_id, response in responses.items():
        topic =  question_id.split('_')[0] 
        topic_scores[topic] += int(response)

    
    # Classify interest level per topic 
    topic_interest = {}
    for topic, score in topic_scores.items():
        if score < 3:
            topic_interest[topic] = 'Low interest'
        elif score <=6:
            topic_interest[topic] = 'Somewhat interested'
        else:
            topic_interest[topic] = 'Very interested'
    return topic_interest