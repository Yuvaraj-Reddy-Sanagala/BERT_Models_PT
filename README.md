# 🧠 BERT_Models_PT

This repository provides scripts and notebooks to fine-tune BERT models for both sentence-level classification and token-level tasks such as Named Entity Recognition (NER). It includes sample datasets, preprocessing utilities, training scripts, and evaluation tools using PyTorch and HuggingFace Transformers.

---

## 📁 Project Structure

```
BERT_Models_PT/
├── Bert_finetuned_Model_PT.py              # Main script for fine-tuning
├── Setup_BERT_Models_PT_env.ps1            # PowerShell script for setting up environment
├── FIneTuned_BERT_CLS_Model.ipynb          # Notebook: Sentence-level classification (local)
├── FIneTuned_BERT_CLS_Model_Colab.ipynb    # Notebook: Sentence-level classification (Colab)
├── FineTune_BERT_TokenCLS_Model.ipynb      # Notebook: Token-level NER (local)
├── FineTune_BERT_TokenCLS_Model_Colab.ipynb# Notebook: Token-level NER (Colab)
├── NER_tags_for BERT.ipynb                 # Utility functions for tagging and preprocessing
├── CLS_Dataset.csv                         # Sample dataset for classification
├── TokenCLS_Dataset.csv                    # Token-level dataset
├── TokenCLS_Dataset_with_ner_tags.csv      # Preprocessed dataset with NER tags
├── synthetic_ner_health_data.csv           # Synthetic healthcare NER dataset
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Yuvaraj-Reddy-Sanagala/BERT_Models_PT.git
cd BERT_Models_PT
```

### 2. Set Up the Environment (Windows)

Use the provided PowerShell script:

```powershell
.\Setup_BERT_Models_PT_env.ps1
```

### 3. Activate the Environment

- **Windows**:
  ```powershell
  .\env\Scripts\Activate
  ```

- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

---

## 🚀 How to Use

### 🔧 Script Usage

Run the training script for fine-tuning:

```bash
python Bert_finetuned_Model_PT.py --task cls --train_data CLS_Dataset.csv --model_output ./models/cls_model
```

**Arguments:**

- `--task`: Task type (`cls` for classification, `tokencls` for NER)
- `--train_data`: Path to the training CSV file
- `--model_output`: Output directory for saving the fine-tuned model

---

### 📓 Notebook Usage

You can launch JupyterLab or run notebooks directly on [Google Colab](https://colab.research.google.com):

- `FIneTuned_BERT_CLS_Model.ipynb`: Sentence classification (local)
- `FIneTuned_BERT_CLS_Model_Colab.ipynb`: Sentence classification (Colab)
- `FineTune_BERT_TokenCLS_Model.ipynb`: Token classification / NER (local)
- `FineTune_BERT_TokenCLS_Model_Colab.ipynb`: Token classification / NER (Colab)
- `NER_tags_for BERT.ipynb`: Tagging utilities and preprocessing help

---

## 📊 Included Datasets

- `CLS_Dataset.csv`: Sentences labeled for classification tasks
- `TokenCLS_Dataset.csv`: Tokens and associated tags
- `TokenCLS_Dataset_with_ner_tags.csv`: NER-tagged token dataset
- `synthetic_ner_health_data.csv`: Synthetic dataset for healthcare NER tasks

---

## 🔧 Model Enhancements

- **LoRA-Based Fine-Tuning**: This project includes **Low-Rank Adaptation (LoRA)** for parameter-efficient fine-tuning. LoRA significantly reduces training time and memory usage by updating only a small number of parameters, making the model more lightweight and efficient for downstream tasks.

- **NER Overfitting Note**: Preliminary results indicate that the NER model shows signs of **overfitting** on the training dataset. Future work should include improvements such as better regularization, hyperparameter tuning, or the use of more diverse training data to enhance generalization.

---

## 💡 Tips & Customization

- Replace the default model (`distilbert-base-uncased`) with any other HuggingFace-compatible transformer.
- Adjust hyperparameters like batch size, learning rate, and epochs in both scripts and notebooks.
- Extend tagging functions in `NER_tags_for BERT.ipynb` to suit your domain-specific needs.

---

## 📎 License

This project is licensed under the MIT License.

---

## 🔗 Repository Link

[👉 BERT_Models_PT on GitHub](https://github.com/Yuvaraj-Reddy-Sanagala/BERT_Models_PT)
