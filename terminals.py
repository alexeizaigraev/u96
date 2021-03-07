from modules import *
from modules_base import *
import os
from papa_class import *

class Terminals(Papa):

    def def_agent(self):
        h = dict()
        h['shablon1'] = ''
        h['shablon2'] = ''
        h['soft'] = ''
        h['limit'] = ''
        a = file_to_arr(COMON_DATA_PATH)
        for vec in a:
            if self.ag_cod in vec[0]:
                h['shablon1'] = vec[self.ColDataShablon1]
                h['shablon2'] = vec[self.ColDataShablon2]
                h['soft'] = vec[self.ColDataSoft]
                h['limit'] = vec[self.ColDataLimit]
                break
        if 'shablon1' in h['shablon1']:
            sos('Незнакомый агент', self.ag_cod)
        return h


    def terminals_main(self):
        vsyo_zapros = file_to_arr(IN_DATA_PATH + 'vsyo_zapros_vneh_otbor.csv')
        head = vsyo_zapros[0]
        data = vsyo_zapros[1:]


        line = ''
        self.ag_cog = ''

        self.ColDataShablon1 = 5
        self.ColDataShablon2 = 6
        self.ColDataSoft = 7
        self.ColDataLimit = 8

        self.ColTermTerm = 0
        self.ColTermId = 1
        self.ColTermSity = 2
        self.ColTermRegion = 3
        self.ColTermStreet = 4
        self.ColTermHouse = 5
        self.ColTermSerial = 6


        fname_out = 'OutTerminals.csv'
        out_text = ''

        for line in data:
            insert_data = vec_to_hash(head, line)

            terminal = insert_data['termial']
            idd = insert_data['id_terminal']
            if not idd:
                idd = terminal
                
            sity = insert_data['city']
            region = insert_data['region']
            if not region:
                region = sity
            
            street = insert_data['street']
            house = insert_data['hous']
            serial = ''.join(insert_data['serial_number'].split('0')[1:])

            self.ag_cod = terminal[:3]
            out = ['','','','','','','','','',]

            out[0] = terminal
            out[1] = idd
            out[2] = self.def_agent()['shablon1']
            out[3] = sity + ', ' + region
            out[4] = street + ', ' + house
            out[5] = self.def_agent()['shablon2']
            out[6] = self.def_agent()['soft']
            out[7] = self.def_agent()['limit']
            out[8] = serial
            
            out_line = ';'.join(out)
            out_text += out_line + "\n"
            p_green(out_line)

        full_out_fname = OUT_DATA_PATH + fname_out
        text_to_file(out_text, full_out_fname)

#u = Terminals()
#u.terminals_main()
