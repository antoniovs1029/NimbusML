# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
NGramExtractor
"""

__all__ = ["NGramExtractor"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.feature_extraction.text._ngramextractor import \
    NGramExtractor as core
from ...internal.utils.utils import trace


class NGramExtractor(core, BaseTransform, TransformerMixin):
    """
    **Description**
        Produces a bag of counts of n-grams (sequences of consecutive values of length 1-n) in a given vector of keys. It does so by building a dictionary of n-grams and using the id in the dictionary as the index in the bag.

    :param columns: see `Columns </nimbusml/concepts/columns>`_.

    :param ngram_length: Maximum n-gram length.

    :param all_lengths: Whether to store all n-gram lengths up to ngramLength,
        or only ngramLength.

    :param skip_length: Maximum number of tokens to skip when constructing an
        n-gram.

    :param max_num_terms: Maximum number of n-grams to store in the dictionary.

    :param weighting: The weighting criteria.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            ngram_length=2,
            all_lengths=True,
            skip_length=0,
            max_num_terms=[10000000],
            weighting='Tf',
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            ngram_length=ngram_length,
            all_lengths=all_lengths,
            skip_length=skip_length,
            max_num_terms=max_num_terms,
            weighting=weighting,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)