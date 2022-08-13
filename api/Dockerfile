FROM python:3.10

# Jumanppの導入
RUN wget https://github.com/ku-nlp/jumanpp/releases/download/v2.0.0-rc3/jumanpp-2.0.0-rc3.tar.xz \
  && apt-get update \
  && apt-get install -y sudo \
  && apt-get install -y make \
  && apt-get install -y cmake \
  && apt-get install -y tar \
  && tar xJvf jumanpp-2.0.0-rc3.tar.xz \
  && cd jumanpp-2.0.0-rc3/ \
  && mkdir bld \
  && cd bld \
  && cmake .. -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local \
  && sudo make install

# 作業ディレクトリ
WORKDIR /api

# パッケージファイルをコンテナにコピー
COPY requirements.txt ./

# パッケージのインストール
RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir
