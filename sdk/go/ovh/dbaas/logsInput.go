// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package dbaas

import (
	"context"
	"reflect"

	"errors"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Creates a dbaas logs input.
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
//			logstash, err := Dbaas.GetLogsInputEngine(ctx, &dbaas.GetLogsInputEngineArgs{
//				Name:    pulumi.StringRef("logstash"),
//				Version: pulumi.StringRef("7.x"),
//			}, nil)
//			if err != nil {
//				return err
//			}
//			stream, err := Dbaas.NewLogsOutputGraylogStream(ctx, "stream", &Dbaas.LogsOutputGraylogStreamArgs{
//				ServiceName: pulumi.String("...."),
//				Title:       pulumi.String("my stream"),
//				Description: pulumi.String("my graylog stream"),
//			})
//			if err != nil {
//				return err
//			}
//			_, err = Dbaas.NewLogsInput(ctx, "input", &Dbaas.LogsInputArgs{
//				ServiceName: stream.ServiceName,
//				Description: stream.Description,
//				Title:       stream.Title,
//				EngineId:    *pulumi.String(logstash.Id),
//				StreamId:    stream.ID(),
//				AllowedNetworks: pulumi.StringArray{
//					pulumi.String("10.0.0.0/16"),
//				},
//				ExposedPort: pulumi.String("6154"),
//				NbInstance:  pulumi.Int(2),
//				Configuration: &dbaas.LogsInputConfigurationArgs{
//					Logstash: &dbaas.LogsInputConfigurationLogstashArgs{
//						InputSection: pulumi.String(`  beats {
//	    port => 6514
//	    ssl => true
//	    ssl_certificate => "/etc/ssl/private/server.crt"
//	    ssl_key => "/etc/ssl/private/server.key"
//	  }
//
// `),
//
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
type LogsInput struct {
	pulumi.CustomResourceState

	// List of IP blocks
	AllowedNetworks pulumi.StringArrayOutput `pulumi:"allowedNetworks"`
	// Input configuration
	Configuration LogsInputConfigurationOutput `pulumi:"configuration"`
	// Input creation
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// Input description
	Description pulumi.StringOutput `pulumi:"description"`
	// Input engine ID
	EngineId pulumi.StringOutput `pulumi:"engineId"`
	// Port
	ExposedPort pulumi.StringOutput `pulumi:"exposedPort"`
	// Hostname
	Hostname pulumi.StringOutput `pulumi:"hostname"`
	// Input ID
	InputId pulumi.StringOutput `pulumi:"inputId"`
	// Indicate if input need to be restarted
	IsRestartRequired pulumi.BoolOutput `pulumi:"isRestartRequired"`
	// Number of instance running
	NbInstance pulumi.IntOutput `pulumi:"nbInstance"`
	// Input IP address
	PublicAddress pulumi.StringOutput `pulumi:"publicAddress"`
	// service name
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// Input SSL certificate
	SslCertificate pulumi.StringOutput `pulumi:"sslCertificate"`
	// init: configuration required, pending: ready to start, running: available
	Status pulumi.StringOutput `pulumi:"status"`
	// Associated Graylog stream
	StreamId pulumi.StringOutput `pulumi:"streamId"`
	// Input title
	Title pulumi.StringOutput `pulumi:"title"`
	// Input last update
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewLogsInput registers a new resource with the given unique name, arguments, and options.
func NewLogsInput(ctx *pulumi.Context,
	name string, args *LogsInputArgs, opts ...pulumi.ResourceOption) (*LogsInput, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Configuration == nil {
		return nil, errors.New("invalid value for required argument 'Configuration'")
	}
	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.EngineId == nil {
		return nil, errors.New("invalid value for required argument 'EngineId'")
	}
	if args.ServiceName == nil {
		return nil, errors.New("invalid value for required argument 'ServiceName'")
	}
	if args.StreamId == nil {
		return nil, errors.New("invalid value for required argument 'StreamId'")
	}
	if args.Title == nil {
		return nil, errors.New("invalid value for required argument 'Title'")
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"sslCertificate",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LogsInput
	err := ctx.RegisterResource("ovh:Dbaas/logsInput:LogsInput", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLogsInput gets an existing LogsInput resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLogsInput(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LogsInputState, opts ...pulumi.ResourceOption) (*LogsInput, error) {
	var resource LogsInput
	err := ctx.ReadResource("ovh:Dbaas/logsInput:LogsInput", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LogsInput resources.
type logsInputState struct {
	// List of IP blocks
	AllowedNetworks []string `pulumi:"allowedNetworks"`
	// Input configuration
	Configuration *LogsInputConfiguration `pulumi:"configuration"`
	// Input creation
	CreatedAt *string `pulumi:"createdAt"`
	// Input description
	Description *string `pulumi:"description"`
	// Input engine ID
	EngineId *string `pulumi:"engineId"`
	// Port
	ExposedPort *string `pulumi:"exposedPort"`
	// Hostname
	Hostname *string `pulumi:"hostname"`
	// Input ID
	InputId *string `pulumi:"inputId"`
	// Indicate if input need to be restarted
	IsRestartRequired *bool `pulumi:"isRestartRequired"`
	// Number of instance running
	NbInstance *int `pulumi:"nbInstance"`
	// Input IP address
	PublicAddress *string `pulumi:"publicAddress"`
	// service name
	ServiceName *string `pulumi:"serviceName"`
	// Input SSL certificate
	SslCertificate *string `pulumi:"sslCertificate"`
	// init: configuration required, pending: ready to start, running: available
	Status *string `pulumi:"status"`
	// Associated Graylog stream
	StreamId *string `pulumi:"streamId"`
	// Input title
	Title *string `pulumi:"title"`
	// Input last update
	UpdatedAt *string `pulumi:"updatedAt"`
}

type LogsInputState struct {
	// List of IP blocks
	AllowedNetworks pulumi.StringArrayInput
	// Input configuration
	Configuration LogsInputConfigurationPtrInput
	// Input creation
	CreatedAt pulumi.StringPtrInput
	// Input description
	Description pulumi.StringPtrInput
	// Input engine ID
	EngineId pulumi.StringPtrInput
	// Port
	ExposedPort pulumi.StringPtrInput
	// Hostname
	Hostname pulumi.StringPtrInput
	// Input ID
	InputId pulumi.StringPtrInput
	// Indicate if input need to be restarted
	IsRestartRequired pulumi.BoolPtrInput
	// Number of instance running
	NbInstance pulumi.IntPtrInput
	// Input IP address
	PublicAddress pulumi.StringPtrInput
	// service name
	ServiceName pulumi.StringPtrInput
	// Input SSL certificate
	SslCertificate pulumi.StringPtrInput
	// init: configuration required, pending: ready to start, running: available
	Status pulumi.StringPtrInput
	// Associated Graylog stream
	StreamId pulumi.StringPtrInput
	// Input title
	Title pulumi.StringPtrInput
	// Input last update
	UpdatedAt pulumi.StringPtrInput
}

func (LogsInputState) ElementType() reflect.Type {
	return reflect.TypeOf((*logsInputState)(nil)).Elem()
}

type logsInputArgs struct {
	// List of IP blocks
	AllowedNetworks []string `pulumi:"allowedNetworks"`
	// Input configuration
	Configuration LogsInputConfiguration `pulumi:"configuration"`
	// Input description
	Description string `pulumi:"description"`
	// Input engine ID
	EngineId string `pulumi:"engineId"`
	// Port
	ExposedPort *string `pulumi:"exposedPort"`
	// Number of instance running
	NbInstance *int `pulumi:"nbInstance"`
	// service name
	ServiceName string `pulumi:"serviceName"`
	// Associated Graylog stream
	StreamId string `pulumi:"streamId"`
	// Input title
	Title string `pulumi:"title"`
}

// The set of arguments for constructing a LogsInput resource.
type LogsInputArgs struct {
	// List of IP blocks
	AllowedNetworks pulumi.StringArrayInput
	// Input configuration
	Configuration LogsInputConfigurationInput
	// Input description
	Description pulumi.StringInput
	// Input engine ID
	EngineId pulumi.StringInput
	// Port
	ExposedPort pulumi.StringPtrInput
	// Number of instance running
	NbInstance pulumi.IntPtrInput
	// service name
	ServiceName pulumi.StringInput
	// Associated Graylog stream
	StreamId pulumi.StringInput
	// Input title
	Title pulumi.StringInput
}

func (LogsInputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*logsInputArgs)(nil)).Elem()
}

type LogsInputInput interface {
	pulumi.Input

	ToLogsInputOutput() LogsInputOutput
	ToLogsInputOutputWithContext(ctx context.Context) LogsInputOutput
}

func (*LogsInput) ElementType() reflect.Type {
	return reflect.TypeOf((**LogsInput)(nil)).Elem()
}

func (i *LogsInput) ToLogsInputOutput() LogsInputOutput {
	return i.ToLogsInputOutputWithContext(context.Background())
}

func (i *LogsInput) ToLogsInputOutputWithContext(ctx context.Context) LogsInputOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LogsInputOutput)
}

// LogsInputArrayInput is an input type that accepts LogsInputArray and LogsInputArrayOutput values.
// You can construct a concrete instance of `LogsInputArrayInput` via:
//
//	LogsInputArray{ LogsInputArgs{...} }
type LogsInputArrayInput interface {
	pulumi.Input

	ToLogsInputArrayOutput() LogsInputArrayOutput
	ToLogsInputArrayOutputWithContext(context.Context) LogsInputArrayOutput
}

type LogsInputArray []LogsInputInput

func (LogsInputArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LogsInput)(nil)).Elem()
}

func (i LogsInputArray) ToLogsInputArrayOutput() LogsInputArrayOutput {
	return i.ToLogsInputArrayOutputWithContext(context.Background())
}

func (i LogsInputArray) ToLogsInputArrayOutputWithContext(ctx context.Context) LogsInputArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LogsInputArrayOutput)
}

// LogsInputMapInput is an input type that accepts LogsInputMap and LogsInputMapOutput values.
// You can construct a concrete instance of `LogsInputMapInput` via:
//
//	LogsInputMap{ "key": LogsInputArgs{...} }
type LogsInputMapInput interface {
	pulumi.Input

	ToLogsInputMapOutput() LogsInputMapOutput
	ToLogsInputMapOutputWithContext(context.Context) LogsInputMapOutput
}

type LogsInputMap map[string]LogsInputInput

func (LogsInputMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LogsInput)(nil)).Elem()
}

func (i LogsInputMap) ToLogsInputMapOutput() LogsInputMapOutput {
	return i.ToLogsInputMapOutputWithContext(context.Background())
}

func (i LogsInputMap) ToLogsInputMapOutputWithContext(ctx context.Context) LogsInputMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LogsInputMapOutput)
}

type LogsInputOutput struct{ *pulumi.OutputState }

func (LogsInputOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LogsInput)(nil)).Elem()
}

func (o LogsInputOutput) ToLogsInputOutput() LogsInputOutput {
	return o
}

func (o LogsInputOutput) ToLogsInputOutputWithContext(ctx context.Context) LogsInputOutput {
	return o
}

// List of IP blocks
func (o LogsInputOutput) AllowedNetworks() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringArrayOutput { return v.AllowedNetworks }).(pulumi.StringArrayOutput)
}

// Input configuration
func (o LogsInputOutput) Configuration() LogsInputConfigurationOutput {
	return o.ApplyT(func(v *LogsInput) LogsInputConfigurationOutput { return v.Configuration }).(LogsInputConfigurationOutput)
}

// Input creation
func (o LogsInputOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// Input description
func (o LogsInputOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// Input engine ID
func (o LogsInputOutput) EngineId() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.EngineId }).(pulumi.StringOutput)
}

// Port
func (o LogsInputOutput) ExposedPort() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.ExposedPort }).(pulumi.StringOutput)
}

// Hostname
func (o LogsInputOutput) Hostname() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.Hostname }).(pulumi.StringOutput)
}

// Input ID
func (o LogsInputOutput) InputId() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.InputId }).(pulumi.StringOutput)
}

// Indicate if input need to be restarted
func (o LogsInputOutput) IsRestartRequired() pulumi.BoolOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.BoolOutput { return v.IsRestartRequired }).(pulumi.BoolOutput)
}

// Number of instance running
func (o LogsInputOutput) NbInstance() pulumi.IntOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.IntOutput { return v.NbInstance }).(pulumi.IntOutput)
}

// Input IP address
func (o LogsInputOutput) PublicAddress() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.PublicAddress }).(pulumi.StringOutput)
}

// service name
func (o LogsInputOutput) ServiceName() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.ServiceName }).(pulumi.StringOutput)
}

// Input SSL certificate
func (o LogsInputOutput) SslCertificate() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.SslCertificate }).(pulumi.StringOutput)
}

// init: configuration required, pending: ready to start, running: available
func (o LogsInputOutput) Status() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.Status }).(pulumi.StringOutput)
}

// Associated Graylog stream
func (o LogsInputOutput) StreamId() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.StreamId }).(pulumi.StringOutput)
}

// Input title
func (o LogsInputOutput) Title() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.Title }).(pulumi.StringOutput)
}

// Input last update
func (o LogsInputOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *LogsInput) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

type LogsInputArrayOutput struct{ *pulumi.OutputState }

func (LogsInputArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*LogsInput)(nil)).Elem()
}

func (o LogsInputArrayOutput) ToLogsInputArrayOutput() LogsInputArrayOutput {
	return o
}

func (o LogsInputArrayOutput) ToLogsInputArrayOutputWithContext(ctx context.Context) LogsInputArrayOutput {
	return o
}

func (o LogsInputArrayOutput) Index(i pulumi.IntInput) LogsInputOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *LogsInput {
		return vs[0].([]*LogsInput)[vs[1].(int)]
	}).(LogsInputOutput)
}

type LogsInputMapOutput struct{ *pulumi.OutputState }

func (LogsInputMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*LogsInput)(nil)).Elem()
}

func (o LogsInputMapOutput) ToLogsInputMapOutput() LogsInputMapOutput {
	return o
}

func (o LogsInputMapOutput) ToLogsInputMapOutputWithContext(ctx context.Context) LogsInputMapOutput {
	return o
}

func (o LogsInputMapOutput) MapIndex(k pulumi.StringInput) LogsInputOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *LogsInput {
		return vs[0].(map[string]*LogsInput)[vs[1].(string)]
	}).(LogsInputOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LogsInputInput)(nil)).Elem(), &LogsInput{})
	pulumi.RegisterInputType(reflect.TypeOf((*LogsInputArrayInput)(nil)).Elem(), LogsInputArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*LogsInputMapInput)(nil)).Elem(), LogsInputMap{})
	pulumi.RegisterOutputType(LogsInputOutput{})
	pulumi.RegisterOutputType(LogsInputArrayOutput{})
	pulumi.RegisterOutputType(LogsInputMapOutput{})
}
