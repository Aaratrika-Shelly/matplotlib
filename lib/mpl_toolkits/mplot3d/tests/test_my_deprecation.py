import pytest
from matplotlib import _api
import matplotlib.pyplot as plt
import warnings


def test_axes3d_set_aspect_arguments():
    """
    Test argument handling for Axes3D.set_aspect.

    - Verifies that the `anchor` parameter correctly raises a
      DeprecationWarning.
    - Verifies that calling without `anchor` does not warn.
    - Verifies that the `adjustable` parameter is passed through correctly.
    """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    # Test that providing the `anchor` parameter raises a deprecation warning.
    with pytest.warns(_api.MatplotlibDeprecationWarning, match="anchor"):
        ax.set_aspect('equal', anchor='C')

    # Test that a call without `anchor` does not raise any warnings.
    with warnings.catch_warnings(record=True) as record:
        warnings.simplefilter("always")
        ax.set_aspect('equal')
        # Assert that the list of caught warnings is empty.
        assert len(record) == 0

    # Test that the `adjustable` parameter is correctly processed to satisfy
    # code coverage.
    ax.set_aspect('equal', adjustable='box')
    assert ax.get_adjustable() == 'box'
