// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Ip.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class GetMitigationPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final GetMitigationPlainArgs Empty = new GetMitigationPlainArgs();

    /**
     * The IP or the CIDR
     * 
     */
    @Import(name="ip", required=true)
    private String ip;

    /**
     * @return The IP or the CIDR
     * 
     */
    public String ip() {
        return this.ip;
    }

    /**
     * IPv4 address
     * 
     */
    @Import(name="ipOnMitigation", required=true)
    private String ipOnMitigation;

    /**
     * @return IPv4 address
     * 
     */
    public String ipOnMitigation() {
        return this.ipOnMitigation;
    }

    private GetMitigationPlainArgs() {}

    private GetMitigationPlainArgs(GetMitigationPlainArgs $) {
        this.ip = $.ip;
        this.ipOnMitigation = $.ipOnMitigation;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(GetMitigationPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private GetMitigationPlainArgs $;

        public Builder() {
            $ = new GetMitigationPlainArgs();
        }

        public Builder(GetMitigationPlainArgs defaults) {
            $ = new GetMitigationPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param ip The IP or the CIDR
         * 
         * @return builder
         * 
         */
        public Builder ip(String ip) {
            $.ip = ip;
            return this;
        }

        /**
         * @param ipOnMitigation IPv4 address
         * 
         * @return builder
         * 
         */
        public Builder ipOnMitigation(String ipOnMitigation) {
            $.ipOnMitigation = ipOnMitigation;
            return this;
        }

        public GetMitigationPlainArgs build() {
            if ($.ip == null) {
                throw new MissingRequiredPropertyException("GetMitigationPlainArgs", "ip");
            }
            if ($.ipOnMitigation == null) {
                throw new MissingRequiredPropertyException("GetMitigationPlainArgs", "ipOnMitigation");
            }
            return $;
        }
    }

}
