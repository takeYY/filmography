FROM python:3.10

# Jumanpp の導入
# RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc3/jumanpp-2.0.0-rc3.tar.xz \
#   && apt-get update \
#   && apt-get install -y sudo \
#   && apt-get install -y make \
#   && apt-get install -y cmake \
#   && apt-get install -y tar \
#   && tar xJvf jumanpp-2.0.0-rc3.tar.xz \
#   && cd jumanpp-2.0.0-rc3/ \
#   && mkdir bld \
#   && cd bld \
#   && cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local \
#   && sudo make install

# 作業ディレクトリ
WORKDIR /api

# poetry のインストール先の指定
ENV POETRY_HOME=/opt/poetry

# poetry インストール
RUN curl -sSL https://install.python-poetry.org | python3 - \
  # シンボリックによる path への poetry コマンドの追加
  && cd /usr/local/bin \
  && ln -s /opt/poetry/bin/poetry \
  # 仮想環境を作成しない設定(コンテナ前提のため，仮想環境を作らない)
  && poetry config virtualenvs.create false

# poetry の定義ファイルをコピー
COPY pyproject.toml* ./
COPY /poetry.lock* ./

# poetry でライブラリをインストール
RUN poetry install --no-root
