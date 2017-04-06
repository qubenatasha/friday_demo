#!/usr/bin/python
"""
Add docstring here
"""
import time
import unittest

import mock

from mock import patch
import mongomock


class Testfriday_demoModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("before class")

    @mock.patch('pymongo.mongo_client.MongoClient', new=mongomock.MongoClient)
    def test_create_friday_demo_model(self):
        from qube.src.models.friday_demo import friday_demo
        friday_demo_data = friday_demo(name='testname')
        friday_demo_data.tenantId = "23432523452345"
        friday_demo_data.orgId = "987656789765670"
        friday_demo_data.createdBy = "1009009009988"
        friday_demo_data.modifiedBy = "1009009009988"
        friday_demo_data.createDate = str(int(time.time()))
        friday_demo_data.modifiedDate = str(int(time.time()))
        with patch('mongomock.write_concern.WriteConcern.__init__',
                   return_value=None):
            friday_demo_data.save()
            self.assertIsNotNone(friday_demo_data.mongo_id)
            friday_demo_data.remove()

    @classmethod
    def tearDownClass(cls):
        print("After class")


if __name__ == '__main__':
    unittest.main()
