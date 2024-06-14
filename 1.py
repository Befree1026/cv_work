import torch
import numpy as np

test = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
x = torch.tensor(test)
print(x)

import torch

print(torch.cuda.is_available())  # 输出为True，则安装无误