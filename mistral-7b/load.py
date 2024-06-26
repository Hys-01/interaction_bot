from huggingface_hub import snapshot_download, login
from pathlib import Path
import os

from transformers import pipeline



#HF_api_key = os.getenv('HF_API_KEY')
#login(token = HF_api_key)

# initial download of model, it will be at C:\Users\[me]\mistral_models
mistral_models_path = Path.home().joinpath('mistral_models', '7B-Instruct-v0.3')
mistral_models_path.mkdir(parents=True, exist_ok=True)

# download select files from repo
snapshot_download(repo_id="mistralai/Mistral-7B-Instruct-v0.3", allow_patterns=["params.json", "consolidated.safetensors", "tokenizer.model.v3"], local_dir=mistral_models_path)


# putting the pipeline call here doesnt make any differece
# login isnt required anymore, since we stored the key somewehere i forgot 



