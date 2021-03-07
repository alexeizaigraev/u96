# -*- coding: utf-8 -*-
import os
import shutil
from pathlib import Path
from modules import *
#from papa import *
#import papa
#

class Accback():

    def accback_main(self):

        in_files = ['R:/DRM/Access/db2.accdb',
                    'R:/DRM/Access/db2_be.accdb',
                    'R:/Obmen/REGISTRATION_JOURNAL/ЖУРНАЛЫ_РЕГИСТРАЦИИ.accdb',
                    'R:/Obmen/REGISTRATION_JOURNAL/ЖУРНАЛЫ_РЕГИСТРАЦИИ_be.accdb',
                    ]

        out_dir = 'R:/DRM/BackupAccess/'
                

        for path in in_files:
            old_name = path
            fname = path.split('/')[-1]
            new_name = out_dir + fname
            coper(old_name, new_name)
                    
#u = Accback()
#u.accback_main()
