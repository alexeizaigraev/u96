from modules import *
#from random import randint
import os
import shutil

class Papa():
    def mk_fio(self):
        fio_split = self.work_vec[self.ColFioOne].replace('  ', ' ' ).strip().split(' ')
        
        if len(fio_split) < 3:
            return fio_split[0] + ' ' \
                + fio_split[1] + ' ' \
                + fio_split[1]
        return ' '.join(fio_split)

    def mk_fio_split(self):
        fio_split = self.work_vec[self.ColFioOne].replace('  ', ' ' ).strip().split(' ')
        
        if len(fio_split) < 3:
            return fio_split[0], fio_split[1], fio_split[1]
        return fio_split[0], fio_split[1], fio_split[2]

    def mk_initial_one_dot(self):
        return f'{self.firstname[0]}.'

    def mk_initial_two_dot(self):
        return f'{self.lastname[0]}.'

    def mk_dep(self):
        if '№' in self.work_vec[self.ColDepOne]:
            return self.work_vec[self.ColDepOne].split('№')[-1].strip()
        return self.work_vec[self.ColDepOne].strip()

    def mk_fio_white(self, fff):
        fs = fff.replace('  ', ' ').strip().split(' ')
        surn = fs[0]
        out = surn
        other = ''.join(fs[1:]).replace('.', '').replace(' ', '')
        for leter in other:
            if leter.isupper() and leter.isalpha():
                out += leter
        return out

    def dep_clear(self, deps):
        out = []
        d = deps.replace('[', '').replace(']', '').replace(' ', '').strip()
        if ',' not in d:
            out.append(d[:7])
        else:
            dd = d.split(',')
            for ddd in dd:
                out.append(ddd[:7])
        return out

    def mk_kass_all(self):
        a = []
        for line_str in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8"):
            line = line_str.split(';')
            try:
                fio_white = self.mk_fio_white(line[2] )
                v = [line[0], fio_white, line[3]]
                a.append(v)
            except:
                print(f'>> err kass_all: {line[self.ColFioTwo]}')
        return a
            



    def login_deep(self, nama, parDep):
        logins = [line[0] for line in self.kass_all
            if ( (parDep in line[2][1:4])
                and (nama in line[1]) ) ]
        
        if logins:
            self.login_ok = True

        return logins


    def login(self):
        parDep = self.mk_dep()
        self.login_ok = False
        nama = self.mk_fio_white(self.mk_fio())

        logins = [line[0] for line in self.kass_all
            if ( (parDep in line[2])
                and (nama in line[1]) ) ]
        
        if logins:
            self.login_ok = True
            return logins

        return self.login_deep(nama, parDep[:3])


    