import os
from transformers import DistilBertTokenizer, DistilBertForTokenClassification
import torch

# Get user input
print("Please enter your medical description:")
text = input()

# Load model and tokenizer
modelname = "YuvarajML/BERTTokenClassification"
tokenizer = DistilBertTokenizer.from_pretrained(modelname)
model = DistilBertForTokenClassification.from_pretrained(modelname)
model.eval()

# Tokenize input
tokenized = tokenizer(text, return_tensors="pt", truncation=True, padding=True, is_split_into_words=False)
tokens = tokenizer.convert_ids_to_tokens(tokenized["input_ids"][0])

# Predict
with torch.no_grad():
    outputs = model(**tokenized)

logits = outputs.logits[0]
predictions = torch.argmax(logits, dim=-1).tolist()

# Label mapping
model.config.id2label = {
    0: "O",
    1: "B-CHEM",
    2: "I-CHEM",
    3: "B-DISE",
    4: "I-DISE",
    5: "B-SYMP",
    6: "I-SYMP"
}
model.config.label2id = {v: k for k, v in model.config.id2label.items()}

# Merge subwords and associate predictions
words = []
current_word = ""
current_label = ""
for tok, pred_id in zip(tokens, predictions):
    if tok in tokenizer.all_special_tokens:
        continue

    label = model.config.id2label.get(pred_id, "O")
    # Merge subwords
    if tok.startswith("##"):
        current_word += tok[2:]
    else:
        if current_word:
            if current_label != "O":
                words.append(f"{current_word}<{current_label}>")
            else:
                words.append(current_word)
        current_word = tok
        current_label = label[2:] if label.startswith("B-") or label.startswith("I-") else "O"

# Append last word
if current_word:
    if current_label != "O":
        words.append(f"{current_word}<{current_label}>")
    else:
        words.append(current_word)

# Output final sentence
print("\nNER Output:\n")
print(" ".join(words))

