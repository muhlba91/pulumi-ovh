# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

__all__ = [
    'GetReferenceResourceTypeResult',
    'AwaitableGetReferenceResourceTypeResult',
    'get_reference_resource_type',
    'get_reference_resource_type_output',
]

@pulumi.output_type
class GetReferenceResourceTypeResult:
    """
    A collection of values returned by getReferenceResourceType.
    """
    def __init__(__self__, id=None, types=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if types and not isinstance(types, list):
            raise TypeError("Expected argument 'types' to be a list")
        pulumi.set(__self__, "types", types)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def types(self) -> Sequence[str]:
        """
        List of resource types
        """
        return pulumi.get(self, "types")


class AwaitableGetReferenceResourceTypeResult(GetReferenceResourceTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReferenceResourceTypeResult(
            id=self.id,
            types=self.types)


def get_reference_resource_type(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReferenceResourceTypeResult:
    """
    Use this data source to list all the IAM resource types.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    types = ovh.Iam.get_reference_resource_type()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Iam/getReferenceResourceType:getReferenceResourceType', __args__, opts=opts, typ=GetReferenceResourceTypeResult).value

    return AwaitableGetReferenceResourceTypeResult(
        id=pulumi.get(__ret__, 'id'),
        types=pulumi.get(__ret__, 'types'))
def get_reference_resource_type_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReferenceResourceTypeResult]:
    """
    Use this data source to list all the IAM resource types.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    types = ovh.Iam.get_reference_resource_type()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:Iam/getReferenceResourceType:getReferenceResourceType', __args__, opts=opts, typ=GetReferenceResourceTypeResult)
    return __ret__.apply(lambda __response__: GetReferenceResourceTypeResult(
        id=pulumi.get(__response__, 'id'),
        types=pulumi.get(__response__, 'types')))
