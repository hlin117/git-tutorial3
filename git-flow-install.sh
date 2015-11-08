# See http://stackoverflow.com/a/1060886/2014591
#
# Tested on:
#
# OS X              git version 2.3.4
# Scientific linux  git version 1.8.4
#
# Failed on
# Mint              git version 1.7.x
#
# Acts differently on
# Ubuntu            git version 1.9.1 (prints to stdout)
# Mint              git version 1.9.1 (prints to stdout)
# Scientific linux  git version 1.7.1 (no colors)
git config --global alias.flow 'log --graph --oneline --all --decorate'
