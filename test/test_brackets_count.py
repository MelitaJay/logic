
from sympy import Symbol
from unittest import TestCase
from unittest.mock import Mock

from classes.proposition import PropositionAtomic, PropositionConnected, PropositionNegated


class Test(TestCase):

    def test_i(self):
        """Each atom has 0 brackets and 0 is even"""

        # Arrange
        proposition = PropositionAtomic("p", 1)

        # Act
        actual = proposition.brackets_count

        # Assert
        self.assertEqual(0, actual)
        self.assertEqual(0, actual % 2)

    def test_ii(self):
        """
        Suppose phi and psi have 2n and 2m brackets,
        then (phi [] psi) has 2(n+m+1) brackets
        """

        # Arrange
        n = Symbol("n")
        m = Symbol("m")

        phi = Mock()
        psi = Mock()

        phi.brackets_count = 2*n
        psi.brackets_count = 2*m

        proposition = PropositionConnected(phi, psi, Mock())

        # Act
        actual = proposition.brackets_count
        expected = 2*(n + m + 1)

        # Assert
        self.assertEqual(expected, actual)

    def test_iii(self):
        """
        Suppose phi has 2n brackets, then (~phi) has 2(n+1) brackets
        """

        # Arrange
        n = Symbol("n")

        phi = Mock()
        phi.brackets_count = 2*n

        proposition = PropositionNegated(phi)

        # Act
        actual = proposition.brackets_count
        expected = 2*(n+1)

        # Assert
        self.assertEqual(expected, actual)