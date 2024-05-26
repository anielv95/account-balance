import functions as f


def test_get_email():
    test1 = "123_aniel_v@gmail.com.csv"
    output = f.get_email(test1)
    assert "123" == output[0]
    assert "aniel_v@gmail.com" == output[1]

    test1 = "123_aniel_v_34@gmail.com.csv"
    output = f.get_email(test1)
    assert "123" == output[0]
    assert "aniel_v_34@gmail.com" == output[1]

    test1 = "123_aniel.csv_v@gmail.com.csv"
    output = f.get_email(test1)
    assert "123" == output[0]
    assert "aniel.csv_v@gmail.com" == output[1]

    test1 = "123_aniel.csv_v.csv4_.csv@gmail.com.csv"
    output = f.get_email(test1)
    assert "123" == output[0]
    assert "aniel.csv_v.csv4_.csv@gmail.com" == output[1]
