// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to retrieve information about a DBaas logs output graylog stream.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const stream = ovh.Dbaas.getLogsOutputGraylogStream({
 *     serviceName: "ldp-xx-xxxxx",
 *     title: "my stream",
 * });
 * ```
 */
export function getLogsOutputGraylogStream(args: GetLogsOutputGraylogStreamArgs, opts?: pulumi.InvokeOptions): Promise<GetLogsOutputGraylogStreamResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:Dbaas/getLogsOutputGraylogStream:getLogsOutputGraylogStream", {
        "serviceName": args.serviceName,
        "title": args.title,
    }, opts);
}

/**
 * A collection of arguments for invoking getLogsOutputGraylogStream.
 */
export interface GetLogsOutputGraylogStreamArgs {
    /**
     * The service name. It's the ID of your Logs Data Platform instance.
     */
    serviceName: string;
    /**
     * Stream description
     */
    title: string;
}

/**
 * A collection of values returned by getLogsOutputGraylogStream.
 */
export interface GetLogsOutputGraylogStreamResult {
    readonly canAlert: boolean;
    /**
     * Cold storage compression method
     */
    readonly coldStorageCompression: string;
    /**
     * ColdStorage content
     */
    readonly coldStorageContent: string;
    /**
     * Is Cold storage enabled?
     */
    readonly coldStorageEnabled: boolean;
    /**
     * Notify on new Cold storage archive
     */
    readonly coldStorageNotifyEnabled: boolean;
    /**
     * Cold storage retention in year
     */
    readonly coldStorageRetention: number;
    /**
     * ColdStorage destination
     */
    readonly coldStorageTarget: string;
    /**
     * Stream creation
     */
    readonly createdAt: string;
    /**
     * Stream description
     */
    readonly description: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Enable ES indexing
     */
    readonly indexingEnabled: boolean;
    /**
     * Maximum indexing size (in GB)
     */
    readonly indexingMaxSize: number;
    /**
     * If set, notify when size is near 80, 90 or 100 % of the maximum configured setting
     */
    readonly indexingNotifyEnabled: boolean;
    /**
     * Indicates if you are allowed to edit entry
     */
    readonly isEditable: boolean;
    /**
     * Indicates if you are allowed to share entry
     */
    readonly isShareable: boolean;
    /**
     * Number of alert condition
     */
    readonly nbAlertCondition: number;
    /**
     * Number of coldstored archives
     */
    readonly nbArchive: number;
    /**
     * Parent stream ID
     */
    readonly parentStreamId: string;
    /**
     * If set, pause indexing when maximum size is reach
     */
    readonly pauseIndexingOnMaxSize: boolean;
    /**
     * Retention ID
     */
    readonly retentionId: string;
    readonly serviceName: string;
    /**
     * Stream ID
     */
    readonly streamId: string;
    readonly title: string;
    /**
     * Stream last update
     */
    readonly updatedAt: string;
    /**
     * Enable Websocket
     */
    readonly webSocketEnabled: boolean;
    /**
     * Write token of the stream (empty if the caller is not the owner of the stream)
     */
    readonly writeToken: string;
}
/**
 * Use this data source to retrieve information about a DBaas logs output graylog stream.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const stream = ovh.Dbaas.getLogsOutputGraylogStream({
 *     serviceName: "ldp-xx-xxxxx",
 *     title: "my stream",
 * });
 * ```
 */
export function getLogsOutputGraylogStreamOutput(args: GetLogsOutputGraylogStreamOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLogsOutputGraylogStreamResult> {
    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invokeOutput("ovh:Dbaas/getLogsOutputGraylogStream:getLogsOutputGraylogStream", {
        "serviceName": args.serviceName,
        "title": args.title,
    }, opts);
}

/**
 * A collection of arguments for invoking getLogsOutputGraylogStream.
 */
export interface GetLogsOutputGraylogStreamOutputArgs {
    /**
     * The service name. It's the ID of your Logs Data Platform instance.
     */
    serviceName: pulumi.Input<string>;
    /**
     * Stream description
     */
    title: pulumi.Input<string>;
}
