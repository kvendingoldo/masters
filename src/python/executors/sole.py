# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import datetime

from padic import *
from generators import *

if __name__ == '__main__':
    print(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f"))
    comparasion()
    print(datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%f"))
