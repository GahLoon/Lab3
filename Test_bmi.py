import Lab2.lab2 as bmi

def test_bmi_normal_weight():   #cannot be capital
    result = bmi.bmi(167, 60)
    assert(result == 0)

def test_bmi_over_weight():
    result = bmi.bmi(167, 80)
    assert(result == 1)

def test_bmi_under_weight():
    result = bmi.bmi(167, 47)
    assert(result == -1)