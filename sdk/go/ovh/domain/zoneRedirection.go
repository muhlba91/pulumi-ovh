// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package domain

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a OVHcloud domain zone redirection.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/Domain"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Domain.NewZoneRedirection(ctx, "test", &Domain.ZoneRedirectionArgs{
//				Subdomain: pulumi.String("test"),
//				Target:    pulumi.String("http://www.ovh"),
//				Type:      pulumi.String("visiblePermanent"),
//				Zone:      pulumi.String("testdemo.ovh"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type ZoneRedirection struct {
	pulumi.CustomResourceState

	// A description of this redirection
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Keywords to describe this redirection
	Keywords pulumi.StringPtrOutput `pulumi:"keywords"`
	// The name of the redirection
	Subdomain pulumi.StringPtrOutput `pulumi:"subdomain"`
	// The value of the redirection
	Target pulumi.StringOutput `pulumi:"target"`
	// Title of this redirection
	Title pulumi.StringPtrOutput `pulumi:"title"`
	// The type of the redirection, with values:
	Type pulumi.StringOutput `pulumi:"type"`
	// The domain to add the redirection to
	Zone pulumi.StringOutput `pulumi:"zone"`
}

// NewZoneRedirection registers a new resource with the given unique name, arguments, and options.
func NewZoneRedirection(ctx *pulumi.Context,
	name string, args *ZoneRedirectionArgs, opts ...pulumi.ResourceOption) (*ZoneRedirection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Target == nil {
		return nil, errors.New("invalid value for required argument 'Target'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	if args.Zone == nil {
		return nil, errors.New("invalid value for required argument 'Zone'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ZoneRedirection
	err := ctx.RegisterResource("ovh:Domain/zoneRedirection:ZoneRedirection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetZoneRedirection gets an existing ZoneRedirection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetZoneRedirection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ZoneRedirectionState, opts ...pulumi.ResourceOption) (*ZoneRedirection, error) {
	var resource ZoneRedirection
	err := ctx.ReadResource("ovh:Domain/zoneRedirection:ZoneRedirection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ZoneRedirection resources.
type zoneRedirectionState struct {
	// A description of this redirection
	Description *string `pulumi:"description"`
	// Keywords to describe this redirection
	Keywords *string `pulumi:"keywords"`
	// The name of the redirection
	Subdomain *string `pulumi:"subdomain"`
	// The value of the redirection
	Target *string `pulumi:"target"`
	// Title of this redirection
	Title *string `pulumi:"title"`
	// The type of the redirection, with values:
	Type *string `pulumi:"type"`
	// The domain to add the redirection to
	Zone *string `pulumi:"zone"`
}

type ZoneRedirectionState struct {
	// A description of this redirection
	Description pulumi.StringPtrInput
	// Keywords to describe this redirection
	Keywords pulumi.StringPtrInput
	// The name of the redirection
	Subdomain pulumi.StringPtrInput
	// The value of the redirection
	Target pulumi.StringPtrInput
	// Title of this redirection
	Title pulumi.StringPtrInput
	// The type of the redirection, with values:
	Type pulumi.StringPtrInput
	// The domain to add the redirection to
	Zone pulumi.StringPtrInput
}

func (ZoneRedirectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*zoneRedirectionState)(nil)).Elem()
}

type zoneRedirectionArgs struct {
	// A description of this redirection
	Description *string `pulumi:"description"`
	// Keywords to describe this redirection
	Keywords *string `pulumi:"keywords"`
	// The name of the redirection
	Subdomain *string `pulumi:"subdomain"`
	// The value of the redirection
	Target string `pulumi:"target"`
	// Title of this redirection
	Title *string `pulumi:"title"`
	// The type of the redirection, with values:
	Type string `pulumi:"type"`
	// The domain to add the redirection to
	Zone string `pulumi:"zone"`
}

// The set of arguments for constructing a ZoneRedirection resource.
type ZoneRedirectionArgs struct {
	// A description of this redirection
	Description pulumi.StringPtrInput
	// Keywords to describe this redirection
	Keywords pulumi.StringPtrInput
	// The name of the redirection
	Subdomain pulumi.StringPtrInput
	// The value of the redirection
	Target pulumi.StringInput
	// Title of this redirection
	Title pulumi.StringPtrInput
	// The type of the redirection, with values:
	Type pulumi.StringInput
	// The domain to add the redirection to
	Zone pulumi.StringInput
}

func (ZoneRedirectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*zoneRedirectionArgs)(nil)).Elem()
}

type ZoneRedirectionInput interface {
	pulumi.Input

	ToZoneRedirectionOutput() ZoneRedirectionOutput
	ToZoneRedirectionOutputWithContext(ctx context.Context) ZoneRedirectionOutput
}

func (*ZoneRedirection) ElementType() reflect.Type {
	return reflect.TypeOf((**ZoneRedirection)(nil)).Elem()
}

func (i *ZoneRedirection) ToZoneRedirectionOutput() ZoneRedirectionOutput {
	return i.ToZoneRedirectionOutputWithContext(context.Background())
}

func (i *ZoneRedirection) ToZoneRedirectionOutputWithContext(ctx context.Context) ZoneRedirectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneRedirectionOutput)
}

// ZoneRedirectionArrayInput is an input type that accepts ZoneRedirectionArray and ZoneRedirectionArrayOutput values.
// You can construct a concrete instance of `ZoneRedirectionArrayInput` via:
//
//	ZoneRedirectionArray{ ZoneRedirectionArgs{...} }
type ZoneRedirectionArrayInput interface {
	pulumi.Input

	ToZoneRedirectionArrayOutput() ZoneRedirectionArrayOutput
	ToZoneRedirectionArrayOutputWithContext(context.Context) ZoneRedirectionArrayOutput
}

type ZoneRedirectionArray []ZoneRedirectionInput

func (ZoneRedirectionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZoneRedirection)(nil)).Elem()
}

func (i ZoneRedirectionArray) ToZoneRedirectionArrayOutput() ZoneRedirectionArrayOutput {
	return i.ToZoneRedirectionArrayOutputWithContext(context.Background())
}

func (i ZoneRedirectionArray) ToZoneRedirectionArrayOutputWithContext(ctx context.Context) ZoneRedirectionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneRedirectionArrayOutput)
}

// ZoneRedirectionMapInput is an input type that accepts ZoneRedirectionMap and ZoneRedirectionMapOutput values.
// You can construct a concrete instance of `ZoneRedirectionMapInput` via:
//
//	ZoneRedirectionMap{ "key": ZoneRedirectionArgs{...} }
type ZoneRedirectionMapInput interface {
	pulumi.Input

	ToZoneRedirectionMapOutput() ZoneRedirectionMapOutput
	ToZoneRedirectionMapOutputWithContext(context.Context) ZoneRedirectionMapOutput
}

type ZoneRedirectionMap map[string]ZoneRedirectionInput

func (ZoneRedirectionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZoneRedirection)(nil)).Elem()
}

func (i ZoneRedirectionMap) ToZoneRedirectionMapOutput() ZoneRedirectionMapOutput {
	return i.ToZoneRedirectionMapOutputWithContext(context.Background())
}

func (i ZoneRedirectionMap) ToZoneRedirectionMapOutputWithContext(ctx context.Context) ZoneRedirectionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ZoneRedirectionMapOutput)
}

type ZoneRedirectionOutput struct{ *pulumi.OutputState }

func (ZoneRedirectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ZoneRedirection)(nil)).Elem()
}

func (o ZoneRedirectionOutput) ToZoneRedirectionOutput() ZoneRedirectionOutput {
	return o
}

func (o ZoneRedirectionOutput) ToZoneRedirectionOutputWithContext(ctx context.Context) ZoneRedirectionOutput {
	return o
}

// A description of this redirection
func (o ZoneRedirectionOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZoneRedirection) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Keywords to describe this redirection
func (o ZoneRedirectionOutput) Keywords() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZoneRedirection) pulumi.StringPtrOutput { return v.Keywords }).(pulumi.StringPtrOutput)
}

// The name of the redirection
func (o ZoneRedirectionOutput) Subdomain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZoneRedirection) pulumi.StringPtrOutput { return v.Subdomain }).(pulumi.StringPtrOutput)
}

// The value of the redirection
func (o ZoneRedirectionOutput) Target() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRedirection) pulumi.StringOutput { return v.Target }).(pulumi.StringOutput)
}

// Title of this redirection
func (o ZoneRedirectionOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ZoneRedirection) pulumi.StringPtrOutput { return v.Title }).(pulumi.StringPtrOutput)
}

// The type of the redirection, with values:
func (o ZoneRedirectionOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRedirection) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// The domain to add the redirection to
func (o ZoneRedirectionOutput) Zone() pulumi.StringOutput {
	return o.ApplyT(func(v *ZoneRedirection) pulumi.StringOutput { return v.Zone }).(pulumi.StringOutput)
}

type ZoneRedirectionArrayOutput struct{ *pulumi.OutputState }

func (ZoneRedirectionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*ZoneRedirection)(nil)).Elem()
}

func (o ZoneRedirectionArrayOutput) ToZoneRedirectionArrayOutput() ZoneRedirectionArrayOutput {
	return o
}

func (o ZoneRedirectionArrayOutput) ToZoneRedirectionArrayOutputWithContext(ctx context.Context) ZoneRedirectionArrayOutput {
	return o
}

func (o ZoneRedirectionArrayOutput) Index(i pulumi.IntInput) ZoneRedirectionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *ZoneRedirection {
		return vs[0].([]*ZoneRedirection)[vs[1].(int)]
	}).(ZoneRedirectionOutput)
}

type ZoneRedirectionMapOutput struct{ *pulumi.OutputState }

func (ZoneRedirectionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*ZoneRedirection)(nil)).Elem()
}

func (o ZoneRedirectionMapOutput) ToZoneRedirectionMapOutput() ZoneRedirectionMapOutput {
	return o
}

func (o ZoneRedirectionMapOutput) ToZoneRedirectionMapOutputWithContext(ctx context.Context) ZoneRedirectionMapOutput {
	return o
}

func (o ZoneRedirectionMapOutput) MapIndex(k pulumi.StringInput) ZoneRedirectionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *ZoneRedirection {
		return vs[0].(map[string]*ZoneRedirection)[vs[1].(string)]
	}).(ZoneRedirectionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneRedirectionInput)(nil)).Elem(), &ZoneRedirection{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneRedirectionArrayInput)(nil)).Elem(), ZoneRedirectionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*ZoneRedirectionMapInput)(nil)).Elem(), ZoneRedirectionMap{})
	pulumi.RegisterOutputType(ZoneRedirectionOutput{})
	pulumi.RegisterOutputType(ZoneRedirectionArrayOutput{})
	pulumi.RegisterOutputType(ZoneRedirectionMapOutput{})
}
