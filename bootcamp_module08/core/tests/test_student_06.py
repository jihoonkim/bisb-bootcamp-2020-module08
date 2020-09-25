from bootcamp_module08.core.student_06 import count_substring  # noqa


def test_count_substring_single():
    test_string = "CGCTAGCGT"
    test_substring = "TAG"

    expected_count = 1
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_repeated():
    test_string = "AGCTAGCAGT"
    test_substring = "AGC"

    expected_count = 2
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_substring_none():
    test_string = "AGTCCCCTAGA"
    test_substring = "AAA"

    expected_count = 0
    observed_count = count_substring(test_string, test_substring)
    assert expected_count == observed_count


def test_count_is_casesensitive():
    test_string_1 = "CGCTAGCGT"
    test_substring_1 = "TAG"

    test_string_2 = "cgcTAGcgt"
    test_substring_2 = "Tag"

    output_1 = count_substring(test_string_1, test_substring_1)
    output_2 = count_substring(test_string_2, test_substring_2)
    assert output_1 == output_2
