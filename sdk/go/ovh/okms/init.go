// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package okms

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/ovh/pulumi-ovh/sdk/go/ovh/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "ovh:Okms/credential:Credential":
		r = &Credential{}
	case "ovh:Okms/okms:Okms":
		r = &Okms{}
	case "ovh:Okms/serviceKey:ServiceKey":
		r = &ServiceKey{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"ovh",
		"Okms/credential",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ovh",
		"Okms/okms",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"ovh",
		"Okms/serviceKey",
		&module{version},
	)
}
