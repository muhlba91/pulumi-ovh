// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Domain;

import com.ovhcloud.pulumi.ovh.Domain.inputs.ZoneOrderArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.ZonePlanArgs;
import com.ovhcloud.pulumi.ovh.Domain.inputs.ZonePlanOptionArgs;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;


public final class ZoneArgs extends com.pulumi.resources.ResourceArgs {

    public static final ZoneArgs Empty = new ZoneArgs();

    /**
     * Details about an Order
     * 
     */
    @Import(name="orders")
    private @Nullable Output<List<ZoneOrderArgs>> orders;

    /**
     * @return Details about an Order
     * 
     */
    public Optional<Output<List<ZoneOrderArgs>>> orders() {
        return Optional.ofNullable(this.orders);
    }

    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     * 
     */
    @Import(name="ovhSubsidiary")
    private @Nullable Output<String> ovhSubsidiary;

    /**
     * @return OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     * 
     */
    public Optional<Output<String>> ovhSubsidiary() {
        return Optional.ofNullable(this.ovhSubsidiary);
    }

    /**
     * Ovh payment mode
     * 
     * @deprecated
     * This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     * 
     */
    @Deprecated /* This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used. */
    @Import(name="paymentMean")
    private @Nullable Output<String> paymentMean;

    /**
     * @return Ovh payment mode
     * 
     * @deprecated
     * This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     * 
     */
    @Deprecated /* This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used. */
    public Optional<Output<String>> paymentMean() {
        return Optional.ofNullable(this.paymentMean);
    }

    /**
     * Product Plan to order
     * 
     */
    @Import(name="plan")
    private @Nullable Output<ZonePlanArgs> plan;

    /**
     * @return Product Plan to order
     * 
     */
    public Optional<Output<ZonePlanArgs>> plan() {
        return Optional.ofNullable(this.plan);
    }

    /**
     * Product Plan to order
     * 
     */
    @Import(name="planOptions")
    private @Nullable Output<List<ZonePlanOptionArgs>> planOptions;

    /**
     * @return Product Plan to order
     * 
     */
    public Optional<Output<List<ZonePlanOptionArgs>>> planOptions() {
        return Optional.ofNullable(this.planOptions);
    }

    private ZoneArgs() {}

    private ZoneArgs(ZoneArgs $) {
        this.orders = $.orders;
        this.ovhSubsidiary = $.ovhSubsidiary;
        this.paymentMean = $.paymentMean;
        this.plan = $.plan;
        this.planOptions = $.planOptions;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(ZoneArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private ZoneArgs $;

        public Builder() {
            $ = new ZoneArgs();
        }

        public Builder(ZoneArgs defaults) {
            $ = new ZoneArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param orders Details about an Order
         * 
         * @return builder
         * 
         */
        public Builder orders(@Nullable Output<List<ZoneOrderArgs>> orders) {
            $.orders = orders;
            return this;
        }

        /**
         * @param orders Details about an Order
         * 
         * @return builder
         * 
         */
        public Builder orders(List<ZoneOrderArgs> orders) {
            return orders(Output.of(orders));
        }

        /**
         * @param orders Details about an Order
         * 
         * @return builder
         * 
         */
        public Builder orders(ZoneOrderArgs... orders) {
            return orders(List.of(orders));
        }

        /**
         * @param ovhSubsidiary OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
         * 
         * @return builder
         * 
         */
        public Builder ovhSubsidiary(@Nullable Output<String> ovhSubsidiary) {
            $.ovhSubsidiary = ovhSubsidiary;
            return this;
        }

        /**
         * @param ovhSubsidiary OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
         * 
         * @return builder
         * 
         */
        public Builder ovhSubsidiary(String ovhSubsidiary) {
            return ovhSubsidiary(Output.of(ovhSubsidiary));
        }

        /**
         * @param paymentMean Ovh payment mode
         * 
         * @return builder
         * 
         * @deprecated
         * This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
         * 
         */
        @Deprecated /* This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used. */
        public Builder paymentMean(@Nullable Output<String> paymentMean) {
            $.paymentMean = paymentMean;
            return this;
        }

        /**
         * @param paymentMean Ovh payment mode
         * 
         * @return builder
         * 
         * @deprecated
         * This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
         * 
         */
        @Deprecated /* This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used. */
        public Builder paymentMean(String paymentMean) {
            return paymentMean(Output.of(paymentMean));
        }

        /**
         * @param plan Product Plan to order
         * 
         * @return builder
         * 
         */
        public Builder plan(@Nullable Output<ZonePlanArgs> plan) {
            $.plan = plan;
            return this;
        }

        /**
         * @param plan Product Plan to order
         * 
         * @return builder
         * 
         */
        public Builder plan(ZonePlanArgs plan) {
            return plan(Output.of(plan));
        }

        /**
         * @param planOptions Product Plan to order
         * 
         * @return builder
         * 
         */
        public Builder planOptions(@Nullable Output<List<ZonePlanOptionArgs>> planOptions) {
            $.planOptions = planOptions;
            return this;
        }

        /**
         * @param planOptions Product Plan to order
         * 
         * @return builder
         * 
         */
        public Builder planOptions(List<ZonePlanOptionArgs> planOptions) {
            return planOptions(Output.of(planOptions));
        }

        /**
         * @param planOptions Product Plan to order
         * 
         * @return builder
         * 
         */
        public Builder planOptions(ZonePlanOptionArgs... planOptions) {
            return planOptions(List.of(planOptions));
        }

        public ZoneArgs build() {
            return $;
        }
    }

}
