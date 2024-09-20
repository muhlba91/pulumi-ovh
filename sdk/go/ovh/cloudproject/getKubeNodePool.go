// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get a OVHcloud Managed Kubernetes node pool.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/CloudProject"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			nodepool, err := CloudProject.GetKubeNodePool(ctx, &cloudproject.GetKubeNodePoolArgs{
//				ServiceName: "XXXXXX",
//				KubeId:      "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxx",
//				Name:        "xxxxxx",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("maxNodes", nodepool.MaxNodes)
//			return nil
//		})
//	}
//
// ```
func LookupKubeNodePool(ctx *pulumi.Context, args *LookupKubeNodePoolArgs, opts ...pulumi.InvokeOption) (*LookupKubeNodePoolResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupKubeNodePoolResult
	err := ctx.Invoke("ovh:CloudProject/getKubeNodePool:getKubeNodePool", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKubeNodePool.
type LookupKubeNodePoolArgs struct {
	// The id of the managed kubernetes cluster.
	KubeId string `pulumi:"kubeId"`
	// The name of the node pool.
	Name string `pulumi:"name"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string                   `pulumi:"serviceName"`
	Template    *GetKubeNodePoolTemplate `pulumi:"template"`
}

// A collection of values returned by getKubeNodePool.
type LookupKubeNodePoolResult struct {
	// (Optional) should the pool use the anti-affinity feature. Default to `false`.
	AntiAffinity bool `pulumi:"antiAffinity"`
	// (Optional) Enable auto-scaling for the pool. Default to `false`.
	Autoscale bool `pulumi:"autoscale"`
	// (Optional) scaleDownUnneededTimeSeconds autoscaling parameter
	// How long a node should be unneeded before it is eligible for scale down
	AutoscalingScaleDownUnneededTimeSeconds int `pulumi:"autoscalingScaleDownUnneededTimeSeconds"`
	// (Optional) scaleDownUnreadyTimeSeconds autoscaling parameter
	// How long an unready node should be unneeded before it is eligible for scale down
	AutoscalingScaleDownUnreadyTimeSeconds int `pulumi:"autoscalingScaleDownUnreadyTimeSeconds"`
	// (Optional) scaleDownUtilizationThreshold autoscaling parameter
	// Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down
	AutoscalingScaleDownUtilizationThreshold float64 `pulumi:"autoscalingScaleDownUtilizationThreshold"`
	// Number of nodes which are actually ready in the pool
	AvailableNodes int `pulumi:"availableNodes"`
	// Creation date
	CreatedAt string `pulumi:"createdAt"`
	// Number of nodes present in the pool
	CurrentNodes int `pulumi:"currentNodes"`
	// Number of nodes you desire in the pool
	DesiredNodes int `pulumi:"desiredNodes"`
	// Flavor name
	Flavor string `pulumi:"flavor"`
	// a valid OVHcloud public cloud flavor ID in which the nodes will be started.
	// Ex: "b2-7". Changing this value recreates the resource.
	// You can find the list of flavor IDs: https://www.ovhcloud.com/fr/public-cloud/prices/
	FlavorName string `pulumi:"flavorName"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// See Argument Reference above.
	KubeId string `pulumi:"kubeId"`
	// maximum number of nodes allowed in the pool.
	// Setting `desiredNodes` over this value will raise an error.
	MaxNodes int `pulumi:"maxNodes"`
	// minimum number of nodes allowed in the pool.
	// Setting `desiredNodes` under this value will raise an error.
	MinNodes int `pulumi:"minNodes"`
	// (Optional) should the nodes be billed on a monthly basis. Default to `false`.
	MonthlyBilled bool `pulumi:"monthlyBilled"`
	// (Optional) The name of the nodepool.
	// Changing this value recreates the resource.
	// Warning: "_" char is not allowed!
	Name string `pulumi:"name"`
	// Project id
	ProjectId string `pulumi:"projectId"`
	// See Argument Reference above.
	ServiceName string `pulumi:"serviceName"`
	// Status describing the state between number of nodes wanted and available ones
	SizeStatus string `pulumi:"sizeStatus"`
	// Current status
	Status   string                   `pulumi:"status"`
	Template *GetKubeNodePoolTemplate `pulumi:"template"`
	// Number of nodes with the latest version installed in the pool
	UpToDateNodes int `pulumi:"upToDateNodes"`
	// Last update date
	UpdatedAt string `pulumi:"updatedAt"`
}

func LookupKubeNodePoolOutput(ctx *pulumi.Context, args LookupKubeNodePoolOutputArgs, opts ...pulumi.InvokeOption) LookupKubeNodePoolResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupKubeNodePoolResultOutput, error) {
			args := v.(LookupKubeNodePoolArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupKubeNodePoolResult
			secret, err := ctx.InvokePackageRaw("ovh:CloudProject/getKubeNodePool:getKubeNodePool", args, &rv, "", opts...)
			if err != nil {
				return LookupKubeNodePoolResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupKubeNodePoolResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupKubeNodePoolResultOutput), nil
			}
			return output, nil
		}).(LookupKubeNodePoolResultOutput)
}

// A collection of arguments for invoking getKubeNodePool.
type LookupKubeNodePoolOutputArgs struct {
	// The id of the managed kubernetes cluster.
	KubeId pulumi.StringInput `pulumi:"kubeId"`
	// The name of the node pool.
	Name pulumi.StringInput `pulumi:"name"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput              `pulumi:"serviceName"`
	Template    GetKubeNodePoolTemplatePtrInput `pulumi:"template"`
}

func (LookupKubeNodePoolOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKubeNodePoolArgs)(nil)).Elem()
}

// A collection of values returned by getKubeNodePool.
type LookupKubeNodePoolResultOutput struct{ *pulumi.OutputState }

func (LookupKubeNodePoolResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupKubeNodePoolResult)(nil)).Elem()
}

func (o LookupKubeNodePoolResultOutput) ToLookupKubeNodePoolResultOutput() LookupKubeNodePoolResultOutput {
	return o
}

func (o LookupKubeNodePoolResultOutput) ToLookupKubeNodePoolResultOutputWithContext(ctx context.Context) LookupKubeNodePoolResultOutput {
	return o
}

// (Optional) should the pool use the anti-affinity feature. Default to `false`.
func (o LookupKubeNodePoolResultOutput) AntiAffinity() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) bool { return v.AntiAffinity }).(pulumi.BoolOutput)
}

// (Optional) Enable auto-scaling for the pool. Default to `false`.
func (o LookupKubeNodePoolResultOutput) Autoscale() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) bool { return v.Autoscale }).(pulumi.BoolOutput)
}

// (Optional) scaleDownUnneededTimeSeconds autoscaling parameter
// How long a node should be unneeded before it is eligible for scale down
func (o LookupKubeNodePoolResultOutput) AutoscalingScaleDownUnneededTimeSeconds() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.AutoscalingScaleDownUnneededTimeSeconds }).(pulumi.IntOutput)
}

// (Optional) scaleDownUnreadyTimeSeconds autoscaling parameter
// How long an unready node should be unneeded before it is eligible for scale down
func (o LookupKubeNodePoolResultOutput) AutoscalingScaleDownUnreadyTimeSeconds() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.AutoscalingScaleDownUnreadyTimeSeconds }).(pulumi.IntOutput)
}

// (Optional) scaleDownUtilizationThreshold autoscaling parameter
// Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down
func (o LookupKubeNodePoolResultOutput) AutoscalingScaleDownUtilizationThreshold() pulumi.Float64Output {
	return o.ApplyT(func(v LookupKubeNodePoolResult) float64 { return v.AutoscalingScaleDownUtilizationThreshold }).(pulumi.Float64Output)
}

// Number of nodes which are actually ready in the pool
func (o LookupKubeNodePoolResultOutput) AvailableNodes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.AvailableNodes }).(pulumi.IntOutput)
}

// Creation date
func (o LookupKubeNodePoolResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// Number of nodes present in the pool
func (o LookupKubeNodePoolResultOutput) CurrentNodes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.CurrentNodes }).(pulumi.IntOutput)
}

// Number of nodes you desire in the pool
func (o LookupKubeNodePoolResultOutput) DesiredNodes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.DesiredNodes }).(pulumi.IntOutput)
}

// Flavor name
func (o LookupKubeNodePoolResultOutput) Flavor() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.Flavor }).(pulumi.StringOutput)
}

// a valid OVHcloud public cloud flavor ID in which the nodes will be started.
// Ex: "b2-7". Changing this value recreates the resource.
// You can find the list of flavor IDs: https://www.ovhcloud.com/fr/public-cloud/prices/
func (o LookupKubeNodePoolResultOutput) FlavorName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.FlavorName }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupKubeNodePoolResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.Id }).(pulumi.StringOutput)
}

// See Argument Reference above.
func (o LookupKubeNodePoolResultOutput) KubeId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.KubeId }).(pulumi.StringOutput)
}

// maximum number of nodes allowed in the pool.
// Setting `desiredNodes` over this value will raise an error.
func (o LookupKubeNodePoolResultOutput) MaxNodes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.MaxNodes }).(pulumi.IntOutput)
}

// minimum number of nodes allowed in the pool.
// Setting `desiredNodes` under this value will raise an error.
func (o LookupKubeNodePoolResultOutput) MinNodes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.MinNodes }).(pulumi.IntOutput)
}

// (Optional) should the nodes be billed on a monthly basis. Default to `false`.
func (o LookupKubeNodePoolResultOutput) MonthlyBilled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) bool { return v.MonthlyBilled }).(pulumi.BoolOutput)
}

// (Optional) The name of the nodepool.
// Changing this value recreates the resource.
// Warning: "_" char is not allowed!
func (o LookupKubeNodePoolResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.Name }).(pulumi.StringOutput)
}

// Project id
func (o LookupKubeNodePoolResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// See Argument Reference above.
func (o LookupKubeNodePoolResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

// Status describing the state between number of nodes wanted and available ones
func (o LookupKubeNodePoolResultOutput) SizeStatus() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.SizeStatus }).(pulumi.StringOutput)
}

// Current status
func (o LookupKubeNodePoolResultOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.Status }).(pulumi.StringOutput)
}

func (o LookupKubeNodePoolResultOutput) Template() GetKubeNodePoolTemplatePtrOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) *GetKubeNodePoolTemplate { return v.Template }).(GetKubeNodePoolTemplatePtrOutput)
}

// Number of nodes with the latest version installed in the pool
func (o LookupKubeNodePoolResultOutput) UpToDateNodes() pulumi.IntOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) int { return v.UpToDateNodes }).(pulumi.IntOutput)
}

// Last update date
func (o LookupKubeNodePoolResultOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v LookupKubeNodePoolResult) string { return v.UpdatedAt }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupKubeNodePoolResultOutput{})
}
