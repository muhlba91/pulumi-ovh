// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.Vps
{
    /// <summary>
    /// ## Example Usage
    /// </summary>
    [OvhResourceType("ovh:Vps/vps:Vps")]
    public partial class Vps : global::Pulumi.CustomResource
    {
        /// <summary>
        /// VPS cluster
        /// </summary>
        [Output("cluster")]
        public Output<string> Cluster { get; private set; } = null!;

        /// <summary>
        /// Custom display name
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// IAM resource information
        /// </summary>
        [Output("iam")]
        public Output<Outputs.VpsIam> Iam { get; private set; } = null!;

        /// <summary>
        /// KVM keyboard layout on VPS Cloud
        /// </summary>
        [Output("keymap")]
        public Output<string> Keymap { get; private set; } = null!;

        /// <summary>
        /// RAM of this VPS
        /// </summary>
        [Output("memoryLimit")]
        public Output<double> MemoryLimit { get; private set; } = null!;

        /// <summary>
        /// Structure describing characteristics of a VPS model
        /// </summary>
        [Output("model")]
        public Output<Outputs.VpsModel> Model { get; private set; } = null!;

        /// <summary>
        /// IP blocks for OVH monitoring servers
        /// </summary>
        [Output("monitoringIpBlocks")]
        public Output<ImmutableArray<string>> MonitoringIpBlocks { get; private set; } = null!;

        /// <summary>
        /// Name of the VPS
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// VPS netboot mode (local┃rescue)
        /// </summary>
        [Output("netbootMode")]
        public Output<string> NetbootMode { get; private set; } = null!;

        /// <summary>
        /// All offers a VPS can have (beta-classic┃classic┃cloud┃cloudram┃game-classic┃lowlat┃ssd)
        /// </summary>
        [Output("offerType")]
        public Output<string> OfferType { get; private set; } = null!;

        /// <summary>
        /// Details about an Order
        /// </summary>
        [Output("order")]
        public Output<Outputs.VpsOrder> Order { get; private set; } = null!;

        /// <summary>
        /// OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json](https://eu.api.ovh.com/console-preview/?section=%2Fme&amp;branch=v1#get-/me)
        /// </summary>
        [Output("ovhSubsidiary")]
        public Output<string?> OvhSubsidiary { get; private set; } = null!;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        [Output("planOptions")]
        public Output<ImmutableArray<Outputs.VpsPlanOption>> PlanOptions { get; private set; } = null!;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        [Output("plans")]
        public Output<ImmutableArray<Outputs.VpsPlan>> Plans { get; private set; } = null!;

        /// <summary>
        /// The internal name of your VPS offer
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        [Output("slaMonitoring")]
        public Output<bool> SlaMonitoring { get; private set; } = null!;

        /// <summary>
        /// State of the VPS (backuping┃installing┃maintenance┃rebooting┃rescued┃running┃stopped┃stopping┃upgrading)
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// Number of vcores
        /// </summary>
        [Output("vcore")]
        public Output<double> Vcore { get; private set; } = null!;

        /// <summary>
        /// OpenStask region where the VPS is located
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Vps resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Vps(string name, VpsArgs? args = null, CustomResourceOptions? options = null)
            : base("ovh:Vps/vps:Vps", name, args ?? new VpsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Vps(string name, Input<string> id, VpsState? state = null, CustomResourceOptions? options = null)
            : base("ovh:Vps/vps:Vps", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/ovh/pulumi-ovh",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Vps resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Vps Get(string name, Input<string> id, VpsState? state = null, CustomResourceOptions? options = null)
        {
            return new Vps(name, id, state, options);
        }
    }

    public sealed class VpsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Custom display name
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// KVM keyboard layout on VPS Cloud
        /// </summary>
        [Input("keymap")]
        public Input<string>? Keymap { get; set; }

        /// <summary>
        /// RAM of this VPS
        /// </summary>
        [Input("memoryLimit")]
        public Input<double>? MemoryLimit { get; set; }

        /// <summary>
        /// Structure describing characteristics of a VPS model
        /// </summary>
        [Input("model")]
        public Input<Inputs.VpsModelArgs>? Model { get; set; }

        [Input("monitoringIpBlocks")]
        private InputList<string>? _monitoringIpBlocks;

        /// <summary>
        /// IP blocks for OVH monitoring servers
        /// </summary>
        public InputList<string> MonitoringIpBlocks
        {
            get => _monitoringIpBlocks ?? (_monitoringIpBlocks = new InputList<string>());
            set => _monitoringIpBlocks = value;
        }

        /// <summary>
        /// Name of the VPS
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// VPS netboot mode (local┃rescue)
        /// </summary>
        [Input("netbootMode")]
        public Input<string>? NetbootMode { get; set; }

        /// <summary>
        /// All offers a VPS can have (beta-classic┃classic┃cloud┃cloudram┃game-classic┃lowlat┃ssd)
        /// </summary>
        [Input("offerType")]
        public Input<string>? OfferType { get; set; }

        /// <summary>
        /// OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json](https://eu.api.ovh.com/console-preview/?section=%2Fme&amp;branch=v1#get-/me)
        /// </summary>
        [Input("ovhSubsidiary")]
        public Input<string>? OvhSubsidiary { get; set; }

        [Input("planOptions")]
        private InputList<Inputs.VpsPlanOptionArgs>? _planOptions;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        public InputList<Inputs.VpsPlanOptionArgs> PlanOptions
        {
            get => _planOptions ?? (_planOptions = new InputList<Inputs.VpsPlanOptionArgs>());
            set => _planOptions = value;
        }

        [Input("plans")]
        private InputList<Inputs.VpsPlanArgs>? _plans;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        public InputList<Inputs.VpsPlanArgs> Plans
        {
            get => _plans ?? (_plans = new InputList<Inputs.VpsPlanArgs>());
            set => _plans = value;
        }

        [Input("slaMonitoring")]
        public Input<bool>? SlaMonitoring { get; set; }

        /// <summary>
        /// State of the VPS (backuping┃installing┃maintenance┃rebooting┃rescued┃running┃stopped┃stopping┃upgrading)
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// Number of vcores
        /// </summary>
        [Input("vcore")]
        public Input<double>? Vcore { get; set; }

        /// <summary>
        /// OpenStask region where the VPS is located
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public VpsArgs()
        {
        }
        public static new VpsArgs Empty => new VpsArgs();
    }

    public sealed class VpsState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// VPS cluster
        /// </summary>
        [Input("cluster")]
        public Input<string>? Cluster { get; set; }

        /// <summary>
        /// Custom display name
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// IAM resource information
        /// </summary>
        [Input("iam")]
        public Input<Inputs.VpsIamGetArgs>? Iam { get; set; }

        /// <summary>
        /// KVM keyboard layout on VPS Cloud
        /// </summary>
        [Input("keymap")]
        public Input<string>? Keymap { get; set; }

        /// <summary>
        /// RAM of this VPS
        /// </summary>
        [Input("memoryLimit")]
        public Input<double>? MemoryLimit { get; set; }

        /// <summary>
        /// Structure describing characteristics of a VPS model
        /// </summary>
        [Input("model")]
        public Input<Inputs.VpsModelGetArgs>? Model { get; set; }

        [Input("monitoringIpBlocks")]
        private InputList<string>? _monitoringIpBlocks;

        /// <summary>
        /// IP blocks for OVH monitoring servers
        /// </summary>
        public InputList<string> MonitoringIpBlocks
        {
            get => _monitoringIpBlocks ?? (_monitoringIpBlocks = new InputList<string>());
            set => _monitoringIpBlocks = value;
        }

        /// <summary>
        /// Name of the VPS
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// VPS netboot mode (local┃rescue)
        /// </summary>
        [Input("netbootMode")]
        public Input<string>? NetbootMode { get; set; }

        /// <summary>
        /// All offers a VPS can have (beta-classic┃classic┃cloud┃cloudram┃game-classic┃lowlat┃ssd)
        /// </summary>
        [Input("offerType")]
        public Input<string>? OfferType { get; set; }

        /// <summary>
        /// Details about an Order
        /// </summary>
        [Input("order")]
        public Input<Inputs.VpsOrderGetArgs>? Order { get; set; }

        /// <summary>
        /// OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json](https://eu.api.ovh.com/console-preview/?section=%2Fme&amp;branch=v1#get-/me)
        /// </summary>
        [Input("ovhSubsidiary")]
        public Input<string>? OvhSubsidiary { get; set; }

        [Input("planOptions")]
        private InputList<Inputs.VpsPlanOptionGetArgs>? _planOptions;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        public InputList<Inputs.VpsPlanOptionGetArgs> PlanOptions
        {
            get => _planOptions ?? (_planOptions = new InputList<Inputs.VpsPlanOptionGetArgs>());
            set => _planOptions = value;
        }

        [Input("plans")]
        private InputList<Inputs.VpsPlanGetArgs>? _plans;

        /// <summary>
        /// Product Plan to order
        /// </summary>
        public InputList<Inputs.VpsPlanGetArgs> Plans
        {
            get => _plans ?? (_plans = new InputList<Inputs.VpsPlanGetArgs>());
            set => _plans = value;
        }

        /// <summary>
        /// The internal name of your VPS offer
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        [Input("slaMonitoring")]
        public Input<bool>? SlaMonitoring { get; set; }

        /// <summary>
        /// State of the VPS (backuping┃installing┃maintenance┃rebooting┃rescued┃running┃stopped┃stopping┃upgrading)
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// Number of vcores
        /// </summary>
        [Input("vcore")]
        public Input<double>? Vcore { get; set; }

        /// <summary>
        /// OpenStask region where the VPS is located
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public VpsState()
        {
        }
        public static new VpsState Empty => new VpsState();
    }
}
