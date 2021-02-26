import os
import unittest

from management_bdd import *

class Test(unittest.TestCase):

    def test_readJson(self):
        var_class = ManagementBdd()
        var_test = var_class.create_database() 
        #self.assertTrue(os.path.exists('./my_stop_areas.csv'))
        
        self.assertTrue(var_test)
        #self.assertTrue(os.path.exists('./stop_areas_maria.json'))

    def test_create_table_videos(self):

        var_class = ManagementBdd()
        
        var_test = var_class.create_table_videos() 
        #self.assertTrue(os.path.exists('./my_stop_areas.csv'))
        
        self.assertTrue(var_test)
    
    def test_insert_donnes(self):
        var_class = ManagementBdd()
        liste_videos= ('test', 'test','https://www.test.fr', '1111',"test description","Test-Test")
        self.assertTrue(var_class.insert_donnes(liste_videos))
        

if __name__  == '__main__':
    unittest.main(verbosity =2)

