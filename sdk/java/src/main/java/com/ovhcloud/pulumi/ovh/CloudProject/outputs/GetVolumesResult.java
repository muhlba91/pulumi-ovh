// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.ovhcloud.pulumi.ovh.CloudProject.outputs.GetVolumesVolume;
import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetVolumesResult {
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return The region name where volumes are available
     * 
     */
    private String regionName;
    /**
     * @return The id of the public cloud project.
     * 
     */
    private String serviceName;
    private List<GetVolumesVolume> volumes;

    private GetVolumesResult() {}
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The region name where volumes are available
     * 
     */
    public String regionName() {
        return this.regionName;
    }
    /**
     * @return The id of the public cloud project.
     * 
     */
    public String serviceName() {
        return this.serviceName;
    }
    public List<GetVolumesVolume> volumes() {
        return this.volumes;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetVolumesResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String id;
        private String regionName;
        private String serviceName;
        private List<GetVolumesVolume> volumes;
        public Builder() {}
        public Builder(GetVolumesResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.id = defaults.id;
    	      this.regionName = defaults.regionName;
    	      this.serviceName = defaults.serviceName;
    	      this.volumes = defaults.volumes;
        }

        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetVolumesResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder regionName(String regionName) {
            if (regionName == null) {
              throw new MissingRequiredPropertyException("GetVolumesResult", "regionName");
            }
            this.regionName = regionName;
            return this;
        }
        @CustomType.Setter
        public Builder serviceName(String serviceName) {
            if (serviceName == null) {
              throw new MissingRequiredPropertyException("GetVolumesResult", "serviceName");
            }
            this.serviceName = serviceName;
            return this;
        }
        @CustomType.Setter
        public Builder volumes(List<GetVolumesVolume> volumes) {
            if (volumes == null) {
              throw new MissingRequiredPropertyException("GetVolumesResult", "volumes");
            }
            this.volumes = volumes;
            return this;
        }
        public Builder volumes(GetVolumesVolume... volumes) {
            return volumes(List.of(volumes));
        }
        public GetVolumesResult build() {
            final var _resultValue = new GetVolumesResult();
            _resultValue.id = id;
            _resultValue.regionName = regionName;
            _resultValue.serviceName = serviceName;
            _resultValue.volumes = volumes;
            return _resultValue;
        }
    }
}
