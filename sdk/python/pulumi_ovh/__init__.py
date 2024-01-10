# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .get_installation_templates import *
from .get_server import *
from .get_servers import *
from .get_vrack_networks import *
from .provider import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_ovh.cloudproject as __cloudproject
    cloudproject = __cloudproject
    import pulumi_ovh.cloudprojectdatabase as __cloudprojectdatabase
    cloudprojectdatabase = __cloudprojectdatabase
    import pulumi_ovh.config as __config
    config = __config
    import pulumi_ovh.dbaas as __dbaas
    dbaas = __dbaas
    import pulumi_ovh.dedicated as __dedicated
    dedicated = __dedicated
    import pulumi_ovh.domain as __domain
    domain = __domain
    import pulumi_ovh.hosting as __hosting
    hosting = __hosting
    import pulumi_ovh.iam as __iam
    iam = __iam
    import pulumi_ovh.ip as __ip
    ip = __ip
    import pulumi_ovh.iploadbalancing as __iploadbalancing
    iploadbalancing = __iploadbalancing
    import pulumi_ovh.me as __me
    me = __me
    import pulumi_ovh.order as __order
    order = __order
    import pulumi_ovh.vps as __vps
    vps = __vps
    import pulumi_ovh.vrack as __vrack
    vrack = __vrack
else:
    cloudproject = _utilities.lazy_import('pulumi_ovh.cloudproject')
    cloudprojectdatabase = _utilities.lazy_import('pulumi_ovh.cloudprojectdatabase')
    config = _utilities.lazy_import('pulumi_ovh.config')
    dbaas = _utilities.lazy_import('pulumi_ovh.dbaas')
    dedicated = _utilities.lazy_import('pulumi_ovh.dedicated')
    domain = _utilities.lazy_import('pulumi_ovh.domain')
    hosting = _utilities.lazy_import('pulumi_ovh.hosting')
    iam = _utilities.lazy_import('pulumi_ovh.iam')
    ip = _utilities.lazy_import('pulumi_ovh.ip')
    iploadbalancing = _utilities.lazy_import('pulumi_ovh.iploadbalancing')
    me = _utilities.lazy_import('pulumi_ovh.me')
    order = _utilities.lazy_import('pulumi_ovh.order')
    vps = _utilities.lazy_import('pulumi_ovh.vps')
    vrack = _utilities.lazy_import('pulumi_ovh.vrack')

_utilities.register(
    resource_modules="""
[
 {
  "pkg": "ovh",
  "mod": "CloudProject/containerRegistry",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/containerRegistry:ContainerRegistry": "ContainerRegistry"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/containerRegistryOIDC",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/containerRegistryOIDC:ContainerRegistryOIDC": "ContainerRegistryOIDC"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/containerRegistryUser",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/containerRegistryUser:ContainerRegistryUser": "ContainerRegistryUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/database",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/database:Database": "Database"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/failoverIpAttach",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/failoverIpAttach:FailoverIpAttach": "FailoverIpAttach"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/kube",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/kube:Kube": "Kube"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/kubeIpRestrictions",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions": "KubeIpRestrictions"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/kubeNodePool",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/kubeNodePool:KubeNodePool": "KubeNodePool"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/kubeOidc",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/kubeOidc:KubeOidc": "KubeOidc"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/networkPrivate",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/networkPrivate:NetworkPrivate": "NetworkPrivate"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/networkPrivateSubnet",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/networkPrivateSubnet:NetworkPrivateSubnet": "NetworkPrivateSubnet"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/project",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/project:Project": "Project"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/regionStoragePresign",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/regionStoragePresign:RegionStoragePresign": "RegionStoragePresign"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/s3Credential",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/s3Credential:S3Credential": "S3Credential"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/s3Policy",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/s3Policy:S3Policy": "S3Policy"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/user",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/user:User": "User"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProject/workflowBackup",
  "fqn": "pulumi_ovh.cloudproject",
  "classes": {
   "ovh:CloudProject/workflowBackup:WorkflowBackup": "WorkflowBackup"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/databaseInstance",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/databaseInstance:DatabaseInstance": "DatabaseInstance"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/integration",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/integration:Integration": "Integration"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/ipRestriction",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/ipRestriction:IpRestriction": "IpRestriction"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/kafkaAcl",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/kafkaAcl:KafkaAcl": "KafkaAcl"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/kafkaSchemaRegistryAcl",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/kafkaSchemaRegistryAcl:KafkaSchemaRegistryAcl": "KafkaSchemaRegistryAcl"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/kafkaTopic",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/kafkaTopic:KafkaTopic": "KafkaTopic"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/m3DbNamespace",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/m3DbNamespace:M3DbNamespace": "M3DbNamespace"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/m3DbUser",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/m3DbUser:M3DbUser": "M3DbUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/mongoDbUser",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/mongoDbUser:MongoDbUser": "MongoDbUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/opensearchPattern",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/opensearchPattern:OpensearchPattern": "OpensearchPattern"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/opensearchUser",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/opensearchUser:OpensearchUser": "OpensearchUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/postgresSqlUser",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/postgresSqlUser:PostgresSqlUser": "PostgresSqlUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/redisUser",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/redisUser:RedisUser": "RedisUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "CloudProjectDatabase/user",
  "fqn": "pulumi_ovh.cloudprojectdatabase",
  "classes": {
   "ovh:CloudProjectDatabase/user:User": "User"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dbaas/logsCluster",
  "fqn": "pulumi_ovh.dbaas",
  "classes": {
   "ovh:Dbaas/logsCluster:LogsCluster": "LogsCluster"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dbaas/logsInput",
  "fqn": "pulumi_ovh.dbaas",
  "classes": {
   "ovh:Dbaas/logsInput:LogsInput": "LogsInput"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dbaas/logsOutputGraylogStream",
  "fqn": "pulumi_ovh.dbaas",
  "classes": {
   "ovh:Dbaas/logsOutputGraylogStream:LogsOutputGraylogStream": "LogsOutputGraylogStream"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/cephAcl",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/cephAcl:CephAcl": "CephAcl"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/nasHAPartition",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/nasHAPartition:NasHAPartition": "NasHAPartition"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/nasHAPartitionAccess",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/nasHAPartitionAccess:NasHAPartitionAccess": "NasHAPartitionAccess"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/nasHAPartitionSnapshot",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/nasHAPartitionSnapshot:NasHAPartitionSnapshot": "NasHAPartitionSnapshot"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/serverInstallTask",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/serverInstallTask:ServerInstallTask": "ServerInstallTask"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/serverNetworking",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/serverNetworking:ServerNetworking": "ServerNetworking"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/serverRebootTask",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/serverRebootTask:ServerRebootTask": "ServerRebootTask"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Dedicated/serverUpdate",
  "fqn": "pulumi_ovh.dedicated",
  "classes": {
   "ovh:Dedicated/serverUpdate:ServerUpdate": "ServerUpdate"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Domain/zone",
  "fqn": "pulumi_ovh.domain",
  "classes": {
   "ovh:Domain/zone:Zone": "Zone"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Domain/zoneRecord",
  "fqn": "pulumi_ovh.domain",
  "classes": {
   "ovh:Domain/zoneRecord:ZoneRecord": "ZoneRecord"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Domain/zoneRedirection",
  "fqn": "pulumi_ovh.domain",
  "classes": {
   "ovh:Domain/zoneRedirection:ZoneRedirection": "ZoneRedirection"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Hosting/privateDatabase",
  "fqn": "pulumi_ovh.hosting",
  "classes": {
   "ovh:Hosting/privateDatabase:PrivateDatabase": "PrivateDatabase"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Hosting/privateDatabaseAllowlist",
  "fqn": "pulumi_ovh.hosting",
  "classes": {
   "ovh:Hosting/privateDatabaseAllowlist:PrivateDatabaseAllowlist": "PrivateDatabaseAllowlist"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Hosting/privateDatabaseDb",
  "fqn": "pulumi_ovh.hosting",
  "classes": {
   "ovh:Hosting/privateDatabaseDb:PrivateDatabaseDb": "PrivateDatabaseDb"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Hosting/privateDatabaseUser",
  "fqn": "pulumi_ovh.hosting",
  "classes": {
   "ovh:Hosting/privateDatabaseUser:PrivateDatabaseUser": "PrivateDatabaseUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Hosting/privateDatabaseUserGrant",
  "fqn": "pulumi_ovh.hosting",
  "classes": {
   "ovh:Hosting/privateDatabaseUserGrant:PrivateDatabaseUserGrant": "PrivateDatabaseUserGrant"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Iam/policy",
  "fqn": "pulumi_ovh.iam",
  "classes": {
   "ovh:Iam/policy:Policy": "Policy"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Iam/resourceGroup",
  "fqn": "pulumi_ovh.iam",
  "classes": {
   "ovh:Iam/resourceGroup:ResourceGroup": "ResourceGroup"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Ip/ipService",
  "fqn": "pulumi_ovh.ip",
  "classes": {
   "ovh:Ip/ipService:IpService": "IpService"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Ip/reverse",
  "fqn": "pulumi_ovh.ip",
  "classes": {
   "ovh:Ip/reverse:Reverse": "Reverse"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/httpFarm",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/httpFarm:HttpFarm": "HttpFarm"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/httpFarmServer",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/httpFarmServer:HttpFarmServer": "HttpFarmServer"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/httpFrontend",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/httpFrontend:HttpFrontend": "HttpFrontend"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/httpRoute",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/httpRoute:HttpRoute": "HttpRoute"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/httpRouteRule",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/httpRouteRule:HttpRouteRule": "HttpRouteRule"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/loadBalancer",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/loadBalancer:LoadBalancer": "LoadBalancer"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/refresh",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/refresh:Refresh": "Refresh"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/tcpFarm",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/tcpFarm:TcpFarm": "TcpFarm"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/tcpFarmServer",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/tcpFarmServer:TcpFarmServer": "TcpFarmServer"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/tcpFrontend",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/tcpFrontend:TcpFrontend": "TcpFrontend"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/tcpRoute",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/tcpRoute:TcpRoute": "TcpRoute"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/tcpRouteRule",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/tcpRouteRule:TcpRouteRule": "TcpRouteRule"
  }
 },
 {
  "pkg": "ovh",
  "mod": "IpLoadBalancing/vrackNetwork",
  "fqn": "pulumi_ovh.iploadbalancing",
  "classes": {
   "ovh:IpLoadBalancing/vrackNetwork:VrackNetwork": "VrackNetwork"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/aPIOAuth2Client",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/aPIOAuth2Client:APIOAuth2Client": "APIOAuth2Client"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/identityGroup",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/identityGroup:IdentityGroup": "IdentityGroup"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/identityUser",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/identityUser:IdentityUser": "IdentityUser"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/installationTemplate",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/installationTemplate:InstallationTemplate": "InstallationTemplate"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/installationTemplatePartitionScheme",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/installationTemplatePartitionScheme:InstallationTemplatePartitionScheme": "InstallationTemplatePartitionScheme"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/installationTemplatePartitionSchemeHardwareRaid",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/installationTemplatePartitionSchemeHardwareRaid:InstallationTemplatePartitionSchemeHardwareRaid": "InstallationTemplatePartitionSchemeHardwareRaid"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/installationTemplatePartitionSchemePartition",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/installationTemplatePartitionSchemePartition:InstallationTemplatePartitionSchemePartition": "InstallationTemplatePartitionSchemePartition"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/ipxeScript",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/ipxeScript:IpxeScript": "IpxeScript"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Me/sshKey",
  "fqn": "pulumi_ovh.me",
  "classes": {
   "ovh:Me/sshKey:SshKey": "SshKey"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Vrack/cloudProject",
  "fqn": "pulumi_ovh.vrack",
  "classes": {
   "ovh:Vrack/cloudProject:CloudProject": "CloudProject"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Vrack/dedicatedServer",
  "fqn": "pulumi_ovh.vrack",
  "classes": {
   "ovh:Vrack/dedicatedServer:DedicatedServer": "DedicatedServer"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Vrack/dedicatedServerInterface",
  "fqn": "pulumi_ovh.vrack",
  "classes": {
   "ovh:Vrack/dedicatedServerInterface:DedicatedServerInterface": "DedicatedServerInterface"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Vrack/ipAddress",
  "fqn": "pulumi_ovh.vrack",
  "classes": {
   "ovh:Vrack/ipAddress:IpAddress": "IpAddress"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Vrack/ipLoadbalancing",
  "fqn": "pulumi_ovh.vrack",
  "classes": {
   "ovh:Vrack/ipLoadbalancing:IpLoadbalancing": "IpLoadbalancing"
  }
 },
 {
  "pkg": "ovh",
  "mod": "Vrack/vrack",
  "fqn": "pulumi_ovh.vrack",
  "classes": {
   "ovh:Vrack/vrack:Vrack": "Vrack"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "ovh",
  "token": "pulumi:providers:ovh",
  "fqn": "pulumi_ovh",
  "class": "Provider"
 }
]
"""
)
