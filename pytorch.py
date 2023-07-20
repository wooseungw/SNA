import os
import torch
from torch import nn
from torch.utils.data import dataloader
from torchvision import datasets, transforms
import torchvision.models as models

device = ('cuda' if torch.cuda.is_available() else "cpu")

class NeuralNetwork(nn.Module):
    #만들 계층구조 설정
    def __init__(self):
        super(NeuralNetwork,self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28,512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512,10),
        )
    #계층구조 가져와서 사용되는 부분
    def forward(self,x):
        x = self.flatten(x)
        logitic = self.linear_relu_stack(x)
        return logitic



X = torch.rand(1,28,28,device = device)

model = NeuralNetwork().to(device)(X)

x_pred = nn.Softmax(dim=1)(model)
y_pred = x_pred.argmax(1)
print(y_pred)
