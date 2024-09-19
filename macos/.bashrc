#!/bin/bash

# Disable bracketed paste mode
bind 'set enable-bracketed-paste off'

# Executed when running interactively
[[ $- == *i* ]] || return

[ -n "$PS1" ] && source ~/.bash_profile
