from mlopskit.ext.store import YAMLDataSet
from mlopskit import Model, ModelLibrary, serving, make
from mlopskit.log_base import create_log_path

import traceback
import numpy as np
import pickle


class RewardServer(Model):
    CONFIGURATIONS = {"rewardserver": {}}

    def _load(self):
        self.reward_logs_path = create_log_path("model_name", "reward_errors")
        self.model_db = make("cache/model_name-v1", db_name="model.db")

    def _predict(self, items):
        return items


library = ModelLibrary(models=[RewardServer])

model = library.get("rewardserver")

serving(
    [RewardServer],
    ["rewardserver"],
    {"port": "$port", "workers": "$worker_num"},
)
