#!/bin/bash

cnt=`ps -ef | grep "gitbook serve"| grep -v grep | wc -l`
start_gitbook() {
    HOME=/root;
    source /root/.bashrc;
    nvm use v10.23.0 > /dev/null;
    cd /root/gitbook/;
    gitbook serve --port 80 &
    sleep 3
    echo "gitbook启动完成!"
}

if [ "$cnt" -ge 1 ];then
    echo "gitbook已运行，将重启服务!"
    ps -ef | grep "gitbook serve" | grep -v grep | awk '{print $2}' | xargs kill -9
    start_gitbook
else
    start_gitbook
fi