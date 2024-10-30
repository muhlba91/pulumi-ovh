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
    'GetVpssResult',
    'AwaitableGetVpssResult',
    'get_vpss',
    'get_vpss_output',
]

@pulumi.output_type
class GetVpssResult:
    """
    A collection of values returned by getVpss.
    """
    def __init__(__self__, id=None, results=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        pulumi.set(__self__, "results", results)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def results(self) -> Sequence[str]:
        """
        The list of VPS IDs associated with your OVH Account.
        """
        return pulumi.get(self, "results")


class AwaitableGetVpssResult(GetVpssResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpssResult(
            id=self.id,
            results=self.results)


def get_vpss(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpssResult:
    """
    Use this data source to get the list of VPS associated with your OVH Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    servers = ovh.Vps.get_vpss()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:Vps/getVpss:getVpss', __args__, opts=opts, typ=GetVpssResult).value

    return AwaitableGetVpssResult(
        id=pulumi.get(__ret__, 'id'),
        results=pulumi.get(__ret__, 'results'))
def get_vpss_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpssResult]:
    """
    Use this data source to get the list of VPS associated with your OVH Account.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    servers = ovh.Vps.get_vpss()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:Vps/getVpss:getVpss', __args__, opts=opts, typ=GetVpssResult)
    return __ret__.apply(lambda __response__: GetVpssResult(
        id=pulumi.get(__response__, 'id'),
        results=pulumi.get(__response__, 'results')))
