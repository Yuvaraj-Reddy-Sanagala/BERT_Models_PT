import os
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
import torch
import flask

print("Please enter your movie review:")
text = input()

modelname = "YuvarajML/distilbert-finetuned-classification"

tokenizer = DistilBertTokenizer.from_pretrained(modelname)
model = DistilBertForSequenceClassification.from_pretrained(modelname)

model.eval()

tokenized_text = tokenizer(text, return_tensors="pt", truncation=True, padding=True)

with torch.no_grad():
    outputs = model(**tokenized_text)

# Get predicted class
predicted_class = torch.argmax(outputs.logits, dim=1).item()

print("Predicted class:", predicted_class)

label_map = {0: "Negative", 1: "Positive"}
print("Sentiment:", label_map[predicted_class])
