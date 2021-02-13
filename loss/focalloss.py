import torch
from torch import nn
import torch.nn.functional as F

from fastai.vision.all import *

class FocalLoss(nn.Module):
    def __init__(self, alpha=0.5, gamma=1.):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma

    def forward(self, inputs, targets, **kwargs):
        CEloss = nn.CrossEntropyLoss(reduction='none')(inputs, targets)
        pt = torch.exp(-CEloss)
        Floss = self.alpha * ((1-pt)**self.gamma) * CEloss
        return Floss.mean()

class FocalLossFlat(BaseLoss):
    @use_kwargs_dict(keep=True, weight=None, ignore_index=-100, reduction='mean')
    def __init__(self, *args, axis=-1, **kwargs): super().__init__(FocalLoss, *args, axis=axis, **kwargs)
    def decodes(self, x):    return x.argmax(dim=self.axis)
    def activation(self, x): return F.softmax(x, dim=self.axis)
