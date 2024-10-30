// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Vrack;

import com.ovhcloud.pulumi.ovh.Utilities;
import com.ovhcloud.pulumi.ovh.Vrack.VrackArgs;
import com.ovhcloud.pulumi.ovh.Vrack.inputs.VrackState;
import com.ovhcloud.pulumi.ovh.Vrack.outputs.VrackOrder;
import com.ovhcloud.pulumi.ovh.Vrack.outputs.VrackPlan;
import com.ovhcloud.pulumi.ovh.Vrack.outputs.VrackPlanOption;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
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
 * import com.pulumi.ovh.Me.MeFunctions;
 * import com.pulumi.ovh.Order.OrderFunctions;
 * import com.pulumi.ovh.Order.inputs.GetCartArgs;
 * import com.pulumi.ovh.Order.inputs.GetCartProductPlanArgs;
 * import com.pulumi.ovh.Vrack.Vrack;
 * import com.pulumi.ovh.Vrack.VrackArgs;
 * import com.pulumi.ovh.Vrack.inputs.VrackPlanArgs;
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
 *         final var myaccount = MeFunctions.getMe();
 * 
 *         final var mycart = OrderFunctions.getCart(GetCartArgs.builder()
 *             .ovhSubsidiary(myaccount.applyValue(getMeResult -> getMeResult.ovhSubsidiary()))
 *             .build());
 * 
 *         final var vrackCartProductPlan = OrderFunctions.getCartProductPlan(GetCartProductPlanArgs.builder()
 *             .cartId(mycart.applyValue(getCartResult -> getCartResult.id()))
 *             .priceCapacity("renew")
 *             .product("vrack")
 *             .planCode("vrack")
 *             .build());
 * 
 *         var vrackVrack = new Vrack("vrackVrack", VrackArgs.builder()
 *             .ovhSubsidiary(mycart.applyValue(getCartResult -> getCartResult.ovhSubsidiary()))
 *             .description("my vrack")
 *             .plan(VrackPlanArgs.builder()
 *                 .duration(vrackCartProductPlan.applyValue(getCartProductPlanResult -> getCartProductPlanResult.selectedPrices()[0].duration()))
 *                 .planCode(vrackCartProductPlan.applyValue(getCartProductPlanResult -> getCartProductPlanResult.planCode()))
 *                 .pricingMode(vrackCartProductPlan.applyValue(getCartProductPlanResult -> getCartProductPlanResult.selectedPrices()[0].pricingMode()))
 *                 .build())
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
 * A vRack can be imported using the `service_name`.
 * 
 * Using the following configuration:
 * 
 * hcl
 * 
 * import {
 * 
 *   to = ovh_vrack.vrack
 * 
 *   id = &#34;&lt;service name&gt;&#34;
 * 
 * }
 * 
 * You can then run:
 * 
 * bash
 * 
 * $ pulumi preview -generate-config-out=vrack.tf
 * 
 * $ pulumi up
 * 
 * The file `vrack.tf` will then contain the imported resource&#39;s configuration, that can be copied next to the `import` block above.
 * 
 * See https://developer.hashicorp.com/terraform/language/import/generating-configuration for more details.
 * 
 */
@ResourceType(type="ovh:Vrack/vrack:Vrack")
public class Vrack extends com.pulumi.resources.CustomResource {
    /**
     * The URN of the vrack, used with IAM permissions
     * 
     */
    @Export(name="VrackURN", refs={String.class}, tree="[0]")
    private Output<String> VrackURN;

    /**
     * @return The URN of the vrack, used with IAM permissions
     * 
     */
    public Output<String> VrackURN() {
        return this.VrackURN;
    }
    /**
     * yourvrackdescription
     * 
     */
    @Export(name="description", refs={String.class}, tree="[0]")
    private Output<String> description;

    /**
     * @return yourvrackdescription
     * 
     */
    public Output<String> description() {
        return this.description;
    }
    /**
     * yourvrackname
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return yourvrackname
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * Details about an Order
     * 
     */
    @Export(name="orders", refs={List.class,VrackOrder.class}, tree="[0,1]")
    private Output<List<VrackOrder>> orders;

    /**
     * @return Details about an Order
     * 
     */
    public Output<List<VrackOrder>> orders() {
        return this.orders;
    }
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     * 
     */
    @Export(name="ovhSubsidiary", refs={String.class}, tree="[0]")
    private Output<String> ovhSubsidiary;

    /**
     * @return OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     * 
     */
    public Output<String> ovhSubsidiary() {
        return this.ovhSubsidiary;
    }
    /**
     * Ovh payment mode
     * 
     * @deprecated
     * This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     * 
     */
    @Deprecated /* This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used. */
    @Export(name="paymentMean", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> paymentMean;

    /**
     * @return Ovh payment mode
     * 
     */
    public Output<Optional<String>> paymentMean() {
        return Codegen.optional(this.paymentMean);
    }
    /**
     * Product Plan to order
     * 
     */
    @Export(name="plan", refs={VrackPlan.class}, tree="[0]")
    private Output<VrackPlan> plan;

    /**
     * @return Product Plan to order
     * 
     */
    public Output<VrackPlan> plan() {
        return this.plan;
    }
    /**
     * Product Plan to order
     * 
     */
    @Export(name="planOptions", refs={List.class,VrackPlanOption.class}, tree="[0,1]")
    private Output</* @Nullable */ List<VrackPlanOption>> planOptions;

    /**
     * @return Product Plan to order
     * 
     */
    public Output<Optional<List<VrackPlanOption>>> planOptions() {
        return Codegen.optional(this.planOptions);
    }
    /**
     * The internal name of your vrack
     * 
     */
    @Export(name="serviceName", refs={String.class}, tree="[0]")
    private Output<String> serviceName;

    /**
     * @return The internal name of your vrack
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Vrack(java.lang.String name) {
        this(name, VrackArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Vrack(java.lang.String name, @Nullable VrackArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Vrack(java.lang.String name, @Nullable VrackArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:Vrack/vrack:Vrack", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Vrack(java.lang.String name, Output<java.lang.String> id, @Nullable VrackState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:Vrack/vrack:Vrack", name, state, makeResourceOptions(options, id), false);
    }

    private static VrackArgs makeArgs(@Nullable VrackArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? VrackArgs.Empty : args;
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
    public static Vrack get(java.lang.String name, Output<java.lang.String> id, @Nullable VrackState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Vrack(name, id, state, options);
    }
}
