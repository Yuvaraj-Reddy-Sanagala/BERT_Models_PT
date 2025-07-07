# Create virtual environment
python -m venv BERT_Models_PT_env

# Activate it
.\BERT_Models_PT_env\Scripts\Activate.ps1

# Install required packages
pip install ipykernel
pip install transformers datasets accelerate scikit-learn seqeval pandas matplotlib seaborn flask nltk spacy scispacy
pip install torch --index-url https://download.pytorch.org/whl/cu118
pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.4/en_ner_bc5cdr_md-0.5.4.tar.gz

# Register kernel for Jupyter
python -m ipykernel install --user --name=bert-pt --display-name "BERT_Models_PT"

#Installing required models for the NER tagging
python -m spacy download en_core_web_sm

