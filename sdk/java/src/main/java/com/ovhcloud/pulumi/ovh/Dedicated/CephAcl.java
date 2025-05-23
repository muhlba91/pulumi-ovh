// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Dedicated;

import com.ovhcloud.pulumi.ovh.Dedicated.CephAclArgs;
import com.ovhcloud.pulumi.ovh.Dedicated.inputs.CephAclState;
import com.ovhcloud.pulumi.ovh.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import javax.annotation.Nullable;

/**
 * Add a new access ACL for the given network/mask.
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
 * import com.pulumi.ovh.Dedicated.DedicatedFunctions;
 * import com.pulumi.ovh.Dedicated.inputs.GetCephArgs;
 * import com.pulumi.ovh.Dedicated.CephAcl;
 * import com.pulumi.ovh.Dedicated.CephAclArgs;
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
 *         final var myCeph = DedicatedFunctions.getCeph(GetCephArgs.builder()
 *             .serviceName("94d423da-0e55-45f2-9812-836460a19939")
 *             .build());
 * 
 *         var my_acl = new CephAcl("my-acl", CephAclArgs.builder()
 *             .serviceName(myCeph.applyValue(getCephResult -> getCephResult.id()))
 *             .network("1.2.3.4")
 *             .netmask("255.255.255.255")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 */
@ResourceType(type="ovh:Dedicated/cephAcl:CephAcl")
public class CephAcl extends com.pulumi.resources.CustomResource {
    /**
     * IP family. `IPv4` or `IPv6`
     * 
     */
    @Export(name="family", refs={String.class}, tree="[0]")
    private Output<String> family;

    /**
     * @return IP family. `IPv4` or `IPv6`
     * 
     */
    public Output<String> family() {
        return this.family;
    }
    /**
     * The network mask to apply
     * 
     */
    @Export(name="netmask", refs={String.class}, tree="[0]")
    private Output<String> netmask;

    /**
     * @return The network mask to apply
     * 
     */
    public Output<String> netmask() {
        return this.netmask;
    }
    /**
     * The network IP to authorize
     * 
     */
    @Export(name="network", refs={String.class}, tree="[0]")
    private Output<String> network;

    /**
     * @return The network IP to authorize
     * 
     */
    public Output<String> network() {
        return this.network;
    }
    /**
     * The internal name of your dedicated CEPH
     * 
     */
    @Export(name="serviceName", refs={String.class}, tree="[0]")
    private Output<String> serviceName;

    /**
     * @return The internal name of your dedicated CEPH
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public CephAcl(java.lang.String name) {
        this(name, CephAclArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public CephAcl(java.lang.String name, CephAclArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public CephAcl(java.lang.String name, CephAclArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:Dedicated/cephAcl:CephAcl", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private CephAcl(java.lang.String name, Output<java.lang.String> id, @Nullable CephAclState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:Dedicated/cephAcl:CephAcl", name, state, makeResourceOptions(options, id), false);
    }

    private static CephAclArgs makeArgs(CephAclArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? CephAclArgs.Empty : args;
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
    public static CephAcl get(java.lang.String name, Output<java.lang.String> id, @Nullable CephAclState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new CephAcl(name, id, state, options);
    }
}
