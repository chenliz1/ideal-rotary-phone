import json
from flask import Flask, request, render_template
from huggingface_hub import InferenceClient

# Load the configuration file
with open("config.json") as config_file:
    config = json.load(config_file)

app = Flask(__name__)

# Initialize Hugging Face InferenceClient
api_key = config["HF_API_KEY"]
client = InferenceClient(api_key=api_key)
model_name = "mistralai/Mixtral-8x7B-Instruct-v0.1"

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    if request.method == "POST":
        question = request.form.get("question")

        if question:
            # Create a message payload for the Hugging Face model
            messages = [
                {
                    "role": "user",
                    "content": question
                }
            ]
            try:
                # Call the Hugging Face API for inference
                completion = client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    max_tokens=500
                )
                response = completion.choices[0].message["content"]
            except Exception as e:
                response = f"Error: {e}"
        else:
            response = "Please enter a question."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
