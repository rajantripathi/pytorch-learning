import sys
print("Python executable:", sys.executable)
print("Python version:", sys.version)

try:
    import torch
    print("PyTorch version:", torch.__version__)
except ImportError:
    print("PyTorch NOT installed in this environment!")
