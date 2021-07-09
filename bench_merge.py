import utils
import pytest


@pytest.mark.parametrize(
    'ncols', [4, 7, 10],
)
@pytest.mark.parametrize(
    'nkey_cols', [2, 3, 4],
)
@pytest.mark.parametrize(
    'nrows', [10, 100, 1000, 10_000, 100_000, 1_000_000],
)
def test_merge(benchmark, ncols, nkey_cols, nrows):
    lhs = utils.make_frame(ncols, nkey_cols, nrows)
    rhs = utils.make_frame(ncols, nkey_cols, nrows // 2)
    benchmark(lhs.merge, rhs, on=[f"key{i}" for i in range(nkey_cols)])
