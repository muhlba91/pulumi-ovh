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

__all__ = ['InstallationTemplatePartitionSchemePartitionArgs', 'InstallationTemplatePartitionSchemePartition']

@pulumi.input_type
class InstallationTemplatePartitionSchemePartitionArgs:
    def __init__(__self__, *,
                 filesystem: pulumi.Input[str],
                 mountpoint: pulumi.Input[str],
                 order: pulumi.Input[int],
                 scheme_name: pulumi.Input[str],
                 size: pulumi.Input[int],
                 template_name: pulumi.Input[str],
                 type: pulumi.Input[str],
                 raid: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a InstallationTemplatePartitionSchemePartition resource.
        :param pulumi.Input[str] filesystem: Partition filesystem. Enum with possibles values:
               - btrfs
               - ext3
               - ext4
               - ntfs
               - reiserfs
               - swap
               - ufs
               - xfs
               - zfs
        :param pulumi.Input[str] mountpoint: partition mount point.
        :param pulumi.Input[int] order: step or order. specifies the creation order of the partition on the disk
        :param pulumi.Input[str] scheme_name: The partition scheme name.
        :param pulumi.Input[int] size: size of partition in MB, 0 => rest of the space.
        :param pulumi.Input[str] template_name: The template name of the partition scheme.
        :param pulumi.Input[str] type: partition type. Enum with possible values:
               - lv
               - primary
               - logical
        :param pulumi.Input[str] raid: raid partition type. Enum with possible values: 
               - raid0
               - raid1
               - raid10
               - raid5
               - raid6
        :param pulumi.Input[str] volume_name: The volume name needed for proxmox distribution
        """
        pulumi.set(__self__, "filesystem", filesystem)
        pulumi.set(__self__, "mountpoint", mountpoint)
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "scheme_name", scheme_name)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "template_name", template_name)
        pulumi.set(__self__, "type", type)
        if raid is not None:
            pulumi.set(__self__, "raid", raid)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter
    def filesystem(self) -> pulumi.Input[str]:
        """
        Partition filesystem. Enum with possibles values:
        - btrfs
        - ext3
        - ext4
        - ntfs
        - reiserfs
        - swap
        - ufs
        - xfs
        - zfs
        """
        return pulumi.get(self, "filesystem")

    @filesystem.setter
    def filesystem(self, value: pulumi.Input[str]):
        pulumi.set(self, "filesystem", value)

    @property
    @pulumi.getter
    def mountpoint(self) -> pulumi.Input[str]:
        """
        partition mount point.
        """
        return pulumi.get(self, "mountpoint")

    @mountpoint.setter
    def mountpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "mountpoint", value)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        step or order. specifies the creation order of the partition on the disk
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="schemeName")
    def scheme_name(self) -> pulumi.Input[str]:
        """
        The partition scheme name.
        """
        return pulumi.get(self, "scheme_name")

    @scheme_name.setter
    def scheme_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "scheme_name", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        size of partition in MB, 0 => rest of the space.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Input[str]:
        """
        The template name of the partition scheme.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        partition type. Enum with possible values:
        - lv
        - primary
        - logical
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def raid(self) -> Optional[pulumi.Input[str]]:
        """
        raid partition type. Enum with possible values: 
        - raid0
        - raid1
        - raid10
        - raid5
        - raid6
        """
        return pulumi.get(self, "raid")

    @raid.setter
    def raid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raid", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The volume name needed for proxmox distribution
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)


@pulumi.input_type
class _InstallationTemplatePartitionSchemePartitionState:
    def __init__(__self__, *,
                 filesystem: Optional[pulumi.Input[str]] = None,
                 mountpoint: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 raid: Optional[pulumi.Input[str]] = None,
                 scheme_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstallationTemplatePartitionSchemePartition resources.
        :param pulumi.Input[str] filesystem: Partition filesystem. Enum with possibles values:
               - btrfs
               - ext3
               - ext4
               - ntfs
               - reiserfs
               - swap
               - ufs
               - xfs
               - zfs
        :param pulumi.Input[str] mountpoint: partition mount point.
        :param pulumi.Input[int] order: step or order. specifies the creation order of the partition on the disk
        :param pulumi.Input[str] raid: raid partition type. Enum with possible values: 
               - raid0
               - raid1
               - raid10
               - raid5
               - raid6
        :param pulumi.Input[str] scheme_name: The partition scheme name.
        :param pulumi.Input[int] size: size of partition in MB, 0 => rest of the space.
        :param pulumi.Input[str] template_name: The template name of the partition scheme.
        :param pulumi.Input[str] type: partition type. Enum with possible values:
               - lv
               - primary
               - logical
        :param pulumi.Input[str] volume_name: The volume name needed for proxmox distribution
        """
        if filesystem is not None:
            pulumi.set(__self__, "filesystem", filesystem)
        if mountpoint is not None:
            pulumi.set(__self__, "mountpoint", mountpoint)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if raid is not None:
            pulumi.set(__self__, "raid", raid)
        if scheme_name is not None:
            pulumi.set(__self__, "scheme_name", scheme_name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if template_name is not None:
            pulumi.set(__self__, "template_name", template_name)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if volume_name is not None:
            pulumi.set(__self__, "volume_name", volume_name)

    @property
    @pulumi.getter
    def filesystem(self) -> Optional[pulumi.Input[str]]:
        """
        Partition filesystem. Enum with possibles values:
        - btrfs
        - ext3
        - ext4
        - ntfs
        - reiserfs
        - swap
        - ufs
        - xfs
        - zfs
        """
        return pulumi.get(self, "filesystem")

    @filesystem.setter
    def filesystem(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filesystem", value)

    @property
    @pulumi.getter
    def mountpoint(self) -> Optional[pulumi.Input[str]]:
        """
        partition mount point.
        """
        return pulumi.get(self, "mountpoint")

    @mountpoint.setter
    def mountpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mountpoint", value)

    @property
    @pulumi.getter
    def order(self) -> Optional[pulumi.Input[int]]:
        """
        step or order. specifies the creation order of the partition on the disk
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter
    def raid(self) -> Optional[pulumi.Input[str]]:
        """
        raid partition type. Enum with possible values: 
        - raid0
        - raid1
        - raid10
        - raid5
        - raid6
        """
        return pulumi.get(self, "raid")

    @raid.setter
    def raid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raid", value)

    @property
    @pulumi.getter(name="schemeName")
    def scheme_name(self) -> Optional[pulumi.Input[str]]:
        """
        The partition scheme name.
        """
        return pulumi.get(self, "scheme_name")

    @scheme_name.setter
    def scheme_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scheme_name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        size of partition in MB, 0 => rest of the space.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> Optional[pulumi.Input[str]]:
        """
        The template name of the partition scheme.
        """
        return pulumi.get(self, "template_name")

    @template_name.setter
    def template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_name", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        partition type. Enum with possible values:
        - lv
        - primary
        - logical
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The volume name needed for proxmox distribution
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_name", value)


class InstallationTemplatePartitionSchemePartition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filesystem: Optional[pulumi.Input[str]] = None,
                 mountpoint: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 raid: Optional[pulumi.Input[str]] = None,
                 scheme_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Use this resource to create a partition in the partition scheme of a custom installation template available for dedicated servers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        mytemplate = ovh.me.InstallationTemplate("mytemplate",
            base_template_name="debian12_64",
            template_name="mytemplate")
        scheme = ovh.me.InstallationTemplatePartitionScheme("scheme",
            template_name=mytemplate.template_name,
            priority=1)
        root = ovh.me.InstallationTemplatePartitionSchemePartition("root",
            template_name=scheme.template_name,
            scheme_name=scheme.name,
            mountpoint="/",
            filesystem="ext4",
            size=400,
            order=1,
            type="primary")
        ```

        ## Import

        The resource can be imported using the `template_name`, `scheme_name`, `mountpoint` of the cluster, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:Me/installationTemplatePartitionSchemePartition:InstallationTemplatePartitionSchemePartition root template_name/scheme_name/mountpoint
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] filesystem: Partition filesystem. Enum with possibles values:
               - btrfs
               - ext3
               - ext4
               - ntfs
               - reiserfs
               - swap
               - ufs
               - xfs
               - zfs
        :param pulumi.Input[str] mountpoint: partition mount point.
        :param pulumi.Input[int] order: step or order. specifies the creation order of the partition on the disk
        :param pulumi.Input[str] raid: raid partition type. Enum with possible values: 
               - raid0
               - raid1
               - raid10
               - raid5
               - raid6
        :param pulumi.Input[str] scheme_name: The partition scheme name.
        :param pulumi.Input[int] size: size of partition in MB, 0 => rest of the space.
        :param pulumi.Input[str] template_name: The template name of the partition scheme.
        :param pulumi.Input[str] type: partition type. Enum with possible values:
               - lv
               - primary
               - logical
        :param pulumi.Input[str] volume_name: The volume name needed for proxmox distribution
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstallationTemplatePartitionSchemePartitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Use this resource to create a partition in the partition scheme of a custom installation template available for dedicated servers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_ovh as ovh

        mytemplate = ovh.me.InstallationTemplate("mytemplate",
            base_template_name="debian12_64",
            template_name="mytemplate")
        scheme = ovh.me.InstallationTemplatePartitionScheme("scheme",
            template_name=mytemplate.template_name,
            priority=1)
        root = ovh.me.InstallationTemplatePartitionSchemePartition("root",
            template_name=scheme.template_name,
            scheme_name=scheme.name,
            mountpoint="/",
            filesystem="ext4",
            size=400,
            order=1,
            type="primary")
        ```

        ## Import

        The resource can be imported using the `template_name`, `scheme_name`, `mountpoint` of the cluster, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:Me/installationTemplatePartitionSchemePartition:InstallationTemplatePartitionSchemePartition root template_name/scheme_name/mountpoint
        ```

        :param str resource_name: The name of the resource.
        :param InstallationTemplatePartitionSchemePartitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstallationTemplatePartitionSchemePartitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 filesystem: Optional[pulumi.Input[str]] = None,
                 mountpoint: Optional[pulumi.Input[str]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 raid: Optional[pulumi.Input[str]] = None,
                 scheme_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 template_name: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstallationTemplatePartitionSchemePartitionArgs.__new__(InstallationTemplatePartitionSchemePartitionArgs)

            if filesystem is None and not opts.urn:
                raise TypeError("Missing required property 'filesystem'")
            __props__.__dict__["filesystem"] = filesystem
            if mountpoint is None and not opts.urn:
                raise TypeError("Missing required property 'mountpoint'")
            __props__.__dict__["mountpoint"] = mountpoint
            if order is None and not opts.urn:
                raise TypeError("Missing required property 'order'")
            __props__.__dict__["order"] = order
            __props__.__dict__["raid"] = raid
            if scheme_name is None and not opts.urn:
                raise TypeError("Missing required property 'scheme_name'")
            __props__.__dict__["scheme_name"] = scheme_name
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
            if template_name is None and not opts.urn:
                raise TypeError("Missing required property 'template_name'")
            __props__.__dict__["template_name"] = template_name
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["volume_name"] = volume_name
        super(InstallationTemplatePartitionSchemePartition, __self__).__init__(
            'ovh:Me/installationTemplatePartitionSchemePartition:InstallationTemplatePartitionSchemePartition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            filesystem: Optional[pulumi.Input[str]] = None,
            mountpoint: Optional[pulumi.Input[str]] = None,
            order: Optional[pulumi.Input[int]] = None,
            raid: Optional[pulumi.Input[str]] = None,
            scheme_name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            template_name: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            volume_name: Optional[pulumi.Input[str]] = None) -> 'InstallationTemplatePartitionSchemePartition':
        """
        Get an existing InstallationTemplatePartitionSchemePartition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] filesystem: Partition filesystem. Enum with possibles values:
               - btrfs
               - ext3
               - ext4
               - ntfs
               - reiserfs
               - swap
               - ufs
               - xfs
               - zfs
        :param pulumi.Input[str] mountpoint: partition mount point.
        :param pulumi.Input[int] order: step or order. specifies the creation order of the partition on the disk
        :param pulumi.Input[str] raid: raid partition type. Enum with possible values: 
               - raid0
               - raid1
               - raid10
               - raid5
               - raid6
        :param pulumi.Input[str] scheme_name: The partition scheme name.
        :param pulumi.Input[int] size: size of partition in MB, 0 => rest of the space.
        :param pulumi.Input[str] template_name: The template name of the partition scheme.
        :param pulumi.Input[str] type: partition type. Enum with possible values:
               - lv
               - primary
               - logical
        :param pulumi.Input[str] volume_name: The volume name needed for proxmox distribution
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstallationTemplatePartitionSchemePartitionState.__new__(_InstallationTemplatePartitionSchemePartitionState)

        __props__.__dict__["filesystem"] = filesystem
        __props__.__dict__["mountpoint"] = mountpoint
        __props__.__dict__["order"] = order
        __props__.__dict__["raid"] = raid
        __props__.__dict__["scheme_name"] = scheme_name
        __props__.__dict__["size"] = size
        __props__.__dict__["template_name"] = template_name
        __props__.__dict__["type"] = type
        __props__.__dict__["volume_name"] = volume_name
        return InstallationTemplatePartitionSchemePartition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def filesystem(self) -> pulumi.Output[str]:
        """
        Partition filesystem. Enum with possibles values:
        - btrfs
        - ext3
        - ext4
        - ntfs
        - reiserfs
        - swap
        - ufs
        - xfs
        - zfs
        """
        return pulumi.get(self, "filesystem")

    @property
    @pulumi.getter
    def mountpoint(self) -> pulumi.Output[str]:
        """
        partition mount point.
        """
        return pulumi.get(self, "mountpoint")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[int]:
        """
        step or order. specifies the creation order of the partition on the disk
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter
    def raid(self) -> pulumi.Output[str]:
        """
        raid partition type. Enum with possible values: 
        - raid0
        - raid1
        - raid10
        - raid5
        - raid6
        """
        return pulumi.get(self, "raid")

    @property
    @pulumi.getter(name="schemeName")
    def scheme_name(self) -> pulumi.Output[str]:
        """
        The partition scheme name.
        """
        return pulumi.get(self, "scheme_name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        size of partition in MB, 0 => rest of the space.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="templateName")
    def template_name(self) -> pulumi.Output[str]:
        """
        The template name of the partition scheme.
        """
        return pulumi.get(self, "template_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        partition type. Enum with possible values:
        - lv
        - primary
        - logical
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Output[str]:
        """
        The volume name needed for proxmox distribution
        """
        return pulumi.get(self, "volume_name")

