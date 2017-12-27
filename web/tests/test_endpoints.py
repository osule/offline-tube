from requests.status_codes import codes


def test_index_page(client):
    rv = client.get('/')
    assert codes.ok == rv.status_code
