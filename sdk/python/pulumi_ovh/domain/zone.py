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
from ._inputs import *

__all__ = ['ZoneArgs', 'Zone']

@pulumi.input_type
class ZoneArgs:
    def __init__(__self__, *,
                 orders: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]]] = None,
                 ovh_subsidiary: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input['ZonePlanArgs']] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]]] = None):
        """
        The set of arguments for constructing a Zone resource.
        :param pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]] orders: Details about an Order
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input['ZonePlanArgs'] plan: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]] plan_options: Product Plan to order
        """
        if orders is not None:
            pulumi.set(__self__, "orders", orders)
        if ovh_subsidiary is not None:
            pulumi.set(__self__, "ovh_subsidiary", ovh_subsidiary)
        if payment_mean is not None:
            warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
            pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
        if payment_mean is not None:
            pulumi.set(__self__, "payment_mean", payment_mean)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if plan_options is not None:
            pulumi.set(__self__, "plan_options", plan_options)

    @property
    @pulumi.getter
    def orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]]]:
        """
        Details about an Order
        """
        return pulumi.get(self, "orders")

    @orders.setter
    def orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]]]):
        pulumi.set(self, "orders", value)

    @property
    @pulumi.getter(name="ovhSubsidiary")
    def ovh_subsidiary(self) -> Optional[pulumi.Input[str]]:
        """
        OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        """
        return pulumi.get(self, "ovh_subsidiary")

    @ovh_subsidiary.setter
    def ovh_subsidiary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ovh_subsidiary", value)

    @property
    @pulumi.getter(name="paymentMean")
    @_utilities.deprecated("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
    def payment_mean(self) -> Optional[pulumi.Input[str]]:
        """
        Ovh payment mode
        """
        return pulumi.get(self, "payment_mean")

    @payment_mean.setter
    def payment_mean(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payment_mean", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['ZonePlanArgs']]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['ZonePlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="planOptions")
    def plan_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]]]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan_options")

    @plan_options.setter
    def plan_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]]]):
        pulumi.set(self, "plan_options", value)


@pulumi.input_type
class _ZoneState:
    def __init__(__self__, *,
                 zone_urn: Optional[pulumi.Input[str]] = None,
                 dnssec_supported: Optional[pulumi.Input[bool]] = None,
                 has_dns_anycast: Optional[pulumi.Input[bool]] = None,
                 last_update: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 orders: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]]] = None,
                 ovh_subsidiary: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input['ZonePlanArgs']] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]]] = None):
        """
        Input properties used for looking up and filtering Zone resources.
        :param pulumi.Input[bool] dnssec_supported: Is DNSSEC supported by this zone
        :param pulumi.Input[bool] has_dns_anycast: hasDnsAnycast flag of the DNS zone
        :param pulumi.Input[str] last_update: Last update date of the DNS zone
        :param pulumi.Input[str] name: Zone name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] name_servers: Name servers that host the DNS zone
        :param pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]] orders: Details about an Order
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input['ZonePlanArgs'] plan: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]] plan_options: Product Plan to order
        """
        if zone_urn is not None:
            pulumi.set(__self__, "zone_urn", zone_urn)
        if dnssec_supported is not None:
            pulumi.set(__self__, "dnssec_supported", dnssec_supported)
        if has_dns_anycast is not None:
            pulumi.set(__self__, "has_dns_anycast", has_dns_anycast)
        if last_update is not None:
            pulumi.set(__self__, "last_update", last_update)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if name_servers is not None:
            pulumi.set(__self__, "name_servers", name_servers)
        if orders is not None:
            pulumi.set(__self__, "orders", orders)
        if ovh_subsidiary is not None:
            pulumi.set(__self__, "ovh_subsidiary", ovh_subsidiary)
        if payment_mean is not None:
            warnings.warn("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""", DeprecationWarning)
            pulumi.log.warn("""payment_mean is deprecated: This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
        if payment_mean is not None:
            pulumi.set(__self__, "payment_mean", payment_mean)
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if plan_options is not None:
            pulumi.set(__self__, "plan_options", plan_options)

    @property
    @pulumi.getter(name="ZoneURN")
    def zone_urn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "zone_urn")

    @zone_urn.setter
    def zone_urn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone_urn", value)

    @property
    @pulumi.getter(name="dnssecSupported")
    def dnssec_supported(self) -> Optional[pulumi.Input[bool]]:
        """
        Is DNSSEC supported by this zone
        """
        return pulumi.get(self, "dnssec_supported")

    @dnssec_supported.setter
    def dnssec_supported(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dnssec_supported", value)

    @property
    @pulumi.getter(name="hasDnsAnycast")
    def has_dns_anycast(self) -> Optional[pulumi.Input[bool]]:
        """
        hasDnsAnycast flag of the DNS zone
        """
        return pulumi.get(self, "has_dns_anycast")

    @has_dns_anycast.setter
    def has_dns_anycast(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_dns_anycast", value)

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> Optional[pulumi.Input[str]]:
        """
        Last update date of the DNS zone
        """
        return pulumi.get(self, "last_update")

    @last_update.setter
    def last_update(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_update", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Zone name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Name servers that host the DNS zone
        """
        return pulumi.get(self, "name_servers")

    @name_servers.setter
    def name_servers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "name_servers", value)

    @property
    @pulumi.getter
    def orders(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]]]:
        """
        Details about an Order
        """
        return pulumi.get(self, "orders")

    @orders.setter
    def orders(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZoneOrderArgs']]]]):
        pulumi.set(self, "orders", value)

    @property
    @pulumi.getter(name="ovhSubsidiary")
    def ovh_subsidiary(self) -> Optional[pulumi.Input[str]]:
        """
        OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        """
        return pulumi.get(self, "ovh_subsidiary")

    @ovh_subsidiary.setter
    def ovh_subsidiary(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ovh_subsidiary", value)

    @property
    @pulumi.getter(name="paymentMean")
    @_utilities.deprecated("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
    def payment_mean(self) -> Optional[pulumi.Input[str]]:
        """
        Ovh payment mode
        """
        return pulumi.get(self, "payment_mean")

    @payment_mean.setter
    def payment_mean(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "payment_mean", value)

    @property
    @pulumi.getter
    def plan(self) -> Optional[pulumi.Input['ZonePlanArgs']]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan")

    @plan.setter
    def plan(self, value: Optional[pulumi.Input['ZonePlanArgs']]):
        pulumi.set(self, "plan", value)

    @property
    @pulumi.getter(name="planOptions")
    def plan_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]]]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan_options")

    @plan_options.setter
    def plan_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ZonePlanOptionArgs']]]]):
        pulumi.set(self, "plan_options", value)


class Zone(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 orders: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZoneOrderArgs', 'ZoneOrderArgsDict']]]]] = None,
                 ovh_subsidiary: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[Union['ZonePlanArgs', 'ZonePlanArgsDict']]] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZonePlanOptionArgs', 'ZonePlanOptionArgsDict']]]]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        myaccount = ovh.Me.get_me()
        mycart = ovh.Order.get_cart(ovh_subsidiary=myaccount.ovh_subsidiary)
        zone_cart_product_plan = ovh.Order.get_cart_product_plan(cart_id=mycart.id,
            price_capacity="renew",
            product="dns",
            plan_code="zone")
        zone_zone = ovh.domain.Zone("zoneZone",
            ovh_subsidiary=mycart.ovh_subsidiary,
            plan={
                "duration": zone_cart_product_plan.selected_prices[0].duration,
                "plan_code": zone_cart_product_plan.plan_code,
                "pricing_mode": zone_cart_product_plan.selected_prices[0].pricing_mode,
                "configurations": [
                    {
                        "label": "zone",
                        "value": "myzone.mydomain.com",
                    },
                    {
                        "label": "template",
                        "value": "minimized",
                    },
                ],
            })
        ```

        ## Import

        Zone can be imported using its `name`.

        Using the following configuration:

        hcl

        import {

          to = ovh_domain_zone.zone

          id = "<zone name>"

        }

        You can then run:

        bash

        $ pulumi preview -generate-config-out=zone.tf

        $ pulumi up

        The file `zone.tf` will then contain the imported resource's configuration, that can be copied next to the `import` block above.

        See https://developer.hashicorp.com/terraform/language/import/generating-configuration for more details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ZoneOrderArgs', 'ZoneOrderArgsDict']]]] orders: Details about an Order
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input[Union['ZonePlanArgs', 'ZonePlanArgsDict']] plan: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input[Union['ZonePlanOptionArgs', 'ZonePlanOptionArgsDict']]]] plan_options: Product Plan to order
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ZoneArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        myaccount = ovh.Me.get_me()
        mycart = ovh.Order.get_cart(ovh_subsidiary=myaccount.ovh_subsidiary)
        zone_cart_product_plan = ovh.Order.get_cart_product_plan(cart_id=mycart.id,
            price_capacity="renew",
            product="dns",
            plan_code="zone")
        zone_zone = ovh.domain.Zone("zoneZone",
            ovh_subsidiary=mycart.ovh_subsidiary,
            plan={
                "duration": zone_cart_product_plan.selected_prices[0].duration,
                "plan_code": zone_cart_product_plan.plan_code,
                "pricing_mode": zone_cart_product_plan.selected_prices[0].pricing_mode,
                "configurations": [
                    {
                        "label": "zone",
                        "value": "myzone.mydomain.com",
                    },
                    {
                        "label": "template",
                        "value": "minimized",
                    },
                ],
            })
        ```

        ## Import

        Zone can be imported using its `name`.

        Using the following configuration:

        hcl

        import {

          to = ovh_domain_zone.zone

          id = "<zone name>"

        }

        You can then run:

        bash

        $ pulumi preview -generate-config-out=zone.tf

        $ pulumi up

        The file `zone.tf` will then contain the imported resource's configuration, that can be copied next to the `import` block above.

        See https://developer.hashicorp.com/terraform/language/import/generating-configuration for more details.

        :param str resource_name: The name of the resource.
        :param ZoneArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ZoneArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 orders: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZoneOrderArgs', 'ZoneOrderArgsDict']]]]] = None,
                 ovh_subsidiary: Optional[pulumi.Input[str]] = None,
                 payment_mean: Optional[pulumi.Input[str]] = None,
                 plan: Optional[pulumi.Input[Union['ZonePlanArgs', 'ZonePlanArgsDict']]] = None,
                 plan_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZonePlanOptionArgs', 'ZonePlanOptionArgsDict']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ZoneArgs.__new__(ZoneArgs)

            __props__.__dict__["orders"] = orders
            __props__.__dict__["ovh_subsidiary"] = ovh_subsidiary
            __props__.__dict__["payment_mean"] = payment_mean
            __props__.__dict__["plan"] = plan
            __props__.__dict__["plan_options"] = plan_options
            __props__.__dict__["zone_urn"] = None
            __props__.__dict__["dnssec_supported"] = None
            __props__.__dict__["has_dns_anycast"] = None
            __props__.__dict__["last_update"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["name_servers"] = None
        super(Zone, __self__).__init__(
            'ovh:Domain/zone:Zone',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            zone_urn: Optional[pulumi.Input[str]] = None,
            dnssec_supported: Optional[pulumi.Input[bool]] = None,
            has_dns_anycast: Optional[pulumi.Input[bool]] = None,
            last_update: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_servers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            orders: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZoneOrderArgs', 'ZoneOrderArgsDict']]]]] = None,
            ovh_subsidiary: Optional[pulumi.Input[str]] = None,
            payment_mean: Optional[pulumi.Input[str]] = None,
            plan: Optional[pulumi.Input[Union['ZonePlanArgs', 'ZonePlanArgsDict']]] = None,
            plan_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ZonePlanOptionArgs', 'ZonePlanOptionArgsDict']]]]] = None) -> 'Zone':
        """
        Get an existing Zone resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] dnssec_supported: Is DNSSEC supported by this zone
        :param pulumi.Input[bool] has_dns_anycast: hasDnsAnycast flag of the DNS zone
        :param pulumi.Input[str] last_update: Last update date of the DNS zone
        :param pulumi.Input[str] name: Zone name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] name_servers: Name servers that host the DNS zone
        :param pulumi.Input[Sequence[pulumi.Input[Union['ZoneOrderArgs', 'ZoneOrderArgsDict']]]] orders: Details about an Order
        :param pulumi.Input[str] ovh_subsidiary: OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        :param pulumi.Input[str] payment_mean: Ovh payment mode
        :param pulumi.Input[Union['ZonePlanArgs', 'ZonePlanArgsDict']] plan: Product Plan to order
        :param pulumi.Input[Sequence[pulumi.Input[Union['ZonePlanOptionArgs', 'ZonePlanOptionArgsDict']]]] plan_options: Product Plan to order
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ZoneState.__new__(_ZoneState)

        __props__.__dict__["zone_urn"] = zone_urn
        __props__.__dict__["dnssec_supported"] = dnssec_supported
        __props__.__dict__["has_dns_anycast"] = has_dns_anycast
        __props__.__dict__["last_update"] = last_update
        __props__.__dict__["name"] = name
        __props__.__dict__["name_servers"] = name_servers
        __props__.__dict__["orders"] = orders
        __props__.__dict__["ovh_subsidiary"] = ovh_subsidiary
        __props__.__dict__["payment_mean"] = payment_mean
        __props__.__dict__["plan"] = plan
        __props__.__dict__["plan_options"] = plan_options
        return Zone(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ZoneURN")
    def zone_urn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "zone_urn")

    @property
    @pulumi.getter(name="dnssecSupported")
    def dnssec_supported(self) -> pulumi.Output[bool]:
        """
        Is DNSSEC supported by this zone
        """
        return pulumi.get(self, "dnssec_supported")

    @property
    @pulumi.getter(name="hasDnsAnycast")
    def has_dns_anycast(self) -> pulumi.Output[bool]:
        """
        hasDnsAnycast flag of the DNS zone
        """
        return pulumi.get(self, "has_dns_anycast")

    @property
    @pulumi.getter(name="lastUpdate")
    def last_update(self) -> pulumi.Output[str]:
        """
        Last update date of the DNS zone
        """
        return pulumi.get(self, "last_update")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Zone name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nameServers")
    def name_servers(self) -> pulumi.Output[Sequence[str]]:
        """
        Name servers that host the DNS zone
        """
        return pulumi.get(self, "name_servers")

    @property
    @pulumi.getter
    def orders(self) -> pulumi.Output[Sequence['outputs.ZoneOrder']]:
        """
        Details about an Order
        """
        return pulumi.get(self, "orders")

    @property
    @pulumi.getter(name="ovhSubsidiary")
    def ovh_subsidiary(self) -> pulumi.Output[str]:
        """
        OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
        """
        return pulumi.get(self, "ovh_subsidiary")

    @property
    @pulumi.getter(name="paymentMean")
    @_utilities.deprecated("""This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.""")
    def payment_mean(self) -> pulumi.Output[Optional[str]]:
        """
        Ovh payment mode
        """
        return pulumi.get(self, "payment_mean")

    @property
    @pulumi.getter
    def plan(self) -> pulumi.Output['outputs.ZonePlan']:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="planOptions")
    def plan_options(self) -> pulumi.Output[Optional[Sequence['outputs.ZonePlanOption']]]:
        """
        Product Plan to order
        """
        return pulumi.get(self, "plan_options")

