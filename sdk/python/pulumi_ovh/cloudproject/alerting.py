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

__all__ = ['AlertingArgs', 'Alerting']

@pulumi.input_type
class AlertingArgs:
    def __init__(__self__, *,
                 delay: pulumi.Input[float],
                 email: pulumi.Input[str],
                 monthly_threshold: pulumi.Input[float],
                 service_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a Alerting resource.
        :param pulumi.Input[float] delay: Delay between two alerts in seconds
        :param pulumi.Input[str] email: Email to contact
        :param pulumi.Input[float] monthly_threshold: Monthly threshold for this alerting in currency
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        pulumi.set(__self__, "delay", delay)
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "monthly_threshold", monthly_threshold)
        pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter
    def delay(self) -> pulumi.Input[float]:
        """
        Delay between two alerts in seconds
        """
        return pulumi.get(self, "delay")

    @delay.setter
    def delay(self, value: pulumi.Input[float]):
        pulumi.set(self, "delay", value)

    @property
    @pulumi.getter
    def email(self) -> pulumi.Input[str]:
        """
        Email to contact
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: pulumi.Input[str]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="monthlyThreshold")
    def monthly_threshold(self) -> pulumi.Input[float]:
        """
        Monthly threshold for this alerting in currency
        """
        return pulumi.get(self, "monthly_threshold")

    @monthly_threshold.setter
    def monthly_threshold(self, value: pulumi.Input[float]):
        pulumi.set(self, "monthly_threshold", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)


@pulumi.input_type
class _AlertingState:
    def __init__(__self__, *,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 delay: Optional[pulumi.Input[float]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 formatted_monthly_threshold: Optional[pulumi.Input['AlertingFormattedMonthlyThresholdArgs']] = None,
                 monthly_threshold: Optional[pulumi.Input[float]] = None,
                 service_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Alerting resources.
        :param pulumi.Input[str] creation_date: Alerting creation date
        :param pulumi.Input[float] delay: Delay between two alerts in seconds
        :param pulumi.Input[str] email: Email to contact
        :param pulumi.Input['AlertingFormattedMonthlyThresholdArgs'] formatted_monthly_threshold: Formatted monthly threshold for this alerting
        :param pulumi.Input[float] monthly_threshold: Monthly threshold for this alerting in currency
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        if creation_date is not None:
            pulumi.set(__self__, "creation_date", creation_date)
        if delay is not None:
            pulumi.set(__self__, "delay", delay)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if formatted_monthly_threshold is not None:
            pulumi.set(__self__, "formatted_monthly_threshold", formatted_monthly_threshold)
        if monthly_threshold is not None:
            pulumi.set(__self__, "monthly_threshold", monthly_threshold)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[str]]:
        """
        Alerting creation date
        """
        return pulumi.get(self, "creation_date")

    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_date", value)

    @property
    @pulumi.getter
    def delay(self) -> Optional[pulumi.Input[float]]:
        """
        Delay between two alerts in seconds
        """
        return pulumi.get(self, "delay")

    @delay.setter
    def delay(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "delay", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email to contact
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="formattedMonthlyThreshold")
    def formatted_monthly_threshold(self) -> Optional[pulumi.Input['AlertingFormattedMonthlyThresholdArgs']]:
        """
        Formatted monthly threshold for this alerting
        """
        return pulumi.get(self, "formatted_monthly_threshold")

    @formatted_monthly_threshold.setter
    def formatted_monthly_threshold(self, value: Optional[pulumi.Input['AlertingFormattedMonthlyThresholdArgs']]):
        pulumi.set(self, "formatted_monthly_threshold", value)

    @property
    @pulumi.getter(name="monthlyThreshold")
    def monthly_threshold(self) -> Optional[pulumi.Input[float]]:
        """
        Monthly threshold for this alerting in currency
        """
        return pulumi.get(self, "monthly_threshold")

    @monthly_threshold.setter
    def monthly_threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "monthly_threshold", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)


class Alerting(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delay: Optional[pulumi.Input[float]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 monthly_threshold: Optional[pulumi.Input[float]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates an alert on a public cloud project.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        my_alert = ovh.cloud_project.Alerting("myAlert",
            delay=3600,
            email="aaa.bbb@domain.com",
            monthly_threshold=1000,
            service_name="XXX")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] delay: Delay between two alerts in seconds
        :param pulumi.Input[str] email: Email to contact
        :param pulumi.Input[float] monthly_threshold: Monthly threshold for this alerting in currency
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates an alert on a public cloud project.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        my_alert = ovh.cloud_project.Alerting("myAlert",
            delay=3600,
            email="aaa.bbb@domain.com",
            monthly_threshold=1000,
            service_name="XXX")
        ```

        :param str resource_name: The name of the resource.
        :param AlertingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delay: Optional[pulumi.Input[float]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 monthly_threshold: Optional[pulumi.Input[float]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlertingArgs.__new__(AlertingArgs)

            if delay is None and not opts.urn:
                raise TypeError("Missing required property 'delay'")
            __props__.__dict__["delay"] = delay
            if email is None and not opts.urn:
                raise TypeError("Missing required property 'email'")
            __props__.__dict__["email"] = email
            if monthly_threshold is None and not opts.urn:
                raise TypeError("Missing required property 'monthly_threshold'")
            __props__.__dict__["monthly_threshold"] = monthly_threshold
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["formatted_monthly_threshold"] = None
        super(Alerting, __self__).__init__(
            'ovh:CloudProject/alerting:Alerting',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            creation_date: Optional[pulumi.Input[str]] = None,
            delay: Optional[pulumi.Input[float]] = None,
            email: Optional[pulumi.Input[str]] = None,
            formatted_monthly_threshold: Optional[pulumi.Input[Union['AlertingFormattedMonthlyThresholdArgs', 'AlertingFormattedMonthlyThresholdArgsDict']]] = None,
            monthly_threshold: Optional[pulumi.Input[float]] = None,
            service_name: Optional[pulumi.Input[str]] = None) -> 'Alerting':
        """
        Get an existing Alerting resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] creation_date: Alerting creation date
        :param pulumi.Input[float] delay: Delay between two alerts in seconds
        :param pulumi.Input[str] email: Email to contact
        :param pulumi.Input[Union['AlertingFormattedMonthlyThresholdArgs', 'AlertingFormattedMonthlyThresholdArgsDict']] formatted_monthly_threshold: Formatted monthly threshold for this alerting
        :param pulumi.Input[float] monthly_threshold: Monthly threshold for this alerting in currency
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AlertingState.__new__(_AlertingState)

        __props__.__dict__["creation_date"] = creation_date
        __props__.__dict__["delay"] = delay
        __props__.__dict__["email"] = email
        __props__.__dict__["formatted_monthly_threshold"] = formatted_monthly_threshold
        __props__.__dict__["monthly_threshold"] = monthly_threshold
        __props__.__dict__["service_name"] = service_name
        return Alerting(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        Alerting creation date
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def delay(self) -> pulumi.Output[float]:
        """
        Delay between two alerts in seconds
        """
        return pulumi.get(self, "delay")

    @property
    @pulumi.getter
    def email(self) -> pulumi.Output[str]:
        """
        Email to contact
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="formattedMonthlyThreshold")
    def formatted_monthly_threshold(self) -> pulumi.Output['outputs.AlertingFormattedMonthlyThreshold']:
        """
        Formatted monthly threshold for this alerting
        """
        return pulumi.get(self, "formatted_monthly_threshold")

    @property
    @pulumi.getter(name="monthlyThreshold")
    def monthly_threshold(self) -> pulumi.Output[float]:
        """
        Monthly threshold for this alerting in currency
        """
        return pulumi.get(self, "monthly_threshold")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

