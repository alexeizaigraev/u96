# -*- coding: utf-8 -*-
from modules import *
import os
import shutil
from papa_class import *

class Site(Papa):

    def mk_regimes(self):
        return file_to_dict_one(COMON_DATA_PATH, 4)


    def site_main(self):
        dir_in = IN_DATA_PATH
        dir_out = OUT_DATA_PATH
        fname_out = 'OutSite.csv'
        fname_out_php = 'page-departments.php'
                
        text1 = '''<?php
get_header();
?> 
<div class="container">
    <div class="row">
      <h1 class="title-normal"><strong>Відділення</strong></h1>
       <h5>Керівник відділень - начальник відділень Кульчицький Андрій Олегович, тел. +380 (44) 300 00 01 (137)</h5>
        <div class="form-group" style="margin-top:10px;">
            <input type="text" class="search-depart form-control" placeholder="Пошук">
        </div>
        <span class="counter"></span>
        <table class="table table-hover table-bordered results">
          <thead>
            <tr>
              <th class="col-md-1">Повне найменування відокремленного підрозділу</th>
              <th class="col-md-4">Адреса відокремленного підрозділу</th>
              <th>Дата та номер рішення про створення відокремленого підрозділу</th>
              <th class="col-md-1">ЄДРПОУ</th>
              <th class="col-md-2">Режим роботи</th>
              <th class="col-md-2">Платежі приймаються в Платіжній системі</th>
              <th class="col-md-2">Платежі виплачуються  в Платіжній системі</th>
            </tr>
            <tr class="warning no-result">
              <td colspan="7"><i class="fa fa-warning"></i> No result</td>
            </tr>
          </thead>
          <tbody>
'''

        text2 = '''          </tbody>
        </table>
        <div class="gap-20"></div>
        <ul class="list-arrow">
            <li><a href="<?php echo $www?>/departments.pdf" target="_blank">Список усіх відділень</a></li>
        </ul>
        <div class="gap-20"></div>
    </div>
    
</div>

<?php
get_footer();
?> '''
        

        regimes = self.mk_regimes()
        natasha = set(mk_natasha())

        site_old = file_to_text(dir_out + "OutSite.csv")
        access_clear = file_to_text(dir_in + 'access.csv')
        access = access_to_arr()
        access_old = file_to_text(dir_in + 'access_old.csv')

        if access_clear == access_old:
            p_red('\n\tno change!')
                
        header0 = ['Повне найменування відокремленного підрозділу', 'Адреса відокремленного підрозділу', 'Дата та номер рішення про створення відокремленого підрозділу', 'ЄДРПОУ', 'Режим роботи', 'Платежі приймаються в Платіжній системі', 'Платежі виплачуються  в Платіжній системі']
        header = ['', header0[0], '', header0[1], '', header0[2], '', header0[3], '', header0[4], '', header0[5], '', header0[6], '']
        header_clear = [header0[0], header0[1], header0[2], header0[3], header0[4], header0[5], header0[6]]

        out = []
        out_clear = []
        out_clear.append(header_clear)

        for access_line in access:
            if '2(Веб-сайт-ПТКС)' in access_line[0]:
                continue
                    
            line = [access_line[0],
                    access_line[2],
                    access_line[ 3 ],
                    access_line[1],
                    'ТИМЧАСОВО НЕ ПРАЦЮЄ',
                    ' ВПС ЕЛЕКТРУМ, ВПС FLASHPAY',
                    ' ВПС ЕЛЕКТРУМ']

            dep = access_line[0].split('№')[1].strip() if '№' in access_line[0] else access_line[0]
            ag_sign = dep.strip()[:3]
            if ag_sign in regimes:
                if dep in natasha:
                    line[4] = regimes[ag_sign]
            else:
                print('#', dep)
                
            if dep == '1':
                line[4] = 'ПН-ПТ 09:00-18:00'
                    
            line_tegs = ['<tr><td>', line[0], '</td><td>', line[1], '</td><td>', line[2], '</td><td>', line[3], '</td><td>',line[4], '</td><td>', line[5], '</td><td>', line[6], '</td></tr>']
            out.append(line_tegs)
            out_clear.append(line)


        shutil.copy(dir_in + 'access.csv' ,dir_in + 'access_old.csv')
                
        full_out_fname = OUT_DATA_PATH + fname_out
        arr_to_file(out_clear, full_out_fname)

        out_text_php = text1 + arr_to_text(out) + text2
        full_out_fname_php = OUT_DATA_PATH + fname_out_php
        text_to_file(out_text_php.replace(';', ''), full_out_fname_php)

#u = Site()
#u.site_main()
