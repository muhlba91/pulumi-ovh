// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovhcloud/pulumi-ovh";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myaccount = ovh.Me.getMe({});
 * const mycart = myaccount.then(myaccount => ovh.Order.getCart({
 *     ovhSubsidiary: myaccount.ovhSubsidiary,
 * }));
 * const vrackCartProductPlan = mycart.then(mycart => ovh.Order.getCartProductPlan({
 *     cartId: mycart.id,
 *     priceCapacity: "renew",
 *     product: "vrack",
 *     planCode: "vrack",
 * }));
 * const vrackVrack = new ovh.vrack.Vrack("vrackVrack", {
 *     ovhSubsidiary: mycart.then(mycart => mycart.ovhSubsidiary),
 *     description: "my vrack",
 *     plan: {
 *         duration: vrackCartProductPlan.then(vrackCartProductPlan => vrackCartProductPlan.selectedPrices?.[0]?.duration),
 *         planCode: vrackCartProductPlan.then(vrackCartProductPlan => vrackCartProductPlan.planCode),
 *         pricingMode: vrackCartProductPlan.then(vrackCartProductPlan => vrackCartProductPlan.selectedPrices?.[0]?.pricingMode),
 *     },
 * });
 * ```
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
 *   id = "<service name>"
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
 * The file `vrack.tf` will then contain the imported resource's configuration, that can be copied next to the `import` block above.
 *
 * See https://developer.hashicorp.com/terraform/language/import/generating-configuration for more details.
 */
export class Vrack extends pulumi.CustomResource {
    /**
     * Get an existing Vrack resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VrackState, opts?: pulumi.CustomResourceOptions): Vrack {
        return new Vrack(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:Vrack/vrack:Vrack';

    /**
     * Returns true if the given object is an instance of Vrack.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Vrack {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Vrack.__pulumiType;
    }

    /**
     * The URN of the vrack, used with IAM permissions
     */
    public /*out*/ readonly VrackURN!: pulumi.Output<string>;
    /**
     * yourvrackdescription
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * yourvrackname
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Details about an Order
     */
    public readonly orders!: pulumi.Output<outputs.Vrack.VrackOrder[]>;
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     */
    public readonly ovhSubsidiary!: pulumi.Output<string>;
    /**
     * Ovh payment mode
     *
     * @deprecated This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     */
    public readonly paymentMean!: pulumi.Output<string | undefined>;
    /**
     * Product Plan to order
     */
    public readonly plan!: pulumi.Output<outputs.Vrack.VrackPlan>;
    /**
     * Product Plan to order
     */
    public readonly planOptions!: pulumi.Output<outputs.Vrack.VrackPlanOption[] | undefined>;
    /**
     * The internal name of your vrack
     */
    public /*out*/ readonly serviceName!: pulumi.Output<string>;

    /**
     * Create a Vrack resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: VrackArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VrackArgs | VrackState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VrackState | undefined;
            resourceInputs["VrackURN"] = state ? state.VrackURN : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["orders"] = state ? state.orders : undefined;
            resourceInputs["ovhSubsidiary"] = state ? state.ovhSubsidiary : undefined;
            resourceInputs["paymentMean"] = state ? state.paymentMean : undefined;
            resourceInputs["plan"] = state ? state.plan : undefined;
            resourceInputs["planOptions"] = state ? state.planOptions : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
        } else {
            const args = argsOrState as VrackArgs | undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["orders"] = args ? args.orders : undefined;
            resourceInputs["ovhSubsidiary"] = args ? args.ovhSubsidiary : undefined;
            resourceInputs["paymentMean"] = args ? args.paymentMean : undefined;
            resourceInputs["plan"] = args ? args.plan : undefined;
            resourceInputs["planOptions"] = args ? args.planOptions : undefined;
            resourceInputs["VrackURN"] = undefined /*out*/;
            resourceInputs["serviceName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Vrack.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Vrack resources.
 */
export interface VrackState {
    /**
     * The URN of the vrack, used with IAM permissions
     */
    VrackURN?: pulumi.Input<string>;
    /**
     * yourvrackdescription
     */
    description?: pulumi.Input<string>;
    /**
     * yourvrackname
     */
    name?: pulumi.Input<string>;
    /**
     * Details about an Order
     */
    orders?: pulumi.Input<pulumi.Input<inputs.Vrack.VrackOrder>[]>;
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     */
    ovhSubsidiary?: pulumi.Input<string>;
    /**
     * Ovh payment mode
     *
     * @deprecated This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     */
    paymentMean?: pulumi.Input<string>;
    /**
     * Product Plan to order
     */
    plan?: pulumi.Input<inputs.Vrack.VrackPlan>;
    /**
     * Product Plan to order
     */
    planOptions?: pulumi.Input<pulumi.Input<inputs.Vrack.VrackPlanOption>[]>;
    /**
     * The internal name of your vrack
     */
    serviceName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Vrack resource.
 */
export interface VrackArgs {
    /**
     * yourvrackdescription
     */
    description?: pulumi.Input<string>;
    /**
     * yourvrackname
     */
    name?: pulumi.Input<string>;
    /**
     * Details about an Order
     */
    orders?: pulumi.Input<pulumi.Input<inputs.Vrack.VrackOrder>[]>;
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you'll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     */
    ovhSubsidiary?: pulumi.Input<string>;
    /**
     * Ovh payment mode
     *
     * @deprecated This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     */
    paymentMean?: pulumi.Input<string>;
    /**
     * Product Plan to order
     */
    plan?: pulumi.Input<inputs.Vrack.VrackPlan>;
    /**
     * Product Plan to order
     */
    planOptions?: pulumi.Input<pulumi.Input<inputs.Vrack.VrackPlanOption>[]>;
}
