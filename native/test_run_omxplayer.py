import pytest
import struct
import sys
from mock import patch
from run_omxplayer import *


class TestClass:
    def test_stdin(self):
         sys.stdout.write(struct.pack('i', len("Testing")) + 'Testing')
         assert read_thread_func() == 'Testing'
    def test_argparse(self):
        # Normal 1 arg not update
        testargs = ['run_omxplayer.py', 'testing']
        with patch.object(sys, 'argv', testargs):
            assert check_arguments() == True
        # Unnormal no args, should be error
        testargs = ['run_omxplayer.py']
        with patch.object(sys, 'argv', testargs):
            with pytest.raises(SystemExit):
                check_arguments()
        # Check called update
        testargs = ['run_omxplayer.py', '-U']
        with patch.object(sys, 'argv', testargs):
            with patch.object('check_update') as mock:
                check_arguments()
            mock.assert_called_with(42)

    def test_update(self):
        check_update()
