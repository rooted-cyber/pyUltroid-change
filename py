#!/bin/bash

msg() {
echo -e "$@" >&2
}




cpf() {
cd ~/pyUltroid-change
git pull
rm -rf ~/Termux-Ultroid/Ultroid/pyUltroid
cp -rf pyUltroid ~/Termux-Ultroid/Ultroid
msg copied pyultroid 
}
chin() {
cd ~
if [ -e pyUltroid-change ];then
cpf
else
git clone https://github.com/rooted-cyber/pyUltroid-change
cpf
fi
}
chin