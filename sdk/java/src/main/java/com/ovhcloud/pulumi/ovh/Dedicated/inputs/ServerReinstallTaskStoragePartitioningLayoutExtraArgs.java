// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Dedicated.inputs;

import com.ovhcloud.pulumi.ovh.Dedicated.inputs.ServerReinstallTaskStoragePartitioningLayoutExtraLvArgs;
import com.ovhcloud.pulumi.ovh.Dedicated.inputs.ServerReinstallTaskStoragePartitioningLayoutExtraZpArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ServerReinstallTaskStoragePartitioningLayoutExtraArgs extends com.pulumi.resources.ResourceArgs {

    public static final ServerReinstallTaskStoragePartitioningLayoutExtraArgs Empty = new ServerReinstallTaskStoragePartitioningLayoutExtraArgs();

    /**
     * LVM-specific parameters (when applicable)
     * 
     */
    @Import(name="lvs")
    private @Nullable Output<List<ServerReinstallTaskStoragePartitioningLayoutExtraLvArgs>> lvs;

    /**
     * @return LVM-specific parameters (when applicable)
     * 
     */
    public Optional<Output<List<ServerReinstallTaskStoragePartitioningLayoutExtraLvArgs>>> lvs() {
        return Optional.ofNullable(this.lvs);
    }

    /**
     * ZFS-specific parameters (when applicable)
     * 
     */
    @Import(name="zps")
    private @Nullable Output<List<ServerReinstallTaskStoragePartitioningLayoutExtraZpArgs>> zps;

    /**
     * @return ZFS-specific parameters (when applicable)
     * 
     */
    public Optional<Output<List<ServerReinstallTaskStoragePartitioningLayoutExtraZpArgs>>> zps() {
        return Optional.ofNullable(this.zps);
    }

    private ServerReinstallTaskStoragePartitioningLayoutExtraArgs() {}

    private ServerReinstallTaskStoragePartitioningLayoutExtraArgs(ServerReinstallTaskStoragePartitioningLayoutExtraArgs $) {
        this.lvs = $.lvs;
        this.zps = $.zps;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ServerReinstallTaskStoragePartitioningLayoutExtraArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ServerReinstallTaskStoragePartitioningLayoutExtraArgs $;

        public Builder() {
            $ = new ServerReinstallTaskStoragePartitioningLayoutExtraArgs();
        }

        public Builder(ServerReinstallTaskStoragePartitioningLayoutExtraArgs defaults) {
            $ = new ServerReinstallTaskStoragePartitioningLayoutExtraArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param lvs LVM-specific parameters (when applicable)
         * 
         * @return builder
         * 
         */
        public Builder lvs(@Nullable Output<List<ServerReinstallTaskStoragePartitioningLayoutExtraLvArgs>> lvs) {
            $.lvs = lvs;
            return this;
        }

        /**
         * @param lvs LVM-specific parameters (when applicable)
         * 
         * @return builder
         * 
         */
        public Builder lvs(List<ServerReinstallTaskStoragePartitioningLayoutExtraLvArgs> lvs) {
            return lvs(Output.of(lvs));
        }

        /**
         * @param lvs LVM-specific parameters (when applicable)
         * 
         * @return builder
         * 
         */
        public Builder lvs(ServerReinstallTaskStoragePartitioningLayoutExtraLvArgs... lvs) {
            return lvs(List.of(lvs));
        }

        /**
         * @param zps ZFS-specific parameters (when applicable)
         * 
         * @return builder
         * 
         */
        public Builder zps(@Nullable Output<List<ServerReinstallTaskStoragePartitioningLayoutExtraZpArgs>> zps) {
            $.zps = zps;
            return this;
        }

        /**
         * @param zps ZFS-specific parameters (when applicable)
         * 
         * @return builder
         * 
         */
        public Builder zps(List<ServerReinstallTaskStoragePartitioningLayoutExtraZpArgs> zps) {
            return zps(Output.of(zps));
        }

        /**
         * @param zps ZFS-specific parameters (when applicable)
         * 
         * @return builder
         * 
         */
        public Builder zps(ServerReinstallTaskStoragePartitioningLayoutExtraZpArgs... zps) {
            return zps(List.of(zps));
        }

        public ServerReinstallTaskStoragePartitioningLayoutExtraArgs build() {
            return $;
        }
    }

}
