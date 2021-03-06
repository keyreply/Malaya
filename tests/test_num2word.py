import malaya

def test_to_cardinal():
    assert malaya.to_cardinal(123456789) == 'seratus dua puluh tiga juta empat ratus lima puluh enam ribu tujuh ratus lapan puluh sembilan'

def test_to_ordinal():
    assert malaya.to_ordinal(11) == 'kesebelas'

def test_to_ordinal_num():
    assert malaya.to_ordinal_num(11) == 'ke-11'

def test_to_currency():
    assert malaya.to_currency(123456789) == 'seratus dua puluh tiga juta empat ratus lima puluh enam ribu tujuh ratus lapan puluh sembilan ringgit'

def test_to_year():
    assert malaya.to_year(123456789) == 'seratus dua puluh tiga juta empat ratus lima puluh enam ribu tujuh ratus lapan puluh sembilan'
