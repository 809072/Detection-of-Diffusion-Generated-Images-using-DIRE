import torch

# Check if CUDA (GPU) is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("PyTorch is using GPU")
else:
    device = torch.device("cpu")
    print("PyTorch is using CPU")

# Example tensor creation (replace this with your actual code)
x = torch.rand(3, 3).to(device)

# Print the device on which the tensor is located
print("Tensor is located on:", x.device)

