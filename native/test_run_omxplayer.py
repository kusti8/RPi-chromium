import pytest
import struct
import sys
from mock import patch
from threading import Thread
from run_omxplayer import read_thread_func, check_arguments, check_update
from time import sleep

class TestClass:
    def run_stdin(self):
        sleep(1)
        sys.stdout.write(struct.pack('i', len("Testing")) + 'Testing')
    def test_stdin(self):
         t = Thread(worker=run_stdin)
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
            with patch('run_omxplayer.check_update') as mock:
                check_arguments()
            mock.assert_called_with(42)

    def test_update(self):
        check_update()
