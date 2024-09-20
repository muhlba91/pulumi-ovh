// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve information about a region associated with a public cloud project. The region must be associated with the project.
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
//			_, err := CloudProject.GetRegion(ctx, &cloudproject.GetRegionArgs{
//				Name:        "GRA1",
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
func GetRegion(ctx *pulumi.Context, args *GetRegionArgs, opts ...pulumi.InvokeOption) (*GetRegionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetRegionResult
	err := ctx.Invoke("ovh:CloudProject/getRegion:getRegion", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getRegion.
type GetRegionArgs struct {
	// The name of the region associated with the public cloud
	// project.
	Name string `pulumi:"name"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getRegion.
type GetRegionResult struct {
	// the code of the geographic continent the region is running.
	// E.g.: EU for Europe, US for America...
	ContinentCode string `pulumi:"continentCode"`
	// The location code of the datacenter.
	// E.g.: "GRA", meaning Gravelines, for region "GRA1"
	DatacenterLocation string `pulumi:"datacenterLocation"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// the name of the public cloud service
	Name        string `pulumi:"name"`
	ServiceName string `pulumi:"serviceName"`
	// The list of public cloud services running within the region
	Services []GetRegionService `pulumi:"services"`
}

func GetRegionOutput(ctx *pulumi.Context, args GetRegionOutputArgs, opts ...pulumi.InvokeOption) GetRegionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetRegionResultOutput, error) {
			args := v.(GetRegionArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetRegionResult
			secret, err := ctx.InvokePackageRaw("ovh:CloudProject/getRegion:getRegion", args, &rv, "", opts...)
			if err != nil {
				return GetRegionResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetRegionResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetRegionResultOutput), nil
			}
			return output, nil
		}).(GetRegionResultOutput)
}

// A collection of arguments for invoking getRegion.
type GetRegionOutputArgs struct {
	// The name of the region associated with the public cloud
	// project.
	Name pulumi.StringInput `pulumi:"name"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (GetRegionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegionArgs)(nil)).Elem()
}

// A collection of values returned by getRegion.
type GetRegionResultOutput struct{ *pulumi.OutputState }

func (GetRegionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetRegionResult)(nil)).Elem()
}

func (o GetRegionResultOutput) ToGetRegionResultOutput() GetRegionResultOutput {
	return o
}

func (o GetRegionResultOutput) ToGetRegionResultOutputWithContext(ctx context.Context) GetRegionResultOutput {
	return o
}

// the code of the geographic continent the region is running.
// E.g.: EU for Europe, US for America...
func (o GetRegionResultOutput) ContinentCode() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegionResult) string { return v.ContinentCode }).(pulumi.StringOutput)
}

// The location code of the datacenter.
// E.g.: "GRA", meaning Gravelines, for region "GRA1"
func (o GetRegionResultOutput) DatacenterLocation() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegionResult) string { return v.DatacenterLocation }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetRegionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegionResult) string { return v.Id }).(pulumi.StringOutput)
}

// the name of the public cloud service
func (o GetRegionResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegionResult) string { return v.Name }).(pulumi.StringOutput)
}

func (o GetRegionResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetRegionResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

// The list of public cloud services running within the region
func (o GetRegionResultOutput) Services() GetRegionServiceArrayOutput {
	return o.ApplyT(func(v GetRegionResult) []GetRegionService { return v.Services }).(GetRegionServiceArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetRegionResultOutput{})
}
