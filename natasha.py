# -*- coding: utf-8 -*-
from modules import *
from papa_class import *
from datetime import datetime, date

class Natasha(Papa):

    def natasha_main(self):

        names = comon_data_dict(1)
                
        fname_out = 'OutNatasha.csv'
        out_text = ''
        #data = set(file_to_arr(IN_DATA_PATH + 'natasha.csv'))
        data = set(mk_natasha())
        h = dict()
        for line in data:
            key = line[:3]
            if key in h:
                h[key] += 1
            else:
                h[key] = 1
            
        sum = 0
        for key in sorted(list(h.keys())):
            sum += h[key]
            name = '_'
            if key in names:
                name = names[key]
                    
            out_text += key + ';' + name + ';' + str(h[key]) + '\n'

        out_text += '__________\n'
        out_text += 'Всего: ' + str(sum)
                
        full_out_fname = OUT_DATA_PATH + fname_out
        text_to_file(out_text, full_out_fname)
        p_green('\n\n' + out_text)

        now = str(datetime.today())[:10]
        ofname = DATA_PATH + f'Количество отделений/Отделения-{now}.csv'
        p_yellow('\n\t Отчёт?\t\t Да [Enter] ->')
        choise = input()
        if not choise:
            text_to_file(out_text, ofname)
        else:
            p_cyan('\tDu-Du :)')

#u = Natasha()
#u.natasha_main()
