// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package me

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve list of user logins of the account's identity users.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/go/ovh/Me"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := Me.GetIdentityUsers(ctx, map[string]interface{}{}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetIdentityUsers(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetIdentityUsersResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetIdentityUsersResult
	err := ctx.Invoke("ovh:Me/getIdentityUsers:getIdentityUsers", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getIdentityUsers.
type GetIdentityUsersResult struct {
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The list of the user's logins of all the identity users.
	Users []string `pulumi:"users"`
}

func GetIdentityUsersOutput(ctx *pulumi.Context, opts ...pulumi.InvokeOption) GetIdentityUsersResultOutput {
	return pulumi.ToOutput(0).ApplyT(func(int) (GetIdentityUsersResultOutput, error) {
		opts = internal.PkgInvokeDefaultOpts(opts)
		var rv GetIdentityUsersResult
		secret, err := ctx.InvokePackageRaw("ovh:Me/getIdentityUsers:getIdentityUsers", nil, &rv, "", opts...)
		if err != nil {
			return GetIdentityUsersResultOutput{}, err
		}

		output := pulumi.ToOutput(rv).(GetIdentityUsersResultOutput)
		if secret {
			return pulumi.ToSecret(output).(GetIdentityUsersResultOutput), nil
		}
		return output, nil
	}).(GetIdentityUsersResultOutput)
}

// A collection of values returned by getIdentityUsers.
type GetIdentityUsersResultOutput struct{ *pulumi.OutputState }

func (GetIdentityUsersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetIdentityUsersResult)(nil)).Elem()
}

func (o GetIdentityUsersResultOutput) ToGetIdentityUsersResultOutput() GetIdentityUsersResultOutput {
	return o
}

func (o GetIdentityUsersResultOutput) ToGetIdentityUsersResultOutputWithContext(ctx context.Context) GetIdentityUsersResultOutput {
	return o
}

// The provider-assigned unique ID for this managed resource.
func (o GetIdentityUsersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetIdentityUsersResult) string { return v.Id }).(pulumi.StringOutput)
}

// The list of the user's logins of all the identity users.
func (o GetIdentityUsersResultOutput) Users() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetIdentityUsersResult) []string { return v.Users }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(GetIdentityUsersResultOutput{})
}
