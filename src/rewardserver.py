from mlopskit.ext.store import YAMLDataSet
from mlopskit import Model, ModelLibrary, serving, make
from mlopskit.log_base import create_log_path

import traceback
import numpy as np
import json
import os


class RewardServer(Model):
    CONFIGURATIONS = {"rewardserver": {}}

    def _load(self):
        self.reward_logs_path = create_log_path("model_name", "reward_errors")
        self.reward_logs_debug = create_log_path("model_name", "reward_debugs")
        self.debug_db = make("cache/feature_store-v1", db_name="debug_tests.db")

        self.model_db = make("cache/model_name-v1", db_name="model.db")

    def _predict(self, items):
        uid = items.get("uid")
        request_id = items.get("request_id")
        try:
            model_name = "model_name"
            debug_key = f"{model_name}:debug"
            debug_param = self.debug_db.get(debug_key)

            # 检查是否设置了调试参数
            if debug_param == "1":
                debug_log_file = os.path.join(
                    self.reward_logs_debug, f"{request_id}_params.txt"
                )
                # 将请求参数写入调试日志文件
                with open(debug_log_file, "w") as f:
                    f.write(json.dumps(items))
            return items
        except:
            # 将异常堆栈信息写入错误日志文件
            log_file = os.path.join(self.reward_logs_path, f"{request_id}_error.txt")
            with open(log_file, "w") as f:
                f.write(str(traceback.format_exc()))

            return items


library = ModelLibrary(models=[RewardServer])

model = library.get("rewardserver")
