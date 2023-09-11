from huggingface_hub import Repository

repo = Repository("AhmadHashim/Student-Score-Prediction")  
repo.push_to_hub(["aap.py", "model.sav", "requirements.txt"])
