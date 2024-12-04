#!/usr/bin/env python3

import pytest

import core


def test_load_input_sample():
    cols, rows, data = core.load_input('sample')
    assert cols == 10
    assert rows == 10
    assert data[0, 0] == 'M'
    assert data[4, 2] == 'X'


def test_load_input_test():
    cols, rows, data = core.load_input('test')
    assert cols == 5
    assert rows == 4
    assert data[0, 0] == 'A'
    assert data[1, 0] == 'B'
    assert data[2, 0] == 'C'
    assert data[3, 0] == 'D'
    assert data[4, 0] == 'E'

    assert data[0, 1] == 'F'
    assert data[1, 1] == 'G'
    assert data[2, 1] == 'H'
    assert data[3, 1] == 'I'
    assert data[4, 1] == 'J'

    assert data[0, 2] == 'K'
    assert data[1, 2] == 'L'
    assert data[2, 2] == 'M'
    assert data[3, 2] == 'N'
    assert data[4, 2] == 'O'

    assert data[0, 3] == 'P'
    assert data[1, 3] == 'Q'
    assert data[2, 3] == 'R'
    assert data[3, 3] == 'S'
    assert data[4, 3] == 'T'


def test_iterate_by_cols():
    cols, rows, data = core.load_input('test')
    _gen = core.iterate_by_cols(cols, rows, data)
    assert core.as_string(next(_gen)) == 'ABCDE'
    assert core.as_string(next(_gen)) == 'FGHIJ'
    assert core.as_string(next(_gen)) == 'KLMNO'
    assert core.as_string(next(_gen)) == 'PQRST'
    with pytest.raises(StopIteration):
        next(_gen)


def test_iterate_by_rows():
    cols, rows, data = core.load_input('test')
    _gen = core.iterate_by_rows(cols, rows, data)
    assert core.as_string(next(_gen)) == 'AFKP'
    assert core.as_string(next(_gen)) == 'BGLQ'
    assert core.as_string(next(_gen)) == 'CHMR'
    assert core.as_string(next(_gen)) == 'DINS'
    assert core.as_string(next(_gen)) == 'EJOT'
    with pytest.raises(StopIteration):
        next(_gen)


def test_iterate_diagonal_down():
    cols, rows, data = core.load_input('test')
    _gen = core.iterate_diagonal_down(cols, rows, data)
    assert core.as_string(next(_gen)) == 'P'
    assert core.as_string(next(_gen)) == 'KQ'
    assert core.as_string(next(_gen)) == 'FLR'
    assert core.as_string(next(_gen)) == 'AGMS'
    assert core.as_string(next(_gen)) == 'BHNT'
    assert core.as_string(next(_gen)) == 'CIO'
    assert core.as_string(next(_gen)) == 'DJ'
    assert core.as_string(next(_gen)) == 'E'
    with pytest.raises(StopIteration):
        next(_gen)


def test_iterate_diagonal_up():
    cols, rows, data = core.load_input('test')
    _gen = core.iterate_diagonal_up(cols, rows, data)
    assert core.as_string(next(_gen)) == 'A'
    assert core.as_string(next(_gen)) == 'FB'
    assert core.as_string(next(_gen)) == 'KGC'
    assert core.as_string(next(_gen)) == 'PLHD'
    assert core.as_string(next(_gen)) == 'QMIE'
    assert core.as_string(next(_gen)) == 'RNJ'
    assert core.as_string(next(_gen)) == 'SO'
    assert core.as_string(next(_gen)) == 'T'
    with pytest.raises(StopIteration):
        next(_gen)



if __name__ == "__main__":
    pytest.main()
