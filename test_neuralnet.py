# test_neuralnet.py
"""
Tests for NeuralNet module.
"""

import unittest
from neuralnet import NeuralNet

class TestNeuralNet(unittest.TestCase):
    """Test cases for NeuralNet class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeuralNet()
        self.assertIsInstance(instance, NeuralNet)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeuralNet()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
