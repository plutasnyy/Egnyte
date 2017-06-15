import unittest
import json
from data import*
from observer import*


class TestData(unittest.TestCase):
    '''Tests for data -> the are very long'''

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
            pass


if __name__=="__main__":
    unittest.main()
