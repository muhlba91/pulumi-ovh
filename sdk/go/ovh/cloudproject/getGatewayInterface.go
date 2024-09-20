// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this datasource to get a public cloud project Gateway Interface.
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
//			_, err := CloudProject.GetGatewayInterface(ctx, &cloudproject.GetGatewayInterfaceArgs{
//				Id:          "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx",
//				InterfaceId: "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyy",
//				Region:      "GRA11",
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
func LookupGatewayInterface(ctx *pulumi.Context, args *LookupGatewayInterfaceArgs, opts ...pulumi.InvokeOption) (*LookupGatewayInterfaceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupGatewayInterfaceResult
	err := ctx.Invoke("ovh:CloudProject/getGatewayInterface:getGatewayInterface", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGatewayInterface.
type LookupGatewayInterfaceArgs struct {
	// ID of the gateway
	Id string `pulumi:"id"`
	// ID of the interface
	InterfaceId string `pulumi:"interfaceId"`
	// Region of the gateway
	Region string `pulumi:"region"`
	// ID of the cloud project
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getGatewayInterface.
type LookupGatewayInterfaceResult struct {
	// ID of the gateway
	Id string `pulumi:"id"`
	// ID of the interface
	InterfaceId string `pulumi:"interfaceId"`
	// IP of the interface
	Ip string `pulumi:"ip"`
	// Network ID of the interface
	NetworkId string `pulumi:"networkId"`
	// Region of the gateway
	Region string `pulumi:"region"`
	// ID of the cloud project
	ServiceName string `pulumi:"serviceName"`
	// ID of the subnet to add
	SubnetId string `pulumi:"subnetId"`
}

func LookupGatewayInterfaceOutput(ctx *pulumi.Context, args LookupGatewayInterfaceOutputArgs, opts ...pulumi.InvokeOption) LookupGatewayInterfaceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupGatewayInterfaceResultOutput, error) {
			args := v.(LookupGatewayInterfaceArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv LookupGatewayInterfaceResult
			secret, err := ctx.InvokePackageRaw("ovh:CloudProject/getGatewayInterface:getGatewayInterface", args, &rv, "", opts...)
			if err != nil {
				return LookupGatewayInterfaceResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(LookupGatewayInterfaceResultOutput)
			if secret {
				return pulumi.ToSecret(output).(LookupGatewayInterfaceResultOutput), nil
			}
			return output, nil
		}).(LookupGatewayInterfaceResultOutput)
}

// A collection of arguments for invoking getGatewayInterface.
type LookupGatewayInterfaceOutputArgs struct {
	// ID of the gateway
	Id pulumi.StringInput `pulumi:"id"`
	// ID of the interface
	InterfaceId pulumi.StringInput `pulumi:"interfaceId"`
	// Region of the gateway
	Region pulumi.StringInput `pulumi:"region"`
	// ID of the cloud project
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (LookupGatewayInterfaceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGatewayInterfaceArgs)(nil)).Elem()
}

// A collection of values returned by getGatewayInterface.
type LookupGatewayInterfaceResultOutput struct{ *pulumi.OutputState }

func (LookupGatewayInterfaceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupGatewayInterfaceResult)(nil)).Elem()
}

func (o LookupGatewayInterfaceResultOutput) ToLookupGatewayInterfaceResultOutput() LookupGatewayInterfaceResultOutput {
	return o
}

func (o LookupGatewayInterfaceResultOutput) ToLookupGatewayInterfaceResultOutputWithContext(ctx context.Context) LookupGatewayInterfaceResultOutput {
	return o
}

// ID of the gateway
func (o LookupGatewayInterfaceResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGatewayInterfaceResult) string { return v.Id }).(pulumi.StringOutput)
}

// ID of the interface
func (o LookupGatewayInterfaceResultOutput) InterfaceId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGatewayInterfaceResult) string { return v.InterfaceId }).(pulumi.StringOutput)
}

// IP of the interface
func (o LookupGatewayInterfaceResultOutput) Ip() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGatewayInterfaceResult) string { return v.Ip }).(pulumi.StringOutput)
}

// Network ID of the interface
func (o LookupGatewayInterfaceResultOutput) NetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGatewayInterfaceResult) string { return v.NetworkId }).(pulumi.StringOutput)
}

// Region of the gateway
func (o LookupGatewayInterfaceResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGatewayInterfaceResult) string { return v.Region }).(pulumi.StringOutput)
}

// ID of the cloud project
func (o LookupGatewayInterfaceResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGatewayInterfaceResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

// ID of the subnet to add
func (o LookupGatewayInterfaceResultOutput) SubnetId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupGatewayInterfaceResult) string { return v.SubnetId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupGatewayInterfaceResultOutput{})
}
