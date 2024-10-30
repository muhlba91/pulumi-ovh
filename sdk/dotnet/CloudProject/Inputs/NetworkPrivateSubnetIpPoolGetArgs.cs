// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.CloudProject.Inputs
{

    public sealed class NetworkPrivateSubnetIpPoolGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable DHCP.
        /// Changing this forces a new resource to be created. Defaults to false.
        /// </summary>
        [Input("dhcp")]
        public Input<bool>? Dhcp { get; set; }

        /// <summary>
        /// Last ip for this region.
        /// Changing this value recreates the subnet.
        /// </summary>
        [Input("end")]
        public Input<string>? End { get; set; }

        /// <summary>
        /// Global network in CIDR format.
        /// Changing this value recreates the subnet
        /// </summary>
        [Input("network")]
        public Input<string>? Network { get; set; }

        /// <summary>
        /// The region in which the network subnet will be created.
        /// Ex.: "GRA1". Changing this value recreates the resource.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// First ip for this region.
        /// Changing this value recreates the subnet.
        /// </summary>
        [Input("start")]
        public Input<string>? Start { get; set; }

        public NetworkPrivateSubnetIpPoolGetArgs()
        {
        }
        public static new NetworkPrivateSubnetIpPoolGetArgs Empty => new NetworkPrivateSubnetIpPoolGetArgs();
    }
}
