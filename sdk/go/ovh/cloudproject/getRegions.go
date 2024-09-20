// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get the regions of a public cloud project.
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
//			_, err := CloudProject.GetRegions(ctx, &cloudproject.GetRegionsArgs{
//				HasServicesUps: []string{
//					"network",
//				},
//				ServiceName: "XXXXXX",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetRegions(ctx *pulumi.Context, args *GetRegionsArgs, opts ...pulumi.InvokeOption) (*GetRegionsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetRegionsResult
	err := ctx.Invoke("ovh:CloudProject/getRegions:getRegions", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRegions.
type GetRegionsArgs struct {
	// List of services which has to be UP in regions.
	// Example: "image", "instance", "network", "storage", "volume", "workflow", ...
	// If left blank, returns all regions associated with the service_name.
	HasServicesUps []string `pulumi:"hasServicesUps"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getRegions.
type GetRegionsResult struct {
	HasServicesUps []string `pulumi:"hasServicesUps"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The list of regions associated with the project, filtered by services UP.
	Names       []string `pulumi:"names"`
	ServiceName string   `pulumi:"serviceName"`
}

func GetRegionsOutput(ctx *pulumi.Context, args GetRegionsOutputArgs, opts ...pulumi.InvokeOption) GetRegionsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetRegionsResultOutput, error) {
			args := v.(GetRegionsArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetRegionsResult
			secret, err := ctx.InvokePackageRaw("ovh:CloudProject/getRegions:getRegions", args, &rv, "", opts...)
			if err != nil {
				return GetRegionsResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetRegionsResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetRegionsResultOutput), nil
			}
			return output, nil
		}).(GetRegionsResultOutput)
}

// A collection of arguments for invoking getRegions.
type GetRegionsOutputArgs struct {
	// List of services which has to be UP in regions.
	// Example: "image", "instance", "network", "storage", "volume", "workflow", ...
	// If left blank, returns all regions associated with the service_name.
	HasServicesUps pulumi.StringArrayInput `pulumi:"hasServicesUps"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (GetRegionsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegionsArgs)(nil)).Elem()
}

// A collection of values returned by getRegions.
type GetRegionsResultOutput struct{ *pulumi.OutputState }

func (GetRegionsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegionsResult)(nil)).Elem()
}

func (o GetRegionsResultOutput) ToGetRegionsResultOutput() GetRegionsResultOutput {
	return o
}

func (o GetRegionsResultOutput) ToGetRegionsResultOutputWithContext(ctx context.Context) GetRegionsResultOutput {
	return o
}

func (o GetRegionsResultOutput) HasServicesUps() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetRegionsResult) []string { return v.HasServicesUps }).(pulumi.StringArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetRegionsResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegionsResult) string { return v.Id }).(pulumi.StringOutput)
}

// The list of regions associated with the project, filtered by services UP.
func (o GetRegionsResultOutput) Names() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetRegionsResult) []string { return v.Names }).(pulumi.StringArrayOutput)
}

func (o GetRegionsResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegionsResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetRegionsResultOutput{})
}
