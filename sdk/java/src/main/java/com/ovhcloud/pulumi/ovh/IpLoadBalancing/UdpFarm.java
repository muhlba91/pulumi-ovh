// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.IpLoadBalancing;

import com.ovhcloud.pulumi.ovh.IpLoadBalancing.UdpFarmArgs;
import com.ovhcloud.pulumi.ovh.IpLoadBalancing.inputs.UdpFarmState;
import com.ovhcloud.pulumi.ovh.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Double;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Creates a backend server group (farm) to be used by loadbalancing frontend(s)
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.ovh.IpLoadBalancing.IpLoadBalancingFunctions;
 * import com.pulumi.ovh.IpLoadBalancing.inputs.GetIpLoadBalancingArgs;
 * import com.pulumi.ovh.IpLoadBalancing.UdpFarm;
 * import com.pulumi.ovh.IpLoadBalancing.UdpFarmArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         final var lb = IpLoadBalancingFunctions.getIpLoadBalancing(GetIpLoadBalancingArgs.builder()
 *             .serviceName("ip-1.2.3.4")
 *             .state("ok")
 *             .build());
 * 
 *         var farmname = new UdpFarm("farmname", UdpFarmArgs.builder()
 *             .displayName("ingress-8080-gra")
 *             .port(80)
 *             .serviceName(lb.applyValue(getIpLoadBalancingResult -> getIpLoadBalancingResult.serviceName()))
 *             .zone("gra")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * UDP Farm can be imported using the following format `service_name` and the `id` of the farm, separated by &#34;/&#34; e.g.
 * 
 * bash
 * 
 * ```sh
 * $ pulumi import ovh:IpLoadBalancing/udpFarm:UdpFarm farmname service_name/farm_id
 * ```
 * 
 */
@ResourceType(type="ovh:IpLoadBalancing/udpFarm:UdpFarm")
public class UdpFarm extends com.pulumi.resources.CustomResource {
    /**
     * Readable label for loadbalancer farm
     * 
     */
    @Export(name="displayName", refs={String.class}, tree="[0]")
    private Output<String> displayName;

    /**
     * @return Readable label for loadbalancer farm
     * 
     */
    public Output<String> displayName() {
        return this.displayName;
    }
    /**
     * Id of your farm.
     * 
     */
    @Export(name="farmId", refs={Double.class}, tree="[0]")
    private Output<Double> farmId;

    /**
     * @return Id of your farm.
     * 
     */
    public Output<Double> farmId() {
        return this.farmId;
    }
    /**
     * Port attached to your farm ([1..49151]). Inherited from frontend if null
     * 
     */
    @Export(name="port", refs={Double.class}, tree="[0]")
    private Output<Double> port;

    /**
     * @return Port attached to your farm ([1..49151]). Inherited from frontend if null
     * 
     */
    public Output<Double> port() {
        return this.port;
    }
    /**
     * The internal name of your IP load balancing
     * 
     */
    @Export(name="serviceName", refs={String.class}, tree="[0]")
    private Output<String> serviceName;

    /**
     * @return The internal name of your IP load balancing
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }
    /**
     * Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
     * 
     */
    @Export(name="vrackNetworkId", refs={Double.class}, tree="[0]")
    private Output<Double> vrackNetworkId;

    /**
     * @return Internal Load Balancer identifier of the vRack private network to attach to your farm, mandatory when your Load Balancer is attached to a vRack
     * 
     */
    public Output<Double> vrackNetworkId() {
        return this.vrackNetworkId;
    }
    /**
     * Zone where the farm will be defined (ie. `gra`, `bhs` also supports `all`)
     * 
     */
    @Export(name="zone", refs={String.class}, tree="[0]")
    private Output<String> zone;

    /**
     * @return Zone where the farm will be defined (ie. `gra`, `bhs` also supports `all`)
     * 
     */
    public Output<String> zone() {
        return this.zone;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public UdpFarm(java.lang.String name) {
        this(name, UdpFarmArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public UdpFarm(java.lang.String name, UdpFarmArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public UdpFarm(java.lang.String name, UdpFarmArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:IpLoadBalancing/udpFarm:UdpFarm", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private UdpFarm(java.lang.String name, Output<java.lang.String> id, @Nullable UdpFarmState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:IpLoadBalancing/udpFarm:UdpFarm", name, state, makeResourceOptions(options, id), false);
    }

    private static UdpFarmArgs makeArgs(UdpFarmArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? UdpFarmArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static UdpFarm get(java.lang.String name, Output<java.lang.String> id, @Nullable UdpFarmState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new UdpFarm(name, id, state, options);
    }
}
