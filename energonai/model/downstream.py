from torch import dtype, nn
from energonai.nn import Classifier1D


class LMHead1D(nn.Module):
    def __init__(self,
                 hidden_size: int,
                 vocab_size: int,
                 word_embedding_weight: nn.Parameter = None,
                 bias: bool = False,
                 dtype: dtype = None) -> None:
        super().__init__()
        self.dense = Classifier1D(hidden_size, vocab_size, word_embedding_weight, bias=bias, dtype=dtype)

    @property
    def weight(self):
        return self.dense.weight

    def forward(self, x):
        x = self.dense(x)
        return x
