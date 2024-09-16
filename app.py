from transformers import pipeline

classifier = pipeline('sentiment-analysis')

def classify(text):
    return classifier(text)

if __name__ == "__main__":
    result = classify("I love working on machine learning projects!")
    print(result)
