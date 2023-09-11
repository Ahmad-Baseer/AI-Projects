from huggingface_hub import Repository

repo = Repository("<username>/<repository-name>")
repo.push_to_hub(["aap.py", "model.sav", "requirements.txt"])
