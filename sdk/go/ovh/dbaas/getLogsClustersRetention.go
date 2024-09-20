// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve information about a DBaas logs cluster retention.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/Dbaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Dbaas.GetLogsClustersRetention(ctx, &dbaas.GetLogsClustersRetentionArgs{
//				ClusterId:   "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
//				RetentionId: pulumi.StringRef("yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy"),
//				ServiceName: "ldp-xx-xxxxx",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// It is also possible to retrieve a retention using its duration:
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/Dbaas"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Dbaas.GetLogsClustersRetention(ctx, &dbaas.GetLogsClustersRetentionArgs{
//				ClusterId:   "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
//				Duration:    pulumi.StringRef("P14D"),
//				ServiceName: "ldp-xx-xxxxx",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetLogsClustersRetention(ctx *pulumi.Context, args *GetLogsClustersRetentionArgs, opts ...pulumi.InvokeOption) (*GetLogsClustersRetentionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetLogsClustersRetentionResult
	err := ctx.Invoke("ovh:Dbaas/getLogsClustersRetention:getLogsClustersRetention", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLogsClustersRetention.
type GetLogsClustersRetentionArgs struct {
	// Cluster ID
	ClusterId string `pulumi:"clusterId"`
	// Indexed duration expressed in ISO-8601 format
	Duration *string `pulumi:"duration"`
	// ID of the retention object
	RetentionId *string `pulumi:"retentionId"`
	// The service name. It's the ID of your Logs Data Platform instance.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getLogsClustersRetention.
type GetLogsClustersRetentionResult struct {
	ClusterId string `pulumi:"clusterId"`
	// Indexed duration expressed in ISO-8601 format
	Duration string `pulumi:"duration"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Indicates if a new stream can use it
	IsSupported bool `pulumi:"isSupported"`
	// ID of the retention that can be used when creating a stream
	RetentionId string `pulumi:"retentionId"`
	ServiceName string `pulumi:"serviceName"`
}

func GetLogsClustersRetentionOutput(ctx *pulumi.Context, args GetLogsClustersRetentionOutputArgs, opts ...pulumi.InvokeOption) GetLogsClustersRetentionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetLogsClustersRetentionResultOutput, error) {
			args := v.(GetLogsClustersRetentionArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetLogsClustersRetentionResult
			secret, err := ctx.InvokePackageRaw("ovh:Dbaas/getLogsClustersRetention:getLogsClustersRetention", args, &rv, "", opts...)
			if err != nil {
				return GetLogsClustersRetentionResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetLogsClustersRetentionResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetLogsClustersRetentionResultOutput), nil
			}
			return output, nil
		}).(GetLogsClustersRetentionResultOutput)
}

// A collection of arguments for invoking getLogsClustersRetention.
type GetLogsClustersRetentionOutputArgs struct {
	// Cluster ID
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
	// Indexed duration expressed in ISO-8601 format
	Duration pulumi.StringPtrInput `pulumi:"duration"`
	// ID of the retention object
	RetentionId pulumi.StringPtrInput `pulumi:"retentionId"`
	// The service name. It's the ID of your Logs Data Platform instance.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (GetLogsClustersRetentionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetLogsClustersRetentionArgs)(nil)).Elem()
}

// A collection of values returned by getLogsClustersRetention.
type GetLogsClustersRetentionResultOutput struct{ *pulumi.OutputState }

func (GetLogsClustersRetentionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetLogsClustersRetentionResult)(nil)).Elem()
}

func (o GetLogsClustersRetentionResultOutput) ToGetLogsClustersRetentionResultOutput() GetLogsClustersRetentionResultOutput {
	return o
}

func (o GetLogsClustersRetentionResultOutput) ToGetLogsClustersRetentionResultOutputWithContext(ctx context.Context) GetLogsClustersRetentionResultOutput {
	return o
}

func (o GetLogsClustersRetentionResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v GetLogsClustersRetentionResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// Indexed duration expressed in ISO-8601 format
func (o GetLogsClustersRetentionResultOutput) Duration() pulumi.StringOutput {
	return o.ApplyT(func(v GetLogsClustersRetentionResult) string { return v.Duration }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetLogsClustersRetentionResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetLogsClustersRetentionResult) string { return v.Id }).(pulumi.StringOutput)
}

// Indicates if a new stream can use it
func (o GetLogsClustersRetentionResultOutput) IsSupported() pulumi.BoolOutput {
	return o.ApplyT(func(v GetLogsClustersRetentionResult) bool { return v.IsSupported }).(pulumi.BoolOutput)
}

// ID of the retention that can be used when creating a stream
func (o GetLogsClustersRetentionResultOutput) RetentionId() pulumi.StringOutput {
	return o.ApplyT(func(v GetLogsClustersRetentionResult) string { return v.RetentionId }).(pulumi.StringOutput)
}

func (o GetLogsClustersRetentionResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetLogsClustersRetentionResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetLogsClustersRetentionResultOutput{})
}
