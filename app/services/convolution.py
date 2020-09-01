import cv2
import torch
from torch import nn
from sklearn.preprocessing import minmax_scale
import numpy as np

def getConv(cv_img, n, k):
	data = torch.Tensor(cv_img)
	data = data.reshape((-1,400,400))
	m = nn.Conv2d(3, n, k)
	output = m(data.unsqueeze(0)).squeeze(0)
	return output.detach().numpy()

def resizeOutput(conv_data, n):
	data = conv_data[n]
	data = cv2.resize(data, (200, 200), interpolation=cv2.INTER_AREA)
	data = minmax_scale(data, feature_range=(0, 255))
	data = np.round(data, 0).astype(np.uint8)
	data = np.stack((data,)*3, axis=-1)
	return data