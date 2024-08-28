// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.CloudProjectDatabase;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class UserArgs extends com.pulumi.resources.ResourceArgs {

    public static final UserArgs Empty = new UserArgs();

    /**
     * Cluster ID.
     * 
     */
    @Import(name="clusterId", required=true)
    private Output<String> clusterId;

    /**
     * @return Cluster ID.
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }

    /**
     * The engine of the database cluster you want to add. You can find the complete list of available engine in the [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     * Available engines:
     * 
     */
    @Import(name="engine", required=true)
    private Output<String> engine;

    /**
     * @return The engine of the database cluster you want to add. You can find the complete list of available engine in the [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     * Available engines:
     * 
     */
    public Output<String> engine() {
        return this.engine;
    }

    /**
     * Name of the user. A user named &#34;avnadmin&#34; is mapped with already created admin user and reset his password instead of creating a new user. The &#34;Grafana&#34; engine only allows the &#34;avnadmin&#34; mapping.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of the user. A user named &#34;avnadmin&#34; is mapped with already created admin user and reset his password instead of creating a new user. The &#34;Grafana&#34; engine only allows the &#34;avnadmin&#34; mapping.
     * 
     */
    public Optional<Output<String>> name() {
        return Optional.ofNullable(this.name);
    }

    /**
     * Arbitrary string to change to trigger a password update
     * 
     */
    @Import(name="passwordReset")
    private @Nullable Output<String> passwordReset;

    /**
     * @return Arbitrary string to change to trigger a password update
     * 
     */
    public Optional<Output<String>> passwordReset() {
        return Optional.ofNullable(this.passwordReset);
    }

    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    @Import(name="serviceName", required=true)
    private Output<String> serviceName;

    /**
     * @return The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }

    private UserArgs() {}

    private UserArgs(UserArgs $) {
        this.clusterId = $.clusterId;
        this.engine = $.engine;
        this.name = $.name;
        this.passwordReset = $.passwordReset;
        this.serviceName = $.serviceName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(UserArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private UserArgs $;

        public Builder() {
            $ = new UserArgs();
        }

        public Builder(UserArgs defaults) {
            $ = new UserArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param clusterId Cluster ID.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(Output<String> clusterId) {
            $.clusterId = clusterId;
            return this;
        }

        /**
         * @param clusterId Cluster ID.
         * 
         * @return builder
         * 
         */
        public Builder clusterId(String clusterId) {
            return clusterId(Output.of(clusterId));
        }

        /**
         * @param engine The engine of the database cluster you want to add. You can find the complete list of available engine in the [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
         * Available engines:
         * 
         * @return builder
         * 
         */
        public Builder engine(Output<String> engine) {
            $.engine = engine;
            return this;
        }

        /**
         * @param engine The engine of the database cluster you want to add. You can find the complete list of available engine in the [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
         * Available engines:
         * 
         * @return builder
         * 
         */
        public Builder engine(String engine) {
            return engine(Output.of(engine));
        }

        /**
         * @param name Name of the user. A user named &#34;avnadmin&#34; is mapped with already created admin user and reset his password instead of creating a new user. The &#34;Grafana&#34; engine only allows the &#34;avnadmin&#34; mapping.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the user. A user named &#34;avnadmin&#34; is mapped with already created admin user and reset his password instead of creating a new user. The &#34;Grafana&#34; engine only allows the &#34;avnadmin&#34; mapping.
         * 
         * @return builder
         * 
         */
        public Builder name(String name) {
            return name(Output.of(name));
        }

        /**
         * @param passwordReset Arbitrary string to change to trigger a password update
         * 
         * @return builder
         * 
         */
        public Builder passwordReset(@Nullable Output<String> passwordReset) {
            $.passwordReset = passwordReset;
            return this;
        }

        /**
         * @param passwordReset Arbitrary string to change to trigger a password update
         * 
         * @return builder
         * 
         */
        public Builder passwordReset(String passwordReset) {
            return passwordReset(Output.of(passwordReset));
        }

        /**
         * @param serviceName The id of the public cloud project. If omitted,
         * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(Output<String> serviceName) {
            $.serviceName = serviceName;
            return this;
        }

        /**
         * @param serviceName The id of the public cloud project. If omitted,
         * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(String serviceName) {
            return serviceName(Output.of(serviceName));
        }

        public UserArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("UserArgs", "clusterId");
            }
            if ($.engine == null) {
                throw new MissingRequiredPropertyException("UserArgs", "engine");
            }
            if ($.serviceName == null) {
                throw new MissingRequiredPropertyException("UserArgs", "serviceName");
            }
            return $;
        }
    }

}
