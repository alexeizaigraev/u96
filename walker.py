# -*- coding: utf-8 -*-
from modules import *
import os
import shutil

class Walker():


    def dir_in_walk(self):
        return file_to_arr(CONFIG_PATH + 'ConfigRaskladPath.txt')[0]

    def dir_out_walk(self):
            return file_to_arr(CONFIG_PATH + 'ConfigGdrivePath.txt')[0]
        
    def show(self):
        a = os.listdir(self.dir_in_walk())
        for aa in a:
            p_cyan(aa)
        if not a:
            p_yellow('\n\tnothing show\n')


    def mk_agents(self):
        return file_to_dict_one(COMON_DATA_PATH, 3)

    def mover(self):
        agents = self.mk_agents()
        a = os.listdir(self.dir_in_walk())
        if len(a) < 1:
                p_yellow('\n\tno files found\n')
        old_dir = self.dir_in_walk()
        for aa in a:
            fname = os.path.abspath(aa).split(os.sep)[-1]
            old_fname = os.path.join(old_dir, fname)
            folder = fname[:7]
            key = fname[:3]
            new_root = os.path.join(self.dir_out_walk(), agents[key])
            new_dir = os.path.join(new_root, folder)
            new_fname = os.path.join(new_dir, fname)
            
            if not os.path.exists(new_dir):
                try:
                    os.mkdir(new_dir)
                    p_green(f'\tnew folder {new_dir}')
                except:
                    p_red(f'>> err creat folder {new_dir}')

            if '_RP_' in fname:
                try:
                    backup_fname = 'R:/DRM/ЗАИГРАЕВ ОБМЕН АРХИВ/Архив/' + fname
                    shutil.copy(old_fname, backup_fname)
                except:
                    pass

            try:
                shutil.move(old_fname, new_fname)
                p_blue(f' Ok move {new_fname}')
            except:
                p_yellow(f'>> err move {new_fname}')
            
        
        
    def walker_main(self):        
        self.mover()

        p_green('\n\trasklad:')
        self.show()

#u = Walker()
#u.walker_main()
