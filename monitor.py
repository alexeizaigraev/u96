# -*- coding: utf-8 -*-
import os
import shutil
from pathlib import Path
from modules import *
from papa_class import *

class Monitor():

    def monitor_main(self):
        in_dirs = file_to_arr(os.path.join(CONFIG_DIR_PATH, 'PathMonitor.txt'))
        out_path = file_to_arr(os.path.join(CONFIG_DIR_PATH, 'PathMonitorOut.txt'))[0]

        flag = False
        start_dirs = in_dirs
        for dir in start_dirs:
            fnames = os.listdir(dir)
            for fname in fnames:
                if '.pdf' in fname:
                    flag = True
                    old_name = dir + fname
                    new_name = out_path + fname
                    mover(old_name, new_name)
        if not flag:
            p_cyan('\n\tПусто\n')

#u = Monitor()
#u.monitor_main()
