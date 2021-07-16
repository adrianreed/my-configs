#!/bin/bash
# colors
RED='\[\e[0;31m\]'
YELLOW='\[\e[0;33m\]'
GREEN='\[\e[0;32m\]'
BLUE='\[\e[0;34m\]'
LIGHTBLUE='\[\033[1;36m\]'
PURPLE='\[\e[0;35m\]'
WHITE='\e[0;37m\]'
NC='\[\e[0m\]'

# git prompt
PS1="${WHITE}\\u at ${RED}[\\W] ${YELLOW}\$(parse_git_branch)\n${GREEN}$ ${NC}"
parse_git_branch() {
 git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
export -f parse_git_branch
if [ -f `brew --prefix`/etc/bash_completion ]; then
  . `brew --prefix`/etc/bash_completion
fi

# alias
alias hg='history | grep'
alias lll='ls -lahtr'
alias falln='sudo find / -name'

# private alias
source ~/.priv_alias
