from bddrest import response, status


def test_home_page(httpreq):
    with httpreq('/'):
        assert status == 200
        assert '<html lang="en">' in response.text
        assert '<title>YHTTP SSR Boilerplate</title>' in response.text
        assert (
            '<h1 id="home-title">Your server-rendered app starts here</h1>'
            in response.text
        )


def test_home_page_rejects_unexpected_input(httpreq):
    with httpreq('/', query={'unexpected': 'value'}):
        assert status == 400
