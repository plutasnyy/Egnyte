import unittest
import json
from data import*
from observer import*


class TestData(unittest.TestCase):
    '''Tests for data -> are very long'''


    '''all tests are in diffrent functions because requairments could change'''
    def action_test(arg):
        if isinstance(arg,str)==False:
            print(arg)
            return False
        arg=arg.split()
        if len(arg) != 1:
            print(arg)
            return False
        return True

    def action_source_test(arg):
        if isinstance(arg,str)==False:
            print(arg)
            return False
        arg=arg.split()
        if len(arg) != 1:
            print(arg)
            return False
        return True

    def space_used_test(arg):
        if isinstance(arg,(int,float))== False:
            print(arg)
            return False
        return True

    def target_creation_time_test(arg):
        if isinstance(arg,(int,float))== False:
            print(arg)
            return False
        return True

    def target_file_check_sum_test(arg):
        if isinstance(arg,str)==False:
            print(arg)
            return False
        arg=arg.split()
        if len(arg) != 1:
            print(arg)
            return False
        return True

    def target_post_time_test(arg):
        if arg is None:
            return True
        if isinstance(arg,(int,float))== False:
            print(arg)
            return False
        return True

    def target_storage_type_test(arg):
        if arg is None:
            return True
        if isinstance(arg,str)==False:
            print(arg)
            return False
        arg=arg.split()
        if len(arg) != 1:
            print(arg)
            return False
        return True

    def user_id_test(arg):
        if isinstance(arg,(int,float))== False:
            print(arg)
            return False
        return True

    def event_category_test(arg):
        if isinstance(arg,str)==False:
            print(arg)
            return False
        arg=arg.split()
        if len(arg) != 1:
            print(arg)
            return False
        return True

    def event_id_test(arg):
        if isinstance(arg,str)==False:
            print(arg)
            return False
        arg=arg.split('-')
        if len(arg) != 5:
            print(arg)
            return False
        return True

    def time_stamp_test(arg):
        if isinstance(arg,(int,float))== False:
            print(arg)
            return False
        return True

    def user_agent_test(arg):
        if isinstance(arg,str)==False:
            print(arg)
            return False
        return True

    def work_group_id_test(arg):
        if isinstance(arg,str)==False:
            print(arg)
            return False
        arg=arg.split('-')
        if len(arg) != 5:
            print(arg)
            return False
        return True


    def setUp(self):
        '''initialization values'''
        ob=Observer()
        self.data=Data(ob)
        self.number_files=33
        self.path='out/FSE_'
        self.lines=[]

    def test_files_exists(self):
        for i in range(self.number_files+1):
            try:
                data_file=open(self.path+str(i))
                data_file.close()
            except: FileNotFoundError

    def test_has_atrr(self):
        for i in range(self.number_files+1):
            data=self.data.return_json_file(self.path+str(i))
            for j in data:
                keys=list(j.keys())
                keys_body=list(j['eventBody'].keys())
                keys_header=list(j['eventHeader'].keys())

                Xkeys=['eventBody','eventHeader']
                Xkeys_body=['action','actionSource','spaceUsed','targetCreationTime',
                'targetFileChecksum','targetPostedTime','targetStorageType','userId']
                Xkeys_header=['eventCategory','eventId','timeStamp','userAgent','workgroupID']

                for i in Xkeys:
                    self.assertTrue(i in keys)

                for i in Xkeys_body:
                    self.assertTrue(i in keys_body)

                for i in Xkeys_header:
                    self.assertTrue(i in keys_header)#fuuuuuuu

                self.lines.append(j)

    def test_quality_of_data(self):
        for line in self.lines:
            self.assertTrue(self.action_test(line['eventBody']['action']))
            self.assertTrue(self.action_source_test(line['eventBody']['actionSource']))
            self.assertTrue(self.space_used_test(line['eventBody']['spaceUsed']))
            self.assertTrue(self.target_creation_time_test(line['eventBody']['targetCreationTime']))
            self.assertTrue(self.target_file_check_sum_test(line['eventBody']['targetFileChecksum']))
            self.assertTrue(self.target_post_time_test(line['eventBody']['targetPostedTime']))
            self.assertTrue(self.target_storage_type_test(line['eventBody']['targetStorageType']))
            self.assertTrue(self.user_id_test(line['eventBody']['userId']))
            self.assertTrue(self.event_category_test(line['eventHeader']['eventCategory']))
            self.assertTrue(self.event_id_test(line['eventHeader']['eventId']))
            self.assertTrue(self.time_stamp_test(line['eventHeader']['timeStamp']))
            self.assertTrue(self.user_agent_test(line['eventHeader']['userAgent']))
            self.assertTrue(self.work_group_id_test(line['eventHeader']['workgroupID']))



if __name__=="__main__":
    unittest.main()
