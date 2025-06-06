// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudproject

import (
	"context"
	"reflect"

	"github.com/ovh/pulumi-ovh/sdk/v2/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to retrieve the Secret Access Key of an Access Key ID associated with a public cloud project's user.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/ovh/pulumi-ovh/sdk/v2/go/ovh/cloudproject"
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			projectUsers, err := cloudproject.GetUsers(ctx, &cloudproject.GetUsersArgs{
//				ServiceName: "XXX",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			// Get the user ID of a previously created user with the description "S3-User"
//			users := "TODO: For expression"
//			s3UserId := users[0]
//			myS3Credentials, err := cloudproject.GetUserS3Credentials(ctx, &cloudproject.GetUserS3CredentialsArgs{
//				ServiceName: projectUsers.ServiceName,
//				UserId:      s3UserId,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			myS3Credential, err := cloudproject.GetUserS3Credential(ctx, &cloudproject.GetUserS3CredentialArgs{
//				ServiceName: myS3Credentials.ServiceName,
//				UserId:      myS3Credentials.UserId,
//				AccessKeyId: myS3Credentials.AccessKeyIds[0],
//			}, nil)
//			if err != nil {
//				return err
//			}
//			ctx.Export("myAccessKeyId", myS3Credential.AccessKeyId)
//			ctx.Export("mySecretAccessKey", myS3Credential.SecretAccessKey)
//			return nil
//		})
//	}
//
// ```
func GetUserS3Credential(ctx *pulumi.Context, args *GetUserS3CredentialArgs, opts ...pulumi.InvokeOption) (*GetUserS3CredentialResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetUserS3CredentialResult
	err := ctx.Invoke("ovh:CloudProject/getUserS3Credential:getUserS3Credential", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUserS3Credential.
type GetUserS3CredentialArgs struct {
	// the Access Key ID
	AccessKeyId string `pulumi:"accessKeyId"`
	// The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName string `pulumi:"serviceName"`
	// The ID of a public cloud project's user.
	UserId string `pulumi:"userId"`
}

// A collection of values returned by getUserS3Credential.
type GetUserS3CredentialResult struct {
	AccessKeyId string `pulumi:"accessKeyId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// (Sensitive) the Secret Access Key
	SecretAccessKey string `pulumi:"secretAccessKey"`
	ServiceName     string `pulumi:"serviceName"`
	UserId          string `pulumi:"userId"`
}

func GetUserS3CredentialOutput(ctx *pulumi.Context, args GetUserS3CredentialOutputArgs, opts ...pulumi.InvokeOption) GetUserS3CredentialResultOutput {
	return pulumi.ToOutputWithContext(ctx.Context(), args).
		ApplyT(func(v interface{}) (GetUserS3CredentialResultOutput, error) {
			args := v.(GetUserS3CredentialArgs)
			options := pulumi.InvokeOutputOptions{InvokeOptions: internal.PkgInvokeDefaultOpts(opts)}
			return ctx.InvokeOutput("ovh:CloudProject/getUserS3Credential:getUserS3Credential", args, GetUserS3CredentialResultOutput{}, options).(GetUserS3CredentialResultOutput), nil
		}).(GetUserS3CredentialResultOutput)
}

// A collection of arguments for invoking getUserS3Credential.
type GetUserS3CredentialOutputArgs struct {
	// the Access Key ID
	AccessKeyId pulumi.StringInput `pulumi:"accessKeyId"`
	// The ID of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
	ServiceName pulumi.StringInput `pulumi:"serviceName"`
	// The ID of a public cloud project's user.
	UserId pulumi.StringInput `pulumi:"userId"`
}

func (GetUserS3CredentialOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserS3CredentialArgs)(nil)).Elem()
}

// A collection of values returned by getUserS3Credential.
type GetUserS3CredentialResultOutput struct{ *pulumi.OutputState }

func (GetUserS3CredentialResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserS3CredentialResult)(nil)).Elem()
}

func (o GetUserS3CredentialResultOutput) ToGetUserS3CredentialResultOutput() GetUserS3CredentialResultOutput {
	return o
}

func (o GetUserS3CredentialResultOutput) ToGetUserS3CredentialResultOutputWithContext(ctx context.Context) GetUserS3CredentialResultOutput {
	return o
}

func (o GetUserS3CredentialResultOutput) AccessKeyId() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialResult) string { return v.AccessKeyId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetUserS3CredentialResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialResult) string { return v.Id }).(pulumi.StringOutput)
}

// (Sensitive) the Secret Access Key
func (o GetUserS3CredentialResultOutput) SecretAccessKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialResult) string { return v.SecretAccessKey }).(pulumi.StringOutput)
}

func (o GetUserS3CredentialResultOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialResult) string { return v.ServiceName }).(pulumi.StringOutput)
}

func (o GetUserS3CredentialResultOutput) UserId() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserS3CredentialResult) string { return v.UserId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUserS3CredentialResultOutput{})
}
