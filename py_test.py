# content of test_sample.py

# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(2) == 5

# ======================================

# import pytest
#
#
# def f():
#     raise SystemExit(1)
#
#
# def my_test():
#     with pytest.raises(SystemExit):
#         f()

#=============================================

# class TestClass:
#     def test_one(self):
#         x = "this"
#         assert "h" in x
#
#     def test_two(self):
#         x = "hello"
#         assert 'l' in x
#
#================================

def test_needfiles(tmpdir):
    print(tmpdir)
    assert 0


