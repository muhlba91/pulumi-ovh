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

__all__ = ['ServiceKeyArgs', 'ServiceKey']

@pulumi.input_type
class ServiceKeyArgs:
    def __init__(__self__, *,
                 okms_id: pulumi.Input[str],
                 operations: pulumi.Input[Sequence[pulumi.Input[str]]],
                 type: pulumi.Input[str],
                 context: Optional[pulumi.Input[str]] = None,
                 curve: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a ServiceKey resource.
        :param pulumi.Input[str] okms_id: Okms ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: The operations for which the key is intended to be used
        :param pulumi.Input[str] type: Type of the key to be created
        :param pulumi.Input[str] context: Context of the key
        :param pulumi.Input[str] curve: Curve type for Elliptic Curve (EC) keys
        :param pulumi.Input[str] name: Key name
        :param pulumi.Input[float] size: Size of the key to be created
        """
        pulumi.set(__self__, "okms_id", okms_id)
        pulumi.set(__self__, "operations", operations)
        pulumi.set(__self__, "type", type)
        if context is not None:
            pulumi.set(__self__, "context", context)
        if curve is not None:
            pulumi.set(__self__, "curve", curve)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter(name="okmsId")
    def okms_id(self) -> pulumi.Input[str]:
        """
        Okms ID
        """
        return pulumi.get(self, "okms_id")

    @okms_id.setter
    def okms_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "okms_id", value)

    @property
    @pulumi.getter
    def operations(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The operations for which the key is intended to be used
        """
        return pulumi.get(self, "operations")

    @operations.setter
    def operations(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "operations", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of the key to be created
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        Context of the key
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter
    def curve(self) -> Optional[pulumi.Input[str]]:
        """
        Curve type for Elliptic Curve (EC) keys
        """
        return pulumi.get(self, "curve")

    @curve.setter
    def curve(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "curve", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Key name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[float]]:
        """
        Size of the key to be created
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size", value)


@pulumi.input_type
class _ServiceKeyState:
    def __init__(__self__, *,
                 context: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 curve: Optional[pulumi.Input[str]] = None,
                 deactivation_reason: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okms_id: Optional[pulumi.Input[str]] = None,
                 operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ServiceKey resources.
        :param pulumi.Input[str] context: Context of the key
        :param pulumi.Input[str] created_at: Creation time of the key
        :param pulumi.Input[str] curve: Curve type for Elliptic Curve (EC) keys
        :param pulumi.Input[str] deactivation_reason: Key deactivation reason
        :param pulumi.Input[str] name: Key name
        :param pulumi.Input[str] okms_id: Okms ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: The operations for which the key is intended to be used
        :param pulumi.Input[float] size: Size of the key to be created
        :param pulumi.Input[str] state: State of the key
        :param pulumi.Input[str] type: Type of the key to be created
        """
        if context is not None:
            pulumi.set(__self__, "context", context)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if curve is not None:
            pulumi.set(__self__, "curve", curve)
        if deactivation_reason is not None:
            pulumi.set(__self__, "deactivation_reason", deactivation_reason)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if okms_id is not None:
            pulumi.set(__self__, "okms_id", okms_id)
        if operations is not None:
            pulumi.set(__self__, "operations", operations)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def context(self) -> Optional[pulumi.Input[str]]:
        """
        Context of the key
        """
        return pulumi.get(self, "context")

    @context.setter
    def context(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "context", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Creation time of the key
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def curve(self) -> Optional[pulumi.Input[str]]:
        """
        Curve type for Elliptic Curve (EC) keys
        """
        return pulumi.get(self, "curve")

    @curve.setter
    def curve(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "curve", value)

    @property
    @pulumi.getter(name="deactivationReason")
    def deactivation_reason(self) -> Optional[pulumi.Input[str]]:
        """
        Key deactivation reason
        """
        return pulumi.get(self, "deactivation_reason")

    @deactivation_reason.setter
    def deactivation_reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deactivation_reason", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Key name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="okmsId")
    def okms_id(self) -> Optional[pulumi.Input[str]]:
        """
        Okms ID
        """
        return pulumi.get(self, "okms_id")

    @okms_id.setter
    def okms_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "okms_id", value)

    @property
    @pulumi.getter
    def operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The operations for which the key is intended to be used
        """
        return pulumi.get(self, "operations")

    @operations.setter
    def operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "operations", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[float]]:
        """
        Size of the key to be created
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        State of the key
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the key to be created
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class ServiceKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 curve: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okms_id: Optional[pulumi.Input[str]] = None,
                 operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a Service Key in an OVHcloud KMS.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context: Context of the key
        :param pulumi.Input[str] curve: Curve type for Elliptic Curve (EC) keys
        :param pulumi.Input[str] name: Key name
        :param pulumi.Input[str] okms_id: Okms ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: The operations for which the key is intended to be used
        :param pulumi.Input[float] size: Size of the key to be created
        :param pulumi.Input[str] type: Type of the key to be created
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a Service Key in an OVHcloud KMS.

        :param str resource_name: The name of the resource.
        :param ServiceKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 context: Optional[pulumi.Input[str]] = None,
                 curve: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 okms_id: Optional[pulumi.Input[str]] = None,
                 operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceKeyArgs.__new__(ServiceKeyArgs)

            __props__.__dict__["context"] = context
            __props__.__dict__["curve"] = curve
            __props__.__dict__["name"] = name
            if okms_id is None and not opts.urn:
                raise TypeError("Missing required property 'okms_id'")
            __props__.__dict__["okms_id"] = okms_id
            if operations is None and not opts.urn:
                raise TypeError("Missing required property 'operations'")
            __props__.__dict__["operations"] = operations
            __props__.__dict__["size"] = size
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["created_at"] = None
            __props__.__dict__["deactivation_reason"] = None
            __props__.__dict__["state"] = None
        super(ServiceKey, __self__).__init__(
            'ovh:Okms/serviceKey:ServiceKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            context: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            curve: Optional[pulumi.Input[str]] = None,
            deactivation_reason: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            okms_id: Optional[pulumi.Input[str]] = None,
            operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            size: Optional[pulumi.Input[float]] = None,
            state: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'ServiceKey':
        """
        Get an existing ServiceKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] context: Context of the key
        :param pulumi.Input[str] created_at: Creation time of the key
        :param pulumi.Input[str] curve: Curve type for Elliptic Curve (EC) keys
        :param pulumi.Input[str] deactivation_reason: Key deactivation reason
        :param pulumi.Input[str] name: Key name
        :param pulumi.Input[str] okms_id: Okms ID
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: The operations for which the key is intended to be used
        :param pulumi.Input[float] size: Size of the key to be created
        :param pulumi.Input[str] state: State of the key
        :param pulumi.Input[str] type: Type of the key to be created
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceKeyState.__new__(_ServiceKeyState)

        __props__.__dict__["context"] = context
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["curve"] = curve
        __props__.__dict__["deactivation_reason"] = deactivation_reason
        __props__.__dict__["name"] = name
        __props__.__dict__["okms_id"] = okms_id
        __props__.__dict__["operations"] = operations
        __props__.__dict__["size"] = size
        __props__.__dict__["state"] = state
        __props__.__dict__["type"] = type
        return ServiceKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def context(self) -> pulumi.Output[str]:
        """
        Context of the key
        """
        return pulumi.get(self, "context")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Creation time of the key
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def curve(self) -> pulumi.Output[str]:
        """
        Curve type for Elliptic Curve (EC) keys
        """
        return pulumi.get(self, "curve")

    @property
    @pulumi.getter(name="deactivationReason")
    def deactivation_reason(self) -> pulumi.Output[str]:
        """
        Key deactivation reason
        """
        return pulumi.get(self, "deactivation_reason")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Key name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="okmsId")
    def okms_id(self) -> pulumi.Output[str]:
        """
        Okms ID
        """
        return pulumi.get(self, "okms_id")

    @property
    @pulumi.getter
    def operations(self) -> pulumi.Output[Sequence[str]]:
        """
        The operations for which the key is intended to be used
        """
        return pulumi.get(self, "operations")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[float]:
        """
        Size of the key to be created
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        State of the key
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the key to be created
        """
        return pulumi.get(self, "type")

