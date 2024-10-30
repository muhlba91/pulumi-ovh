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
    'ServerDetailsArgs',
    'ServerDetailsArgsDict',
    'ServerIamArgs',
    'ServerIamArgsDict',
    'ServerInstallTaskDetailsArgs',
    'ServerInstallTaskDetailsArgsDict',
    'ServerInstallTaskUserMetadataArgs',
    'ServerInstallTaskUserMetadataArgsDict',
    'ServerNetworkingInterfaceArgs',
    'ServerNetworkingInterfaceArgsDict',
    'ServerOrderArgs',
    'ServerOrderArgsDict',
    'ServerOrderDetailArgs',
    'ServerOrderDetailArgsDict',
    'ServerPlanArgs',
    'ServerPlanArgsDict',
    'ServerPlanConfigurationArgs',
    'ServerPlanConfigurationArgsDict',
    'ServerPlanOptionArgs',
    'ServerPlanOptionArgsDict',
    'ServerPlanOptionConfigurationArgs',
    'ServerPlanOptionConfigurationArgsDict',
    'ServerUserMetadataArgs',
    'ServerUserMetadataArgsDict',
]

MYPY = False

if not MYPY:
    class ServerDetailsArgsDict(TypedDict):
        custom_hostname: NotRequired[pulumi.Input[str]]
        """
        Personnal hostname to use in server reinstallation
        """
        disk_group_id: NotRequired[pulumi.Input[float]]
        """
        Disk group id to process install on (only available for some templates)
        """
        no_raid: NotRequired[pulumi.Input[bool]]
        """
        true if you want to install only on the first disk
        """
        soft_raid_devices: NotRequired[pulumi.Input[float]]
        """
        Number of devices to use for system's software RAID
        """
elif False:
    ServerDetailsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerDetailsArgs:
    def __init__(__self__, *,
                 custom_hostname: Optional[pulumi.Input[str]] = None,
                 disk_group_id: Optional[pulumi.Input[float]] = None,
                 no_raid: Optional[pulumi.Input[bool]] = None,
                 soft_raid_devices: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] custom_hostname: Personnal hostname to use in server reinstallation
        :param pulumi.Input[float] disk_group_id: Disk group id to process install on (only available for some templates)
        :param pulumi.Input[bool] no_raid: true if you want to install only on the first disk
        :param pulumi.Input[float] soft_raid_devices: Number of devices to use for system's software RAID
        """
        if custom_hostname is not None:
            pulumi.set(__self__, "custom_hostname", custom_hostname)
        if disk_group_id is not None:
            pulumi.set(__self__, "disk_group_id", disk_group_id)
        if no_raid is not None:
            pulumi.set(__self__, "no_raid", no_raid)
        if soft_raid_devices is not None:
            pulumi.set(__self__, "soft_raid_devices", soft_raid_devices)

    @property
    @pulumi.getter(name="customHostname")
    def custom_hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Personnal hostname to use in server reinstallation
        """
        return pulumi.get(self, "custom_hostname")

    @custom_hostname.setter
    def custom_hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_hostname", value)

    @property
    @pulumi.getter(name="diskGroupId")
    def disk_group_id(self) -> Optional[pulumi.Input[float]]:
        """
        Disk group id to process install on (only available for some templates)
        """
        return pulumi.get(self, "disk_group_id")

    @disk_group_id.setter
    def disk_group_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "disk_group_id", value)

    @property
    @pulumi.getter(name="noRaid")
    def no_raid(self) -> Optional[pulumi.Input[bool]]:
        """
        true if you want to install only on the first disk
        """
        return pulumi.get(self, "no_raid")

    @no_raid.setter
    def no_raid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_raid", value)

    @property
    @pulumi.getter(name="softRaidDevices")
    def soft_raid_devices(self) -> Optional[pulumi.Input[float]]:
        """
        Number of devices to use for system's software RAID
        """
        return pulumi.get(self, "soft_raid_devices")

    @soft_raid_devices.setter
    def soft_raid_devices(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "soft_raid_devices", value)


if not MYPY:
    class ServerIamArgsDict(TypedDict):
        display_name: NotRequired[pulumi.Input[str]]
        """
        Resource display name
        """
        id: NotRequired[pulumi.Input[str]]
        """
        Unique identifier of the resource in the IAM
        """
        tags: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[str]]]]
        """
        Resource tags. Tags that were internally computed are prefixed with `ovh:`
        """
        urn: NotRequired[pulumi.Input[str]]
        """
        URN of the private database, used when writing IAM policies
        """
elif False:
    ServerIamArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerIamArgs:
    def __init__(__self__, *,
                 display_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 urn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] display_name: Resource display name
        :param pulumi.Input[str] id: Unique identifier of the resource in the IAM
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags. Tags that were internally computed are prefixed with `ovh:`
        :param pulumi.Input[str] urn: URN of the private database, used when writing IAM policies
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if urn is not None:
            pulumi.set(__self__, "urn", urn)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource display name
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique identifier of the resource in the IAM
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags. Tags that were internally computed are prefixed with `ovh:`
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def urn(self) -> Optional[pulumi.Input[str]]:
        """
        URN of the private database, used when writing IAM policies
        """
        return pulumi.get(self, "urn")

    @urn.setter
    def urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "urn", value)


if not MYPY:
    class ServerInstallTaskDetailsArgsDict(TypedDict):
        custom_hostname: NotRequired[pulumi.Input[str]]
        """
        Set up the server using the provided hostname instead of the default hostname.
        """
        disk_group_id: NotRequired[pulumi.Input[int]]
        """
        Disk group id.
        """
        no_raid: NotRequired[pulumi.Input[bool]]
        """
        Set to true to disable RAID.
        """
        soft_raid_devices: NotRequired[pulumi.Input[int]]
        """
        soft raid devices.
        """
elif False:
    ServerInstallTaskDetailsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerInstallTaskDetailsArgs:
    def __init__(__self__, *,
                 custom_hostname: Optional[pulumi.Input[str]] = None,
                 disk_group_id: Optional[pulumi.Input[int]] = None,
                 no_raid: Optional[pulumi.Input[bool]] = None,
                 soft_raid_devices: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] custom_hostname: Set up the server using the provided hostname instead of the default hostname.
        :param pulumi.Input[int] disk_group_id: Disk group id.
        :param pulumi.Input[bool] no_raid: Set to true to disable RAID.
        :param pulumi.Input[int] soft_raid_devices: soft raid devices.
        """
        if custom_hostname is not None:
            pulumi.set(__self__, "custom_hostname", custom_hostname)
        if disk_group_id is not None:
            pulumi.set(__self__, "disk_group_id", disk_group_id)
        if no_raid is not None:
            pulumi.set(__self__, "no_raid", no_raid)
        if soft_raid_devices is not None:
            pulumi.set(__self__, "soft_raid_devices", soft_raid_devices)

    @property
    @pulumi.getter(name="customHostname")
    def custom_hostname(self) -> Optional[pulumi.Input[str]]:
        """
        Set up the server using the provided hostname instead of the default hostname.
        """
        return pulumi.get(self, "custom_hostname")

    @custom_hostname.setter
    def custom_hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_hostname", value)

    @property
    @pulumi.getter(name="diskGroupId")
    def disk_group_id(self) -> Optional[pulumi.Input[int]]:
        """
        Disk group id.
        """
        return pulumi.get(self, "disk_group_id")

    @disk_group_id.setter
    def disk_group_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "disk_group_id", value)

    @property
    @pulumi.getter(name="noRaid")
    def no_raid(self) -> Optional[pulumi.Input[bool]]:
        """
        Set to true to disable RAID.
        """
        return pulumi.get(self, "no_raid")

    @no_raid.setter
    def no_raid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_raid", value)

    @property
    @pulumi.getter(name="softRaidDevices")
    def soft_raid_devices(self) -> Optional[pulumi.Input[int]]:
        """
        soft raid devices.
        """
        return pulumi.get(self, "soft_raid_devices")

    @soft_raid_devices.setter
    def soft_raid_devices(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "soft_raid_devices", value)


if not MYPY:
    class ServerInstallTaskUserMetadataArgsDict(TypedDict):
        key: pulumi.Input[str]
        """
        The key for the user_metadata
        """
        value: pulumi.Input[str]
        """
        The value for the user_metadata
        """
elif False:
    ServerInstallTaskUserMetadataArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerInstallTaskUserMetadataArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] key: The key for the user_metadata
        :param pulumi.Input[str] value: The value for the user_metadata
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key for the user_metadata
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value for the user_metadata
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


if not MYPY:
    class ServerNetworkingInterfaceArgsDict(TypedDict):
        macs: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        Interface Mac address
        """
        type: pulumi.Input[str]
        """
        Interface type
        """
elif False:
    ServerNetworkingInterfaceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerNetworkingInterfaceArgs:
    def __init__(__self__, *,
                 macs: pulumi.Input[Sequence[pulumi.Input[str]]],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] macs: Interface Mac address
        :param pulumi.Input[str] type: Interface type
        """
        pulumi.set(__self__, "macs", macs)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def macs(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Interface Mac address
        """
        return pulumi.get(self, "macs")

    @macs.setter
    def macs(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "macs", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Interface type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


if not MYPY:
    class ServerOrderArgsDict(TypedDict):
        date: NotRequired[pulumi.Input[str]]
        details: NotRequired[pulumi.Input[Sequence[pulumi.Input['ServerOrderDetailArgsDict']]]]
        """
        Details object when reinstalling server (see https://eu.api.ovh.com/console/?section=%2Fdedicated%2Fserver&branch=v1#post-/dedicated/server/-serviceName-/install/start)
        """
        expiration_date: NotRequired[pulumi.Input[str]]
        order_id: NotRequired[pulumi.Input[float]]
elif False:
    ServerOrderArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerOrderArgs:
    def __init__(__self__, *,
                 date: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[Sequence[pulumi.Input['ServerOrderDetailArgs']]]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 order_id: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['ServerOrderDetailArgs']]] details: Details object when reinstalling server (see https://eu.api.ovh.com/console/?section=%2Fdedicated%2Fserver&branch=v1#post-/dedicated/server/-serviceName-/install/start)
        """
        if date is not None:
            pulumi.set(__self__, "date", date)
        if details is not None:
            pulumi.set(__self__, "details", details)
        if expiration_date is not None:
            pulumi.set(__self__, "expiration_date", expiration_date)
        if order_id is not None:
            pulumi.set(__self__, "order_id", order_id)

    @property
    @pulumi.getter
    def date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "date")

    @date.setter
    def date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "date", value)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerOrderDetailArgs']]]]:
        """
        Details object when reinstalling server (see https://eu.api.ovh.com/console/?section=%2Fdedicated%2Fserver&branch=v1#post-/dedicated/server/-serviceName-/install/start)
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerOrderDetailArgs']]]]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expiration_date")

    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_date", value)

    @property
    @pulumi.getter(name="orderId")
    def order_id(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "order_id")

    @order_id.setter
    def order_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "order_id", value)


if not MYPY:
    class ServerOrderDetailArgsDict(TypedDict):
        description: NotRequired[pulumi.Input[str]]
        detail_type: NotRequired[pulumi.Input[str]]
        """
        Product type of item in order
        """
        domain: NotRequired[pulumi.Input[str]]
        order_detail_id: NotRequired[pulumi.Input[float]]
        quantity: NotRequired[pulumi.Input[str]]
elif False:
    ServerOrderDetailArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerOrderDetailArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 detail_type: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 order_detail_id: Optional[pulumi.Input[float]] = None,
                 quantity: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] detail_type: Product type of item in order
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if detail_type is not None:
            pulumi.set(__self__, "detail_type", detail_type)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if order_detail_id is not None:
            pulumi.set(__self__, "order_detail_id", order_detail_id)
        if quantity is not None:
            pulumi.set(__self__, "quantity", quantity)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="detailType")
    def detail_type(self) -> Optional[pulumi.Input[str]]:
        """
        Product type of item in order
        """
        return pulumi.get(self, "detail_type")

    @detail_type.setter
    def detail_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detail_type", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="orderDetailId")
    def order_detail_id(self) -> Optional[pulumi.Input[float]]:
        return pulumi.get(self, "order_detail_id")

    @order_detail_id.setter
    def order_detail_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "order_detail_id", value)

    @property
    @pulumi.getter
    def quantity(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "quantity")

    @quantity.setter
    def quantity(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "quantity", value)


if not MYPY:
    class ServerPlanArgsDict(TypedDict):
        duration: pulumi.Input[str]
        """
        Duration selected for the purchase of the product
        """
        plan_code: pulumi.Input[str]
        """
        Identifier of the option offer
        """
        pricing_mode: pulumi.Input[str]
        """
        Pricing mode selected for the purchase of the product
        """
        configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input['ServerPlanConfigurationArgsDict']]]]
        item_id: NotRequired[pulumi.Input[float]]
        """
        Cart item to be linked
        """
        quantity: NotRequired[pulumi.Input[float]]
        """
        Quantity of product desired
        """
elif False:
    ServerPlanArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerPlanArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[str],
                 plan_code: pulumi.Input[str],
                 pricing_mode: pulumi.Input[str],
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ServerPlanConfigurationArgs']]]] = None,
                 item_id: Optional[pulumi.Input[float]] = None,
                 quantity: Optional[pulumi.Input[float]] = None):
        """
        :param pulumi.Input[str] duration: Duration selected for the purchase of the product
        :param pulumi.Input[str] plan_code: Identifier of the option offer
        :param pulumi.Input[str] pricing_mode: Pricing mode selected for the purchase of the product
        :param pulumi.Input[float] item_id: Cart item to be linked
        :param pulumi.Input[float] quantity: Quantity of product desired
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "plan_code", plan_code)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        if configurations is not None:
            pulumi.set(__self__, "configurations", configurations)
        if item_id is not None:
            pulumi.set(__self__, "item_id", item_id)
        if quantity is not None:
            pulumi.set(__self__, "quantity", quantity)

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[str]:
        """
        Duration selected for the purchase of the product
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter(name="planCode")
    def plan_code(self) -> pulumi.Input[str]:
        """
        Identifier of the option offer
        """
        return pulumi.get(self, "plan_code")

    @plan_code.setter
    def plan_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "plan_code", value)

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> pulumi.Input[str]:
        """
        Pricing mode selected for the purchase of the product
        """
        return pulumi.get(self, "pricing_mode")

    @pricing_mode.setter
    def pricing_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "pricing_mode", value)

    @property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerPlanConfigurationArgs']]]]:
        return pulumi.get(self, "configurations")

    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerPlanConfigurationArgs']]]]):
        pulumi.set(self, "configurations", value)

    @property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[float]]:
        """
        Cart item to be linked
        """
        return pulumi.get(self, "item_id")

    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "item_id", value)

    @property
    @pulumi.getter
    def quantity(self) -> Optional[pulumi.Input[float]]:
        """
        Quantity of product desired
        """
        return pulumi.get(self, "quantity")

    @quantity.setter
    def quantity(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "quantity", value)


if not MYPY:
    class ServerPlanConfigurationArgsDict(TypedDict):
        label: pulumi.Input[str]
        """
        Label for your configuration item
        """
        value: pulumi.Input[str]
        """
        Value or resource URL on API.OVH.COM of your configuration item
        """
elif False:
    ServerPlanConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerPlanConfigurationArgs:
    def __init__(__self__, *,
                 label: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] label: Label for your configuration item
        :param pulumi.Input[str] value: Value or resource URL on API.OVH.COM of your configuration item
        """
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        Label for your configuration item
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Value or resource URL on API.OVH.COM of your configuration item
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


if not MYPY:
    class ServerPlanOptionArgsDict(TypedDict):
        duration: pulumi.Input[str]
        """
        Duration selected for the purchase of the product
        """
        plan_code: pulumi.Input[str]
        """
        Identifier of the option offer
        """
        pricing_mode: pulumi.Input[str]
        """
        Pricing mode selected for the purchase of the product
        """
        quantity: pulumi.Input[float]
        """
        Quantity of product desired
        """
        configurations: NotRequired[pulumi.Input[Sequence[pulumi.Input['ServerPlanOptionConfigurationArgsDict']]]]
elif False:
    ServerPlanOptionArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerPlanOptionArgs:
    def __init__(__self__, *,
                 duration: pulumi.Input[str],
                 plan_code: pulumi.Input[str],
                 pricing_mode: pulumi.Input[str],
                 quantity: pulumi.Input[float],
                 configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ServerPlanOptionConfigurationArgs']]]] = None):
        """
        :param pulumi.Input[str] duration: Duration selected for the purchase of the product
        :param pulumi.Input[str] plan_code: Identifier of the option offer
        :param pulumi.Input[str] pricing_mode: Pricing mode selected for the purchase of the product
        :param pulumi.Input[float] quantity: Quantity of product desired
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "plan_code", plan_code)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        pulumi.set(__self__, "quantity", quantity)
        if configurations is not None:
            pulumi.set(__self__, "configurations", configurations)

    @property
    @pulumi.getter
    def duration(self) -> pulumi.Input[str]:
        """
        Duration selected for the purchase of the product
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: pulumi.Input[str]):
        pulumi.set(self, "duration", value)

    @property
    @pulumi.getter(name="planCode")
    def plan_code(self) -> pulumi.Input[str]:
        """
        Identifier of the option offer
        """
        return pulumi.get(self, "plan_code")

    @plan_code.setter
    def plan_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "plan_code", value)

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> pulumi.Input[str]:
        """
        Pricing mode selected for the purchase of the product
        """
        return pulumi.get(self, "pricing_mode")

    @pricing_mode.setter
    def pricing_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "pricing_mode", value)

    @property
    @pulumi.getter
    def quantity(self) -> pulumi.Input[float]:
        """
        Quantity of product desired
        """
        return pulumi.get(self, "quantity")

    @quantity.setter
    def quantity(self, value: pulumi.Input[float]):
        pulumi.set(self, "quantity", value)

    @property
    @pulumi.getter
    def configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerPlanOptionConfigurationArgs']]]]:
        return pulumi.get(self, "configurations")

    @configurations.setter
    def configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerPlanOptionConfigurationArgs']]]]):
        pulumi.set(self, "configurations", value)


if not MYPY:
    class ServerPlanOptionConfigurationArgsDict(TypedDict):
        label: pulumi.Input[str]
        """
        Label for your configuration item
        """
        value: pulumi.Input[str]
        """
        Value or resource URL on API.OVH.COM of your configuration item
        """
elif False:
    ServerPlanOptionConfigurationArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerPlanOptionConfigurationArgs:
    def __init__(__self__, *,
                 label: pulumi.Input[str],
                 value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] label: Label for your configuration item
        :param pulumi.Input[str] value: Value or resource URL on API.OVH.COM of your configuration item
        """
        pulumi.set(__self__, "label", label)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def label(self) -> pulumi.Input[str]:
        """
        Label for your configuration item
        """
        return pulumi.get(self, "label")

    @label.setter
    def label(self, value: pulumi.Input[str]):
        pulumi.set(self, "label", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        Value or resource URL on API.OVH.COM of your configuration item
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


if not MYPY:
    class ServerUserMetadataArgsDict(TypedDict):
        key: NotRequired[pulumi.Input[str]]
        value: NotRequired[pulumi.Input[str]]
elif False:
    ServerUserMetadataArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ServerUserMetadataArgs:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


