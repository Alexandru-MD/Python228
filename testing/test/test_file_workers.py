from testing.my_funcs.file_workers import read_from_file



def create_test_data(test_data):
    with open("test/test_file.txt", 'w') as f:
        f.writelines(test_data)


def test_read_from_file():
    test_data = ['one\n, two\n, three\n']
    create_test_data(test_data)
    assert test_data == read_from_file("test_file.txt")
