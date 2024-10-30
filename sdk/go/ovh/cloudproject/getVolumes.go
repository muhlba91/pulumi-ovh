// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Get all the volume from a region of a public cloud project
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
//			_, err := CloudProject.GetVolume(ctx, &cloudproject.GetVolumeArgs{
//				RegionName:  "xxx",
//				ServiceName: "yyy",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetVolumes(ctx *pulumi.Context, args *GetVolumesArgs, opts ...pulumi.InvokeOption) (*GetVolumesResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetVolumesResult
	err := ctx.Invoke("ovh:CloudProject/getVolumes:getVolumes", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVolumes.
type GetVolumesArgs struct {
	// A valid OVHcloud public cloud region name in which the volumes are available. Ex.: "GRA11".
	RegionName string `pulumi:"regionName"`
	// The id of the public cloud project.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getVolumes.
type GetVolumesResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The region name where volumes are available
	RegionName string `pulumi:"regionName"`
	// The id of the public cloud project.
	ServiceName string             `pulumi:"serviceName"`
	Volumes     []GetVolumesVolume `pulumi:"volumes"`
}

func GetVolumesOutput(ctx *pulumi.Context, args GetVolumesOutputArgs, opts ...pulumi.InvokeOption) GetVolumesResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetVolumesResultOutput, error) {
			args := v.(GetVolumesArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetVolumesResult
			secret, err := ctx.InvokePackageRaw("ovh:CloudProject/getVolumes:getVolumes", args, &rv, "", opts...)
			if err != nil {
				return GetVolumesResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetVolumesResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetVolumesResultOutput), nil
			}
			return output, nil
		}).(GetVolumesResultOutput)
}

// A collection of arguments for invoking getVolumes.
type GetVolumesOutputArgs struct {
	// A valid OVHcloud public cloud region name in which the volumes are available. Ex.: "GRA11".
	RegionName pulumi.StringInput `pulumi:"regionName"`
	// The id of the public cloud project.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (GetVolumesOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVolumesArgs)(nil)).Elem()
}

// A collection of values returned by getVolumes.
type GetVolumesResultOutput struct{ *pulumi.OutputState }

func (GetVolumesResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetVolumesResult)(nil)).Elem()
}

func (o GetVolumesResultOutput) ToGetVolumesResultOutput() GetVolumesResultOutput {
	return o
}

func (o GetVolumesResultOutput) ToGetVolumesResultOutputWithContext(ctx context.Context) GetVolumesResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetVolumesResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumesResult) string { return v.Id }).(pulumi.StringOutput)
}

// The region name where volumes are available
func (o GetVolumesResultOutput) RegionName() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumesResult) string { return v.RegionName }).(pulumi.StringOutput)
}

// The id of the public cloud project.
func (o GetVolumesResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetVolumesResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func (o GetVolumesResultOutput) Volumes() GetVolumesVolumeArrayOutput {
	return o.ApplyT(func(v GetVolumesResult) []GetVolumesVolume { return v.Volumes }).(GetVolumesVolumeArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetVolumesResultOutput{})
}
