def test_cors_permite_origen_del_frontend(client):
    r = client.get("/health", headers={"Origin": "http://localhost:5500"})
    assert r.headers.get("access-control-allow-origin") == "http://localhost:5500"


def test_cors_rechaza_origen_desconocido(client):
    r = client.get("/health", headers={"Origin": "http://sitio-malicioso.com"})
    assert "access-control-allow-origin" not in r.headers
