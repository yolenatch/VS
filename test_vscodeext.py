# test_vscodeext.py
"""
Tests for VSCodeExt module.
"""

import unittest
from vscodeext import VSCodeExt

class TestVSCodeExt(unittest.TestCase):
    """Test cases for VSCodeExt class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VSCodeExt()
        self.assertIsInstance(instance, VSCodeExt)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VSCodeExt()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
