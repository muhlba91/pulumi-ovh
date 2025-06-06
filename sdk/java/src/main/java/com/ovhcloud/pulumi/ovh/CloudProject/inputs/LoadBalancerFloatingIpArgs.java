// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class LoadBalancerFloatingIpArgs extends com.pulumi.resources.ResourceArgs {

    public static final LoadBalancerFloatingIpArgs Empty = new LoadBalancerFloatingIpArgs();

    /**
     * ID of the resource
     * 
     */
    @Import(name="id")
    private @Nullable Output<String> id;

    /**
     * @return ID of the resource
     * 
     */
    public Optional<Output<String>> id() {
        return Optional.ofNullable(this.id);
    }

    /**
     * IP Address of the resource
     * 
     */
    @Import(name="ip")
    private @Nullable Output<String> ip;

    /**
     * @return IP Address of the resource
     * 
     */
    public Optional<Output<String>> ip() {
        return Optional.ofNullable(this.ip);
    }

    private LoadBalancerFloatingIpArgs() {}

    private LoadBalancerFloatingIpArgs(LoadBalancerFloatingIpArgs $) {
        this.id = $.id;
        this.ip = $.ip;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(LoadBalancerFloatingIpArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private LoadBalancerFloatingIpArgs $;

        public Builder() {
            $ = new LoadBalancerFloatingIpArgs();
        }

        public Builder(LoadBalancerFloatingIpArgs defaults) {
            $ = new LoadBalancerFloatingIpArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param id ID of the resource
         * 
         * @return builder
         * 
         */
        public Builder id(@Nullable Output<String> id) {
            $.id = id;
            return this;
        }

        /**
         * @param id ID of the resource
         * 
         * @return builder
         * 
         */
        public Builder id(String id) {
            return id(Output.of(id));
        }

        /**
         * @param ip IP Address of the resource
         * 
         * @return builder
         * 
         */
        public Builder ip(@Nullable Output<String> ip) {
            $.ip = ip;
            return this;
        }

        /**
         * @param ip IP Address of the resource
         * 
         * @return builder
         * 
         */
        public Builder ip(String ip) {
            return ip(Output.of(ip));
        }

        public LoadBalancerFloatingIpArgs build() {
            return $;
        }
    }

}
