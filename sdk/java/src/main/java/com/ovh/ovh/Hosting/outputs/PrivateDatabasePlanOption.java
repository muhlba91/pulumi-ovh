// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Hosting.outputs;

import com.ovh.ovh.Hosting.outputs.PrivateDatabasePlanOptionConfiguration;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;
import java.util.Optional;
import javax.annotation.Nullable;

@CustomType
public final class PrivateDatabasePlanOption {
    /**
     * @return Catalog name
     * 
     */
    private @Nullable String catalogName;
    /**
     * @return Representation of a configuration item for personalizing product
     * 
     */
    private @Nullable List<PrivateDatabasePlanOptionConfiguration> configurations;
    /**
     * @return Service duration
     * 
     */
    private String duration;
    /**
     * @return Plan code
     * 
     */
    private String planCode;
    /**
     * @return Pricing model identifier
     * 
     */
    private String pricingMode;

    private PrivateDatabasePlanOption() {}
    /**
     * @return Catalog name
     * 
     */
    public Optional<String> catalogName() {
        return Optional.ofNullable(this.catalogName);
    }
    /**
     * @return Representation of a configuration item for personalizing product
     * 
     */
    public List<PrivateDatabasePlanOptionConfiguration> configurations() {
        return this.configurations == null ? List.of() : this.configurations;
    }
    /**
     * @return Service duration
     * 
     */
    public String duration() {
        return this.duration;
    }
    /**
     * @return Plan code
     * 
     */
    public String planCode() {
        return this.planCode;
    }
    /**
     * @return Pricing model identifier
     * 
     */
    public String pricingMode() {
        return this.pricingMode;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(PrivateDatabasePlanOption defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private @Nullable String catalogName;
        private @Nullable List<PrivateDatabasePlanOptionConfiguration> configurations;
        private String duration;
        private String planCode;
        private String pricingMode;
        public Builder() {}
        public Builder(PrivateDatabasePlanOption defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.catalogName = defaults.catalogName;
    	      this.configurations = defaults.configurations;
    	      this.duration = defaults.duration;
    	      this.planCode = defaults.planCode;
    	      this.pricingMode = defaults.pricingMode;
        }

        @CustomType.Setter
        public Builder catalogName(@Nullable String catalogName) {

            this.catalogName = catalogName;
            return this;
        }
        @CustomType.Setter
        public Builder configurations(@Nullable List<PrivateDatabasePlanOptionConfiguration> configurations) {

            this.configurations = configurations;
            return this;
        }
        public Builder configurations(PrivateDatabasePlanOptionConfiguration... configurations) {
            return configurations(List.of(configurations));
        }
        @CustomType.Setter
        public Builder duration(String duration) {
            if (duration == null) {
              throw new MissingRequiredPropertyException("PrivateDatabasePlanOption", "duration");
            }
            this.duration = duration;
            return this;
        }
        @CustomType.Setter
        public Builder planCode(String planCode) {
            if (planCode == null) {
              throw new MissingRequiredPropertyException("PrivateDatabasePlanOption", "planCode");
            }
            this.planCode = planCode;
            return this;
        }
        @CustomType.Setter
        public Builder pricingMode(String pricingMode) {
            if (pricingMode == null) {
              throw new MissingRequiredPropertyException("PrivateDatabasePlanOption", "pricingMode");
            }
            this.pricingMode = pricingMode;
            return this;
        }
        public PrivateDatabasePlanOption build() {
            final var _resultValue = new PrivateDatabasePlanOption();
            _resultValue.catalogName = catalogName;
            _resultValue.configurations = configurations;
            _resultValue.duration = duration;
            _resultValue.planCode = planCode;
            _resultValue.pricingMode = pricingMode;
            return _resultValue;
        }
    }
}
