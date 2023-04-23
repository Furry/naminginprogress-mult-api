# Import flask
from flask import Flask, request
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast, pipeline

import numpy as np
import pathlib as pl
import os

# Create an app
app = Flask(__name__)

ValidLabels = [
    "humiliate",
    "dehumanize",
    "violence",
    "genocide",
    "hatespeech",
    "normal"
]

file = pl.Path(__file__).parent.joinpath("hatespeechModel")
print(file)
model = DistilBertForSequenceClassification.from_pretrained(file)
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")

# Create a post route to receive raw text body
@app.route('/vulgarity', methods=['POST'])
def vulgarity():
    # Get the body of the request
    body = request.get_data(as_text=True)

    fill = pipeline("text-classification", model = model, tokenizer = tokenizer)

    result = fill(body)
    label = ValidLabels[int(result[0]["label"][-1:])]

    print(result)
    return {
        "label": label,
        "score": result[0]["score"]
    }

# Listen on port 8081
if __name__ == '__main__':
    # Use the port that's passed in from the command line
    port = int(os.environ.get('PORT', 8081))
    app.run(host='0.0.0.0', port=port, debug=False)