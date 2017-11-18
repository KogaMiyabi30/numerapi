import pytest
import os

from numerapi.numerapi import NumerAPI


def test_get_competitions():
    api = NumerAPI()

    # get all competions
    res = api.get_competitions()
    assert isinstance(res, dict)
    assert len(res['data']['rounds']) > 80

    # get one competion
    res = api.get_competitions(67)
    assert isinstance(res, dict)
    print(res)
    assert len(res['data']['rounds']) == 1


def test_download_current_dataset():
    api = NumerAPI()
    path = api.download_current_dataset(unzip=True)
    assert os.path.exists(path)

    directory = path.replace(".zip", "")
    filename = "numerai_tournament_data.csv"
    assert os.path.exists(os.path.join(directory, filename))


def test_get_current_round():
    api = NumerAPI()
    current_round = api.get_current_round()
    assert current_round >= 82
