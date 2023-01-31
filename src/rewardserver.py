from banditrl.bandit import usermodel
from mlopskit.ext.store import YAMLDataSet
from mlopskit import Model, ModelLibrary, serving
from mlopskit.pastry import HTTPClient
import traceback
import numpy as np
import pickle

mlops_client = HTTPClient()


class RewardServer(Model):
    CONFIGURATIONS = {"rewardserver": {}}

    def _load(self):
        return None

    def _predict(self, items):
        return items


library = ModelLibrary(models=[RewardServer])

model = library.get("rewardserver")

serving(
    [RewardServer],
    ["rewardserver"],
    {"port": "$port", "workers": "$worker_num"},
)
