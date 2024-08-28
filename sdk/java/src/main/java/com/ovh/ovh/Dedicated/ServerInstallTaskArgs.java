// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Dedicated;

import com.ovh.ovh.Dedicated.inputs.ServerInstallTaskDetailsArgs;
import com.ovh.ovh.Dedicated.inputs.ServerInstallTaskUserMetadataArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ServerInstallTaskArgs extends com.pulumi.resources.ResourceArgs {

    public static final ServerInstallTaskArgs Empty = new ServerInstallTaskArgs();

    /**
     * If set, reboot the server on the specified boot id during destroy phase.
     * 
     */
    @Import(name="bootidOnDestroy")
    private @Nullable Output<Integer> bootidOnDestroy;

    /**
     * @return If set, reboot the server on the specified boot id during destroy phase.
     * 
     */
    public Optional<Output<Integer>> bootidOnDestroy() {
        return Optional.ofNullable(this.bootidOnDestroy);
    }

    /**
     * see `details` block below.
     * 
     */
    @Import(name="details")
    private @Nullable Output<ServerInstallTaskDetailsArgs> details;

    /**
     * @return see `details` block below.
     * 
     */
    public Optional<Output<ServerInstallTaskDetailsArgs>> details() {
        return Optional.ofNullable(this.details);
    }

    /**
     * Partition scheme name.
     * 
     */
    @Import(name="partitionSchemeName")
    private @Nullable Output<String> partitionSchemeName;

    /**
     * @return Partition scheme name.
     * 
     */
    public Optional<Output<String>> partitionSchemeName() {
        return Optional.ofNullable(this.partitionSchemeName);
    }

    /**
     * The service_name of your dedicated server.
     * 
     */
    @Import(name="serviceName", required=true)
    private Output<String> serviceName;

    /**
     * @return The service_name of your dedicated server.
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }

    /**
     * Template name.
     * 
     */
    @Import(name="templateName", required=true)
    private Output<String> templateName;

    /**
     * @return Template name.
     * 
     */
    public Output<String> templateName() {
        return this.templateName;
    }

    /**
     * see `user_metadata` block below.
     * 
     */
    @Import(name="userMetadatas")
    private @Nullable Output<List<ServerInstallTaskUserMetadataArgs>> userMetadatas;

    /**
     * @return see `user_metadata` block below.
     * 
     */
    public Optional<Output<List<ServerInstallTaskUserMetadataArgs>>> userMetadatas() {
        return Optional.ofNullable(this.userMetadatas);
    }

    private ServerInstallTaskArgs() {}

    private ServerInstallTaskArgs(ServerInstallTaskArgs $) {
        this.bootidOnDestroy = $.bootidOnDestroy;
        this.details = $.details;
        this.partitionSchemeName = $.partitionSchemeName;
        this.serviceName = $.serviceName;
        this.templateName = $.templateName;
        this.userMetadatas = $.userMetadatas;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ServerInstallTaskArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ServerInstallTaskArgs $;

        public Builder() {
            $ = new ServerInstallTaskArgs();
        }

        public Builder(ServerInstallTaskArgs defaults) {
            $ = new ServerInstallTaskArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param bootidOnDestroy If set, reboot the server on the specified boot id during destroy phase.
         * 
         * @return builder
         * 
         */
        public Builder bootidOnDestroy(@Nullable Output<Integer> bootidOnDestroy) {
            $.bootidOnDestroy = bootidOnDestroy;
            return this;
        }

        /**
         * @param bootidOnDestroy If set, reboot the server on the specified boot id during destroy phase.
         * 
         * @return builder
         * 
         */
        public Builder bootidOnDestroy(Integer bootidOnDestroy) {
            return bootidOnDestroy(Output.of(bootidOnDestroy));
        }

        /**
         * @param details see `details` block below.
         * 
         * @return builder
         * 
         */
        public Builder details(@Nullable Output<ServerInstallTaskDetailsArgs> details) {
            $.details = details;
            return this;
        }

        /**
         * @param details see `details` block below.
         * 
         * @return builder
         * 
         */
        public Builder details(ServerInstallTaskDetailsArgs details) {
            return details(Output.of(details));
        }

        /**
         * @param partitionSchemeName Partition scheme name.
         * 
         * @return builder
         * 
         */
        public Builder partitionSchemeName(@Nullable Output<String> partitionSchemeName) {
            $.partitionSchemeName = partitionSchemeName;
            return this;
        }

        /**
         * @param partitionSchemeName Partition scheme name.
         * 
         * @return builder
         * 
         */
        public Builder partitionSchemeName(String partitionSchemeName) {
            return partitionSchemeName(Output.of(partitionSchemeName));
        }

        /**
         * @param serviceName The service_name of your dedicated server.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(Output<String> serviceName) {
            $.serviceName = serviceName;
            return this;
        }

        /**
         * @param serviceName The service_name of your dedicated server.
         * 
         * @return builder
         * 
         */
        public Builder serviceName(String serviceName) {
            return serviceName(Output.of(serviceName));
        }

        /**
         * @param templateName Template name.
         * 
         * @return builder
         * 
         */
        public Builder templateName(Output<String> templateName) {
            $.templateName = templateName;
            return this;
        }

        /**
         * @param templateName Template name.
         * 
         * @return builder
         * 
         */
        public Builder templateName(String templateName) {
            return templateName(Output.of(templateName));
        }

        /**
         * @param userMetadatas see `user_metadata` block below.
         * 
         * @return builder
         * 
         */
        public Builder userMetadatas(@Nullable Output<List<ServerInstallTaskUserMetadataArgs>> userMetadatas) {
            $.userMetadatas = userMetadatas;
            return this;
        }

        /**
         * @param userMetadatas see `user_metadata` block below.
         * 
         * @return builder
         * 
         */
        public Builder userMetadatas(List<ServerInstallTaskUserMetadataArgs> userMetadatas) {
            return userMetadatas(Output.of(userMetadatas));
        }

        /**
         * @param userMetadatas see `user_metadata` block below.
         * 
         * @return builder
         * 
         */
        public Builder userMetadatas(ServerInstallTaskUserMetadataArgs... userMetadatas) {
            return userMetadatas(List.of(userMetadatas));
        }

        public ServerInstallTaskArgs build() {
            if ($.serviceName == null) {
                throw new MissingRequiredPropertyException("ServerInstallTaskArgs", "serviceName");
            }
            if ($.templateName == null) {
                throw new MissingRequiredPropertyException("ServerInstallTaskArgs", "templateName");
            }
            return $;
        }
    }

}
