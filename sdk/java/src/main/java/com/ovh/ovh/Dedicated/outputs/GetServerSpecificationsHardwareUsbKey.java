// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Dedicated.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Double;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetServerSpecificationsHardwareUsbKey {
    private String unit;
    private Double value;

    private GetServerSpecificationsHardwareUsbKey() {}
    public String unit() {
        return this.unit;
    }
    public Double value() {
        return this.value;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetServerSpecificationsHardwareUsbKey defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String unit;
        private Double value;
        public Builder() {}
        public Builder(GetServerSpecificationsHardwareUsbKey defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.unit = defaults.unit;
    	      this.value = defaults.value;
        }

        @CustomType.Setter
        public Builder unit(String unit) {
            if (unit == null) {
              throw new MissingRequiredPropertyException("GetServerSpecificationsHardwareUsbKey", "unit");
            }
            this.unit = unit;
            return this;
        }
        @CustomType.Setter
        public Builder value(Double value) {
            if (value == null) {
              throw new MissingRequiredPropertyException("GetServerSpecificationsHardwareUsbKey", "value");
            }
            this.value = value;
            return this;
        }
        public GetServerSpecificationsHardwareUsbKey build() {
            final var _resultValue = new GetServerSpecificationsHardwareUsbKey();
            _resultValue.unit = unit;
            _resultValue.value = value;
            return _resultValue;
        }
    }
}
