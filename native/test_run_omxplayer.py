import unittest
import struct
import sys
from run_omxplayer import *
from mock import patch

class OmxplayerTestCase(unittest.TestCase):
    def test_input(self):
        sys.stdout.write(struct.pack('i', len("Testing")) + 'Testing')
        self.failUnlessEqual(read_thread_func(), 'Testing')
    def test_arguments(self):
        with self.assertRaises(SystemExit) as cm:
            check_arguments()

        self.assertEqual(cm.exception.code, -1)

        self.assertTrue(check_arguments())

if __name__ == "__main__":
    sys.exit(unittest.main())
