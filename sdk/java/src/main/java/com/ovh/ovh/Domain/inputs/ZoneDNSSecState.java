// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Domain.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ZoneDNSSecState extends com.pulumi.resources.ResourceArgs {

    public static final ZoneDNSSecState Empty = new ZoneDNSSecState();

    /**
     * DNSSEC status (`disableInProgress`, `disabled`, `enableInProgress` or `enabled`)
     * 
     */
    @Import(name="status")
    private @Nullable Output<String> status;

    /**
     * @return DNSSEC status (`disableInProgress`, `disabled`, `enableInProgress` or `enabled`)
     * 
     */
    public Optional<Output<String>> status() {
        return Optional.ofNullable(this.status);
    }

    /**
     * The name of the domain zone
     * 
     */
    @Import(name="zoneName")
    private @Nullable Output<String> zoneName;

    /**
     * @return The name of the domain zone
     * 
     */
    public Optional<Output<String>> zoneName() {
        return Optional.ofNullable(this.zoneName);
    }

    private ZoneDNSSecState() {}

    private ZoneDNSSecState(ZoneDNSSecState $) {
        this.status = $.status;
        this.zoneName = $.zoneName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ZoneDNSSecState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ZoneDNSSecState $;

        public Builder() {
            $ = new ZoneDNSSecState();
        }

        public Builder(ZoneDNSSecState defaults) {
            $ = new ZoneDNSSecState(Objects.requireNonNull(defaults));
        }

        /**
         * @param status DNSSEC status (`disableInProgress`, `disabled`, `enableInProgress` or `enabled`)
         * 
         * @return builder
         * 
         */
        public Builder status(@Nullable Output<String> status) {
            $.status = status;
            return this;
        }

        /**
         * @param status DNSSEC status (`disableInProgress`, `disabled`, `enableInProgress` or `enabled`)
         * 
         * @return builder
         * 
         */
        public Builder status(String status) {
            return status(Output.of(status));
        }

        /**
         * @param zoneName The name of the domain zone
         * 
         * @return builder
         * 
         */
        public Builder zoneName(@Nullable Output<String> zoneName) {
            $.zoneName = zoneName;
            return this;
        }

        /**
         * @param zoneName The name of the domain zone
         * 
         * @return builder
         * 
         */
        public Builder zoneName(String zoneName) {
            return zoneName(Output.of(zoneName));
        }

        public ZoneDNSSecState build() {
            return $;
        }
    }

}
