# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
RegressorDisagreement
"""

__all__ = ["RegressorDisagreement"]


from ....internal.core.ensemble.sub_model_selector.diversity_measure.regressordisagreement import \
    RegressorDisagreement as core
from ....internal.utils.utils import trace


class RegressorDisagreement(core):
    """
    **Description**
        A measure of absolute value of disagreement in predictions between a pair of regressors, averaged over all pairs

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            **params):
        core.__init__(
            self,
            **params)

    def get_params(self, deep=False):
        """
        Get the parameters for this operator.
        """
        return core.get_params(self)
