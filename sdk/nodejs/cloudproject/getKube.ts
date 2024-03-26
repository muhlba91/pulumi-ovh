// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this data source to get a OVHcloud Managed Kubernetes Service cluster.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myKubeCluster = ovh.CloudProject.getKube({
 *     serviceName: "XXXXXX",
 *     kubeId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",
 * });
 * export const version = myKubeCluster.then(myKubeCluster => myKubeCluster.version);
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getKube(args: GetKubeArgs, opts?: pulumi.InvokeOptions): Promise<GetKubeResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("ovh:CloudProject/getKube:getKube", {
        "customizationApiservers": args.customizationApiservers,
        "customizationKubeProxy": args.customizationKubeProxy,
        "customizations": args.customizations,
        "kubeId": args.kubeId,
        "kubeProxyMode": args.kubeProxyMode,
        "name": args.name,
        "region": args.region,
        "serviceName": args.serviceName,
        "updatePolicy": args.updatePolicy,
        "version": args.version,
    }, opts);
}

/**
 * A collection of arguments for invoking getKube.
 */
export interface GetKubeArgs {
    /**
     * Kubernetes API server customization
     */
    customizationApiservers?: inputs.CloudProject.GetKubeCustomizationApiserver[];
    /**
     * Kubernetes kube-proxy customization
     */
    customizationKubeProxy?: inputs.CloudProject.GetKubeCustomizationKubeProxy;
    /**
     * **Deprecated** (Optional) Use `customizationApiserver` and `customizationKubeProxy` instead. Kubernetes cluster customization
     *
     * @deprecated Use customizationApiserver instead
     */
    customizations?: inputs.CloudProject.GetKubeCustomization[];
    /**
     * The id of the managed kubernetes cluster.
     */
    kubeId: string;
    /**
     * Selected mode for kube-proxy.
     */
    kubeProxyMode?: string;
    /**
     * The name of the managed kubernetes cluster.
     */
    name?: string;
    /**
     * The OVHcloud public cloud region ID of the managed kubernetes cluster.
     */
    region?: string;
    /**
     * The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: string;
    /**
     * Cluster update policy. Choose between [ALWAYS_UPDATE,MINIMAL_DOWNTIME,NEVER_UPDATE]'.
     */
    updatePolicy?: string;
    /**
     * Kubernetes version of the managed kubernetes cluster.
     */
    version?: string;
}

/**
 * A collection of values returned by getKube.
 */
export interface GetKubeResult {
    /**
     * True if control-plane is up-to-date.
     */
    readonly controlPlaneIsUpToDate: boolean;
    /**
     * Kubernetes API server customization
     */
    readonly customizationApiservers: outputs.CloudProject.GetKubeCustomizationApiserver[];
    /**
     * Kubernetes kube-proxy customization
     */
    readonly customizationKubeProxy?: outputs.CloudProject.GetKubeCustomizationKubeProxy;
    /**
     * **Deprecated** (Optional) Use `customizationApiserver` and `customizationKubeProxy` instead. Kubernetes cluster customization
     *
     * @deprecated Use customizationApiserver instead
     */
    readonly customizations: outputs.CloudProject.GetKubeCustomization[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * True if all nodes and control-plane are up-to-date.
     */
    readonly isUpToDate: boolean;
    /**
     * See Argument Reference above.
     */
    readonly kubeId: string;
    /**
     * Selected mode for kube-proxy.
     */
    readonly kubeProxyMode?: string;
    /**
     * The name of the managed kubernetes cluster.
     */
    readonly name?: string;
    /**
     * Kubernetes versions available for upgrade.
     */
    readonly nextUpgradeVersions: string[];
    /**
     * Cluster nodes URL.
     */
    readonly nodesUrl: string;
    /**
     * OpenStack private network (or vrack) ID to use.
     */
    readonly privateNetworkId: string;
    /**
     * The OVHcloud public cloud region ID of the managed kubernetes cluster.
     */
    readonly region?: string;
    /**
     * See Argument Reference above.
     */
    readonly serviceName: string;
    /**
     * Cluster status. Should be normally set to 'READY'.
     */
    readonly status: string;
    /**
     * Cluster update policy. Choose between [ALWAYS_UPDATE,MINIMAL_DOWNTIME,NEVER_UPDATE]'.
     */
    readonly updatePolicy?: string;
    /**
     * Management URL of your cluster.
     */
    readonly url: string;
    /**
     * Kubernetes version of the managed kubernetes cluster.
     */
    readonly version?: string;
}
/**
 * Use this data source to get a OVHcloud Managed Kubernetes Service cluster.
 *
 * ## Example Usage
 *
 * <!--Start PulumiCodeChooser -->
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as ovh from "@pulumi/ovh";
 *
 * const myKubeCluster = ovh.CloudProject.getKube({
 *     serviceName: "XXXXXX",
 *     kubeId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",
 * });
 * export const version = myKubeCluster.then(myKubeCluster => myKubeCluster.version);
 * ```
 * <!--End PulumiCodeChooser -->
 */
export function getKubeOutput(args: GetKubeOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetKubeResult> {
    return pulumi.output(args).apply((a: any) => getKube(a, opts))
}

/**
 * A collection of arguments for invoking getKube.
 */
export interface GetKubeOutputArgs {
    /**
     * Kubernetes API server customization
     */
    customizationApiservers?: pulumi.Input<pulumi.Input<inputs.CloudProject.GetKubeCustomizationApiserverArgs>[]>;
    /**
     * Kubernetes kube-proxy customization
     */
    customizationKubeProxy?: pulumi.Input<inputs.CloudProject.GetKubeCustomizationKubeProxyArgs>;
    /**
     * **Deprecated** (Optional) Use `customizationApiserver` and `customizationKubeProxy` instead. Kubernetes cluster customization
     *
     * @deprecated Use customizationApiserver instead
     */
    customizations?: pulumi.Input<pulumi.Input<inputs.CloudProject.GetKubeCustomizationArgs>[]>;
    /**
     * The id of the managed kubernetes cluster.
     */
    kubeId: pulumi.Input<string>;
    /**
     * Selected mode for kube-proxy.
     */
    kubeProxyMode?: pulumi.Input<string>;
    /**
     * The name of the managed kubernetes cluster.
     */
    name?: pulumi.Input<string>;
    /**
     * The OVHcloud public cloud region ID of the managed kubernetes cluster.
     */
    region?: pulumi.Input<string>;
    /**
     * The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     */
    serviceName: pulumi.Input<string>;
    /**
     * Cluster update policy. Choose between [ALWAYS_UPDATE,MINIMAL_DOWNTIME,NEVER_UPDATE]'.
     */
    updatePolicy?: pulumi.Input<string>;
    /**
     * Kubernetes version of the managed kubernetes cluster.
     */
    version?: pulumi.Input<string>;
}
