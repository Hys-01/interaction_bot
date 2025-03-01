import torch
print(f"CUDA available: {torch.cuda.is_available()}")  
print(f"Device: {torch.cuda.get_device_name(0)}")  

'''
CUDA available: True
Device: NVIDIA GeForce RTX 2070 SUPER
'''
