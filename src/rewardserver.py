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
        self.model_db = mlops_client.build_cache_store(
            name="model_name",
            version=3,
            db_name="model_db.db",
            db_type="rlite",
            return_type="dbobj",
        )

    def _predict(self, items):
        return items


library = ModelLibrary(models=[RewardServer])

model = library.get("rewardserver")

serving(
    [RewardServer],
    ["rewardserver"],
    {"port": "$port", "workers": "$worker_num"},
)
