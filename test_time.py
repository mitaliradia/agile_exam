import pytest
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from app import check_appointment_availability


@pytest.mark.parametrize("start_time,end_time,expected",
                         [
                             (2,4,True),
                             (4,6,False),
                             (10,0,False),
                             (10,-2,False),
                         ])

def test_check_leave_balance(start_time,end_time,expected):
    result=check_appointment_availability(start_time,end_time)
    assert result==expected

