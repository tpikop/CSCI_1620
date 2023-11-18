import pytest
from television import Television

def test_television_initialization():
    tv = Television()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_television_power_toggle():
    tv = Television()
    tv.power()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'
    tv.power()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

def test_television_mute_toggle():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.power()
    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    tv.mute()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'
    
def test_television_channel_up():
    tv = Television()
    tv.channel_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 1, Volume = 0'

    for _ in range(Television.MAX_CHANNEL):
        tv.channel_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

def test_television_channel_down():
    tv = Television()
    tv.channel_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    tv.channel_down()
    assert str(tv) == 'Power = True, Channel = 3, Volume = 0'

def test_television_volume_up():
    tv = Television()
    tv.volume_up()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 1'

    tv.power()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    tv.mute()
    tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 2'

def test_television_volume_down():
    tv = Television()
    tv.volume_down()
    assert str(tv) == 'Power = False, Channel = 0, Volume = 0'

    tv.power()
    for _ in range(Television.MAX_VOLUME):
        tv.volume_up()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 1'

    tv.mute()
    tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

    for _ in range(Television.MIN_VOLUME):
        tv.volume_down()
    assert str(tv) == 'Power = True, Channel = 0, Volume = 0'

if __name__ == "__main__":
    pytest.main()
