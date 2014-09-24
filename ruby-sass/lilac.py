#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['ruby-yard', 'ruby-maruku']
pre_build = aur_pre_build
post_build = aur_post_build

if __name__ == '__main__':
  single_main()