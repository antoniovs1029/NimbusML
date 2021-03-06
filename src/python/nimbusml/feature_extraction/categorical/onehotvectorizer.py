# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
OneHotVectorizer
"""

__all__ = ["OneHotVectorizer"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.feature_extraction.categorical.onehotvectorizer import \
    OneHotVectorizer as core
from ...internal.utils.utils import trace


class OneHotVectorizer(core, BaseTransform, TransformerMixin):
    """

    Categorical transform that can be performed on data before
    training a model.

    .. remarks::
        The ``OneHotVectorizer`` transform passes through a data set,
        operating
        on text columns, to build a dictionary of categories. For each row,
        the entire text string appearing in the input column is defined as a
        category. The output of the categorical transform is an indicator
        vector.
        Each slot in this vector corresponds to a category in the dictionary,
        so
        its length is the size of the built dictionary. The categorical
        transform
        can be applied to one or more columns, in which case it builds a
        separate
        dictionary for each column that it is applied to.

        ``OneHotVectorizer`` is not currently supported to handle factor
        data.

    :param columns: a dictionary of key-value pairs, where key is the output
        column name and value is the input column name.

        * Multiple key-value pairs are allowed.
        * Input column type: numeric or string.
        * Output column type:
         `Vector Type </nimbusml/concepts/types#vectortype-column>`_.
        * If the output column names are same as the input column names, then
        simply specify ``columns`` as a list of strings.

        The << operator can be used to set this value (see
        `Column Operator </nimbusml/concepts/columns>`_)

        For example
         * OneHotVectorizer(columns={'out1':'input1', 'out2':'input2'})
         * OneHotVectorizer() << {'out1':'input1', 'out2':'input2'}

        For more details see `Columns </nimbusml/concepts/columns>`_.

    :param max_num_terms: An integer that specifies the maximum number of
        categories to include in the dictionary. The default value is
        1000000.

    :param output_kind: A character string that specifies the kind of output
        kind.

        * ``"Bag"``: Outputs a multi-set vector. If the input column is a
          vector of categories, the output contains one vector, where the
        value in
          each slot is the number of occurrences of the category in the input
          vector. If the input column contains a single category, the
        indicator
          vector and the bag vector are equivalent
        * ``"Ind"``: Outputs an indicator vector. The input column is a
        vector
          of categories, and the output contains one indicator vector per
        slot in
          the input column.
        * ``"Key"``: Outputs an index. The output is an integer id (between
          1 and the number of categories in the dictionary) of the category.
        * ``"Bin"``: Outputs a vector which is the binary representation of
        the category.

        The default value is ``"Ind"``.

    :param term: Optional character vector of terms or categories.

    :param sort: A character string that specifies the sorting criteria.

        * ``"Occurrence"``: Sort categories by occurences. Most frequent is
        first.
        * ``"Value"``: Sort categories by values.

    :param text_key_values: Whether key value metadata should be text,
        regardless of the actual input type.

    :param params: Additional arguments sent to compute engine.

    .. seealso::
        :py:class:`OneHotHashVectorizer
        <nimbusml.feature_extraction.categorical.OneHotHashVectorizer>`

    .. index:: transform, category

    Example:
       .. literalinclude:: /../nimbusml/examples/OneHotVectorizer.py
              :language: python
    """

    @trace
    def __init__(
            self,
            max_num_terms=1000000,
            output_kind='Indicator',
            term=None,
            sort='ByOccurrence',
            text_key_values=True,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            max_num_terms=max_num_terms,
            output_kind=output_kind,
            term=term,
            sort=sort,
            text_key_values=text_key_values,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
