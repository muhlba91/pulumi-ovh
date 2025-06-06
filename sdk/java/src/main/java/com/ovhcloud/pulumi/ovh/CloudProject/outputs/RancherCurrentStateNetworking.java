// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.pulumi.core.annotations.CustomType;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import javax.annotation.Nullable;

@CustomType
public final class RancherCurrentStateNetworking {
    /**
     * @return Specifies the CIDR ranges for egress IP addresses used by Rancher. Ensure these ranges are allowed in any IP restrictions for services that Rancher will access.
     * 
     */
    private @Nullable List<String> egressCidrBlocks;

    private RancherCurrentStateNetworking() {}
    /**
     * @return Specifies the CIDR ranges for egress IP addresses used by Rancher. Ensure these ranges are allowed in any IP restrictions for services that Rancher will access.
     * 
     */
    public List<String> egressCidrBlocks() {
        return this.egressCidrBlocks == null ? List.of() : this.egressCidrBlocks;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(RancherCurrentStateNetworking defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable List<String> egressCidrBlocks;
        public Builder() {}
        public Builder(RancherCurrentStateNetworking defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.egressCidrBlocks = defaults.egressCidrBlocks;
        }

        @CustomType.Setter
        public Builder egressCidrBlocks(@Nullable List<String> egressCidrBlocks) {

            this.egressCidrBlocks = egressCidrBlocks;
            return this;
        }
        public Builder egressCidrBlocks(String... egressCidrBlocks) {
            return egressCidrBlocks(List.of(egressCidrBlocks));
        }
        public RancherCurrentStateNetworking build() {
            final var _resultValue = new RancherCurrentStateNetworking();
            _resultValue.egressCidrBlocks = egressCidrBlocks;
            return _resultValue;
        }
    }
}
