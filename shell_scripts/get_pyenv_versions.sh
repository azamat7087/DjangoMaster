#!/usr/bin/zsh

rm ./data/versions.txt
export PYENV_ROOT="$HOME"/.pyenv
export PATH="$PYENV_ROOT"/bin:"$PATH"
pyenv versions >> ./data/versions.txt
