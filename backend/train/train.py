import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from tqdm import tqdm
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model import DeepfakeCNN
from dataset import DeepfakeDataset, transform

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
dataset = DeepfakeDataset(root_dir="../../train", transform=transform)
train_loader = DataLoader(dataset, batch_size=16, shuffle=True)

model = DeepfakeCNN().to(device)
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.BCELoss()

for epoch in range(10):
    model.train()
    total_loss = 0
    for images, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}/10"):
        images, labels = images.to(device), labels.to(device).unsqueeze(1)
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Loss: {total_loss/len(train_loader):.4f}")
print(len(dataset))
torch.save(model.state_dict(), "/models/deepfake_model.pth")

