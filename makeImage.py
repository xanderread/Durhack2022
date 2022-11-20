import replicate
import webbrowser
import os
os.environ["REPLICATE_API_TOKEN"] = "9ff8bf0bb7d80eac82a4edb4dd3c50db980918bb"

def makeImage(phrase):
    model = replicate.models.get("stability-ai/stable-diffusion")
    output_url = model.predict(prompt=phrase+', without text')[0]
    return output_url