import os
import torch
from torch import nn
from torch.utils.data import dataloader
from torchvision import datasets, transforms
import torchvision.models as models

device = ('cuda' if torch.cuda.is_available() else "cpu")

class Regressor(nn.Module):
    def __init__(self, input_dim=768, score_dim=3, hidden_dim=32):
        super(Regressor, self).__init__()
        
        # Feature 부분 (768차원 입력)
        self.mlp_feature = nn.Sequential(
            nn.BatchNorm1d(input_dim),
            nn.Linear(input_dim, hidden_dim * 2),
            nn.ReLU(),
            nn.BatchNorm1d(hidden_dim * 2),
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
        )
        
        
        self.transformer_layer = nn.TransformerEncoderLayer(d_model=hidden_dim, nhead=4, dim_feedforward=hidden_dim*2)
        self.transformer = nn.TransformerEncoder(self.transformer_layer, num_layers=2)

        # Fully Connected Layer
        self.fc = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),
            nn.Linear(hidden_dim // 2, 1)
        )

    def forward(self, x):
        # 입력 x: (batch_size, 771)
        batch_size = x.size(0)

        # 각각 MLP 통과
        x = self.mlp_feature(x).unsqueeze(1)  # (batch_size, 1, hidden_dim)
        # feature_emb = self.mlp_feature(features)  # (batch_size, 1, hidden_dim)
        
        x = self.transformer(x).unsqueeze(1)  # (batch_size, 1, hidden_dim)
        
        # Attention 결과를 FC 통과
        T_pred = self.fc(x.squeeze(1)).squeeze(-1)  # (batch_size,)
        
        return T_pred
    
if __name__ == "__main__":
    import time
    
    # Example usage
    model = Regressor().to(device)
    # print(model)

    # print(model)
    
    # Dummy data
    x = torch.randn(32, 1536).to(device)  # (batch_size, 1536)
    # print(x.shape)
    start_time = time.time()
    output = model(x)
    print("Time taken: ", time.time() - start_time)
    print("Parameter count: ", sum(p.numel() for p in model.parameters() if p.requires_grad))
    print(output.shape)  # Should be (batch_size,)