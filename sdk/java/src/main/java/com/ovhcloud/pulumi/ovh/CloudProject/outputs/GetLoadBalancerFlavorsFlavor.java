// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetLoadBalancerFlavorsFlavor {
    /**
     * @return Flavor id
     * 
     */
    private String id;
    /**
     * @return Flavor name
     * 
     */
    private String name;
    /**
     * @return Region name
     * 
     */
    private String region;

    private GetLoadBalancerFlavorsFlavor() {}
    /**
     * @return Flavor id
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Flavor name
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return Region name
     * 
     */
    public String region() {
        return this.region;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetLoadBalancerFlavorsFlavor defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String id;
        private String name;
        private String region;
        public Builder() {}
        public Builder(GetLoadBalancerFlavorsFlavor defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.id = defaults.id;
    	      this.name = defaults.name;
    	      this.region = defaults.region;
        }

        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerFlavorsFlavor", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerFlavorsFlavor", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder region(String region) {
            if (region == null) {
              throw new MissingRequiredPropertyException("GetLoadBalancerFlavorsFlavor", "region");
            }
            this.region = region;
            return this;
        }
        public GetLoadBalancerFlavorsFlavor build() {
            final var _resultValue = new GetLoadBalancerFlavorsFlavor();
            _resultValue.id = id;
            _resultValue.name = name;
            _resultValue.region = region;
            return _resultValue;
        }
    }
}
