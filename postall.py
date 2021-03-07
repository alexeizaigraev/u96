# -*- coding: utf-8 -*-
from modules import *
import os

class Postall():


    def dir_out_post(self):
        return file_to_arr(CONFIG_PATH + 'ConfigPostPath.txt')[0]

    def post_all(self, ag, fout):
        out_text = "Логин; ФИО; Терминал\n"
        for line_str in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8"):
            line = line_str.split(';')
            if (len(line) > 3 \
                and ag in line[-1] \
                and ('true' in line[1])):
                out_text += line[0] + ';' \
                        + line[2] + ';' \
                        + line[-2].replace('[', '').replace(']', '') + "\n"
        text_to_file(out_text, fout)


    def kass(self, ag):
        out = []
        
        for line_str in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8"):
            line = line_str.split(';')
            if (len(line) > 3 \
                and (ag in line[-1]) \
                and (line[-2]) \
                and (line[-1]) \
                and ('true' in line[1])):
                out.append(line[0])
        return out

    def post_otpuska(self, ag, fout):
        logins = self.kass(ag)
        out_text = "Логин;Начало отпуска;Конец отпуска;Дата увольнения\n"
        
        for line_str in open(IN_DATA_PATH + 'all_otpuska.csv', 'r', encoding="UTF-8"):
            line = line_str.split(';')
            if line[0] in logins:
                line_new = line[:4]
                out_text += ';'.join(line_new).replace('null', '') + "\n"
                
        text_to_file(out_text, fout)

    def postall_main(self):

        post_path = self.dir_out_post()
        #all_kass = file_to_arr(IN_DATA_PATH + 'kass_all.csv')
        all_kass = [line.split(';') for line in open(IN_DATA_PATH + 'kass_all.csv', 'r', encoding="UTF-8") if len(line.split(';')) > 4 and 'true' in line.split(';')[1]]

        aktiv_logins = [line[0] for line in all_kass]

        #all_otpuska = file_to_arr(IN_DATA_PATH + 'all_otpuska.csv')
        #all_otpuska[:] = [line for line in all_otpuska if line[0] in aktiv_logins]
        all_otpuska = [line for line in open(IN_DATA_PATH + 'all_otpuska.csv', 'r', encoding="UTF-8") if line.split(';')[0] in aktiv_logins]


        self.post_all('justin', post_path + 'justin/OutPostAll.csv')
        self.post_otpuska('justin', post_path + 'justin/OutPostOtpuskaJust.csv')

        self.post_all('allo', post_path + 'allo/OutPostAllAllo.csv')

#u = Postall()
#u.postall_main()



