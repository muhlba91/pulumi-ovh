# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UdpFrontendArgs', 'UdpFrontend']

@pulumi.input_type
class UdpFrontendArgs:
    def __init__(__self__, *,
                 port: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 zone: pulumi.Input[str],
                 dedicated_ipfos: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_farm_id: Optional[pulumi.Input[float]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UdpFrontend resource.
        :param pulumi.Input[str] port: Port(s) attached to your frontend. Supports single port (numerical value), 
               range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
               and/or 'range'. Each port must be in the [1;49151] range
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] zone: Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dedicated_ipfos: Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        :param pulumi.Input[float] default_farm_id: Default UDP Farm of your frontend
        :param pulumi.Input[bool] disabled: Disable your frontend. Default: 'false'
        :param pulumi.Input[str] display_name: Human readable name for your frontend
        """
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "zone", zone)
        if dedicated_ipfos is not None:
            pulumi.set(__self__, "dedicated_ipfos", dedicated_ipfos)
        if default_farm_id is not None:
            pulumi.set(__self__, "default_farm_id", default_farm_id)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[str]:
        """
        Port(s) attached to your frontend. Supports single port (numerical value), 
        range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        and/or 'range'. Each port must be in the [1;49151] range
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[str]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Input[str]:
        """
        Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: pulumi.Input[str]):
        pulumi.set(self, "zone", value)

    @property
    @pulumi.getter(name="dedicatedIpfos")
    def dedicated_ipfos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        """
        return pulumi.get(self, "dedicated_ipfos")

    @dedicated_ipfos.setter
    def dedicated_ipfos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dedicated_ipfos", value)

    @property
    @pulumi.getter(name="defaultFarmId")
    def default_farm_id(self) -> Optional[pulumi.Input[float]]:
        """
        Default UDP Farm of your frontend
        """
        return pulumi.get(self, "default_farm_id")

    @default_farm_id.setter
    def default_farm_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "default_farm_id", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable your frontend. Default: 'false'
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for your frontend
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


@pulumi.input_type
class _UdpFrontendState:
    def __init__(__self__, *,
                 dedicated_ipfos: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_farm_id: Optional[pulumi.Input[float]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 frontend_id: Optional[pulumi.Input[float]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering UdpFrontend resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dedicated_ipfos: Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        :param pulumi.Input[float] default_farm_id: Default UDP Farm of your frontend
        :param pulumi.Input[bool] disabled: Disable your frontend. Default: 'false'
        :param pulumi.Input[str] display_name: Human readable name for your frontend
        :param pulumi.Input[float] frontend_id: Id of your frontend
        :param pulumi.Input[str] port: Port(s) attached to your frontend. Supports single port (numerical value), 
               range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
               and/or 'range'. Each port must be in the [1;49151] range
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] zone: Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        """
        if dedicated_ipfos is not None:
            pulumi.set(__self__, "dedicated_ipfos", dedicated_ipfos)
        if default_farm_id is not None:
            pulumi.set(__self__, "default_farm_id", default_farm_id)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if frontend_id is not None:
            pulumi.set(__self__, "frontend_id", frontend_id)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter(name="dedicatedIpfos")
    def dedicated_ipfos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        """
        return pulumi.get(self, "dedicated_ipfos")

    @dedicated_ipfos.setter
    def dedicated_ipfos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "dedicated_ipfos", value)

    @property
    @pulumi.getter(name="defaultFarmId")
    def default_farm_id(self) -> Optional[pulumi.Input[float]]:
        """
        Default UDP Farm of your frontend
        """
        return pulumi.get(self, "default_farm_id")

    @default_farm_id.setter
    def default_farm_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "default_farm_id", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Disable your frontend. Default: 'false'
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Human readable name for your frontend
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> Optional[pulumi.Input[float]]:
        """
        Id of your frontend
        """
        return pulumi.get(self, "frontend_id")

    @frontend_id.setter
    def frontend_id(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "frontend_id", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[str]]:
        """
        Port(s) attached to your frontend. Supports single port (numerical value), 
        range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        and/or 'range'. Each port must be in the [1;49151] range
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


class UdpFrontend(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dedicated_ipfos: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_farm_id: Optional[pulumi.Input[float]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a backend server group (frontend) to be used by loadbalancing frontend(s)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        lb = ovh.IpLoadBalancing.get_ip_load_balancing(service_name="ip-1.2.3.4",
            state="ok")
        testfrontend = ovh.ip_load_balancing.UdpFrontend("testfrontend",
            service_name=lb.service_name,
            display_name="ingress-8080-gra",
            zone="all",
            port="10,11")
        ```

        ## Import

        UDP frontend can be imported using the following format `service_name` and the `id` of the frontend separated by "/" e.g.

        bash

        ```sh
        $ pulumi import ovh:IpLoadBalancing/udpFrontend:UdpFrontend testfrontend service_name/frontend_id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dedicated_ipfos: Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        :param pulumi.Input[float] default_farm_id: Default UDP Farm of your frontend
        :param pulumi.Input[bool] disabled: Disable your frontend. Default: 'false'
        :param pulumi.Input[str] display_name: Human readable name for your frontend
        :param pulumi.Input[str] port: Port(s) attached to your frontend. Supports single port (numerical value), 
               range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
               and/or 'range'. Each port must be in the [1;49151] range
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] zone: Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UdpFrontendArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a backend server group (frontend) to be used by loadbalancing frontend(s)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        lb = ovh.IpLoadBalancing.get_ip_load_balancing(service_name="ip-1.2.3.4",
            state="ok")
        testfrontend = ovh.ip_load_balancing.UdpFrontend("testfrontend",
            service_name=lb.service_name,
            display_name="ingress-8080-gra",
            zone="all",
            port="10,11")
        ```

        ## Import

        UDP frontend can be imported using the following format `service_name` and the `id` of the frontend separated by "/" e.g.

        bash

        ```sh
        $ pulumi import ovh:IpLoadBalancing/udpFrontend:UdpFrontend testfrontend service_name/frontend_id
        ```

        :param str resource_name: The name of the resource.
        :param UdpFrontendArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UdpFrontendArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dedicated_ipfos: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 default_farm_id: Optional[pulumi.Input[float]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UdpFrontendArgs.__new__(UdpFrontendArgs)

            __props__.__dict__["dedicated_ipfos"] = dedicated_ipfos
            __props__.__dict__["default_farm_id"] = default_farm_id
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["display_name"] = display_name
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = port
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if zone is None and not opts.urn:
                raise TypeError("Missing required property 'zone'")
            __props__.__dict__["zone"] = zone
            __props__.__dict__["frontend_id"] = None
        super(UdpFrontend, __self__).__init__(
            'ovh:IpLoadBalancing/udpFrontend:UdpFrontend',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            dedicated_ipfos: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            default_farm_id: Optional[pulumi.Input[float]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            frontend_id: Optional[pulumi.Input[float]] = None,
            port: Optional[pulumi.Input[str]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            zone: Optional[pulumi.Input[str]] = None) -> 'UdpFrontend':
        """
        Get an existing UdpFrontend resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] dedicated_ipfos: Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        :param pulumi.Input[float] default_farm_id: Default UDP Farm of your frontend
        :param pulumi.Input[bool] disabled: Disable your frontend. Default: 'false'
        :param pulumi.Input[str] display_name: Human readable name for your frontend
        :param pulumi.Input[float] frontend_id: Id of your frontend
        :param pulumi.Input[str] port: Port(s) attached to your frontend. Supports single port (numerical value), 
               range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
               and/or 'range'. Each port must be in the [1;49151] range
        :param pulumi.Input[str] service_name: The internal name of your IP load balancing
        :param pulumi.Input[str] zone: Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UdpFrontendState.__new__(_UdpFrontendState)

        __props__.__dict__["dedicated_ipfos"] = dedicated_ipfos
        __props__.__dict__["default_farm_id"] = default_farm_id
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["frontend_id"] = frontend_id
        __props__.__dict__["port"] = port
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["zone"] = zone
        return UdpFrontend(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dedicatedIpfos")
    def dedicated_ipfos(self) -> pulumi.Output[Sequence[str]]:
        """
        Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        """
        return pulumi.get(self, "dedicated_ipfos")

    @property
    @pulumi.getter(name="defaultFarmId")
    def default_farm_id(self) -> pulumi.Output[float]:
        """
        Default UDP Farm of your frontend
        """
        return pulumi.get(self, "default_farm_id")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[bool]:
        """
        Disable your frontend. Default: 'false'
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        Human readable name for your frontend
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="frontendId")
    def frontend_id(self) -> pulumi.Output[float]:
        """
        Id of your frontend
        """
        return pulumi.get(self, "frontend_id")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[str]:
        """
        Port(s) attached to your frontend. Supports single port (numerical value), 
        range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        and/or 'range'. Each port must be in the [1;49151] range
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The internal name of your IP load balancing
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def zone(self) -> pulumi.Output[str]:
        """
        Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        """
        return pulumi.get(self, "zone")

