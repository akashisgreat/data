#!/bin/bash

version="v1.5.0"
filename="ttyper.tar.gz"

pkg update
pkg install wget -y

wget https://github.com/max-niederman/ttyper/releases/download/$version/ttyper-aarch64-unknown-linux-musl.tar.gz -O $filename

tar -xvf $filename

mv ttyper /data/data/com.termux/files/usr/bin/
rm $filename
