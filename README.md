# BERT_Models_PT

This repository provides scripts and notebooks for fine-tuning BERT models for both sentence-level classification and token-level tasks like Named Entity Recognition (NER). It includes sample datasets, preprocessing code, and utilities for training and evaluation.

## 📂 Project Structure

```
BERT_Models_PT/
├── Bert_finetuned_Model_PT.py
├── Setup_BERT_Models_PT_env.ps1
├── FIneTuned_BERT_CLS_Model.ipynb
├── FIneTuned_BERT_CLS_Model_Colab.ipynb
├── FineTune_BERT_TokenCLS_Model.ipynb
├── FineTune_BERT_TokenCLS_Model_Colab.ipynb
├── NER_tags_for BERT.ipynb
├── CLS_Dataset.csv
├── TokenCLS_Dataset.csv
├── TokenCLS_Dataset_with_ner_tags.csv
├── synthetic_ner_health_data.csv
└── .gitignore
```

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Yuvaraj-Reddy-Sanagala/BERT_Models_PT.git
cd BERT_Models_PT
```

### 2. Set Up the Environment

Use the PowerShell script to set up a virtual environment and install dependencies:

```powershell
.\Setup_BERT_Models_PT_env.ps1
```

### 3. Activate Environment

- Windows:

```powershell
.env\Scripts\Activate
```

- macOS/Linux:

```bash
source venv/bin/activate
```

## 🧠 Usage

### Run Script for Fine-Tuning

```bash
python Bert_finetuned_Model_PT.py --task cls --train_data CLS_Dataset.csv --model_output ./models/cls_model
```

Supported arguments:

- `--task`: Task type (`cls` for classification, `tokencls` for NER)
- `--train_data`: Path to training CSV
- `--model_output`: Output directory to save the model

### Use Notebooks

Launch JupyterLab or use Google Colab to run the provided `.ipynb` notebooks:

- `FineTuned_BERT_CLS_Model.ipynb` — Sentence classification
- `FineTune_BERT_TokenCLS_Model.ipynb` — Token-level NER
- `NER_tags_for BERT.ipynb` — Helper functions for tagging and preprocessing

## 📊 Sample Datasets

This repo includes example CSVs:

- `CLS_Dataset.csv`: Sentences with class labels
- `TokenCLS_Dataset.csv`: Tokens with corresponding tags
- `synthetic_ner_health_data.csv`: Synthetic health-related NER dataset

## 💡 Tips

- You can replace the pretrained model (`distilbert-base-uncased`) with any HuggingFace transformer.
- Customize hyperparameters like batch size, learning rate, and epochs in the notebooks or script.

