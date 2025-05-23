// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Domain.inputs;

import com.ovhcloud.pulumi.ovh.Domain.inputs.NameCurrentStateArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.NameCurrentTaskArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.NameIamArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.NameOrderArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.NamePlanArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.NamePlanOptionArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.NameTargetSpecArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class NameState extends com.pulumi.resources.ResourceArgs {

    public static final NameState Empty = new NameState();

    /**
     * Computed hash used to control concurrent modification requests. Here, it represents the current target specification value
     * 
     */
    @Import(name="checksum")
    private @Nullable Output<String> checksum;

    /**
     * @return Computed hash used to control concurrent modification requests. Here, it represents the current target specification value
     * 
     */
    public Optional<Output<String>> checksum() {
        return Optional.ofNullable(this.checksum);
    }

    /**
     * Current state of the domain name
     * 
     */
    @Import(name="currentState")
    private @Nullable Output<NameCurrentStateArgs> currentState;

    /**
     * @return Current state of the domain name
     * 
     */
    public Optional<Output<NameCurrentStateArgs>> currentState() {
        return Optional.ofNullable(this.currentState);
    }

    /**
     * Ongoing asynchronous tasks related to the domain name resource
     * 
     */
    @Import(name="currentTasks")
    private @Nullable Output<List<NameCurrentTaskArgs>> currentTasks;

    /**
     * @return Ongoing asynchronous tasks related to the domain name resource
     * 
     */
    public Optional<Output<List<NameCurrentTaskArgs>>> currentTasks() {
        return Optional.ofNullable(this.currentTasks);
    }

    /**
     * Domain name
     * 
     */
    @Import(name="domainName")
    private @Nullable Output<String> domainName;

    /**
     * @return Domain name
     * 
     */
    public Optional<Output<String>> domainName() {
        return Optional.ofNullable(this.domainName);
    }

    /**
     * IAM resource metadata
     * 
     */
    @Import(name="iam")
    private @Nullable Output<NameIamArgs> iam;

    /**
     * @return IAM resource metadata
     * 
     */
    public Optional<Output<NameIamArgs>> iam() {
        return Optional.ofNullable(this.iam);
    }

    /**
     * Details about an Order
     * 
     */
    @Import(name="order")
    private @Nullable Output<NameOrderArgs> order;

    /**
     * @return Details about an Order
     * 
     */
    public Optional<Output<NameOrderArgs>> order() {
        return Optional.ofNullable(this.order);
    }

    /**
     * OVH subsidiaries
     * 
     */
    @Import(name="ovhSubsidiary")
    private @Nullable Output<String> ovhSubsidiary;

    /**
     * @return OVH subsidiaries
     * 
     */
    public Optional<Output<String>> ovhSubsidiary() {
        return Optional.ofNullable(this.ovhSubsidiary);
    }

    @Import(name="planOptions")
    private @Nullable Output<List<NamePlanOptionArgs>> planOptions;

    public Optional<Output<List<NamePlanOptionArgs>>> planOptions() {
        return Optional.ofNullable(this.planOptions);
    }

    @Import(name="plans")
    private @Nullable Output<List<NamePlanArgs>> plans;

    public Optional<Output<List<NamePlanArgs>>> plans() {
        return Optional.ofNullable(this.plans);
    }

    /**
     * Reflects the readiness of the domain name resource. A new target specification request will be accepted only in `READY`, `UPDATING` or `ERROR` status
     * 
     */
    @Import(name="resourceStatus")
    private @Nullable Output<String> resourceStatus;

    /**
     * @return Reflects the readiness of the domain name resource. A new target specification request will be accepted only in `READY`, `UPDATING` or `ERROR` status
     * 
     */
    public Optional<Output<String>> resourceStatus() {
        return Optional.ofNullable(this.resourceStatus);
    }

    /**
     * Latest target specification of the domain name resource.
     * 
     */
    @Import(name="targetSpec")
    private @Nullable Output<NameTargetSpecArgs> targetSpec;

    /**
     * @return Latest target specification of the domain name resource.
     * 
     */
    public Optional<Output<NameTargetSpecArgs>> targetSpec() {
        return Optional.ofNullable(this.targetSpec);
    }

    private NameState() {}

    private NameState(NameState $) {
        this.checksum = $.checksum;
        this.currentState = $.currentState;
        this.currentTasks = $.currentTasks;
        this.domainName = $.domainName;
        this.iam = $.iam;
        this.order = $.order;
        this.ovhSubsidiary = $.ovhSubsidiary;
        this.planOptions = $.planOptions;
        this.plans = $.plans;
        this.resourceStatus = $.resourceStatus;
        this.targetSpec = $.targetSpec;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(NameState defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private NameState $;

        public Builder() {
            $ = new NameState();
        }

        public Builder(NameState defaults) {
            $ = new NameState(Objects.requireNonNull(defaults));
        }

        /**
         * @param checksum Computed hash used to control concurrent modification requests. Here, it represents the current target specification value
         * 
         * @return builder
         * 
         */
        public Builder checksum(@Nullable Output<String> checksum) {
            $.checksum = checksum;
            return this;
        }

        /**
         * @param checksum Computed hash used to control concurrent modification requests. Here, it represents the current target specification value
         * 
         * @return builder
         * 
         */
        public Builder checksum(String checksum) {
            return checksum(Output.of(checksum));
        }

        /**
         * @param currentState Current state of the domain name
         * 
         * @return builder
         * 
         */
        public Builder currentState(@Nullable Output<NameCurrentStateArgs> currentState) {
            $.currentState = currentState;
            return this;
        }

        /**
         * @param currentState Current state of the domain name
         * 
         * @return builder
         * 
         */
        public Builder currentState(NameCurrentStateArgs currentState) {
            return currentState(Output.of(currentState));
        }

        /**
         * @param currentTasks Ongoing asynchronous tasks related to the domain name resource
         * 
         * @return builder
         * 
         */
        public Builder currentTasks(@Nullable Output<List<NameCurrentTaskArgs>> currentTasks) {
            $.currentTasks = currentTasks;
            return this;
        }

        /**
         * @param currentTasks Ongoing asynchronous tasks related to the domain name resource
         * 
         * @return builder
         * 
         */
        public Builder currentTasks(List<NameCurrentTaskArgs> currentTasks) {
            return currentTasks(Output.of(currentTasks));
        }

        /**
         * @param currentTasks Ongoing asynchronous tasks related to the domain name resource
         * 
         * @return builder
         * 
         */
        public Builder currentTasks(NameCurrentTaskArgs... currentTasks) {
            return currentTasks(List.of(currentTasks));
        }

        /**
         * @param domainName Domain name
         * 
         * @return builder
         * 
         */
        public Builder domainName(@Nullable Output<String> domainName) {
            $.domainName = domainName;
            return this;
        }

        /**
         * @param domainName Domain name
         * 
         * @return builder
         * 
         */
        public Builder domainName(String domainName) {
            return domainName(Output.of(domainName));
        }

        /**
         * @param iam IAM resource metadata
         * 
         * @return builder
         * 
         */
        public Builder iam(@Nullable Output<NameIamArgs> iam) {
            $.iam = iam;
            return this;
        }

        /**
         * @param iam IAM resource metadata
         * 
         * @return builder
         * 
         */
        public Builder iam(NameIamArgs iam) {
            return iam(Output.of(iam));
        }

        /**
         * @param order Details about an Order
         * 
         * @return builder
         * 
         */
        public Builder order(@Nullable Output<NameOrderArgs> order) {
            $.order = order;
            return this;
        }

        /**
         * @param order Details about an Order
         * 
         * @return builder
         * 
         */
        public Builder order(NameOrderArgs order) {
            return order(Output.of(order));
        }

        /**
         * @param ovhSubsidiary OVH subsidiaries
         * 
         * @return builder
         * 
         */
        public Builder ovhSubsidiary(@Nullable Output<String> ovhSubsidiary) {
            $.ovhSubsidiary = ovhSubsidiary;
            return this;
        }

        /**
         * @param ovhSubsidiary OVH subsidiaries
         * 
         * @return builder
         * 
         */
        public Builder ovhSubsidiary(String ovhSubsidiary) {
            return ovhSubsidiary(Output.of(ovhSubsidiary));
        }

        public Builder planOptions(@Nullable Output<List<NamePlanOptionArgs>> planOptions) {
            $.planOptions = planOptions;
            return this;
        }

        public Builder planOptions(List<NamePlanOptionArgs> planOptions) {
            return planOptions(Output.of(planOptions));
        }

        public Builder planOptions(NamePlanOptionArgs... planOptions) {
            return planOptions(List.of(planOptions));
        }

        public Builder plans(@Nullable Output<List<NamePlanArgs>> plans) {
            $.plans = plans;
            return this;
        }

        public Builder plans(List<NamePlanArgs> plans) {
            return plans(Output.of(plans));
        }

        public Builder plans(NamePlanArgs... plans) {
            return plans(List.of(plans));
        }

        /**
         * @param resourceStatus Reflects the readiness of the domain name resource. A new target specification request will be accepted only in `READY`, `UPDATING` or `ERROR` status
         * 
         * @return builder
         * 
         */
        public Builder resourceStatus(@Nullable Output<String> resourceStatus) {
            $.resourceStatus = resourceStatus;
            return this;
        }

        /**
         * @param resourceStatus Reflects the readiness of the domain name resource. A new target specification request will be accepted only in `READY`, `UPDATING` or `ERROR` status
         * 
         * @return builder
         * 
         */
        public Builder resourceStatus(String resourceStatus) {
            return resourceStatus(Output.of(resourceStatus));
        }

        /**
         * @param targetSpec Latest target specification of the domain name resource.
         * 
         * @return builder
         * 
         */
        public Builder targetSpec(@Nullable Output<NameTargetSpecArgs> targetSpec) {
            $.targetSpec = targetSpec;
            return this;
        }

        /**
         * @param targetSpec Latest target specification of the domain name resource.
         * 
         * @return builder
         * 
         */
        public Builder targetSpec(NameTargetSpecArgs targetSpec) {
            return targetSpec(Output.of(targetSpec));
        }

        public NameState build() {
            return $;
        }
    }

}
