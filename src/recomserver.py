from mlopskit.ext.store import YAMLDataSet
from mlopskit import Model, ModelLibrary, serving, make
from mlopskit.log_base import create_log_path

import traceback
import numpy as np
import random


class RecomServer(Model):
    CONFIGURATIONS = {"recomserver": {}}

    def _load(self):
        self.reocm_logs_path = create_log_path("model_name", "recom_errors")
        self.model_db = make("cache/model_name-v1", db_name="model.db")

    def _predict(self, items):
        return items


library = ModelLibrary(models=[RecomServer])

model = library.get("recomserver")
serving(
    [RecomServer],
    ["recomserver"],
    {"port": "$port", "workers": "$worker_num"},
)
