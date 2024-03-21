import pytest
from uuid import uuid4
from time import sleep
from datetime import datetime
from main import root, get_list
import json
import asyncio
from fastapi import Query

def test_read_root():
    res = asyncio.run(root())
    assert 'pages' in res.keys()
    assert (type(res['pages']) == int)


def test_read_list():
    res = asyncio.run(get_list(q=[1]))
    res = res[0]
    assert (res['pages'] == 368)