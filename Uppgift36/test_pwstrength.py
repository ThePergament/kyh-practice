from pwstrength import compute_strength

def test_compute_strength_11():
    user_answer ="1"*11
    assert compute_strength(user_answer)==1
