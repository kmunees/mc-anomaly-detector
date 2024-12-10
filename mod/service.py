import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.absolute()))
from fuzzywuzzy import fuzz
sys.path.append(str(Path(__file__).parent.absolute()))
def print_service():
    print("************************************************************************************2")
    # sys.path.append(str(Path(__file__).parent.absolute()))
    print(fuzz.partial_ratio("", "") > 80)
