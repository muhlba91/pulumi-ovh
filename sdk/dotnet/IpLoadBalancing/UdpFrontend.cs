// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Ovh.IpLoadBalancing
{
    /// <summary>
    /// Creates a backend server group (frontend) to be used by loadbalancing frontend(s)
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Ovh = Pulumi.Ovh;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var lb = Ovh.IpLoadBalancing.GetIpLoadBalancing.Invoke(new()
    ///     {
    ///         ServiceName = "ip-1.2.3.4",
    ///         State = "ok",
    ///     });
    /// 
    ///     var testfrontend = new Ovh.IpLoadBalancing.UdpFrontend("testfrontend", new()
    ///     {
    ///         ServiceName = lb.Apply(getIpLoadBalancingResult =&gt; getIpLoadBalancingResult.ServiceName),
    ///         DisplayName = "ingress-8080-gra",
    ///         Zone = "all",
    ///         Port = "10,11",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// UDP frontend can be imported using the following format `service_name` and the `id` of the frontend separated by "/" e.g.
    /// 
    /// bash
    /// 
    /// ```sh
    /// $ pulumi import ovh:IpLoadBalancing/udpFrontend:UdpFrontend testfrontend service_name/frontend_id
    /// ```
    /// </summary>
    [OvhResourceType("ovh:IpLoadBalancing/udpFrontend:UdpFrontend")]
    public partial class UdpFrontend : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        /// </summary>
        [Output("dedicatedIpfos")]
        public Output<ImmutableArray<string>> DedicatedIpfos { get; private set; } = null!;

        /// <summary>
        /// Default UDP Farm of your frontend
        /// </summary>
        [Output("defaultFarmId")]
        public Output<double> DefaultFarmId { get; private set; } = null!;

        /// <summary>
        /// Disable your frontend. Default: 'false'
        /// </summary>
        [Output("disabled")]
        public Output<bool> Disabled { get; private set; } = null!;

        /// <summary>
        /// Human readable name for your frontend
        /// </summary>
        [Output("displayName")]
        public Output<string> DisplayName { get; private set; } = null!;

        /// <summary>
        /// Id of your frontend
        /// </summary>
        [Output("frontendId")]
        public Output<double> FrontendId { get; private set; } = null!;

        /// <summary>
        /// Port(s) attached to your frontend. Supports single port (numerical value), 
        /// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        /// and/or 'range'. Each port must be in the [1;49151] range
        /// </summary>
        [Output("port")]
        public Output<string> Port { get; private set; } = null!;

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Output("serviceName")]
        public Output<string> ServiceName { get; private set; } = null!;

        /// <summary>
        /// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a UdpFrontend resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public UdpFrontend(string name, UdpFrontendArgs args, CustomResourceOptions? options = null)
            : base("ovh:IpLoadBalancing/udpFrontend:UdpFrontend", name, args ?? new UdpFrontendArgs(), MakeResourceOptions(options, ""))
        {
        }

        private UdpFrontend(string name, Input<string> id, UdpFrontendState? state = null, CustomResourceOptions? options = null)
            : base("ovh:IpLoadBalancing/udpFrontend:UdpFrontend", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing UdpFrontend resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static UdpFrontend Get(string name, Input<string> id, UdpFrontendState? state = null, CustomResourceOptions? options = null)
        {
            return new UdpFrontend(name, id, state, options);
        }
    }

    public sealed class UdpFrontendArgs : global::Pulumi.ResourceArgs
    {
        [Input("dedicatedIpfos")]
        private InputList<string>? _dedicatedIpfos;

        /// <summary>
        /// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        /// </summary>
        public InputList<string> DedicatedIpfos
        {
            get => _dedicatedIpfos ?? (_dedicatedIpfos = new InputList<string>());
            set => _dedicatedIpfos = value;
        }

        /// <summary>
        /// Default UDP Farm of your frontend
        /// </summary>
        [Input("defaultFarmId")]
        public Input<double>? DefaultFarmId { get; set; }

        /// <summary>
        /// Disable your frontend. Default: 'false'
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        /// <summary>
        /// Human readable name for your frontend
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Port(s) attached to your frontend. Supports single port (numerical value), 
        /// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        /// and/or 'range'. Each port must be in the [1;49151] range
        /// </summary>
        [Input("port", required: true)]
        public Input<string> Port { get; set; } = null!;

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        /// <summary>
        /// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        /// </summary>
        [Input("zone", required: true)]
        public Input<string> Zone { get; set; } = null!;

        public UdpFrontendArgs()
        {
        }
        public static new UdpFrontendArgs Empty => new UdpFrontendArgs();
    }

    public sealed class UdpFrontendState : global::Pulumi.ResourceArgs
    {
        [Input("dedicatedIpfos")]
        private InputList<string>? _dedicatedIpfos;

        /// <summary>
        /// Only attach frontend on these ip. No restriction if null. List of Ip blocks.
        /// </summary>
        public InputList<string> DedicatedIpfos
        {
            get => _dedicatedIpfos ?? (_dedicatedIpfos = new InputList<string>());
            set => _dedicatedIpfos = value;
        }

        /// <summary>
        /// Default UDP Farm of your frontend
        /// </summary>
        [Input("defaultFarmId")]
        public Input<double>? DefaultFarmId { get; set; }

        /// <summary>
        /// Disable your frontend. Default: 'false'
        /// </summary>
        [Input("disabled")]
        public Input<bool>? Disabled { get; set; }

        /// <summary>
        /// Human readable name for your frontend
        /// </summary>
        [Input("displayName")]
        public Input<string>? DisplayName { get; set; }

        /// <summary>
        /// Id of your frontend
        /// </summary>
        [Input("frontendId")]
        public Input<double>? FrontendId { get; set; }

        /// <summary>
        /// Port(s) attached to your frontend. Supports single port (numerical value), 
        /// range (2 dash-delimited increasing ports) and comma-separated list of 'single port'
        /// and/or 'range'. Each port must be in the [1;49151] range
        /// </summary>
        [Input("port")]
        public Input<string>? Port { get; set; }

        /// <summary>
        /// The internal name of your IP load balancing
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// Zone where the frontend will be defined (ie. `gra`, `bhs` also supports `all`)
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public UdpFrontendState()
        {
        }
        public static new UdpFrontendState Empty => new UdpFrontendState();
    }
}
