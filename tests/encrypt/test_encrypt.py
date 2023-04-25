from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message("xablau", 3) == "bax_ual"
    assert encrypt_message("xablau", 9) == "ualbax"

    with pytest.raises(TypeError):
        encrypt_message(3, "xablau")
