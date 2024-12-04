import google.generativeai as palm

# Set your API Key
palm.configure(api_key="AIzaSyAMUh1U-sBeQ68B9MWi-6N6PqlMcNiOy1Y")

# List models
models = palm.list_models()
for model in models:
    print(f"Model: {model['name']}, Supported Methods: {model.get('supported_methods', [])}")
