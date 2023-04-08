# 標準ライブラリ
import logging
import os
from datetime import datetime


def setup_logger(name):
    # ファイル名
    today = datetime.today().strftime("%Y%m%d")
    log_filename = f"{os.getcwd()}/logs/api_{today}.log"

    # フォーマッター
    formatter = "[%(asctime)s] [%(levelname)s] %(message)s [File: %(filename)s:%(funcName)s():%(lineno)d]"

    # 設定
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format=formatter,
        encoding="utf-8",
        force=True,
    )

    return logging.getLogger(name)


if __name__ == "__main__":
    pass
