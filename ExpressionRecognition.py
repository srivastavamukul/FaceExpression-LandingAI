from PIL import Image
from landingai.predict import Predictor
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
endpoint_id = os.getenv("ENDPOINT_ID")

# Enter your API Key
endpoint_id = endpoint_id
api_key = api_key

predictor = Predictor(endpoint_id, api_key=api_key)

# Load your image
imageDir = os.path.join(os.getcwd(), 'images')

for filename in os.listdir(imageDir):
    filePath = os.path.join(imageDir, filename)
    if os.path.isfile(filePath) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(filePath)

        try:
            # Run inference
            predictions = predictor.predict(image)

            print(f"Results for {filename}")
            for p in predictions:
                label = p.label_name
                score = round(p.score*100, 2)
                print(f"Expression: {label}, Confidence Score: {score}")
        except Exception as e:
            print(f"Failed to process {filename}: {e}")
