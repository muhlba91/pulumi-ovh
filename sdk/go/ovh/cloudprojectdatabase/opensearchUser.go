// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudprojectdatabase

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// OVHcloud Managed OpenSearch clusters users can be imported using the `service_name`, `cluster_id` and `id` of the user, separated by "/" E.g., bash
//
// ```sh
//
//	$ pulumi import ovh:CloudProjectDatabase/opensearchUser:OpensearchUser my_user service_name/cluster_id/id
//
// ```
type OpensearchUser struct {
	pulumi.CustomResourceState

	// Acls of the user.
	Acls OpensearchUserAclArrayOutput `pulumi:"acls"`
	// Cluster ID.
	ClusterId pulumi.StringOutput `pulumi:"clusterId"`
	// Date of the creation of the user.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// Username affected by this acl. A user named "avnadmin" is map with already created admin user and reset his password instead of create a new user.
	Name pulumi.StringOutput `pulumi:"name"`
	// (Sensitive) Password of the user.
	Password pulumi.StringOutput `pulumi:"password"`
	// Arbitrary string to change to trigger a password update
	PasswordReset pulumi.StringPtrOutput `pulumi:"passwordReset"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// Current status of the user.
	Status pulumi.StringOutput `pulumi:"status"`
}

// NewOpensearchUser registers a new resource with the given unique name, arguments, and options.
func NewOpensearchUser(ctx *pulumi.Context,
	name string, args *OpensearchUserArgs, opts ...pulumi.ResourceOption) (*OpensearchUser, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterId'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"password",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource OpensearchUser
	err := ctx.RegisterResource("ovh:CloudProjectDatabase/opensearchUser:OpensearchUser", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOpensearchUser gets an existing OpensearchUser resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOpensearchUser(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OpensearchUserState, opts ...pulumi.ResourceOption) (*OpensearchUser, error) {
	var resource OpensearchUser
	err := ctx.ReadResource("ovh:CloudProjectDatabase/opensearchUser:OpensearchUser", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering OpensearchUser resources.
type opensearchUserState struct {
	// Acls of the user.
	Acls []OpensearchUserAcl `pulumi:"acls"`
	// Cluster ID.
	ClusterId *string `pulumi:"clusterId"`
	// Date of the creation of the user.
	CreatedAt *string `pulumi:"createdAt"`
	// Username affected by this acl. A user named "avnadmin" is map with already created admin user and reset his password instead of create a new user.
	Name *string `pulumi:"name"`
	// (Sensitive) Password of the user.
	Password *string `pulumi:"password"`
	// Arbitrary string to change to trigger a password update
	PasswordReset *string `pulumi:"passwordReset"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName *string `pulumi:"serviceName"`
	// Current status of the user.
	Status *string `pulumi:"status"`
}

type OpensearchUserState struct {
	// Acls of the user.
	Acls OpensearchUserAclArrayInput
	// Cluster ID.
	ClusterId pulumi.StringPtrInput
	// Date of the creation of the user.
	CreatedAt pulumi.StringPtrInput
	// Username affected by this acl. A user named "avnadmin" is map with already created admin user and reset his password instead of create a new user.
	Name pulumi.StringPtrInput
	// (Sensitive) Password of the user.
	Password pulumi.StringPtrInput
	// Arbitrary string to change to trigger a password update
	PasswordReset pulumi.StringPtrInput
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringPtrInput
	// Current status of the user.
	Status pulumi.StringPtrInput
}

func (OpensearchUserState) ElementType() reflect.Type {
	return reflect.TypeOf((*opensearchUserState)(nil)).Elem()
}

type opensearchUserArgs struct {
	// Acls of the user.
	Acls []OpensearchUserAcl `pulumi:"acls"`
	// Cluster ID.
	ClusterId string `pulumi:"clusterId"`
	// Username affected by this acl. A user named "avnadmin" is map with already created admin user and reset his password instead of create a new user.
	Name *string `pulumi:"name"`
	// Arbitrary string to change to trigger a password update
	PasswordReset *string `pulumi:"passwordReset"`
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
}

// The set of arguments for constructing a OpensearchUser resource.
type OpensearchUserArgs struct {
	// Acls of the user.
	Acls OpensearchUserAclArrayInput
	// Cluster ID.
	ClusterId pulumi.StringInput
	// Username affected by this acl. A user named "avnadmin" is map with already created admin user and reset his password instead of create a new user.
	Name pulumi.StringPtrInput
	// Arbitrary string to change to trigger a password update
	PasswordReset pulumi.StringPtrInput
	// The id of the public cloud project. If omitted,
	// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput
}

func (OpensearchUserArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*opensearchUserArgs)(nil)).Elem()
}

type OpensearchUserInput interface {
	pulumi.Input

	ToOpensearchUserOutput() OpensearchUserOutput
	ToOpensearchUserOutputWithContext(ctx context.Context) OpensearchUserOutput
}

func (*OpensearchUser) ElementType() reflect.Type {
	return reflect.TypeOf((**OpensearchUser)(nil)).Elem()
}

func (i *OpensearchUser) ToOpensearchUserOutput() OpensearchUserOutput {
	return i.ToOpensearchUserOutputWithContext(context.Background())
}

func (i *OpensearchUser) ToOpensearchUserOutputWithContext(ctx context.Context) OpensearchUserOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OpensearchUserOutput)
}

// OpensearchUserArrayInput is an input type that accepts OpensearchUserArray and OpensearchUserArrayOutput values.
// You can construct a concrete instance of `OpensearchUserArrayInput` via:
//
//	OpensearchUserArray{ OpensearchUserArgs{...} }
type OpensearchUserArrayInput interface {
	pulumi.Input

	ToOpensearchUserArrayOutput() OpensearchUserArrayOutput
	ToOpensearchUserArrayOutputWithContext(context.Context) OpensearchUserArrayOutput
}

type OpensearchUserArray []OpensearchUserInput

func (OpensearchUserArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OpensearchUser)(nil)).Elem()
}

func (i OpensearchUserArray) ToOpensearchUserArrayOutput() OpensearchUserArrayOutput {
	return i.ToOpensearchUserArrayOutputWithContext(context.Background())
}

func (i OpensearchUserArray) ToOpensearchUserArrayOutputWithContext(ctx context.Context) OpensearchUserArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OpensearchUserArrayOutput)
}

// OpensearchUserMapInput is an input type that accepts OpensearchUserMap and OpensearchUserMapOutput values.
// You can construct a concrete instance of `OpensearchUserMapInput` via:
//
//	OpensearchUserMap{ "key": OpensearchUserArgs{...} }
type OpensearchUserMapInput interface {
	pulumi.Input

	ToOpensearchUserMapOutput() OpensearchUserMapOutput
	ToOpensearchUserMapOutputWithContext(context.Context) OpensearchUserMapOutput
}

type OpensearchUserMap map[string]OpensearchUserInput

func (OpensearchUserMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OpensearchUser)(nil)).Elem()
}

func (i OpensearchUserMap) ToOpensearchUserMapOutput() OpensearchUserMapOutput {
	return i.ToOpensearchUserMapOutputWithContext(context.Background())
}

func (i OpensearchUserMap) ToOpensearchUserMapOutputWithContext(ctx context.Context) OpensearchUserMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OpensearchUserMapOutput)
}

type OpensearchUserOutput struct{ *pulumi.OutputState }

func (OpensearchUserOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**OpensearchUser)(nil)).Elem()
}

func (o OpensearchUserOutput) ToOpensearchUserOutput() OpensearchUserOutput {
	return o
}

func (o OpensearchUserOutput) ToOpensearchUserOutputWithContext(ctx context.Context) OpensearchUserOutput {
	return o
}

// Acls of the user.
func (o OpensearchUserOutput) Acls() OpensearchUserAclArrayOutput {
	return o.ApplyT(func(v *OpensearchUser) OpensearchUserAclArrayOutput { return v.Acls }).(OpensearchUserAclArrayOutput)
}

// Cluster ID.
func (o OpensearchUserOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v *OpensearchUser) pulumi.StringOutput { return v.ClusterId }).(pulumi.StringOutput)
}

// Date of the creation of the user.
func (o OpensearchUserOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *OpensearchUser) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// Username affected by this acl. A user named "avnadmin" is map with already created admin user and reset his password instead of create a new user.
func (o OpensearchUserOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *OpensearchUser) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// (Sensitive) Password of the user.
func (o OpensearchUserOutput) Password() pulumi.StringOutput {
	return o.ApplyT(func(v *OpensearchUser) pulumi.StringOutput { return v.Password }).(pulumi.StringOutput)
}

// Arbitrary string to change to trigger a password update
func (o OpensearchUserOutput) PasswordReset() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *OpensearchUser) pulumi.StringPtrOutput { return v.PasswordReset }).(pulumi.StringPtrOutput)
}

// The id of the public cloud project. If omitted,
// the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
func (o OpensearchUserOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *OpensearchUser) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// Current status of the user.
func (o OpensearchUserOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *OpensearchUser) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

type OpensearchUserArrayOutput struct{ *pulumi.OutputState }

func (OpensearchUserArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*OpensearchUser)(nil)).Elem()
}

func (o OpensearchUserArrayOutput) ToOpensearchUserArrayOutput() OpensearchUserArrayOutput {
	return o
}

func (o OpensearchUserArrayOutput) ToOpensearchUserArrayOutputWithContext(ctx context.Context) OpensearchUserArrayOutput {
	return o
}

func (o OpensearchUserArrayOutput) Index(i pulumi.IntInput) OpensearchUserOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *OpensearchUser {
		return vs[0].([]*OpensearchUser)[vs[1].(int)]
	}).(OpensearchUserOutput)
}

type OpensearchUserMapOutput struct{ *pulumi.OutputState }

func (OpensearchUserMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*OpensearchUser)(nil)).Elem()
}

func (o OpensearchUserMapOutput) ToOpensearchUserMapOutput() OpensearchUserMapOutput {
	return o
}

func (o OpensearchUserMapOutput) ToOpensearchUserMapOutputWithContext(ctx context.Context) OpensearchUserMapOutput {
	return o
}

func (o OpensearchUserMapOutput) MapIndex(k pulumi.StringInput) OpensearchUserOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *OpensearchUser {
		return vs[0].(map[string]*OpensearchUser)[vs[1].(string)]
	}).(OpensearchUserOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*OpensearchUserInput)(nil)).Elem(), &OpensearchUser{})
	pulumi.RegisterInputType(reflect.TypeOf((*OpensearchUserArrayInput)(nil)).Elem(), OpensearchUserArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*OpensearchUserMapInput)(nil)).Elem(), OpensearchUserMap{})
	pulumi.RegisterOutputType(OpensearchUserOutput{})
	pulumi.RegisterOutputType(OpensearchUserArrayOutput{})
	pulumi.RegisterOutputType(OpensearchUserMapOutput{})
}
