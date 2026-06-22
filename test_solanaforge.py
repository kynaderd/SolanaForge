# test_solanaforge.py
"""
Tests for SolanaForge module.
"""

import unittest
from solanaforge import SolanaForge

class TestSolanaForge(unittest.TestCase):
    """Test cases for SolanaForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SolanaForge()
        self.assertIsInstance(instance, SolanaForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SolanaForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
