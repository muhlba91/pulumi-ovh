// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Vps;

import com.ovh.ovh.Utilities;
import com.ovh.ovh.Vps.VpsArgs;
import com.ovh.ovh.Vps.inputs.VpsState;
import com.ovh.ovh.Vps.outputs.VpsIam;
import com.ovh.ovh.Vps.outputs.VpsModel;
import com.ovh.ovh.Vps.outputs.VpsOrder;
import com.ovh.ovh.Vps.outputs.VpsPlan;
import com.ovh.ovh.Vps.outputs.VpsPlanOption;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Boolean;
import java.lang.Double;
import java.lang.String;
import java.util.List;
import javax.annotation.Nullable;

/**
 * ## Example Usage
 * 
 */
@ResourceType(type="ovh:Vps/vps:Vps")
public class Vps extends com.pulumi.resources.CustomResource {
    /**
     * VPS cluster
     * 
     */
    @Export(name="cluster", refs={String.class}, tree="[0]")
    private Output<String> cluster;

    /**
     * @return VPS cluster
     * 
     */
    public Output<String> cluster() {
        return this.cluster;
    }
    /**
     * Custom display name
     * 
     */
    @Export(name="displayName", refs={String.class}, tree="[0]")
    private Output<String> displayName;

    /**
     * @return Custom display name
     * 
     */
    public Output<String> displayName() {
        return this.displayName;
    }
    /**
     * IAM resource information
     * 
     */
    @Export(name="iam", refs={VpsIam.class}, tree="[0]")
    private Output<VpsIam> iam;

    /**
     * @return IAM resource information
     * 
     */
    public Output<VpsIam> iam() {
        return this.iam;
    }
    /**
     * KVM keyboard layout on VPS Cloud
     * 
     */
    @Export(name="keymap", refs={String.class}, tree="[0]")
    private Output<String> keymap;

    /**
     * @return KVM keyboard layout on VPS Cloud
     * 
     */
    public Output<String> keymap() {
        return this.keymap;
    }
    /**
     * RAM of this VPS
     * 
     */
    @Export(name="memoryLimit", refs={Double.class}, tree="[0]")
    private Output<Double> memoryLimit;

    /**
     * @return RAM of this VPS
     * 
     */
    public Output<Double> memoryLimit() {
        return this.memoryLimit;
    }
    /**
     * Structure describing characteristics of a VPS model
     * 
     */
    @Export(name="model", refs={VpsModel.class}, tree="[0]")
    private Output<VpsModel> model;

    /**
     * @return Structure describing characteristics of a VPS model
     * 
     */
    public Output<VpsModel> model() {
        return this.model;
    }
    /**
     * IP blocks for OVH monitoring servers
     * 
     */
    @Export(name="monitoringIpBlocks", refs={List.class,String.class}, tree="[0,1]")
    private Output<List<String>> monitoringIpBlocks;

    /**
     * @return IP blocks for OVH monitoring servers
     * 
     */
    public Output<List<String>> monitoringIpBlocks() {
        return this.monitoringIpBlocks;
    }
    /**
     * Name of the VPS
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return Name of the VPS
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * VPS netboot mode (local┃rescue)
     * 
     */
    @Export(name="netbootMode", refs={String.class}, tree="[0]")
    private Output<String> netbootMode;

    /**
     * @return VPS netboot mode (local┃rescue)
     * 
     */
    public Output<String> netbootMode() {
        return this.netbootMode;
    }
    /**
     * All offers a VPS can have (beta-classic┃classic┃cloud┃cloudram┃game-classic┃lowlat┃ssd)
     * 
     */
    @Export(name="offerType", refs={String.class}, tree="[0]")
    private Output<String> offerType;

    /**
     * @return All offers a VPS can have (beta-classic┃classic┃cloud┃cloudram┃game-classic┃lowlat┃ssd)
     * 
     */
    public Output<String> offerType() {
        return this.offerType;
    }
    /**
     * Details about an Order
     * 
     */
    @Export(name="order", refs={VpsOrder.class}, tree="[0]")
    private Output<VpsOrder> order;

    /**
     * @return Details about an Order
     * 
     */
    public Output<VpsOrder> order() {
        return this.order;
    }
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json](https://eu.api.ovh.com/console-preview/?section=%2Fme&amp;branch=v1#get-/me)
     * 
     */
    @Export(name="ovhSubsidiary", refs={String.class}, tree="[0]")
    private Output<String> ovhSubsidiary;

    /**
     * @return OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json](https://eu.api.ovh.com/console-preview/?section=%2Fme&amp;branch=v1#get-/me)
     * 
     */
    public Output<String> ovhSubsidiary() {
        return this.ovhSubsidiary;
    }
    /**
     * Product Plan to order
     * 
     */
    @Export(name="planOptions", refs={List.class,VpsPlanOption.class}, tree="[0,1]")
    private Output<List<VpsPlanOption>> planOptions;

    /**
     * @return Product Plan to order
     * 
     */
    public Output<List<VpsPlanOption>> planOptions() {
        return this.planOptions;
    }
    /**
     * Product Plan to order
     * 
     */
    @Export(name="plans", refs={List.class,VpsPlan.class}, tree="[0,1]")
    private Output<List<VpsPlan>> plans;

    /**
     * @return Product Plan to order
     * 
     */
    public Output<List<VpsPlan>> plans() {
        return this.plans;
    }
    /**
     * The internal name of your VPS offer
     * 
     */
    @Export(name="serviceName", refs={String.class}, tree="[0]")
    private Output<String> serviceName;

    /**
     * @return The internal name of your VPS offer
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }
    @Export(name="slaMonitoring", refs={Boolean.class}, tree="[0]")
    private Output<Boolean> slaMonitoring;

    public Output<Boolean> slaMonitoring() {
        return this.slaMonitoring;
    }
    /**
     * State of the VPS (backuping┃installing┃maintenance┃rebooting┃rescued┃running┃stopped┃stopping┃upgrading)
     * 
     */
    @Export(name="state", refs={String.class}, tree="[0]")
    private Output<String> state;

    /**
     * @return State of the VPS (backuping┃installing┃maintenance┃rebooting┃rescued┃running┃stopped┃stopping┃upgrading)
     * 
     */
    public Output<String> state() {
        return this.state;
    }
    /**
     * Number of vcores
     * 
     */
    @Export(name="vcore", refs={Double.class}, tree="[0]")
    private Output<Double> vcore;

    /**
     * @return Number of vcores
     * 
     */
    public Output<Double> vcore() {
        return this.vcore;
    }
    /**
     * OpenStask region where the VPS is located
     * 
     */
    @Export(name="zone", refs={String.class}, tree="[0]")
    private Output<String> zone;

    /**
     * @return OpenStask region where the VPS is located
     * 
     */
    public Output<String> zone() {
        return this.zone;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Vps(String name) {
        this(name, VpsArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Vps(String name, VpsArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Vps(String name, VpsArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:Vps/vps:Vps", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()));
    }

    private Vps(String name, Output<String> id, @Nullable VpsState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:Vps/vps:Vps", name, state, makeResourceOptions(options, id));
    }

    private static VpsArgs makeArgs(VpsArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? VpsArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
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
    public static Vps get(String name, Output<String> id, @Nullable VpsState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Vps(name, id, state, options);
    }
}
