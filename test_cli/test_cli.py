import unittest
from unittest.mock import patch
import io
import sys
from cli.cli import Cli
  
class TestCli(unittest.TestCase):
    def setUp(self):
        self.cli = Cli()
        # Redirigir stdout para capturar las impresiones
        self.held_output = io.StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Restaurar stdout
        sys.stdout = sys.__stdout__

    @patch('builtins.input')
    def test_run_quit(self, mock_input):
        mock_input.return_value = '4'
        self.cli.run()
        self.assertFalse(self.cli.running)
        # Verificar que se imprimió "Quitting the game."
        self.assertIn("Quitting the game.", self.held_output.getvalue())

    

if __name__ == '__main__':
    unittest.main()