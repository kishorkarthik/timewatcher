import importlib

import pytest

import timewatcher_cli.bootstrap as bootstrap


@pytest.fixture(autouse=True)
def reset_bootstrap():
    importlib.reload(bootstrap)