from transformers import pipeline

def load_model():
    # Load the text-generation model (you can replace 'gpt2' with your own model if necessary)
    model = pipeline("text-generation", model="gpt2")
    print("Model loaded successfully")
    return model

def generate_playbook(data, model):
    # Extract necessary fields from data
    description = data.get("description")
    severity = data.get("severity")

    # Construct the prompt using the description and severity
    prompt = f"Generate a playbook for an incident with description: {description} and severity: {severity}"

    # Call the model to generate the text based on the prompt
    response = model(prompt, max_length=200, num_return_sequences=1)
    
    # Return the generated text
    return response[0]['generated_text']
