import sys, os

current_dir = os.path.dirname(__file__)
sys.path.append(f"{current_dir}/..")

from .test_data_processor import DataProcessTests
