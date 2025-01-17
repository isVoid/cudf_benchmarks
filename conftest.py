from itertools import product

import pytest

from utils import make_col, make_frame


@pytest.fixture(params=product([100, 10000], [True, False]))
def col(request):
    """Create a cudf column.

    The two parameters are `nrows` and `has_nulls`
    """
    return make_col(*request.param)


@pytest.fixture(params=[100, 10000])
def df(request):
    """Create a cudf DataFrame.

    The two parameters are `nrows`
    """
    return make_frame(ncols=5, nkey_cols=0, nrows=request.param)
