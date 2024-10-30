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

__all__ = ['PostgresSqlConnectionPoolArgs', 'PostgresSqlConnectionPool']

@pulumi.input_type
class PostgresSqlConnectionPoolArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 database_id: pulumi.Input[str],
                 mode: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 size: pulumi.Input[int],
                 name: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a PostgresSqlConnectionPool resource.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] database_id: Database ID for a database that belongs to the Database cluster given above.
        :param pulumi.Input[str] mode: Connection mode to the connection pool
               Available modes:
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[int] size: Size of the connection pool.
        :param pulumi.Input[str] name: Name of the connection pool.
        :param pulumi.Input[str] user_id: Database user authorized to connect to the pool, if none all the users are allowed.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "database_id", database_id)
        pulumi.set(__self__, "mode", mode)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "size", size)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Input[str]:
        """
        Database ID for a database that belongs to the Database cluster given above.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[str]:
        """
        Connection mode to the connection pool
        Available modes:
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def size(self) -> pulumi.Input[int]:
        """
        Size of the connection pool.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: pulumi.Input[int]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the connection pool.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        Database user authorized to connect to the pool, if none all the users are allowed.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


@pulumi.input_type
class _PostgresSqlConnectionPoolState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 ssl_mode: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering PostgresSqlConnectionPool resources.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] database_id: Database ID for a database that belongs to the Database cluster given above.
        :param pulumi.Input[str] mode: Connection mode to the connection pool
               Available modes:
        :param pulumi.Input[str] name: Name of the connection pool.
        :param pulumi.Input[int] port: Port of the connection pool.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[int] size: Size of the connection pool.
        :param pulumi.Input[str] ssl_mode: Ssl connection mode for the pool.
        :param pulumi.Input[str] uri: Connection URI to the pool.
        :param pulumi.Input[str] user_id: Database user authorized to connect to the pool, if none all the users are allowed.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if database_id is not None:
            pulumi.set(__self__, "database_id", database_id)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if service_name is not None:
            pulumi.set(__self__, "service_name", service_name)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if ssl_mode is not None:
            pulumi.set(__self__, "ssl_mode", ssl_mode)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> Optional[pulumi.Input[str]]:
        """
        Database ID for a database that belongs to the Database cluster given above.
        """
        return pulumi.get(self, "database_id")

    @database_id.setter
    def database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_id", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[str]]:
        """
        Connection mode to the connection pool
        Available modes:
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the connection pool.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        Port of the connection pool.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        Size of the connection pool.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Ssl connection mode for the pool.
        """
        return pulumi.get(self, "ssl_mode")

    @ssl_mode.setter
    def ssl_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_mode", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        Connection URI to the pool.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        Database user authorized to connect to the pool, if none all the users are allowed.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)


class PostgresSqlConnectionPool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Import

        OVHcloud Managed PostgreSQL clusters connection pools can be imported using the `service_name`, `cluster_id` and `id` of the connection pool, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProjectDatabase/postgresSqlConnectionPool:PostgresSqlConnectionPool my_connection_pool service_name/cluster_id/id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] database_id: Database ID for a database that belongs to the Database cluster given above.
        :param pulumi.Input[str] mode: Connection mode to the connection pool
               Available modes:
        :param pulumi.Input[str] name: Name of the connection pool.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[int] size: Size of the connection pool.
        :param pulumi.Input[str] user_id: Database user authorized to connect to the pool, if none all the users are allowed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PostgresSqlConnectionPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        OVHcloud Managed PostgreSQL clusters connection pools can be imported using the `service_name`, `cluster_id` and `id` of the connection pool, separated by "/" E.g.,

        bash

        ```sh
        $ pulumi import ovh:CloudProjectDatabase/postgresSqlConnectionPool:PostgresSqlConnectionPool my_connection_pool service_name/cluster_id/id
        ```

        :param str resource_name: The name of the resource.
        :param PostgresSqlConnectionPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PostgresSqlConnectionPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 database_id: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PostgresSqlConnectionPoolArgs.__new__(PostgresSqlConnectionPoolArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if database_id is None and not opts.urn:
                raise TypeError("Missing required property 'database_id'")
            __props__.__dict__["database_id"] = database_id
            if mode is None and not opts.urn:
                raise TypeError("Missing required property 'mode'")
            __props__.__dict__["mode"] = mode
            __props__.__dict__["name"] = name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if size is None and not opts.urn:
                raise TypeError("Missing required property 'size'")
            __props__.__dict__["size"] = size
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["port"] = None
            __props__.__dict__["ssl_mode"] = None
            __props__.__dict__["uri"] = None
        super(PostgresSqlConnectionPool, __self__).__init__(
            'ovh:CloudProjectDatabase/postgresSqlConnectionPool:PostgresSqlConnectionPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            database_id: Optional[pulumi.Input[str]] = None,
            mode: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port: Optional[pulumi.Input[int]] = None,
            service_name: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            ssl_mode: Optional[pulumi.Input[str]] = None,
            uri: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'PostgresSqlConnectionPool':
        """
        Get an existing PostgresSqlConnectionPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: Cluster ID.
        :param pulumi.Input[str] database_id: Database ID for a database that belongs to the Database cluster given above.
        :param pulumi.Input[str] mode: Connection mode to the connection pool
               Available modes:
        :param pulumi.Input[str] name: Name of the connection pool.
        :param pulumi.Input[int] port: Port of the connection pool.
        :param pulumi.Input[str] service_name: The id of the public cloud project. If omitted,
               the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        :param pulumi.Input[int] size: Size of the connection pool.
        :param pulumi.Input[str] ssl_mode: Ssl connection mode for the pool.
        :param pulumi.Input[str] uri: Connection URI to the pool.
        :param pulumi.Input[str] user_id: Database user authorized to connect to the pool, if none all the users are allowed.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _PostgresSqlConnectionPoolState.__new__(_PostgresSqlConnectionPoolState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["database_id"] = database_id
        __props__.__dict__["mode"] = mode
        __props__.__dict__["name"] = name
        __props__.__dict__["port"] = port
        __props__.__dict__["service_name"] = service_name
        __props__.__dict__["size"] = size
        __props__.__dict__["ssl_mode"] = ssl_mode
        __props__.__dict__["uri"] = uri
        __props__.__dict__["user_id"] = user_id
        return PostgresSqlConnectionPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        Cluster ID.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="databaseId")
    def database_id(self) -> pulumi.Output[str]:
        """
        Database ID for a database that belongs to the Database cluster given above.
        """
        return pulumi.get(self, "database_id")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[str]:
        """
        Connection mode to the connection pool
        Available modes:
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the connection pool.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def port(self) -> pulumi.Output[int]:
        """
        Port of the connection pool.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Output[str]:
        """
        The id of the public cloud project. If omitted,
        the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
        """
        return pulumi.get(self, "service_name")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        Size of the connection pool.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sslMode")
    def ssl_mode(self) -> pulumi.Output[str]:
        """
        Ssl connection mode for the pool.
        """
        return pulumi.get(self, "ssl_mode")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        Connection URI to the pool.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        Database user authorized to connect to the pool, if none all the users are allowed.
        """
        return pulumi.get(self, "user_id")

