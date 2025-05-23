// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Dedicated.outputs;

import com.ovhcloud.pulumi.ovh.Dedicated.outputs.GetCloudIam;
import com.ovhcloud.pulumi.ovh.Dedicated.outputs.GetCloudVersion;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Double;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetCloudResult {
    /**
     * @return Advanced security state
     * 
     */
    private Boolean advancedSecurity;
    /**
     * @return The current bandwidth of your VMware on OVHcloud
     * 
     */
    private String bandwidth;
    /**
     * @return Billing type of your VMware on OVHcloud
     * 
     */
    private String billingType;
    /**
     * @return Can the PCC be migrated to VCD
     * 
     */
    private Boolean canMigrateToVcd;
    /**
     * @return Url to the VMware on OVHcloud certified interface
     * 
     */
    private String certifiedInterfaceUrl;
    /**
     * @return The current version of your VMware on OVHcloud
     * 
     */
    private String commercialRange;
    /**
     * @return Description of your VMware on OVHcloud
     * 
     */
    private String description;
    /**
     * @return Generation of your VMware on OVHcloud
     * 
     */
    private String generation;
    /**
     * @return IAM resource metadata
     * 
     */
    private GetCloudIam iam;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return Datacenter where your VMware on OVHcloud is physically located
     * 
     */
    private String location;
    /**
     * @return The management interface name
     * 
     */
    private String managementInterface;
    /**
     * @return The reference universe information for your VMware on OVHcloud
     * 
     */
    private String productReference;
    /**
     * @return Domain of the service
     * 
     */
    private String serviceName;
    /**
     * @return Name of the current service pack
     * 
     */
    private String servicePackName;
    /**
     * @return SPLA licensing state
     * 
     */
    private Boolean spla;
    /**
     * @return Enable SSL v3 support. Warning : this option is not recommended as it was recognized as a security breach. If this is enabled, we advise you to enable the filtered User access policy
     * 
     */
    private Boolean sslV3;
    /**
     * @return Current state of your VMware on OVHcloud
     * 
     */
    private String state;
    /**
     * @return Access policy of your VMware on OVHcloud : opened to every IPs or filtered
     * 
     */
    private String userAccessPolicy;
    /**
     * @return The maximum amount of connected users allowed on the VMware on OVHcloud management interface
     * 
     */
    private Double userLimitConcurrentSession;
    /**
     * @return Which user will be disconnected first in case of quota of maximum connection is reached
     * 
     */
    private String userLogoutPolicy;
    /**
     * @return The timeout (in seconds) for the user sessions on the VMware on OVHcloud management interface. 0 value disable the timeout
     * 
     */
    private Double userSessionTimeout;
    /**
     * @return Url to the VMware on OVHcloud vScope interface
     * 
     */
    private String vScopeUrl;
    /**
     * @return Version of the management interface
     * 
     */
    private GetCloudVersion version;
    /**
     * @return Url to the VMware on OVHcloud web interface
     * 
     */
    private String webInterfaceUrl;

    private GetCloudResult() {}
    /**
     * @return Advanced security state
     * 
     */
    public Boolean advancedSecurity() {
        return this.advancedSecurity;
    }
    /**
     * @return The current bandwidth of your VMware on OVHcloud
     * 
     */
    public String bandwidth() {
        return this.bandwidth;
    }
    /**
     * @return Billing type of your VMware on OVHcloud
     * 
     */
    public String billingType() {
        return this.billingType;
    }
    /**
     * @return Can the PCC be migrated to VCD
     * 
     */
    public Boolean canMigrateToVcd() {
        return this.canMigrateToVcd;
    }
    /**
     * @return Url to the VMware on OVHcloud certified interface
     * 
     */
    public String certifiedInterfaceUrl() {
        return this.certifiedInterfaceUrl;
    }
    /**
     * @return The current version of your VMware on OVHcloud
     * 
     */
    public String commercialRange() {
        return this.commercialRange;
    }
    /**
     * @return Description of your VMware on OVHcloud
     * 
     */
    public String description() {
        return this.description;
    }
    /**
     * @return Generation of your VMware on OVHcloud
     * 
     */
    public String generation() {
        return this.generation;
    }
    /**
     * @return IAM resource metadata
     * 
     */
    public GetCloudIam iam() {
        return this.iam;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Datacenter where your VMware on OVHcloud is physically located
     * 
     */
    public String location() {
        return this.location;
    }
    /**
     * @return The management interface name
     * 
     */
    public String managementInterface() {
        return this.managementInterface;
    }
    /**
     * @return The reference universe information for your VMware on OVHcloud
     * 
     */
    public String productReference() {
        return this.productReference;
    }
    /**
     * @return Domain of the service
     * 
     */
    public String serviceName() {
        return this.serviceName;
    }
    /**
     * @return Name of the current service pack
     * 
     */
    public String servicePackName() {
        return this.servicePackName;
    }
    /**
     * @return SPLA licensing state
     * 
     */
    public Boolean spla() {
        return this.spla;
    }
    /**
     * @return Enable SSL v3 support. Warning : this option is not recommended as it was recognized as a security breach. If this is enabled, we advise you to enable the filtered User access policy
     * 
     */
    public Boolean sslV3() {
        return this.sslV3;
    }
    /**
     * @return Current state of your VMware on OVHcloud
     * 
     */
    public String state() {
        return this.state;
    }
    /**
     * @return Access policy of your VMware on OVHcloud : opened to every IPs or filtered
     * 
     */
    public String userAccessPolicy() {
        return this.userAccessPolicy;
    }
    /**
     * @return The maximum amount of connected users allowed on the VMware on OVHcloud management interface
     * 
     */
    public Double userLimitConcurrentSession() {
        return this.userLimitConcurrentSession;
    }
    /**
     * @return Which user will be disconnected first in case of quota of maximum connection is reached
     * 
     */
    public String userLogoutPolicy() {
        return this.userLogoutPolicy;
    }
    /**
     * @return The timeout (in seconds) for the user sessions on the VMware on OVHcloud management interface. 0 value disable the timeout
     * 
     */
    public Double userSessionTimeout() {
        return this.userSessionTimeout;
    }
    /**
     * @return Url to the VMware on OVHcloud vScope interface
     * 
     */
    public String vScopeUrl() {
        return this.vScopeUrl;
    }
    /**
     * @return Version of the management interface
     * 
     */
    public GetCloudVersion version() {
        return this.version;
    }
    /**
     * @return Url to the VMware on OVHcloud web interface
     * 
     */
    public String webInterfaceUrl() {
        return this.webInterfaceUrl;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCloudResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private Boolean advancedSecurity;
        private String bandwidth;
        private String billingType;
        private Boolean canMigrateToVcd;
        private String certifiedInterfaceUrl;
        private String commercialRange;
        private String description;
        private String generation;
        private GetCloudIam iam;
        private String id;
        private String location;
        private String managementInterface;
        private String productReference;
        private String serviceName;
        private String servicePackName;
        private Boolean spla;
        private Boolean sslV3;
        private String state;
        private String userAccessPolicy;
        private Double userLimitConcurrentSession;
        private String userLogoutPolicy;
        private Double userSessionTimeout;
        private String vScopeUrl;
        private GetCloudVersion version;
        private String webInterfaceUrl;
        public Builder() {}
        public Builder(GetCloudResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.advancedSecurity = defaults.advancedSecurity;
    	      this.bandwidth = defaults.bandwidth;
    	      this.billingType = defaults.billingType;
    	      this.canMigrateToVcd = defaults.canMigrateToVcd;
    	      this.certifiedInterfaceUrl = defaults.certifiedInterfaceUrl;
    	      this.commercialRange = defaults.commercialRange;
    	      this.description = defaults.description;
    	      this.generation = defaults.generation;
    	      this.iam = defaults.iam;
    	      this.id = defaults.id;
    	      this.location = defaults.location;
    	      this.managementInterface = defaults.managementInterface;
    	      this.productReference = defaults.productReference;
    	      this.serviceName = defaults.serviceName;
    	      this.servicePackName = defaults.servicePackName;
    	      this.spla = defaults.spla;
    	      this.sslV3 = defaults.sslV3;
    	      this.state = defaults.state;
    	      this.userAccessPolicy = defaults.userAccessPolicy;
    	      this.userLimitConcurrentSession = defaults.userLimitConcurrentSession;
    	      this.userLogoutPolicy = defaults.userLogoutPolicy;
    	      this.userSessionTimeout = defaults.userSessionTimeout;
    	      this.vScopeUrl = defaults.vScopeUrl;
    	      this.version = defaults.version;
    	      this.webInterfaceUrl = defaults.webInterfaceUrl;
        }

        @CustomType.Setter
        public Builder advancedSecurity(Boolean advancedSecurity) {
            if (advancedSecurity == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "advancedSecurity");
            }
            this.advancedSecurity = advancedSecurity;
            return this;
        }
        @CustomType.Setter
        public Builder bandwidth(String bandwidth) {
            if (bandwidth == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "bandwidth");
            }
            this.bandwidth = bandwidth;
            return this;
        }
        @CustomType.Setter
        public Builder billingType(String billingType) {
            if (billingType == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "billingType");
            }
            this.billingType = billingType;
            return this;
        }
        @CustomType.Setter
        public Builder canMigrateToVcd(Boolean canMigrateToVcd) {
            if (canMigrateToVcd == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "canMigrateToVcd");
            }
            this.canMigrateToVcd = canMigrateToVcd;
            return this;
        }
        @CustomType.Setter
        public Builder certifiedInterfaceUrl(String certifiedInterfaceUrl) {
            if (certifiedInterfaceUrl == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "certifiedInterfaceUrl");
            }
            this.certifiedInterfaceUrl = certifiedInterfaceUrl;
            return this;
        }
        @CustomType.Setter
        public Builder commercialRange(String commercialRange) {
            if (commercialRange == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "commercialRange");
            }
            this.commercialRange = commercialRange;
            return this;
        }
        @CustomType.Setter
        public Builder description(String description) {
            if (description == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder generation(String generation) {
            if (generation == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "generation");
            }
            this.generation = generation;
            return this;
        }
        @CustomType.Setter
        public Builder iam(GetCloudIam iam) {
            if (iam == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "iam");
            }
            this.iam = iam;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder location(String location) {
            if (location == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "location");
            }
            this.location = location;
            return this;
        }
        @CustomType.Setter
        public Builder managementInterface(String managementInterface) {
            if (managementInterface == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "managementInterface");
            }
            this.managementInterface = managementInterface;
            return this;
        }
        @CustomType.Setter
        public Builder productReference(String productReference) {
            if (productReference == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "productReference");
            }
            this.productReference = productReference;
            return this;
        }
        @CustomType.Setter
        public Builder serviceName(String serviceName) {
            if (serviceName == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "serviceName");
            }
            this.serviceName = serviceName;
            return this;
        }
        @CustomType.Setter
        public Builder servicePackName(String servicePackName) {
            if (servicePackName == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "servicePackName");
            }
            this.servicePackName = servicePackName;
            return this;
        }
        @CustomType.Setter
        public Builder spla(Boolean spla) {
            if (spla == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "spla");
            }
            this.spla = spla;
            return this;
        }
        @CustomType.Setter
        public Builder sslV3(Boolean sslV3) {
            if (sslV3 == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "sslV3");
            }
            this.sslV3 = sslV3;
            return this;
        }
        @CustomType.Setter
        public Builder state(String state) {
            if (state == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "state");
            }
            this.state = state;
            return this;
        }
        @CustomType.Setter
        public Builder userAccessPolicy(String userAccessPolicy) {
            if (userAccessPolicy == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "userAccessPolicy");
            }
            this.userAccessPolicy = userAccessPolicy;
            return this;
        }
        @CustomType.Setter
        public Builder userLimitConcurrentSession(Double userLimitConcurrentSession) {
            if (userLimitConcurrentSession == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "userLimitConcurrentSession");
            }
            this.userLimitConcurrentSession = userLimitConcurrentSession;
            return this;
        }
        @CustomType.Setter
        public Builder userLogoutPolicy(String userLogoutPolicy) {
            if (userLogoutPolicy == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "userLogoutPolicy");
            }
            this.userLogoutPolicy = userLogoutPolicy;
            return this;
        }
        @CustomType.Setter
        public Builder userSessionTimeout(Double userSessionTimeout) {
            if (userSessionTimeout == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "userSessionTimeout");
            }
            this.userSessionTimeout = userSessionTimeout;
            return this;
        }
        @CustomType.Setter
        public Builder vScopeUrl(String vScopeUrl) {
            if (vScopeUrl == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "vScopeUrl");
            }
            this.vScopeUrl = vScopeUrl;
            return this;
        }
        @CustomType.Setter
        public Builder version(GetCloudVersion version) {
            if (version == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "version");
            }
            this.version = version;
            return this;
        }
        @CustomType.Setter
        public Builder webInterfaceUrl(String webInterfaceUrl) {
            if (webInterfaceUrl == null) {
              throw new MissingRequiredPropertyException("GetCloudResult", "webInterfaceUrl");
            }
            this.webInterfaceUrl = webInterfaceUrl;
            return this;
        }
        public GetCloudResult build() {
            final var _resultValue = new GetCloudResult();
            _resultValue.advancedSecurity = advancedSecurity;
            _resultValue.bandwidth = bandwidth;
            _resultValue.billingType = billingType;
            _resultValue.canMigrateToVcd = canMigrateToVcd;
            _resultValue.certifiedInterfaceUrl = certifiedInterfaceUrl;
            _resultValue.commercialRange = commercialRange;
            _resultValue.description = description;
            _resultValue.generation = generation;
            _resultValue.iam = iam;
            _resultValue.id = id;
            _resultValue.location = location;
            _resultValue.managementInterface = managementInterface;
            _resultValue.productReference = productReference;
            _resultValue.serviceName = serviceName;
            _resultValue.servicePackName = servicePackName;
            _resultValue.spla = spla;
            _resultValue.sslV3 = sslV3;
            _resultValue.state = state;
            _resultValue.userAccessPolicy = userAccessPolicy;
            _resultValue.userLimitConcurrentSession = userLimitConcurrentSession;
            _resultValue.userLogoutPolicy = userLogoutPolicy;
            _resultValue.userSessionTimeout = userSessionTimeout;
            _resultValue.vScopeUrl = vScopeUrl;
            _resultValue.version = version;
            _resultValue.webInterfaceUrl = webInterfaceUrl;
            return _resultValue;
        }
    }
}
