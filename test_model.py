from transformers import pipeline

def test_classification():
    classifier = pipeline('sentiment-analysis')
    result = classifier("I love this project!")
    assert result[0]['label'] == 'POSITIVE'
