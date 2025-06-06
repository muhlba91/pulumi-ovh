// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Double;
import java.lang.String;
import java.util.List;
import java.util.Objects;

@CustomType
public final class GetImagesImage {
    /**
     * @return Image creation date
     * 
     */
    private String creationDate;
    /**
     * @return Image usable only for this type of flavor if not null
     * 
     */
    private String flavorType;
    /**
     * @return Image ID
     * 
     */
    private String id;
    /**
     * @return Minimum disks required to use image
     * 
     */
    private Double minDisk;
    /**
     * @return Minimum RAM required to use image
     * 
     */
    private Double minRam;
    /**
     * @return Image name
     * 
     */
    private String name;
    /**
     * @return Order plan code
     * 
     */
    private String planCode;
    /**
     * @return Image region
     * 
     */
    private String region;
    /**
     * @return Image size (in GiB)
     * 
     */
    private Double size;
    /**
     * @return Image status
     * 
     */
    private String status;
    /**
     * @return Tags about the image
     * 
     */
    private List<String> tags;
    /**
     * @return Image type
     * 
     */
    private String type;
    /**
     * @return User to connect with
     * 
     */
    private String user;
    /**
     * @return Image visibility
     * 
     */
    private String visibility;

    private GetImagesImage() {}
    /**
     * @return Image creation date
     * 
     */
    public String creationDate() {
        return this.creationDate;
    }
    /**
     * @return Image usable only for this type of flavor if not null
     * 
     */
    public String flavorType() {
        return this.flavorType;
    }
    /**
     * @return Image ID
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return Minimum disks required to use image
     * 
     */
    public Double minDisk() {
        return this.minDisk;
    }
    /**
     * @return Minimum RAM required to use image
     * 
     */
    public Double minRam() {
        return this.minRam;
    }
    /**
     * @return Image name
     * 
     */
    public String name() {
        return this.name;
    }
    /**
     * @return Order plan code
     * 
     */
    public String planCode() {
        return this.planCode;
    }
    /**
     * @return Image region
     * 
     */
    public String region() {
        return this.region;
    }
    /**
     * @return Image size (in GiB)
     * 
     */
    public Double size() {
        return this.size;
    }
    /**
     * @return Image status
     * 
     */
    public String status() {
        return this.status;
    }
    /**
     * @return Tags about the image
     * 
     */
    public List<String> tags() {
        return this.tags;
    }
    /**
     * @return Image type
     * 
     */
    public String type() {
        return this.type;
    }
    /**
     * @return User to connect with
     * 
     */
    public String user() {
        return this.user;
    }
    /**
     * @return Image visibility
     * 
     */
    public String visibility() {
        return this.visibility;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetImagesImage defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String creationDate;
        private String flavorType;
        private String id;
        private Double minDisk;
        private Double minRam;
        private String name;
        private String planCode;
        private String region;
        private Double size;
        private String status;
        private List<String> tags;
        private String type;
        private String user;
        private String visibility;
        public Builder() {}
        public Builder(GetImagesImage defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.creationDate = defaults.creationDate;
    	      this.flavorType = defaults.flavorType;
    	      this.id = defaults.id;
    	      this.minDisk = defaults.minDisk;
    	      this.minRam = defaults.minRam;
    	      this.name = defaults.name;
    	      this.planCode = defaults.planCode;
    	      this.region = defaults.region;
    	      this.size = defaults.size;
    	      this.status = defaults.status;
    	      this.tags = defaults.tags;
    	      this.type = defaults.type;
    	      this.user = defaults.user;
    	      this.visibility = defaults.visibility;
        }

        @CustomType.Setter
        public Builder creationDate(String creationDate) {
            if (creationDate == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "creationDate");
            }
            this.creationDate = creationDate;
            return this;
        }
        @CustomType.Setter
        public Builder flavorType(String flavorType) {
            if (flavorType == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "flavorType");
            }
            this.flavorType = flavorType;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder minDisk(Double minDisk) {
            if (minDisk == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "minDisk");
            }
            this.minDisk = minDisk;
            return this;
        }
        @CustomType.Setter
        public Builder minRam(Double minRam) {
            if (minRam == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "minRam");
            }
            this.minRam = minRam;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder planCode(String planCode) {
            if (planCode == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "planCode");
            }
            this.planCode = planCode;
            return this;
        }
        @CustomType.Setter
        public Builder region(String region) {
            if (region == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "region");
            }
            this.region = region;
            return this;
        }
        @CustomType.Setter
        public Builder size(Double size) {
            if (size == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "size");
            }
            this.size = size;
            return this;
        }
        @CustomType.Setter
        public Builder status(String status) {
            if (status == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "status");
            }
            this.status = status;
            return this;
        }
        @CustomType.Setter
        public Builder tags(List<String> tags) {
            if (tags == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "tags");
            }
            this.tags = tags;
            return this;
        }
        public Builder tags(String... tags) {
            return tags(List.of(tags));
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "type");
            }
            this.type = type;
            return this;
        }
        @CustomType.Setter
        public Builder user(String user) {
            if (user == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "user");
            }
            this.user = user;
            return this;
        }
        @CustomType.Setter
        public Builder visibility(String visibility) {
            if (visibility == null) {
              throw new MissingRequiredPropertyException("GetImagesImage", "visibility");
            }
            this.visibility = visibility;
            return this;
        }
        public GetImagesImage build() {
            final var _resultValue = new GetImagesImage();
            _resultValue.creationDate = creationDate;
            _resultValue.flavorType = flavorType;
            _resultValue.id = id;
            _resultValue.minDisk = minDisk;
            _resultValue.minRam = minRam;
            _resultValue.name = name;
            _resultValue.planCode = planCode;
            _resultValue.region = region;
            _resultValue.size = size;
            _resultValue.status = status;
            _resultValue.tags = tags;
            _resultValue.type = type;
            _resultValue.user = user;
            _resultValue.visibility = visibility;
            return _resultValue;
        }
    }
}
