# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetResourceGroupsResult',
    'AwaitableGetResourceGroupsResult',
    'get_resource_groups',
    'get_resource_groups_output',
]

@pulumi.output_type
class GetResourceGroupsResult:
    """
    A collection of values returned by getResourceGroups.
    """
    def __init__(__self__, id=None, resource_groups=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if resource_groups and not isinstance(resource_groups, list):
            raise TypeError("Expected argument 'resource_groups' to be a list")
        pulumi.set(__self__, "resource_groups", resource_groups)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Sequence[str]:
        """
        List of the resource groups IDs.
        """
        return pulumi.get(self, "resource_groups")


class AwaitableGetResourceGroupsResult(GetResourceGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceGroupsResult(
            id=self.id,
            resource_groups=self.resource_groups)


def get_resource_groups(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceGroupsResult:
    """
    Use this data source to list the existing IAM policies of an account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    my_groups = ovh.Iam.get_resource_groups()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Iam/getResourceGroups:getResourceGroups', __args__, opts=opts, typ=GetResourceGroupsResult).value

    return AwaitableGetResourceGroupsResult(
        id=pulumi.get(__ret__, 'id'),
        resource_groups=pulumi.get(__ret__, 'resource_groups'))


@_utilities.lift_output_func(get_resource_groups)
def get_resource_groups_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceGroupsResult]:
    """
    Use this data source to list the existing IAM policies of an account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    my_groups = ovh.Iam.get_resource_groups()
    ```
    """
    ...
