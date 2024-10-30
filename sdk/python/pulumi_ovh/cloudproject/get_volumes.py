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
from . import outputs

__all__ = [
    'GetVolumesResult',
    'AwaitableGetVolumesResult',
    'get_volumes',
    'get_volumes_output',
]

@pulumi.output_type
class GetVolumesResult:
    """
    A collection of values returned by getVolumes.
    """
    def __init__(__self__, id=None, region_name=None, service_name=None, volumes=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if region_name and not isinstance(region_name, str):
            raise TypeError("Expected argument 'region_name' to be a str")
        pulumi.set(__self__, "region_name", region_name)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)
        if volumes and not isinstance(volumes, list):
            raise TypeError("Expected argument 'volumes' to be a list")
        pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="regionName")
    def region_name(self) -> str:
        """
        The region name where volumes are available
        """
        return pulumi.get(self, "region_name")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        The id of the public cloud project.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def volumes(self) -> Sequence['outputs.GetVolumesVolumeResult']:
        return pulumi.get(self, "volumes")


class AwaitableGetVolumesResult(GetVolumesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumesResult(
            id=self.id,
            region_name=self.region_name,
            service_name=self.service_name,
            volumes=self.volumes)


def get_volumes(region_name: Optional[str] = None,
                service_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumesResult:
    """
    Get all the volume from a region of a public cloud project

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    volume = ovh.CloudProject.get_volume(region_name="xxx",
        service_name="yyy")
    ```


    :param str region_name: A valid OVHcloud public cloud region name in which the volumes are available. Ex.: "GRA11".
    :param str service_name: The id of the public cloud project.
    """
    __args__ = dict()
    __args__['regionName'] = region_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:CloudProject/getVolumes:getVolumes', __args__, opts=opts, typ=GetVolumesResult).value

    return AwaitableGetVolumesResult(
        id=pulumi.get(__ret__, 'id'),
        region_name=pulumi.get(__ret__, 'region_name'),
        service_name=pulumi.get(__ret__, 'service_name'),
        volumes=pulumi.get(__ret__, 'volumes'))
def get_volumes_output(region_name: Optional[pulumi.Input[str]] = None,
                       service_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumesResult]:
    """
    Get all the volume from a region of a public cloud project

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    volume = ovh.CloudProject.get_volume(region_name="xxx",
        service_name="yyy")
    ```


    :param str region_name: A valid OVHcloud public cloud region name in which the volumes are available. Ex.: "GRA11".
    :param str service_name: The id of the public cloud project.
    """
    __args__ = dict()
    __args__['regionName'] = region_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:CloudProject/getVolumes:getVolumes', __args__, opts=opts, typ=GetVolumesResult)
    return __ret__.apply(lambda __response__: GetVolumesResult(
        id=pulumi.get(__response__, 'id'),
        region_name=pulumi.get(__response__, 'region_name'),
        service_name=pulumi.get(__response__, 'service_name'),
        volumes=pulumi.get(__response__, 'volumes')))
