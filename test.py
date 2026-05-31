import subprocess
import torch

from model import SimpleNet

# Run shell script
subprocess.run(
    ["bash", "setup.sh"],
    check=True
)

# Create model
model = SimpleNet()

# Example inference
x = torch.randn(1, 10)

with torch.no_grad():
    y = model(x)

print(y)
