# Create virtual environment
python -m venv BERT_Models_PT_env

# Activate it
.\BERT_Models_PT_env\Scripts\Activate.ps1

# Install required packages
pip install ipykernel
pip install torch transformers datasets scikit-learn seqeval pandas matplotlib seaborn flask

# Register kernel for Jupyter
python -m ipykernel install --user --name=bert-pt --display-name "BERT_Models_PT"