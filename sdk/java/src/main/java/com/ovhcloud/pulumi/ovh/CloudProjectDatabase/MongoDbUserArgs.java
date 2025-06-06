// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProjectDatabase;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class MongoDbUserArgs extends com.pulumi.resources.ResourceArgs {

    public static final MongoDbUserArgs Empty = new MongoDbUserArgs();

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
     * Name of the user. A user named &#34;admin&#34; is mapped with already created admin{@literal @}admin user instead of creating a new user.
     * 
     */
    @Import(name="name")
    private @Nullable Output<String> name;

    /**
     * @return Name of the user. A user named &#34;admin&#34; is mapped with already created admin{@literal @}admin user instead of creating a new user.
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
     * Roles the user belongs to. Since version 0.37.0, the authentication database must be indicated for all roles. Available roles:
     * * `backup{@literal @}admin`
     * * `clusterAdmin{@literal @}admin`
     * * `clusterManager{@literal @}admin`
     * * `clusterMonitor{@literal @}admin`
     * * `dbAdmin{@literal @}(defined db)`
     * * `dbAdminAnyDatabase{@literal @}admin`
     * * `dbOwner{@literal @}(defined db)`
     * * `enableSharding{@literal @}(defined db)`
     * * `hostManager{@literal @}admin`
     * * `read{@literal @}(defined db)`
     * * `readAnyDatabase{@literal @}admin`
     * * `readWrite{@literal @}(defined db)`
     * * `readWriteAnyDatabase{@literal @}admin`
     * * `restore{@literal @}admin`
     * * `root{@literal @}admin`
     * * `userAdmin{@literal @}(defined db)`
     * * `userAdminAnyDatabase{@literal @}admin`
     * 
     */
    @Import(name="roles")
    private @Nullable Output<List<String>> roles;

    /**
     * @return Roles the user belongs to. Since version 0.37.0, the authentication database must be indicated for all roles. Available roles:
     * * `backup{@literal @}admin`
     * * `clusterAdmin{@literal @}admin`
     * * `clusterManager{@literal @}admin`
     * * `clusterMonitor{@literal @}admin`
     * * `dbAdmin{@literal @}(defined db)`
     * * `dbAdminAnyDatabase{@literal @}admin`
     * * `dbOwner{@literal @}(defined db)`
     * * `enableSharding{@literal @}(defined db)`
     * * `hostManager{@literal @}admin`
     * * `read{@literal @}(defined db)`
     * * `readAnyDatabase{@literal @}admin`
     * * `readWrite{@literal @}(defined db)`
     * * `readWriteAnyDatabase{@literal @}admin`
     * * `restore{@literal @}admin`
     * * `root{@literal @}admin`
     * * `userAdmin{@literal @}(defined db)`
     * * `userAdminAnyDatabase{@literal @}admin`
     * 
     */
    public Optional<Output<List<String>>> roles() {
        return Optional.ofNullable(this.roles);
    }

    /**
     * The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    @Import(name="serviceName", required=true)
    private Output<String> serviceName;

    /**
     * @return The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }

    private MongoDbUserArgs() {}

    private MongoDbUserArgs(MongoDbUserArgs $) {
        this.clusterId = $.clusterId;
        this.name = $.name;
        this.passwordReset = $.passwordReset;
        this.roles = $.roles;
        this.serviceName = $.serviceName;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(MongoDbUserArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private MongoDbUserArgs $;

        public Builder() {
            $ = new MongoDbUserArgs();
        }

        public Builder(MongoDbUserArgs defaults) {
            $ = new MongoDbUserArgs(Objects.requireNonNull(defaults));
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
         * @param name Name of the user. A user named &#34;admin&#34; is mapped with already created admin{@literal @}admin user instead of creating a new user.
         * 
         * @return builder
         * 
         */
        public Builder name(@Nullable Output<String> name) {
            $.name = name;
            return this;
        }

        /**
         * @param name Name of the user. A user named &#34;admin&#34; is mapped with already created admin{@literal @}admin user instead of creating a new user.
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
         * @param roles Roles the user belongs to. Since version 0.37.0, the authentication database must be indicated for all roles. Available roles:
         * * `backup{@literal @}admin`
         * * `clusterAdmin{@literal @}admin`
         * * `clusterManager{@literal @}admin`
         * * `clusterMonitor{@literal @}admin`
         * * `dbAdmin{@literal @}(defined db)`
         * * `dbAdminAnyDatabase{@literal @}admin`
         * * `dbOwner{@literal @}(defined db)`
         * * `enableSharding{@literal @}(defined db)`
         * * `hostManager{@literal @}admin`
         * * `read{@literal @}(defined db)`
         * * `readAnyDatabase{@literal @}admin`
         * * `readWrite{@literal @}(defined db)`
         * * `readWriteAnyDatabase{@literal @}admin`
         * * `restore{@literal @}admin`
         * * `root{@literal @}admin`
         * * `userAdmin{@literal @}(defined db)`
         * * `userAdminAnyDatabase{@literal @}admin`
         * 
         * @return builder
         * 
         */
        public Builder roles(@Nullable Output<List<String>> roles) {
            $.roles = roles;
            return this;
        }

        /**
         * @param roles Roles the user belongs to. Since version 0.37.0, the authentication database must be indicated for all roles. Available roles:
         * * `backup{@literal @}admin`
         * * `clusterAdmin{@literal @}admin`
         * * `clusterManager{@literal @}admin`
         * * `clusterMonitor{@literal @}admin`
         * * `dbAdmin{@literal @}(defined db)`
         * * `dbAdminAnyDatabase{@literal @}admin`
         * * `dbOwner{@literal @}(defined db)`
         * * `enableSharding{@literal @}(defined db)`
         * * `hostManager{@literal @}admin`
         * * `read{@literal @}(defined db)`
         * * `readAnyDatabase{@literal @}admin`
         * * `readWrite{@literal @}(defined db)`
         * * `readWriteAnyDatabase{@literal @}admin`
         * * `restore{@literal @}admin`
         * * `root{@literal @}admin`
         * * `userAdmin{@literal @}(defined db)`
         * * `userAdminAnyDatabase{@literal @}admin`
         * 
         * @return builder
         * 
         */
        public Builder roles(List<String> roles) {
            return roles(Output.of(roles));
        }

        /**
         * @param roles Roles the user belongs to. Since version 0.37.0, the authentication database must be indicated for all roles. Available roles:
         * * `backup{@literal @}admin`
         * * `clusterAdmin{@literal @}admin`
         * * `clusterManager{@literal @}admin`
         * * `clusterMonitor{@literal @}admin`
         * * `dbAdmin{@literal @}(defined db)`
         * * `dbAdminAnyDatabase{@literal @}admin`
         * * `dbOwner{@literal @}(defined db)`
         * * `enableSharding{@literal @}(defined db)`
         * * `hostManager{@literal @}admin`
         * * `read{@literal @}(defined db)`
         * * `readAnyDatabase{@literal @}admin`
         * * `readWrite{@literal @}(defined db)`
         * * `readWriteAnyDatabase{@literal @}admin`
         * * `restore{@literal @}admin`
         * * `root{@literal @}admin`
         * * `userAdmin{@literal @}(defined db)`
         * * `userAdminAnyDatabase{@literal @}admin`
         * 
         * @return builder
         * 
         */
        public Builder roles(String... roles) {
            return roles(List.of(roles));
        }

        /**
         * @param serviceName The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(Output<String> serviceName) {
            $.serviceName = serviceName;
            return this;
        }

        /**
         * @param serviceName The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(String serviceName) {
            return serviceName(Output.of(serviceName));
        }

        public MongoDbUserArgs build() {
            if ($.clusterId == null) {
                throw new MissingRequiredPropertyException("MongoDbUserArgs", "clusterId");
            }
            if ($.serviceName == null) {
                throw new MissingRequiredPropertyException("MongoDbUserArgs", "serviceName");
            }
            return $;
        }
    }

}
