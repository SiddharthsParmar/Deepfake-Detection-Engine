import torch
from PIL import Image
import torchvision.transforms as transforms
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from model import DeepfakeCNN
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../models/deepfake_model.pth")

model = DeepfakeCNN()
model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))

model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)), transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def detect_deepfake(image_path):
    image = Image.open(image_path).convert("RGB")
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(image)
    return "Real" if output.item() > 0.5 else "Fake"