// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dedicated

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

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
//			rescue, err := Dedicated.GetServerBoots(ctx, &dedicated.GetServerBootsArgs{
//				ServiceName: "nsxxxxxxx.ip-xx-xx-xx.eu",
//				BootType:    pulumi.StringRef("rescue"),
//				Kernel:      pulumi.StringRef("rescue64-pro"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			_, err = Dedicated.NewServerUpdate(ctx, "server", &Dedicated.ServerUpdateArgs{
//				ServiceName: pulumi.String("nsxxxxxxx.ip-xx-xx-xx.eu"),
//				BootId:      pulumi.Int(rescue.Results[0]),
//				Monitoring:  pulumi.Bool(true),
//				State:       pulumi.String("ok"),
//				DisplayName: pulumi.String("Some human-readable name"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type ServerUpdate struct {
	pulumi.CustomResourceState

	// boot id of the server
	BootId pulumi.IntOutput `pulumi:"bootId"`
	// boot script of the server
	BootScript pulumi.StringPtrOutput `pulumi:"bootScript"`
	// display name of the dedicated server
	DisplayName pulumi.StringOutput `pulumi:"displayName"`
	// Icmp monitoring state
	Monitoring pulumi.BoolOutput `pulumi:"monitoring"`
	// The serviceName of your dedicated server.
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// error, hacked, hackedBlocked, ok
	State pulumi.StringOutput `pulumi:"state"`
}

// NewServerUpdate registers a new resource with the given unique name, arguments, and options.
func NewServerUpdate(ctx *pulumi.Context,
	name string, args *ServerUpdateArgs, opts ...pulumi.ResourceOption) (*ServerUpdate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ServerUpdate
	err := ctx.RegisterResource("ovh:Dedicated/serverUpdate:ServerUpdate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServerUpdate gets an existing ServerUpdate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServerUpdate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServerUpdateState, opts ...pulumi.ResourceOption) (*ServerUpdate, error) {
	var resource ServerUpdate
	err := ctx.ReadResource("ovh:Dedicated/serverUpdate:ServerUpdate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ServerUpdate resources.
type serverUpdateState struct {
	// boot id of the server
	BootId *int `pulumi:"bootId"`
	// boot script of the server
	BootScript *string `pulumi:"bootScript"`
	// display name of the dedicated server
	DisplayName *string `pulumi:"displayName"`
	// Icmp monitoring state
	Monitoring *bool `pulumi:"monitoring"`
	// The serviceName of your dedicated server.
	ServiceName *string `pulumi:"serviceName"`
	// error, hacked, hackedBlocked, ok
	State *string `pulumi:"state"`
}

type ServerUpdateState struct {
	// boot id of the server
	BootId pulumi.IntPtrInput
	// boot script of the server
	BootScript pulumi.StringPtrInput
	// display name of the dedicated server
	DisplayName pulumi.StringPtrInput
	// Icmp monitoring state
	Monitoring pulumi.BoolPtrInput
	// The serviceName of your dedicated server.
	ServiceName pulumi.StringPtrInput
	// error, hacked, hackedBlocked, ok
	State pulumi.StringPtrInput
}

func (ServerUpdateState) ElementType() reflect.Type {
	return reflect.TypeOf((*serverUpdateState)(nil)).Elem()
}

type serverUpdateArgs struct {
	// boot id of the server
	BootId *int `pulumi:"bootId"`
	// boot script of the server
	BootScript *string `pulumi:"bootScript"`
	// display name of the dedicated server
	DisplayName *string `pulumi:"displayName"`
	// Icmp monitoring state
	Monitoring *bool `pulumi:"monitoring"`
	// The serviceName of your dedicated server.
	ServiceName string `pulumi:"serviceName"`
	// error, hacked, hackedBlocked, ok
	State *string `pulumi:"state"`
}

// The set of arguments for constructing a ServerUpdate resource.
type ServerUpdateArgs struct {
	// boot id of the server
	BootId pulumi.IntPtrInput
	// boot script of the server
	BootScript pulumi.StringPtrInput
	// display name of the dedicated server
	DisplayName pulumi.StringPtrInput
	// Icmp monitoring state
	Monitoring pulumi.BoolPtrInput
	// The serviceName of your dedicated server.
	ServiceName pulumi.StringInput
	// error, hacked, hackedBlocked, ok
	State pulumi.StringPtrInput
}

func (ServerUpdateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serverUpdateArgs)(nil)).Elem()
}

type ServerUpdateInput interface {
	pulumi.Input

	ToServerUpdateOutput() ServerUpdateOutput
	ToServerUpdateOutputWithContext(ctx context.Context) ServerUpdateOutput
}

func (*ServerUpdate) ElementType() reflect.Type {
	return reflect.TypeOf((**ServerUpdate)(nil)).Elem()
}

func (i *ServerUpdate) ToServerUpdateOutput() ServerUpdateOutput {
	return i.ToServerUpdateOutputWithContext(context.Background())
}

func (i *ServerUpdate) ToServerUpdateOutputWithContext(ctx context.Context) ServerUpdateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerUpdateOutput)
}

// ServerUpdateArrayInput is an input type that accepts ServerUpdateArray and ServerUpdateArrayOutput values.
// You can construct a concrete instance of `ServerUpdateArrayInput` via:
//
//	ServerUpdateArray{ ServerUpdateArgs{...} }
type ServerUpdateArrayInput interface {
	pulumi.Input

	ToServerUpdateArrayOutput() ServerUpdateArrayOutput
	ToServerUpdateArrayOutputWithContext(context.Context) ServerUpdateArrayOutput
}

type ServerUpdateArray []ServerUpdateInput

func (ServerUpdateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServerUpdate)(nil)).Elem()
}

func (i ServerUpdateArray) ToServerUpdateArrayOutput() ServerUpdateArrayOutput {
	return i.ToServerUpdateArrayOutputWithContext(context.Background())
}

func (i ServerUpdateArray) ToServerUpdateArrayOutputWithContext(ctx context.Context) ServerUpdateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerUpdateArrayOutput)
}

// ServerUpdateMapInput is an input type that accepts ServerUpdateMap and ServerUpdateMapOutput values.
// You can construct a concrete instance of `ServerUpdateMapInput` via:
//
//	ServerUpdateMap{ "key": ServerUpdateArgs{...} }
type ServerUpdateMapInput interface {
	pulumi.Input

	ToServerUpdateMapOutput() ServerUpdateMapOutput
	ToServerUpdateMapOutputWithContext(context.Context) ServerUpdateMapOutput
}

type ServerUpdateMap map[string]ServerUpdateInput

func (ServerUpdateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServerUpdate)(nil)).Elem()
}

func (i ServerUpdateMap) ToServerUpdateMapOutput() ServerUpdateMapOutput {
	return i.ToServerUpdateMapOutputWithContext(context.Background())
}

func (i ServerUpdateMap) ToServerUpdateMapOutputWithContext(ctx context.Context) ServerUpdateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerUpdateMapOutput)
}

type ServerUpdateOutput struct{ *pulumi.OutputState }

func (ServerUpdateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ServerUpdate)(nil)).Elem()
}

func (o ServerUpdateOutput) ToServerUpdateOutput() ServerUpdateOutput {
	return o
}

func (o ServerUpdateOutput) ToServerUpdateOutputWithContext(ctx context.Context) ServerUpdateOutput {
	return o
}

// boot id of the server
func (o ServerUpdateOutput) BootId() pulumi.IntOutput {
	return o.ApplyT(func(v *ServerUpdate) pulumi.IntOutput { return v.BootId }).(pulumi.IntOutput)
}

// boot script of the server
func (o ServerUpdateOutput) BootScript() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ServerUpdate) pulumi.StringPtrOutput { return v.BootScript }).(pulumi.StringPtrOutput)
}

// display name of the dedicated server
func (o ServerUpdateOutput) DisplayName() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerUpdate) pulumi.StringOutput { return v.DisplayName }).(pulumi.StringOutput)
}

// Icmp monitoring state
func (o ServerUpdateOutput) Monitoring() pulumi.BoolOutput {
	return o.ApplyT(func(v *ServerUpdate) pulumi.BoolOutput { return v.Monitoring }).(pulumi.BoolOutput)
}

// The serviceName of your dedicated server.
func (o ServerUpdateOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerUpdate) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// error, hacked, hackedBlocked, ok
func (o ServerUpdateOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *ServerUpdate) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

type ServerUpdateArrayOutput struct{ *pulumi.OutputState }

func (ServerUpdateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ServerUpdate)(nil)).Elem()
}

func (o ServerUpdateArrayOutput) ToServerUpdateArrayOutput() ServerUpdateArrayOutput {
	return o
}

func (o ServerUpdateArrayOutput) ToServerUpdateArrayOutputWithContext(ctx context.Context) ServerUpdateArrayOutput {
	return o
}

func (o ServerUpdateArrayOutput) Index(i pulumi.IntInput) ServerUpdateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ServerUpdate {
		return vs[0].([]*ServerUpdate)[vs[1].(int)]
	}).(ServerUpdateOutput)
}

type ServerUpdateMapOutput struct{ *pulumi.OutputState }

func (ServerUpdateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ServerUpdate)(nil)).Elem()
}

func (o ServerUpdateMapOutput) ToServerUpdateMapOutput() ServerUpdateMapOutput {
	return o
}

func (o ServerUpdateMapOutput) ToServerUpdateMapOutputWithContext(ctx context.Context) ServerUpdateMapOutput {
	return o
}

func (o ServerUpdateMapOutput) MapIndex(k pulumi.StringInput) ServerUpdateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ServerUpdate {
		return vs[0].(map[string]*ServerUpdate)[vs[1].(string)]
	}).(ServerUpdateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ServerUpdateInput)(nil)).Elem(), &ServerUpdate{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServerUpdateArrayInput)(nil)).Elem(), ServerUpdateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ServerUpdateMapInput)(nil)).Elem(), ServerUpdateMap{})
	pulumi.RegisterOutputType(ServerUpdateOutput{})
	pulumi.RegisterOutputType(ServerUpdateArrayOutput{})
	pulumi.RegisterOutputType(ServerUpdateMapOutput{})
}
