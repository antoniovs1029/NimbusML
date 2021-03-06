# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# --------------------------------------------------------------------------------------------
# - Generated by tools/entrypoint_compiler.py: do not edit by hand
"""
RegressorAllSelector
"""

__all__ = ["RegressorAllSelector"]


from ....utils.entrypoints import Component
from ....utils.utils import trace


class RegressorAllSelector(Component):
    """
    **Description**
        Combines all the models to create the output. This is the default submodel selector.

    :param params: Additional arguments sent to compute engine.

    """

    @trace
    def __init__(
            self,
            **params):

        self.kind = 'EnsembleRegressionSubModelSelector'
        self.name = 'AllSelector'
        self.settings = {}

        super(
            RegressorAllSelector,
            self).__init__(
            name=self.name,
            settings=self.settings,
            kind=self.kind)
