// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get the linked vrack on your public cloud project.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const vrackVRack = ovh.CloudProject.getVRack({
 *     serviceName: "XXXXXX",
 * });
 * export const vrack = vrackVRack;
 * ```
 */
export function getVRack(args: GetVRackArgs, opts?: pulumi.InvokeOptions): Promise<GetVRackResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:CloudProject/getVRack:getVRack", {
        "serviceName": args.serviceName,
    }, opts);
}

/**
 * A collection of arguments for invoking getVRack.
 */
export interface GetVRackArgs {
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: string;
}

/**
 * A collection of values returned by getVRack.
 */
export interface GetVRackResult {
    readonly description: string;
    /**
     * The id of the vrack
     */
    readonly id: string;
    /**
     * The name of the vrack
     */
    readonly name: string;
    /**
     * The id of the public cloud project
     */
    readonly serviceName: string;
}
/**
 * Use this data source to get the linked vrack on your public cloud project.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const vrackVRack = ovh.CloudProject.getVRack({
 *     serviceName: "XXXXXX",
 * });
 * export const vrack = vrackVRack;
 * ```
 */
export function getVRackOutput(args: GetVRackOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVRackResult> {
    return pulumi.output(args).apply((a: any) => getVRack(a, opts))
}

/**
 * A collection of arguments for invoking getVRack.
 */
export interface GetVRackOutputArgs {
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
}
