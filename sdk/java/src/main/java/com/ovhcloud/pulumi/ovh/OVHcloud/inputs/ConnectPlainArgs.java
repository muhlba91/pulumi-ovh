// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.OVHcloud.inputs;

import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;


public final class ConnectPlainArgs extends com.pulumi.resources.InvokeArgs {

    public static final ConnectPlainArgs Empty = new ConnectPlainArgs();

    /**
     * The uuid of the Ovhcloud connect.
     * 
     */
    @Import(name="serviceName", required=true)
    private String serviceName;

    /**
     * @return The uuid of the Ovhcloud connect.
     * 
     */
    public String serviceName() {
        return this.serviceName;
    }

    private ConnectPlainArgs() {}

    private ConnectPlainArgs(ConnectPlainArgs $) {
        this.serviceName = $.serviceName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ConnectPlainArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ConnectPlainArgs $;

        public Builder() {
            $ = new ConnectPlainArgs();
        }

        public Builder(ConnectPlainArgs defaults) {
            $ = new ConnectPlainArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param serviceName The uuid of the Ovhcloud connect.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(String serviceName) {
            $.serviceName = serviceName;
            return this;
        }

        public ConnectPlainArgs build() {
            if ($.serviceName == null) {
                throw new MissingRequiredPropertyException("ConnectPlainArgs", "serviceName");
            }
            return $;
        }
    }

}
