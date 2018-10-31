# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
MinMaxScaler
"""

__all__ = ["MinMaxScaler"]


from sklearn.base import TransformerMixin

from ...base_transform import BaseTransform
from ...internal.core.preprocessing.normalization._minmaxscaler import \
    MinMaxScaler as core
from ...internal.utils.utils import trace


class MinMaxScaler(core, BaseTransform, TransformerMixin):
    """

    Normalizes columns as specified below.

    .. remarks::
        In linear classification algorithms instances are viewed as vectors
        in
        multi-dimensional space. Since the range of values of raw data varies
        widely, some objective functions do not work properly without
        normalization. For example, if one of the features has a broad range
        of
        values, the distances between points is governed by this particular
        feature. Therefore, the range of all features should be normalized so
        that each feature contributes approximately proportionately to the
        final
        distance. This can provide significant speedup and accuracy benefits.
        In
        all the linear algorithms in nimbusml (:py:class:`Logistic Regression
        <nimbusml.linear_model.LogisticRegressionClassifier>`,
        :py:class:`Averaged Perceptron
        <nimbusml.linear_model.AveragedPerceptronBinaryClassifier>`, etc.),
        the default is to normalize features before training.

        ``MinMaxScaler`` is the default normalizer for many `nimbusml`
        algorithms
        and linearly rescales every feature to the [0,1] or the [-1,1]
        interval.
        Rescaling to the [0,1] interval is done by shifting the values of
        each
        feature so that the minimal value is 0, and then dividing by the new
        maximal value (which is the difference between the original maximal
        and
        minimal values). Rescaling to the [-1,1] interval is done by dividing
        the values of each feature by the maximal absolute value of the
        feature.
        This method is useful for preserving the sparsity of a dataset, since
        0
        values do not change. The scaling method can be specified by setting
        the
        `fix_zero` to `False` for the first method, or setting it to `True`
        for
        the second method.

    :param columns: a dictionary of key-value pairs, where key is the output
        column name and value is the input column name.

        * Multiple key-value pairs are allowed.
        * Input column type: float or double or
         `Vector Type </nimbusml/concepts/types#vectortype-column>`_
         of floats
        or doubles.
        * Output column type:
         `Vector Type </nimbusml/concepts/types#vectortype-column>`_.
        * If the output column names are same as the input column names, then
        simply specify ``columns`` as a list of strings.

        The << operator can be used to set this value (see
        `Column Operator </nimbusml/concepts/columns>`_)

        For example
         * MinMaxScaler(columns={'out1':'input1', 'out2':'input2'})
         * MinMaxScaler() << {'out1':'input1', 'out2':'input2'}

        For more details see `Columns </nimbusml/concepts/columns>`_.

    :param fix_zero: Whether to map zero to zero, preserving sparsity.

    :param max_training_examples: Max number of examples used to train the
        normalizer.

    :param params: Additional arguments sent to compute engine.

    .. note::

        *MinMaxScaler* as many other transforms requires input to be of
        numeric type.
        It will fail for other types. Most of the times, features are
        float but a column could be unexpectedly of type string. That
        explains why
        the following code raises an exception.
        ::
            in_df = pandas.DataFrame(data=dict(Sepal_Length=["2,2", 1, 2,
        1]))
            normed = MinMaxScaler() << [Sepal_Length']
            normed.fit_transform(in_df)

        The displayed message is::

            'Source column 'Petal_Length' has invalid type ('TX'): Expected
        R4 or R8 item type.

        The input column must be converted into float or double in the
        dataframe
        before running the pipeline or inside the pipeline with transform
        :py:class:`TypeConverter <nimbusml.preprocessing.schema.TypeConverter>`.
        This transform is automatically added in case of integers.

    .. seealso::
        :py:class:`Binner
        <nimbusml.preprocessing.normalization.Binner>`,
        :py:class:`MeanVarianceScaler
        <nimbusml.preprocessing.normalization.MeanVarianceScaler>`,
        :py:class:`LogMeanVarianceScaler
        <nimbusml.preprocessing.normalization.LogMeanVarianceScaler>`,
        :py:class:`GlobalContrastRowScaler
        <nimbusml.preprocessing.normalization.GlobalContrastRowScaler>`.

    .. index:: normalize, preprocessing

    Example:
       .. literalinclude:: /../nimbusml/examples/MinMaxScaler.py
              :language: python
    """

    @trace
    def __init__(
            self,
            fix_zero=True,
            max_training_examples=1000000000,
            columns=None,
            **params):

        if columns:
            params['columns'] = columns
        BaseTransform.__init__(self, **params)
        core.__init__(
            self,
            fix_zero=fix_zero,
            max_training_examples=max_training_examples,
            **params)
        self._columns = columns

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)

    def _nodes_with_presteps(self):
        """
        Inserts preprocessing before this one.
        """
        from ..schema import TypeConverter
        return [
            TypeConverter(
                result_type='R4')._steal_io(self),
            self]