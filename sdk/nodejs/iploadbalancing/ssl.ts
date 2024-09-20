// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates a new custom SSL certificate on your IP Load Balancing
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@ovhcloud/pulumi-ovh";
 * import * as ovh from "@pulumi/ovh";
 *
 * const lb = ovh.IpLoadBalancing.getIpLoadBalancing({
 *     serviceName: "ip-1.2.3.4",
 *     state: "ok",
 * });
 * const sslname = new ovh.iploadbalancing.Ssl("sslname", {
 *     certificate: "...",
 *     chain: "...",
 *     displayName: "test",
 *     key: "...",
 *     serviceName: lb.then(lb => lb.serviceName),
 * });
 * ```
 *
 * ## Import
 *
 * SSL can be imported using the following format `service_name` and the `id` of the ssl, separated by "/" e.g.
 *
 * bash
 *
 * ```sh
 * $ pulumi import ovh:IpLoadBalancing/ssl:Ssl sslname service_name/ssl_id
 * ```
 */
export class Ssl extends pulumi.CustomResource {
    /**
     * Get an existing Ssl resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SslState, opts?: pulumi.CustomResourceOptions): Ssl {
        return new Ssl(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'ovh:IpLoadBalancing/ssl:Ssl';

    /**
     * Returns true if the given object is an instance of Ssl.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Ssl {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Ssl.__pulumiType;
    }

    /**
     * Certificate
     */
    public readonly certificate!: pulumi.Output<string>;
    /**
     * Certificate chain
     */
    public readonly chain!: pulumi.Output<string>;
    /**
     * Readable label for loadbalancer ssl
     */
    public readonly displayName!: pulumi.Output<string>;
    /**
     * Expire date of your SSL certificate.
     */
    public /*out*/ readonly expireDate!: pulumi.Output<string>;
    /**
     * Fingerprint of your SSL certificate.
     */
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * Certificate key
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * Subject Alternative Name of your SSL certificate.
     */
    public /*out*/ readonly sans!: pulumi.Output<string[]>;
    /**
     * Serial of your SSL certificate (Deprecated, use fingerprint instead !)
     */
    public /*out*/ readonly serial!: pulumi.Output<string>;
    /**
     * The internal name of your IP load balancing
     */
    public readonly serviceName!: pulumi.Output<string>;
    /**
     * Subject of your SSL certificate.
     */
    public /*out*/ readonly subject!: pulumi.Output<string>;
    /**
     * Type of your SSL certificate. 'built' for SSL certificates managed by the IP Load Balancing. 'custom' for user manager certificates.
     */
    public /*out*/ readonly type!: pulumi.Output<string>;

    /**
     * Create a Ssl resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SslArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SslArgs | SslState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as SslState | undefined;
            resourceInputs["certificate"] = state ? state.certificate : undefined;
            resourceInputs["chain"] = state ? state.chain : undefined;
            resourceInputs["displayName"] = state ? state.displayName : undefined;
            resourceInputs["expireDate"] = state ? state.expireDate : undefined;
            resourceInputs["fingerprint"] = state ? state.fingerprint : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["sans"] = state ? state.sans : undefined;
            resourceInputs["serial"] = state ? state.serial : undefined;
            resourceInputs["serviceName"] = state ? state.serviceName : undefined;
            resourceInputs["subject"] = state ? state.subject : undefined;
            resourceInputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as SslArgs | undefined;
            if ((!args || args.certificate === undefined) && !opts.urn) {
                throw new Error("Missing required property 'certificate'");
            }
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            if ((!args || args.serviceName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serviceName'");
            }
            resourceInputs["certificate"] = args ? args.certificate : undefined;
            resourceInputs["chain"] = args ? args.chain : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["key"] = args?.key ? pulumi.secret(args.key) : undefined;
            resourceInputs["serviceName"] = args ? args.serviceName : undefined;
            resourceInputs["expireDate"] = undefined /*out*/;
            resourceInputs["fingerprint"] = undefined /*out*/;
            resourceInputs["sans"] = undefined /*out*/;
            resourceInputs["serial"] = undefined /*out*/;
            resourceInputs["subject"] = undefined /*out*/;
            resourceInputs["type"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["key"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Ssl.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Ssl resources.
 */
export interface SslState {
    /**
     * Certificate
     */
    certificate?: pulumi.Input<string>;
    /**
     * Certificate chain
     */
    chain?: pulumi.Input<string>;
    /**
     * Readable label for loadbalancer ssl
     */
    displayName?: pulumi.Input<string>;
    /**
     * Expire date of your SSL certificate.
     */
    expireDate?: pulumi.Input<string>;
    /**
     * Fingerprint of your SSL certificate.
     */
    fingerprint?: pulumi.Input<string>;
    /**
     * Certificate key
     */
    key?: pulumi.Input<string>;
    /**
     * Subject Alternative Name of your SSL certificate.
     */
    sans?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Serial of your SSL certificate (Deprecated, use fingerprint instead !)
     */
    serial?: pulumi.Input<string>;
    /**
     * The internal name of your IP load balancing
     */
    serviceName?: pulumi.Input<string>;
    /**
     * Subject of your SSL certificate.
     */
    subject?: pulumi.Input<string>;
    /**
     * Type of your SSL certificate. 'built' for SSL certificates managed by the IP Load Balancing. 'custom' for user manager certificates.
     */
    type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Ssl resource.
 */
export interface SslArgs {
    /**
     * Certificate
     */
    certificate: pulumi.Input<string>;
    /**
     * Certificate chain
     */
    chain?: pulumi.Input<string>;
    /**
     * Readable label for loadbalancer ssl
     */
    displayName?: pulumi.Input<string>;
    /**
     * Certificate key
     */
    key: pulumi.Input<string>;
    /**
     * The internal name of your IP load balancing
     */
    serviceName: pulumi.Input<string>;
}
