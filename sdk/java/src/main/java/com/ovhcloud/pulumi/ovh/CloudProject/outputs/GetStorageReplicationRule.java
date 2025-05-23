// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.ovhcloud.pulumi.ovh.CloudProject.outputs.GetStorageReplicationRuleDestination;
import com.ovhcloud.pulumi.ovh.CloudProject.outputs.GetStorageReplicationRuleFilter;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Double;
import java.lang.String;
import java.util.Objects;

@CustomType
public final class GetStorageReplicationRule {
    /**
     * @return Delete marker replication
     * 
     */
    private String deleteMarkerReplication;
    /**
     * @return Rule destination configuration
     * 
     */
    private GetStorageReplicationRuleDestination destination;
    /**
     * @return Rule filters
     * 
     */
    private GetStorageReplicationRuleFilter filter;
    /**
     * @return Rule ID
     * 
     */
    private String id;
    /**
     * @return Rule priority
     * 
     */
    private Double priority;
    /**
     * @return Rule status
     * 
     */
    private String status;

    private GetStorageReplicationRule() {}
    /**
     * @return Delete marker replication
     * 
     */
    public String deleteMarkerReplication() {
        return this.deleteMarkerReplication;
    }
    /**
     * @return Rule destination configuration
     * 
     */
    public GetStorageReplicationRuleDestination destination() {
        return this.destination;
    }
    /**
     * @return Rule filters
     * 
     */
    public GetStorageReplicationRuleFilter filter() {
        return this.filter;
    }
    /**
     * @return Rule ID
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Rule priority
     * 
     */
    public Double priority() {
        return this.priority;
    }
    /**
     * @return Rule status
     * 
     */
    public String status() {
        return this.status;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetStorageReplicationRule defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String deleteMarkerReplication;
        private GetStorageReplicationRuleDestination destination;
        private GetStorageReplicationRuleFilter filter;
        private String id;
        private Double priority;
        private String status;
        public Builder() {}
        public Builder(GetStorageReplicationRule defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.deleteMarkerReplication = defaults.deleteMarkerReplication;
    	      this.destination = defaults.destination;
    	      this.filter = defaults.filter;
    	      this.id = defaults.id;
    	      this.priority = defaults.priority;
    	      this.status = defaults.status;
        }

        @CustomType.Setter
        public Builder deleteMarkerReplication(String deleteMarkerReplication) {
            if (deleteMarkerReplication == null) {
              throw new MissingRequiredPropertyException("GetStorageReplicationRule", "deleteMarkerReplication");
            }
            this.deleteMarkerReplication = deleteMarkerReplication;
            return this;
        }
        @CustomType.Setter
        public Builder destination(GetStorageReplicationRuleDestination destination) {
            if (destination == null) {
              throw new MissingRequiredPropertyException("GetStorageReplicationRule", "destination");
            }
            this.destination = destination;
            return this;
        }
        @CustomType.Setter
        public Builder filter(GetStorageReplicationRuleFilter filter) {
            if (filter == null) {
              throw new MissingRequiredPropertyException("GetStorageReplicationRule", "filter");
            }
            this.filter = filter;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetStorageReplicationRule", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder priority(Double priority) {
            if (priority == null) {
              throw new MissingRequiredPropertyException("GetStorageReplicationRule", "priority");
            }
            this.priority = priority;
            return this;
        }
        @CustomType.Setter
        public Builder status(String status) {
            if (status == null) {
              throw new MissingRequiredPropertyException("GetStorageReplicationRule", "status");
            }
            this.status = status;
            return this;
        }
        public GetStorageReplicationRule build() {
            final var _resultValue = new GetStorageReplicationRule();
            _resultValue.deleteMarkerReplication = deleteMarkerReplication;
            _resultValue.destination = destination;
            _resultValue.filter = filter;
            _resultValue.id = id;
            _resultValue.priority = priority;
            _resultValue.status = status;
            return _resultValue;
        }
    }
}
