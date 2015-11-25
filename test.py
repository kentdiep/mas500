import logging
import unittest
import MC_HW1intermediate


class TestMediaCloudAPICall (unittest.TestCase):
	def testMediaCloudAPICall (self):
		res= MC_HW1intermediate.callMediaCloud()
		assert res!=None 

if __name__ == "__main__":
    unittest.main()
