// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dedicated

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get the hardward information about a dedicated server associated with your OVHcloud Account.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/Dedicated"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Dedicated.GetServerSpecificationsHardware(ctx, &dedicated.GetServerSpecificationsHardwareArgs{
//				ServiceName: "myserver",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetServerSpecificationsHardware(ctx *pulumi.Context, args *GetServerSpecificationsHardwareArgs, opts ...pulumi.InvokeOption) (*GetServerSpecificationsHardwareResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetServerSpecificationsHardwareResult
	err := ctx.Invoke("ovh:Dedicated/getServerSpecificationsHardware:getServerSpecificationsHardware", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getServerSpecificationsHardware.
type GetServerSpecificationsHardwareArgs struct {
	// The internal name of your dedicated server.
	ServiceName string `pulumi:"serviceName"`
}

// A collection of values returned by getServerSpecificationsHardware.
type GetServerSpecificationsHardwareResult struct {
	// Server boot mode
	BootMode string `pulumi:"bootMode"`
	// Number of cores per processor
	CoresPerProcessor float64 `pulumi:"coresPerProcessor"`
	// Default hardware raid size for this disk group
	DefaultHardwareRaidSize GetServerSpecificationsHardwareDefaultHardwareRaidSize `pulumi:"defaultHardwareRaidSize"`
	// Default hardware raid type for this disk group
	DefaultHardwareRaidType string `pulumi:"defaultHardwareRaidType"`
	// Expansion card description
	Description string `pulumi:"description"`
	// Details about the groups of disks in the server
	DiskGroups []GetServerSpecificationsHardwareDiskGroup `pulumi:"diskGroups"`
	// Details about the server's expansion cards
	ExpansionCards []GetServerSpecificationsHardwareExpansionCard `pulumi:"expansionCards"`
	// Server form factor
	FormFactor string `pulumi:"formFactor"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// RAM capacity
	MemorySize GetServerSpecificationsHardwareMemorySize `pulumi:"memorySize"`
	// Server motherboard
	Motherboard string `pulumi:"motherboard"`
	// Number of processors in this dedicated server
	NumberOfProcessors float64 `pulumi:"numberOfProcessors"`
	// Processor architecture bit
	ProcessorArchitecture string `pulumi:"processorArchitecture"`
	// Processor name
	ProcessorName string `pulumi:"processorName"`
	ServiceName   string `pulumi:"serviceName"`
	// Number of threads per processor
	ThreadsPerProcessor float64 `pulumi:"threadsPerProcessor"`
	// Capacity of the USB keys installed on your server, if any
	UsbKeys []GetServerSpecificationsHardwareUsbKey `pulumi:"usbKeys"`
}

func GetServerSpecificationsHardwareOutput(ctx *pulumi.Context, args GetServerSpecificationsHardwareOutputArgs, opts ...pulumi.InvokeOption) GetServerSpecificationsHardwareResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetServerSpecificationsHardwareResultOutput, error) {
			args := v.(GetServerSpecificationsHardwareArgs)
			opts = internal.PkgInvokeDefaultOpts(opts)
			var rv GetServerSpecificationsHardwareResult
			secret, err := ctx.InvokePackageRaw("ovh:Dedicated/getServerSpecificationsHardware:getServerSpecificationsHardware", args, &rv, "", opts...)
			if err != nil {
				return GetServerSpecificationsHardwareResultOutput{}, err
			}

			output := pulumi.ToOutput(rv).(GetServerSpecificationsHardwareResultOutput)
			if secret {
				return pulumi.ToSecret(output).(GetServerSpecificationsHardwareResultOutput), nil
			}
			return output, nil
		}).(GetServerSpecificationsHardwareResultOutput)
}

// A collection of arguments for invoking getServerSpecificationsHardware.
type GetServerSpecificationsHardwareOutputArgs struct {
	// The internal name of your dedicated server.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
}

func (GetServerSpecificationsHardwareOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetServerSpecificationsHardwareArgs)(nil)).Elem()
}

// A collection of values returned by getServerSpecificationsHardware.
type GetServerSpecificationsHardwareResultOutput struct{ *pulumi.OutputState }

func (GetServerSpecificationsHardwareResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetServerSpecificationsHardwareResult)(nil)).Elem()
}

func (o GetServerSpecificationsHardwareResultOutput) ToGetServerSpecificationsHardwareResultOutput() GetServerSpecificationsHardwareResultOutput {
	return o
}

func (o GetServerSpecificationsHardwareResultOutput) ToGetServerSpecificationsHardwareResultOutputWithContext(ctx context.Context) GetServerSpecificationsHardwareResultOutput {
	return o
}

// Server boot mode
func (o GetServerSpecificationsHardwareResultOutput) BootMode() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.BootMode }).(pulumi.StringOutput)
}

// Number of cores per processor
func (o GetServerSpecificationsHardwareResultOutput) CoresPerProcessor() pulumi.Float64Output {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) float64 { return v.CoresPerProcessor }).(pulumi.Float64Output)
}

// Default hardware raid size for this disk group
func (o GetServerSpecificationsHardwareResultOutput) DefaultHardwareRaidSize() GetServerSpecificationsHardwareDefaultHardwareRaidSizeOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) GetServerSpecificationsHardwareDefaultHardwareRaidSize {
		return v.DefaultHardwareRaidSize
	}).(GetServerSpecificationsHardwareDefaultHardwareRaidSizeOutput)
}

// Default hardware raid type for this disk group
func (o GetServerSpecificationsHardwareResultOutput) DefaultHardwareRaidType() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.DefaultHardwareRaidType }).(pulumi.StringOutput)
}

// Expansion card description
func (o GetServerSpecificationsHardwareResultOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.Description }).(pulumi.StringOutput)
}

// Details about the groups of disks in the server
func (o GetServerSpecificationsHardwareResultOutput) DiskGroups() GetServerSpecificationsHardwareDiskGroupArrayOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) []GetServerSpecificationsHardwareDiskGroup {
		return v.DiskGroups
	}).(GetServerSpecificationsHardwareDiskGroupArrayOutput)
}

// Details about the server's expansion cards
func (o GetServerSpecificationsHardwareResultOutput) ExpansionCards() GetServerSpecificationsHardwareExpansionCardArrayOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) []GetServerSpecificationsHardwareExpansionCard {
		return v.ExpansionCards
	}).(GetServerSpecificationsHardwareExpansionCardArrayOutput)
}

// Server form factor
func (o GetServerSpecificationsHardwareResultOutput) FormFactor() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.FormFactor }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetServerSpecificationsHardwareResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.Id }).(pulumi.StringOutput)
}

// RAM capacity
func (o GetServerSpecificationsHardwareResultOutput) MemorySize() GetServerSpecificationsHardwareMemorySizeOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) GetServerSpecificationsHardwareMemorySize {
		return v.MemorySize
	}).(GetServerSpecificationsHardwareMemorySizeOutput)
}

// Server motherboard
func (o GetServerSpecificationsHardwareResultOutput) Motherboard() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.Motherboard }).(pulumi.StringOutput)
}

// Number of processors in this dedicated server
func (o GetServerSpecificationsHardwareResultOutput) NumberOfProcessors() pulumi.Float64Output {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) float64 { return v.NumberOfProcessors }).(pulumi.Float64Output)
}

// Processor architecture bit
func (o GetServerSpecificationsHardwareResultOutput) ProcessorArchitecture() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.ProcessorArchitecture }).(pulumi.StringOutput)
}

// Processor name
func (o GetServerSpecificationsHardwareResultOutput) ProcessorName() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.ProcessorName }).(pulumi.StringOutput)
}

func (o GetServerSpecificationsHardwareResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

// Number of threads per processor
func (o GetServerSpecificationsHardwareResultOutput) ThreadsPerProcessor() pulumi.Float64Output {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) float64 { return v.ThreadsPerProcessor }).(pulumi.Float64Output)
}

// Capacity of the USB keys installed on your server, if any
func (o GetServerSpecificationsHardwareResultOutput) UsbKeys() GetServerSpecificationsHardwareUsbKeyArrayOutput {
	return o.ApplyT(func(v GetServerSpecificationsHardwareResult) []GetServerSpecificationsHardwareUsbKey {
		return v.UsbKeys
	}).(GetServerSpecificationsHardwareUsbKeyArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetServerSpecificationsHardwareResultOutput{})
}
