################# Functional Api Tests #####################
import json
from subprocess import call
import pytest
from pyramid import testing
import requests
from webtest.app import AppError
from apflow.counterparty.models import Counterparty


counterparty_data = [
    dict(name='Company 1', eik_egn='111222333'),
    dict(name='Company 2', eik_egn='223456712'),
    dict(name='Company 3', eik_egn='323456712'),
    dict(name='ЕООД 1234', eik_egn='444444712'),
]
bad_data = [
    dict(name='Company less than 8', eik_egn='11122233'),
    dict(name='Company more than 13', eik_egn='12345678901234'),
]


# @pytest.fixture(scope='session')
# def db():
#     call('apflow testing.ini db init', shell=True)
#     yield
#     call('apflow testing.ini db drop_all', shell=True)


@pytest.fixture
def token(app):
    r = app.post_json('/user/login',
                      dict(identity='admin', password='password'))
    token  = r.json['token']
    return token


def test_login(app):
    r = app.post_json('/user/login',
                      dict(identity='admin', password='password'))
    assert r.json['result'] == 'ok'


def test_counterparty_api(token, app):
    headers = {'Authorization': f'JWT {token}'}
    bad_headers = {'Authorization': f'JWT {token[1:]}'}
    # Create new object
    res = app.post_json('/counterparty/',
                        counterparty_data[0],
                        headers=headers)
    assert res.status_code == 201
    assert res.json['result'] == 'ok'

    # Create new object - bad data
    res = app.post_json('/counterparty/',
                        bad_data[0],
                        headers=headers, expect_errors=True)
    assert res.status_code == 422

    # # Create new object with bad token
    res = app.post_json('/counterparty/',
                        counterparty_data[1],
                        headers=bad_headers,
                        expect_errors=True)
    assert res.status_code == 403

    # # Update object
    data = {
        "name": "Updated name",
        "eik_egn": "987456124"
    }
    res = app.put_json('/counterparty/1',
                        data,
                        headers=headers)
    assert res.status_code == 202
    assert res.json['result'] == 'ok'

    # # Delete object
    res = app.delete_json('/counterparty/1',
                          headers=headers)
    assert res.status_code == 202

    res = app.delete_json('/counterparty/2',
                          headers=headers, expect_errors=True)
    assert res.status_code == 404
