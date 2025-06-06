// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.ovhcloud.pulumi.ovh.CloudProject.outputs.LoadBalancerListenerPoolHealthMonitorHttpConfiguration;
import com.pulumi.core.annotations.CustomType;
import java.lang.Double;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class LoadBalancerListenerPoolHealthMonitor {
    /**
     * @return Duration between sending probes to members, in seconds
     * 
     */
    private @Nullable Double delay;
    /**
     * @return Monitor HTTP configuration
     * 
     */
    private @Nullable LoadBalancerListenerPoolHealthMonitorHttpConfiguration httpConfiguration;
    /**
     * @return Number of successful checks before changing the operating status of the member to ONLINE
     * 
     */
    private @Nullable Double maxRetries;
    /**
     * @return Number of allowed check failures before changing the operating status of the member to ERROR
     * 
     */
    private @Nullable Double maxRetriesDown;
    /**
     * @return Type of the monitor
     * 
     */
    private @Nullable String monitorType;
    /**
     * @return The name of the resource
     * 
     */
    private @Nullable String name;
    /**
     * @return The operating status of the resource
     * 
     */
    private @Nullable String operatingStatus;
    /**
     * @return The provisioning status of the resource
     * 
     */
    private @Nullable String provisioningStatus;
    /**
     * @return Maximum time, in seconds, that a monitor waits to connect before it times out. This value must be less than the delay value
     * 
     */
    private @Nullable Double timeout;

    private LoadBalancerListenerPoolHealthMonitor() {}
    /**
     * @return Duration between sending probes to members, in seconds
     * 
     */
    public Optional<Double> delay() {
        return Optional.ofNullable(this.delay);
    }
    /**
     * @return Monitor HTTP configuration
     * 
     */
    public Optional<LoadBalancerListenerPoolHealthMonitorHttpConfiguration> httpConfiguration() {
        return Optional.ofNullable(this.httpConfiguration);
    }
    /**
     * @return Number of successful checks before changing the operating status of the member to ONLINE
     * 
     */
    public Optional<Double> maxRetries() {
        return Optional.ofNullable(this.maxRetries);
    }
    /**
     * @return Number of allowed check failures before changing the operating status of the member to ERROR
     * 
     */
    public Optional<Double> maxRetriesDown() {
        return Optional.ofNullable(this.maxRetriesDown);
    }
    /**
     * @return Type of the monitor
     * 
     */
    public Optional<String> monitorType() {
        return Optional.ofNullable(this.monitorType);
    }
    /**
     * @return The name of the resource
     * 
     */
    public Optional<String> name() {
        return Optional.ofNullable(this.name);
    }
    /**
     * @return The operating status of the resource
     * 
     */
    public Optional<String> operatingStatus() {
        return Optional.ofNullable(this.operatingStatus);
    }
    /**
     * @return The provisioning status of the resource
     * 
     */
    public Optional<String> provisioningStatus() {
        return Optional.ofNullable(this.provisioningStatus);
    }
    /**
     * @return Maximum time, in seconds, that a monitor waits to connect before it times out. This value must be less than the delay value
     * 
     */
    public Optional<Double> timeout() {
        return Optional.ofNullable(this.timeout);
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(LoadBalancerListenerPoolHealthMonitor defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable Double delay;
        private @Nullable LoadBalancerListenerPoolHealthMonitorHttpConfiguration httpConfiguration;
        private @Nullable Double maxRetries;
        private @Nullable Double maxRetriesDown;
        private @Nullable String monitorType;
        private @Nullable String name;
        private @Nullable String operatingStatus;
        private @Nullable String provisioningStatus;
        private @Nullable Double timeout;
        public Builder() {}
        public Builder(LoadBalancerListenerPoolHealthMonitor defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.delay = defaults.delay;
    	      this.httpConfiguration = defaults.httpConfiguration;
    	      this.maxRetries = defaults.maxRetries;
    	      this.maxRetriesDown = defaults.maxRetriesDown;
    	      this.monitorType = defaults.monitorType;
    	      this.name = defaults.name;
    	      this.operatingStatus = defaults.operatingStatus;
    	      this.provisioningStatus = defaults.provisioningStatus;
    	      this.timeout = defaults.timeout;
        }

        @CustomType.Setter
        public Builder delay(@Nullable Double delay) {

            this.delay = delay;
            return this;
        }
        @CustomType.Setter
        public Builder httpConfiguration(@Nullable LoadBalancerListenerPoolHealthMonitorHttpConfiguration httpConfiguration) {

            this.httpConfiguration = httpConfiguration;
            return this;
        }
        @CustomType.Setter
        public Builder maxRetries(@Nullable Double maxRetries) {

            this.maxRetries = maxRetries;
            return this;
        }
        @CustomType.Setter
        public Builder maxRetriesDown(@Nullable Double maxRetriesDown) {

            this.maxRetriesDown = maxRetriesDown;
            return this;
        }
        @CustomType.Setter
        public Builder monitorType(@Nullable String monitorType) {

            this.monitorType = monitorType;
            return this;
        }
        @CustomType.Setter
        public Builder name(@Nullable String name) {

            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder operatingStatus(@Nullable String operatingStatus) {

            this.operatingStatus = operatingStatus;
            return this;
        }
        @CustomType.Setter
        public Builder provisioningStatus(@Nullable String provisioningStatus) {

            this.provisioningStatus = provisioningStatus;
            return this;
        }
        @CustomType.Setter
        public Builder timeout(@Nullable Double timeout) {

            this.timeout = timeout;
            return this;
        }
        public LoadBalancerListenerPoolHealthMonitor build() {
            final var _resultValue = new LoadBalancerListenerPoolHealthMonitor();
            _resultValue.delay = delay;
            _resultValue.httpConfiguration = httpConfiguration;
            _resultValue.maxRetries = maxRetries;
            _resultValue.maxRetriesDown = maxRetriesDown;
            _resultValue.monitorType = monitorType;
            _resultValue.name = name;
            _resultValue.operatingStatus = operatingStatus;
            _resultValue.provisioningStatus = provisioningStatus;
            _resultValue.timeout = timeout;
            return _resultValue;
        }
    }
}
