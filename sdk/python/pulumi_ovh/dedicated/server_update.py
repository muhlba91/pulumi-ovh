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

__all__ = ['ServerUpdateArgs', 'ServerUpdate']

@pulumi.input_type
class ServerUpdateArgs:
    def __init__(__self__, *,
                 service_name: pulumi.Input[str],
                 boot_id: Optional[pulumi.Input[int]] = None,
                 boot_script: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 monitoring: Optional[pulumi.Input[bool]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerUpdate resource.
        :param pulumi.Input[str] service_name: The service_name of your dedicated server.
        :param pulumi.Input[int] boot_id: boot id of the server
        :param pulumi.Input[str] boot_script: boot script of the server
        :param pulumi.Input[str] display_name: display name of the dedicated server
        :param pulumi.Input[bool] monitoring: Icmp monitoring state
        :param pulumi.Input[str] state: error, hacked, hackedBlocked, ok
        """
        pulumi.set(__self__, "service_name", service_name)
        if boot_id is not None:
            pulumi.set(__self__, "boot_id", boot_id)
        if boot_script is not None:
            pulumi.set(__self__, "boot_script", boot_script)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if monitoring is not None:
            pulumi.set(__self__, "monitoring", monitoring)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The service_name of your dedicated server.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="bootId")
    def boot_id(self) -> Optional[pulumi.Input[int]]:
        """
        boot id of the server
        """
        return pulumi.get(self, "boot_id")

    @boot_id.setter
    def boot_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "boot_id", value)

    @property
    @pulumi.getter(name="bootScript")
    def boot_script(self) -> Optional[pulumi.Input[str]]:
        """
        boot script of the server
        """
        return pulumi.get(self, "boot_script")

    @boot_script.setter
    def boot_script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "boot_script", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        display name of the dedicated server
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[bool]]:
        """
        Icmp monitoring state
        """
        return pulumi.get(self, "monitoring")

    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "monitoring", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        error, hacked, hackedBlocked, ok
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class _ServerUpdateState:
    def __init__(__self__, *,
                 boot_id: Optional[pulumi.Input[int]] = None,
                 boot_script: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 monitoring: Optional[pulumi.Input[bool]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServerUpdate resources.
        :param pulumi.Input[int] boot_id: boot id of the server
        :param pulumi.Input[str] boot_script: boot script of the server
        :param pulumi.Input[str] display_name: display name of the dedicated server
        :param pulumi.Input[bool] monitoring: Icmp monitoring state
        :param pulumi.Input[str] service_name: The service_name of your dedicated server.
        :param pulumi.Input[str] state: error, hacked, hackedBlocked, ok
        """
        if boot_id is not None:
            pulumi.set(__self__, "boot_id", boot_id)
        if boot_script is not None:
            pulumi.set(__self__, "boot_script", boot_script)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if monitoring is not None:
            pulumi.set(__self__, "monitoring", monitoring)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="bootId")
    def boot_id(self) -> Optional[pulumi.Input[int]]:
        """
        boot id of the server
        """
        return pulumi.get(self, "boot_id")

    @boot_id.setter
    def boot_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "boot_id", value)

    @property
    @pulumi.getter(name="bootScript")
    def boot_script(self) -> Optional[pulumi.Input[str]]:
        """
        boot script of the server
        """
        return pulumi.get(self, "boot_script")

    @boot_script.setter
    def boot_script(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "boot_script", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        display name of the dedicated server
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def monitoring(self) -> Optional[pulumi.Input[bool]]:
        """
        Icmp monitoring state
        """
        return pulumi.get(self, "monitoring")

    @monitoring.setter
    def monitoring(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "monitoring", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The service_name of your dedicated server.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        error, hacked, hackedBlocked, ok
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class ServerUpdate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boot_id: Optional[pulumi.Input[int]] = None,
                 boot_script: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 monitoring: Optional[pulumi.Input[bool]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        rescue = ovh.Dedicated.get_server_boots(service_name="nsxxxxxxx.ip-xx-xx-xx.eu",
            boot_type="rescue",
            kernel="rescue64-pro")
        server = ovh.dedicated.ServerUpdate("server",
            service_name="nsxxxxxxx.ip-xx-xx-xx.eu",
            boot_id=rescue.results[0],
            monitoring=True,
            state="ok",
            display_name="Some human-readable name")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] boot_id: boot id of the server
        :param pulumi.Input[str] boot_script: boot script of the server
        :param pulumi.Input[str] display_name: display name of the dedicated server
        :param pulumi.Input[bool] monitoring: Icmp monitoring state
        :param pulumi.Input[str] service_name: The service_name of your dedicated server.
        :param pulumi.Input[str] state: error, hacked, hackedBlocked, ok
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerUpdateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        rescue = ovh.Dedicated.get_server_boots(service_name="nsxxxxxxx.ip-xx-xx-xx.eu",
            boot_type="rescue",
            kernel="rescue64-pro")
        server = ovh.dedicated.ServerUpdate("server",
            service_name="nsxxxxxxx.ip-xx-xx-xx.eu",
            boot_id=rescue.results[0],
            monitoring=True,
            state="ok",
            display_name="Some human-readable name")
        ```

        :param str resource_name: The name of the resource.
        :param ServerUpdateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerUpdateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 boot_id: Optional[pulumi.Input[int]] = None,
                 boot_script: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 monitoring: Optional[pulumi.Input[bool]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerUpdateArgs.__new__(ServerUpdateArgs)

            __props__.__dict__["boot_id"] = boot_id
            __props__.__dict__["boot_script"] = boot_script
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["monitoring"] = monitoring
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["state"] = state
        super(ServerUpdate, __self__).__init__(
            'ovh:Dedicated/serverUpdate:ServerUpdate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            boot_id: Optional[pulumi.Input[int]] = None,
            boot_script: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            monitoring: Optional[pulumi.Input[bool]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'ServerUpdate':
        """
        Get an existing ServerUpdate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] boot_id: boot id of the server
        :param pulumi.Input[str] boot_script: boot script of the server
        :param pulumi.Input[str] display_name: display name of the dedicated server
        :param pulumi.Input[bool] monitoring: Icmp monitoring state
        :param pulumi.Input[str] service_name: The service_name of your dedicated server.
        :param pulumi.Input[str] state: error, hacked, hackedBlocked, ok
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServerUpdateState.__new__(_ServerUpdateState)

        __props__.__dict__["boot_id"] = boot_id
        __props__.__dict__["boot_script"] = boot_script
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["monitoring"] = monitoring
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["state"] = state
        return ServerUpdate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bootId")
    def boot_id(self) -> pulumi.Output[int]:
        """
        boot id of the server
        """
        return pulumi.get(self, "boot_id")

    @property
    @pulumi.getter(name="bootScript")
    def boot_script(self) -> pulumi.Output[Optional[str]]:
        """
        boot script of the server
        """
        return pulumi.get(self, "boot_script")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        display name of the dedicated server
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def monitoring(self) -> pulumi.Output[bool]:
        """
        Icmp monitoring state
        """
        return pulumi.get(self, "monitoring")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The service_name of your dedicated server.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        error, hacked, hackedBlocked, ok
        """
        return pulumi.get(self, "state")

