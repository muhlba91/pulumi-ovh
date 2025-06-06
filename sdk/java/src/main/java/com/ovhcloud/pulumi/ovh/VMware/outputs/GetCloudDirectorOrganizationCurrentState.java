// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.VMware.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetCloudDirectorOrganizationCurrentState {
    /**
     * @return API URL to interact with your VMware Cloud Director organization at OVHcloud
     * 
     */
    private String apiUrl;
    /**
     * @return Billing type of your VMware Cloud Director project
     * 
     */
    private String billingType;
    /**
     * @return Description of your VMware Cloud Director organization on OVHcloud
     * 
     */
    private String description;
    /**
     * @return Human readable full name of your VMware Cloud Director organization
     * 
     */
    private String fullName;
    /**
     * @return Name of your VMware Cloud Director organization
     * 
     */
    private String name;
    /**
     * @return Datacenter where your VMware Cloud Director organization is physically located
     * 
     */
    private String region;
    /**
     * @return SPLA licensing state
     * 
     */
    private Boolean spla;
    /**
     * @return URL to administrate your VMware Cloud Director organization at OVHcloud
     * 
     */
    private String webInterfaceUrl;

    private GetCloudDirectorOrganizationCurrentState() {}
    /**
     * @return API URL to interact with your VMware Cloud Director organization at OVHcloud
     * 
     */
    public String apiUrl() {
        return this.apiUrl;
    }
    /**
     * @return Billing type of your VMware Cloud Director project
     * 
     */
    public String billingType() {
        return this.billingType;
    }
    /**
     * @return Description of your VMware Cloud Director organization on OVHcloud
     * 
     */
    public String description() {
        return this.description;
    }
    /**
     * @return Human readable full name of your VMware Cloud Director organization
     * 
     */
    public String fullName() {
        return this.fullName;
    }
    /**
     * @return Name of your VMware Cloud Director organization
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return Datacenter where your VMware Cloud Director organization is physically located
     * 
     */
    public String region() {
        return this.region;
    }
    /**
     * @return SPLA licensing state
     * 
     */
    public Boolean spla() {
        return this.spla;
    }
    /**
     * @return URL to administrate your VMware Cloud Director organization at OVHcloud
     * 
     */
    public String webInterfaceUrl() {
        return this.webInterfaceUrl;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetCloudDirectorOrganizationCurrentState defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String apiUrl;
        private String billingType;
        private String description;
        private String fullName;
        private String name;
        private String region;
        private Boolean spla;
        private String webInterfaceUrl;
        public Builder() {}
        public Builder(GetCloudDirectorOrganizationCurrentState defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.apiUrl = defaults.apiUrl;
    	      this.billingType = defaults.billingType;
    	      this.description = defaults.description;
    	      this.fullName = defaults.fullName;
    	      this.name = defaults.name;
    	      this.region = defaults.region;
    	      this.spla = defaults.spla;
    	      this.webInterfaceUrl = defaults.webInterfaceUrl;
        }

        @CustomType.Setter
        public Builder apiUrl(String apiUrl) {
            if (apiUrl == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "apiUrl");
            }
            this.apiUrl = apiUrl;
            return this;
        }
        @CustomType.Setter
        public Builder billingType(String billingType) {
            if (billingType == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "billingType");
            }
            this.billingType = billingType;
            return this;
        }
        @CustomType.Setter
        public Builder description(String description) {
            if (description == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "description");
            }
            this.description = description;
            return this;
        }
        @CustomType.Setter
        public Builder fullName(String fullName) {
            if (fullName == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "fullName");
            }
            this.fullName = fullName;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder region(String region) {
            if (region == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "region");
            }
            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder spla(Boolean spla) {
            if (spla == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "spla");
            }
            this.spla = spla;
            return this;
        }
        @CustomType.Setter
        public Builder webInterfaceUrl(String webInterfaceUrl) {
            if (webInterfaceUrl == null) {
              throw new MissingRequiredPropertyException("GetCloudDirectorOrganizationCurrentState", "webInterfaceUrl");
            }
            this.webInterfaceUrl = webInterfaceUrl;
            return this;
        }
        public GetCloudDirectorOrganizationCurrentState build() {
            final var _resultValue = new GetCloudDirectorOrganizationCurrentState();
            _resultValue.apiUrl = apiUrl;
            _resultValue.billingType = billingType;
            _resultValue.description = description;
            _resultValue.fullName = fullName;
            _resultValue.name = name;
            _resultValue.region = region;
            _resultValue.spla = spla;
            _resultValue.webInterfaceUrl = webInterfaceUrl;
            return _resultValue;
        }
    }
}
