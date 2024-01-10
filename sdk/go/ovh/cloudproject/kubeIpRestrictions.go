// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Apply IP restrictions to an OVHcloud Managed Kubernetes cluster.
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
//			_, err := CloudProject.NewKubeIpRestrictions(ctx, "vrackOnly", &CloudProject.KubeIpRestrictionsArgs{
//				Ips: pulumi.StringArray{
//					pulumi.String("10.42.0.0/16"),
//				},
//				KubeId:      pulumi.String("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx"),
//				ServiceName: pulumi.String("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"),
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// OVHcloud Managed Kubernetes Service cluster IP restrictions can be imported using the `service_name` and the `id` of the cluster, separated by "/" E.g., bash
//
// ```sh
//
//	$ pulumi import ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions iprestrictions service_name/kube_id
//
// ```
type KubeIpRestrictions struct {
	pulumi.CustomResourceState

	// List of CIDR authorized to interact with the managed Kubernetes cluster.
	Ips pulumi.StringArrayOutput `pulumi:"ips"`
	// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
	KubeId pulumi.StringOutput `pulumi:"kubeId"`
	// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
}

// NewKubeIpRestrictions registers a new resource with the given unique name, arguments, and options.
func NewKubeIpRestrictions(ctx *pulumi.Context,
	name string, args *KubeIpRestrictionsArgs, opts ...pulumi.ResourceOption) (*KubeIpRestrictions, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Ips == nil {
		return nil, errors.New("invalid value for required argument 'Ips'")
	}
	if args.KubeId == nil {
		return nil, errors.New("invalid value for required argument 'KubeId'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource KubeIpRestrictions
	err := ctx.RegisterResource("ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetKubeIpRestrictions gets an existing KubeIpRestrictions resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetKubeIpRestrictions(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *KubeIpRestrictionsState, opts ...pulumi.ResourceOption) (*KubeIpRestrictions, error) {
	var resource KubeIpRestrictions
	err := ctx.ReadResource("ovh:CloudProject/kubeIpRestrictions:KubeIpRestrictions", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering KubeIpRestrictions resources.
type kubeIpRestrictionsState struct {
	// List of CIDR authorized to interact with the managed Kubernetes cluster.
	Ips []string `pulumi:"ips"`
	// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
	KubeId *string `pulumi:"kubeId"`
	// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
	ServiceName *string `pulumi:"serviceName"`
}

type KubeIpRestrictionsState struct {
	// List of CIDR authorized to interact with the managed Kubernetes cluster.
	Ips pulumi.StringArrayInput
	// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
	KubeId pulumi.StringPtrInput
	// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
	ServiceName pulumi.StringPtrInput
}

func (KubeIpRestrictionsState) ElementType() reflect.Type {
	return reflect.TypeOf((*kubeIpRestrictionsState)(nil)).Elem()
}

type kubeIpRestrictionsArgs struct {
	// List of CIDR authorized to interact with the managed Kubernetes cluster.
	Ips []string `pulumi:"ips"`
	// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
	KubeId string `pulumi:"kubeId"`
	// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
	ServiceName string `pulumi:"serviceName"`
}

// The set of arguments for constructing a KubeIpRestrictions resource.
type KubeIpRestrictionsArgs struct {
	// List of CIDR authorized to interact with the managed Kubernetes cluster.
	Ips pulumi.StringArrayInput
	// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
	KubeId pulumi.StringInput
	// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
	ServiceName pulumi.StringInput
}

func (KubeIpRestrictionsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*kubeIpRestrictionsArgs)(nil)).Elem()
}

type KubeIpRestrictionsInput interface {
	pulumi.Input

	ToKubeIpRestrictionsOutput() KubeIpRestrictionsOutput
	ToKubeIpRestrictionsOutputWithContext(ctx context.Context) KubeIpRestrictionsOutput
}

func (*KubeIpRestrictions) ElementType() reflect.Type {
	return reflect.TypeOf((**KubeIpRestrictions)(nil)).Elem()
}

func (i *KubeIpRestrictions) ToKubeIpRestrictionsOutput() KubeIpRestrictionsOutput {
	return i.ToKubeIpRestrictionsOutputWithContext(context.Background())
}

func (i *KubeIpRestrictions) ToKubeIpRestrictionsOutputWithContext(ctx context.Context) KubeIpRestrictionsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubeIpRestrictionsOutput)
}

// KubeIpRestrictionsArrayInput is an input type that accepts KubeIpRestrictionsArray and KubeIpRestrictionsArrayOutput values.
// You can construct a concrete instance of `KubeIpRestrictionsArrayInput` via:
//
//	KubeIpRestrictionsArray{ KubeIpRestrictionsArgs{...} }
type KubeIpRestrictionsArrayInput interface {
	pulumi.Input

	ToKubeIpRestrictionsArrayOutput() KubeIpRestrictionsArrayOutput
	ToKubeIpRestrictionsArrayOutputWithContext(context.Context) KubeIpRestrictionsArrayOutput
}

type KubeIpRestrictionsArray []KubeIpRestrictionsInput

func (KubeIpRestrictionsArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KubeIpRestrictions)(nil)).Elem()
}

func (i KubeIpRestrictionsArray) ToKubeIpRestrictionsArrayOutput() KubeIpRestrictionsArrayOutput {
	return i.ToKubeIpRestrictionsArrayOutputWithContext(context.Background())
}

func (i KubeIpRestrictionsArray) ToKubeIpRestrictionsArrayOutputWithContext(ctx context.Context) KubeIpRestrictionsArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubeIpRestrictionsArrayOutput)
}

// KubeIpRestrictionsMapInput is an input type that accepts KubeIpRestrictionsMap and KubeIpRestrictionsMapOutput values.
// You can construct a concrete instance of `KubeIpRestrictionsMapInput` via:
//
//	KubeIpRestrictionsMap{ "key": KubeIpRestrictionsArgs{...} }
type KubeIpRestrictionsMapInput interface {
	pulumi.Input

	ToKubeIpRestrictionsMapOutput() KubeIpRestrictionsMapOutput
	ToKubeIpRestrictionsMapOutputWithContext(context.Context) KubeIpRestrictionsMapOutput
}

type KubeIpRestrictionsMap map[string]KubeIpRestrictionsInput

func (KubeIpRestrictionsMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KubeIpRestrictions)(nil)).Elem()
}

func (i KubeIpRestrictionsMap) ToKubeIpRestrictionsMapOutput() KubeIpRestrictionsMapOutput {
	return i.ToKubeIpRestrictionsMapOutputWithContext(context.Background())
}

func (i KubeIpRestrictionsMap) ToKubeIpRestrictionsMapOutputWithContext(ctx context.Context) KubeIpRestrictionsMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(KubeIpRestrictionsMapOutput)
}

type KubeIpRestrictionsOutput struct{ *pulumi.OutputState }

func (KubeIpRestrictionsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**KubeIpRestrictions)(nil)).Elem()
}

func (o KubeIpRestrictionsOutput) ToKubeIpRestrictionsOutput() KubeIpRestrictionsOutput {
	return o
}

func (o KubeIpRestrictionsOutput) ToKubeIpRestrictionsOutputWithContext(ctx context.Context) KubeIpRestrictionsOutput {
	return o
}

// List of CIDR authorized to interact with the managed Kubernetes cluster.
func (o KubeIpRestrictionsOutput) Ips() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *KubeIpRestrictions) pulumi.StringArrayOutput { return v.Ips }).(pulumi.StringArrayOutput)
}

// The id of the managed Kubernetes cluster. **Changing this value recreates the resource.**
func (o KubeIpRestrictionsOutput) KubeId() pulumi.StringOutput {
	return o.ApplyT(func(v *KubeIpRestrictions) pulumi.StringOutput { return v.KubeId }).(pulumi.StringOutput)
}

// The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used. **Changing this value recreates the resource.**
func (o KubeIpRestrictionsOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *KubeIpRestrictions) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

type KubeIpRestrictionsArrayOutput struct{ *pulumi.OutputState }

func (KubeIpRestrictionsArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*KubeIpRestrictions)(nil)).Elem()
}

func (o KubeIpRestrictionsArrayOutput) ToKubeIpRestrictionsArrayOutput() KubeIpRestrictionsArrayOutput {
	return o
}

func (o KubeIpRestrictionsArrayOutput) ToKubeIpRestrictionsArrayOutputWithContext(ctx context.Context) KubeIpRestrictionsArrayOutput {
	return o
}

func (o KubeIpRestrictionsArrayOutput) Index(i pulumi.IntInput) KubeIpRestrictionsOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *KubeIpRestrictions {
		return vs[0].([]*KubeIpRestrictions)[vs[1].(int)]
	}).(KubeIpRestrictionsOutput)
}

type KubeIpRestrictionsMapOutput struct{ *pulumi.OutputState }

func (KubeIpRestrictionsMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*KubeIpRestrictions)(nil)).Elem()
}

func (o KubeIpRestrictionsMapOutput) ToKubeIpRestrictionsMapOutput() KubeIpRestrictionsMapOutput {
	return o
}

func (o KubeIpRestrictionsMapOutput) ToKubeIpRestrictionsMapOutputWithContext(ctx context.Context) KubeIpRestrictionsMapOutput {
	return o
}

func (o KubeIpRestrictionsMapOutput) MapIndex(k pulumi.StringInput) KubeIpRestrictionsOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *KubeIpRestrictions {
		return vs[0].(map[string]*KubeIpRestrictions)[vs[1].(string)]
	}).(KubeIpRestrictionsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*KubeIpRestrictionsInput)(nil)).Elem(), &KubeIpRestrictions{})
	pulumi.RegisterInputType(reflect.TypeOf((*KubeIpRestrictionsArrayInput)(nil)).Elem(), KubeIpRestrictionsArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*KubeIpRestrictionsMapInput)(nil)).Elem(), KubeIpRestrictionsMap{})
	pulumi.RegisterOutputType(KubeIpRestrictionsOutput{})
	pulumi.RegisterOutputType(KubeIpRestrictionsArrayOutput{})
	pulumi.RegisterOutputType(KubeIpRestrictionsMapOutput{})
}
