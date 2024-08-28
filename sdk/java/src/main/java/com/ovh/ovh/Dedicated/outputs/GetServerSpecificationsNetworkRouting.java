// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Dedicated.outputs;

import com.ovh.ovh.Dedicated.outputs.GetServerSpecificationsNetworkRoutingIpv4;
import com.ovh.ovh.Dedicated.outputs.GetServerSpecificationsNetworkRoutingIpv6;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.util.Objects;

@CustomType
public final class GetServerSpecificationsNetworkRouting {
    /**
     * @return Ipv4 routing details
     * 
     */
    private GetServerSpecificationsNetworkRoutingIpv4 ipv4;
    /**
     * @return Ipv6 routing details
     * 
     */
    private GetServerSpecificationsNetworkRoutingIpv6 ipv6;

    private GetServerSpecificationsNetworkRouting() {}
    /**
     * @return Ipv4 routing details
     * 
     */
    public GetServerSpecificationsNetworkRoutingIpv4 ipv4() {
        return this.ipv4;
    }
    /**
     * @return Ipv6 routing details
     * 
     */
    public GetServerSpecificationsNetworkRoutingIpv6 ipv6() {
        return this.ipv6;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetServerSpecificationsNetworkRouting defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private GetServerSpecificationsNetworkRoutingIpv4 ipv4;
        private GetServerSpecificationsNetworkRoutingIpv6 ipv6;
        public Builder() {}
        public Builder(GetServerSpecificationsNetworkRouting defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.ipv4 = defaults.ipv4;
    	      this.ipv6 = defaults.ipv6;
        }

        @CustomType.Setter
        public Builder ipv4(GetServerSpecificationsNetworkRoutingIpv4 ipv4) {
            if (ipv4 == null) {
              throw new MissingRequiredPropertyException("GetServerSpecificationsNetworkRouting", "ipv4");
            }
            this.ipv4 = ipv4;
            return this;
        }
        @CustomType.Setter
        public Builder ipv6(GetServerSpecificationsNetworkRoutingIpv6 ipv6) {
            if (ipv6 == null) {
              throw new MissingRequiredPropertyException("GetServerSpecificationsNetworkRouting", "ipv6");
            }
            this.ipv6 = ipv6;
            return this;
        }
        public GetServerSpecificationsNetworkRouting build() {
            final var _resultValue = new GetServerSpecificationsNetworkRouting();
            _resultValue.ipv4 = ipv4;
            _resultValue.ipv6 = ipv6;
            return _resultValue;
        }
    }
}
