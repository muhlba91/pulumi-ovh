// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve the list of all the S3 accessKeyId associated with a public cloud project's user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myS3Credentials = ovh.CloudProject.getUserS3Credentials({
 *     serviceName: "XXXXXX",
 *     userId: "1234",
 * });
 * export const accessKeyIds = myS3Credentials.then(myS3Credentials => myS3Credentials.accessKeyIds);
 * ```
 */
export function getUserS3Credentials(args: GetUserS3CredentialsArgs, opts?: pulumi.InvokeOptions): Promise<GetUserS3CredentialsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:CloudProject/getUserS3Credentials:getUserS3Credentials", {
        "serviceName": args.serviceName,
        "userId": args.userId,
    }, opts);
}

/**
 * A collection of arguments for invoking getUserS3Credentials.
 */
export interface GetUserS3CredentialsArgs {
    /**
     * The ID of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: string;
    /**
     * The ID of a public cloud project's user.
     */
    userId: string;
}

/**
 * A collection of values returned by getUserS3Credentials.
 */
export interface GetUserS3CredentialsResult {
    /**
     * The list of the Access Key ID associated with this user.
     */
    readonly accessKeyIds: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly serviceName: string;
    readonly userId: string;
}
/**
 * Use this data source to retrieve the list of all the S3 accessKeyId associated with a public cloud project's user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myS3Credentials = ovh.CloudProject.getUserS3Credentials({
 *     serviceName: "XXXXXX",
 *     userId: "1234",
 * });
 * export const accessKeyIds = myS3Credentials.then(myS3Credentials => myS3Credentials.accessKeyIds);
 * ```
 */
export function getUserS3CredentialsOutput(args: GetUserS3CredentialsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserS3CredentialsResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ovh:CloudProject/getUserS3Credentials:getUserS3Credentials", {
        "serviceName": args.serviceName,
        "userId": args.userId,
    }, opts);
}

/**
 * A collection of arguments for invoking getUserS3Credentials.
 */
export interface GetUserS3CredentialsOutputArgs {
    /**
     * The ID of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
    /**
     * The ID of a public cloud project's user.
     */
    userId: pulumi.Input<string>;
}
