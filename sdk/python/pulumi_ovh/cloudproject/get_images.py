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
    'GetImagesResult',
    'AwaitableGetImagesResult',
    'get_images',
    'get_images_output',
]

@pulumi.output_type
class GetImagesResult:
    """
    A collection of values returned by getImages.
    """
    def __init__(__self__, flavor_type=None, id=None, images=None, os_type=None, region=None, service_name=None):
        if flavor_type and not isinstance(flavor_type, str):
            raise TypeError("Expected argument 'flavor_type' to be a str")
        pulumi.set(__self__, "flavor_type", flavor_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if images and not isinstance(images, list):
            raise TypeError("Expected argument 'images' to be a list")
        pulumi.set(__self__, "images", images)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if service_name and not isinstance(service_name, str):
            raise TypeError("Expected argument 'service_name' to be a str")
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="flavorType")
    def flavor_type(self) -> str:
        """
        Get compatible images with flavor type
        """
        return pulumi.get(self, "flavor_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def images(self) -> Sequence['outputs.GetImagesImageResult']:
        return pulumi.get(self, "images")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        Image OS (Allowed values: baremetal-linux ┃ bsd ┃ linux ┃ windows)
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        Image region
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> str:
        """
        Public cloud project ID
        """
        return pulumi.get(self, "service_name")


class AwaitableGetImagesResult(GetImagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImagesResult(
            flavor_type=self.flavor_type,
            id=self.id,
            images=self.images,
            os_type=self.os_type,
            region=self.region,
            service_name=self.service_name)


def get_images(flavor_type: Optional[str] = None,
               os_type: Optional[str] = None,
               region: Optional[str] = None,
               service_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImagesResult:
    """
    Get available images in the given public cloud project.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    images = ovh.CloudProject.get_images(os_type="linux",
        region="WAW1",
        service_name="<public cloud project ID>")
    ```


    :param str flavor_type: Get compatible images with flavor type
    :param str os_type: Image OS (Allowed values: baremetal-linux ┃ bsd ┃ linux ┃ windows)
    :param str region: Image region
    :param str service_name: Public cloud project ID
    """
    __args__ = dict()
    __args__['flavorType'] = flavor_type
    __args__['osType'] = os_type
    __args__['region'] = region
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('ovh:CloudProject/getImages:getImages', __args__, opts=opts, typ=GetImagesResult).value

    return AwaitableGetImagesResult(
        flavor_type=pulumi.get(__ret__, 'flavor_type'),
        id=pulumi.get(__ret__, 'id'),
        images=pulumi.get(__ret__, 'images'),
        os_type=pulumi.get(__ret__, 'os_type'),
        region=pulumi.get(__ret__, 'region'),
        service_name=pulumi.get(__ret__, 'service_name'))
def get_images_output(flavor_type: Optional[pulumi.Input[Optional[str]]] = None,
                      os_type: Optional[pulumi.Input[Optional[str]]] = None,
                      region: Optional[pulumi.Input[Optional[str]]] = None,
                      service_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = None) -> pulumi.Output[GetImagesResult]:
    """
    Get available images in the given public cloud project.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_ovh as ovh

    images = ovh.CloudProject.get_images(os_type="linux",
        region="WAW1",
        service_name="<public cloud project ID>")
    ```


    :param str flavor_type: Get compatible images with flavor type
    :param str os_type: Image OS (Allowed values: baremetal-linux ┃ bsd ┃ linux ┃ windows)
    :param str region: Image region
    :param str service_name: Public cloud project ID
    """
    __args__ = dict()
    __args__['flavorType'] = flavor_type
    __args__['osType'] = os_type
    __args__['region'] = region
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOutputOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('ovh:CloudProject/getImages:getImages', __args__, opts=opts, typ=GetImagesResult)
    return __ret__.apply(lambda __response__: GetImagesResult(
        flavor_type=pulumi.get(__response__, 'flavor_type'),
        id=pulumi.get(__response__, 'id'),
        images=pulumi.get(__response__, 'images'),
        os_type=pulumi.get(__response__, 'os_type'),
        region=pulumi.get(__response__, 'region'),
        service_name=pulumi.get(__response__, 'service_name')))
