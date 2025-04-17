import os, cv2, torch
from torch.utils.data import Dataset
from PIL import Image
import torchvision.transforms as transforms

class DeepfakeDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images, self.labels = [], []
        for label_dir, label in [("real", 0), ("fake", 1)]:
            full_path = os.path.join(root_dir, label_dir)
            for img in os.listdir(full_path):
                if img.endswith((".jpg", ".png", ".jpeg")):
                    self.images.append(os.path.join(full_path, img))
                    self.labels.append(label)

    def __len__(self): return len(self.images)

    def __getitem__(self, idx):
        image = Image.open(self.images[idx]).convert("RGB")
        if self.transform: image = self.transform(image)
        return image, torch.tensor(self.labels[idx], dtype=torch.float32)

transform = transforms.Compose([
    transforms.Resize((224, 224)), transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
