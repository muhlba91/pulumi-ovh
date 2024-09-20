// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve information about an identity user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myUser = ovh.Me.getIdentityUser({
 *     user: "my_user_login",
 * });
 * ```
 */
export function getIdentityUser(args: GetIdentityUserArgs, opts?: pulumi.InvokeOptions): Promise<GetIdentityUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Me/getIdentityUser:getIdentityUser", {
        "user": args.user,
    }, opts);
}

/**
 * A collection of arguments for invoking getIdentityUser.
 */
export interface GetIdentityUserArgs {
    /**
     * User's login.
     */
    user: string;
}

/**
 * A collection of values returned by getIdentityUser.
 */
export interface GetIdentityUserResult {
    /**
     * User's identity URN.
     */
    readonly UserURN: string;
    /**
     * Creation date of this user.
     */
    readonly creation: string;
    /**
     * User description.
     */
    readonly description: string;
    /**
     * User's email.
     */
    readonly email: string;
    /**
     * User's group.
     */
    readonly group: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Last update of this user.
     */
    readonly lastUpdate: string;
    /**
     * User's login suffix.
     */
    readonly login: string;
    /**
     * When the user changed his password for the last time.
     */
    readonly passwordLastUpdate: string;
    /**
     * Current user's status.
     */
    readonly status: string;
    readonly user: string;
}
/**
 * Use this data source to retrieve information about an identity user.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myUser = ovh.Me.getIdentityUser({
 *     user: "my_user_login",
 * });
 * ```
 */
export function getIdentityUserOutput(args: GetIdentityUserOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIdentityUserResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ovh:Me/getIdentityUser:getIdentityUser", {
        "user": args.user,
    }, opts);
}

/**
 * A collection of arguments for invoking getIdentityUser.
 */
export interface GetIdentityUserOutputArgs {
    /**
     * User's login.
     */
    user: pulumi.Input<string>;
}
