from mlopskit.ext.store import YAMLDataSet
from mlopskit import Model, ModelLibrary, serving
from mlopskit.pastry import HTTPClient
import traceback
import numpy as np
import random

mlops_client = HTTPClient()


class RecomServer(Model):
    CONFIGURATIONS = {"recomserver": {}}

    def _load(self):
        return None

    def _predict(self, items):
        return items


library = ModelLibrary(models=[RecomServer])

model = library.get("recomserver")
serving(
    [RecomServer],
    ["recomserver"],
    {"port": "$port", "workers": "$worker_num"},
)
