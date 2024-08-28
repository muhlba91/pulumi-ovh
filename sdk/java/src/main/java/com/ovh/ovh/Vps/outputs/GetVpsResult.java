// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.Vps.outputs;

import com.pulumi.core.annotations.CustomType;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.Boolean;
import java.lang.Integer;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;

@CustomType
public final class GetVpsResult {
    /**
     * @return The URN of the vps
     * 
     */
    private String VpsURN;
    /**
     * @return The OVHcloud cluster the vps is in
     * 
     */
    private String cluster;
    /**
     * @return The datacenter in which the vps is located
     * 
     */
    private Map<String,String> datacenter;
    /**
     * @return The displayed name in the OVHcloud web admin
     * 
     */
    private String displayname;
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    private String id;
    /**
     * @return The list of IPs addresses attached to the vps
     * 
     */
    private List<String> ips;
    /**
     * @return The keymap for the ip kvm, valid values &#34;&#34;, &#34;fr&#34;, &#34;us&#34;
     * 
     */
    private String keymap;
    /**
     * @return The amount of memory in MB of the vps.
     * 
     */
    private Integer memory;
    /**
     * @return A dict describing the type of vps.
     * 
     */
    private Map<String,String> model;
    private String name;
    /**
     * @return The source of the boot kernel
     * 
     */
    private String netbootmode;
    /**
     * @return The type of offer (ssd, cloud, classic)
     * 
     */
    private String offertype;
    private String serviceName;
    /**
     * @return A boolean to indicate if OVHcloud SLA monitoring is active.
     * 
     */
    private Boolean slamonitoring;
    /**
     * @return The state of the vps
     * 
     */
    private String state;
    /**
     * @return The type of server
     * 
     */
    private String type;
    /**
     * @return The number of vcore of the vps
     * 
     */
    private Integer vcore;
    /**
     * @return The OVHcloud zone where the vps is
     * 
     */
    private String zone;

    private GetVpsResult() {}
    /**
     * @return The URN of the vps
     * 
     */
    public String VpsURN() {
        return this.VpsURN;
    }
    /**
     * @return The OVHcloud cluster the vps is in
     * 
     */
    public String cluster() {
        return this.cluster;
    }
    /**
     * @return The datacenter in which the vps is located
     * 
     */
    public Map<String,String> datacenter() {
        return this.datacenter;
    }
    /**
     * @return The displayed name in the OVHcloud web admin
     * 
     */
    public String displayname() {
        return this.displayname;
    }
    /**
     * @return The provider-assigned unique ID for this managed resource.
     * 
     */
    public String id() {
        return this.id;
    }
    /**
     * @return The list of IPs addresses attached to the vps
     * 
     */
    public List<String> ips() {
        return this.ips;
    }
    /**
     * @return The keymap for the ip kvm, valid values &#34;&#34;, &#34;fr&#34;, &#34;us&#34;
     * 
     */
    public String keymap() {
        return this.keymap;
    }
    /**
     * @return The amount of memory in MB of the vps.
     * 
     */
    public Integer memory() {
        return this.memory;
    }
    /**
     * @return A dict describing the type of vps.
     * 
     */
    public Map<String,String> model() {
        return this.model;
    }
    public String name() {
        return this.name;
    }
    /**
     * @return The source of the boot kernel
     * 
     */
    public String netbootmode() {
        return this.netbootmode;
    }
    /**
     * @return The type of offer (ssd, cloud, classic)
     * 
     */
    public String offertype() {
        return this.offertype;
    }
    public String serviceName() {
        return this.serviceName;
    }
    /**
     * @return A boolean to indicate if OVHcloud SLA monitoring is active.
     * 
     */
    public Boolean slamonitoring() {
        return this.slamonitoring;
    }
    /**
     * @return The state of the vps
     * 
     */
    public String state() {
        return this.state;
    }
    /**
     * @return The type of server
     * 
     */
    public String type() {
        return this.type;
    }
    /**
     * @return The number of vcore of the vps
     * 
     */
    public Integer vcore() {
        return this.vcore;
    }
    /**
     * @return The OVHcloud zone where the vps is
     * 
     */
    public String zone() {
        return this.zone;
    }

    public static Builder builder() {
        return new Builder();
    }

    public static Builder builder(GetVpsResult defaults) {
        return new Builder(defaults);
    }
    @CustomType.Builder
    public static final class Builder {
        private String VpsURN;
        private String cluster;
        private Map<String,String> datacenter;
        private String displayname;
        private String id;
        private List<String> ips;
        private String keymap;
        private Integer memory;
        private Map<String,String> model;
        private String name;
        private String netbootmode;
        private String offertype;
        private String serviceName;
        private Boolean slamonitoring;
        private String state;
        private String type;
        private Integer vcore;
        private String zone;
        public Builder() {}
        public Builder(GetVpsResult defaults) {
    	      Objects.requireNonNull(defaults);
    	      this.VpsURN = defaults.VpsURN;
    	      this.cluster = defaults.cluster;
    	      this.datacenter = defaults.datacenter;
    	      this.displayname = defaults.displayname;
    	      this.id = defaults.id;
    	      this.ips = defaults.ips;
    	      this.keymap = defaults.keymap;
    	      this.memory = defaults.memory;
    	      this.model = defaults.model;
    	      this.name = defaults.name;
    	      this.netbootmode = defaults.netbootmode;
    	      this.offertype = defaults.offertype;
    	      this.serviceName = defaults.serviceName;
    	      this.slamonitoring = defaults.slamonitoring;
    	      this.state = defaults.state;
    	      this.type = defaults.type;
    	      this.vcore = defaults.vcore;
    	      this.zone = defaults.zone;
        }

        @CustomType.Setter
        public Builder VpsURN(String VpsURN) {
            if (VpsURN == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "VpsURN");
            }
            this.VpsURN = VpsURN;
            return this;
        }
        @CustomType.Setter
        public Builder cluster(String cluster) {
            if (cluster == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "cluster");
            }
            this.cluster = cluster;
            return this;
        }
        @CustomType.Setter
        public Builder datacenter(Map<String,String> datacenter) {
            if (datacenter == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "datacenter");
            }
            this.datacenter = datacenter;
            return this;
        }
        @CustomType.Setter
        public Builder displayname(String displayname) {
            if (displayname == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "displayname");
            }
            this.displayname = displayname;
            return this;
        }
        @CustomType.Setter
        public Builder id(String id) {
            if (id == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "id");
            }
            this.id = id;
            return this;
        }
        @CustomType.Setter
        public Builder ips(List<String> ips) {
            if (ips == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "ips");
            }
            this.ips = ips;
            return this;
        }
        public Builder ips(String... ips) {
            return ips(List.of(ips));
        }
        @CustomType.Setter
        public Builder keymap(String keymap) {
            if (keymap == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "keymap");
            }
            this.keymap = keymap;
            return this;
        }
        @CustomType.Setter
        public Builder memory(Integer memory) {
            if (memory == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "memory");
            }
            this.memory = memory;
            return this;
        }
        @CustomType.Setter
        public Builder model(Map<String,String> model) {
            if (model == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "model");
            }
            this.model = model;
            return this;
        }
        @CustomType.Setter
        public Builder name(String name) {
            if (name == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "name");
            }
            this.name = name;
            return this;
        }
        @CustomType.Setter
        public Builder netbootmode(String netbootmode) {
            if (netbootmode == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "netbootmode");
            }
            this.netbootmode = netbootmode;
            return this;
        }
        @CustomType.Setter
        public Builder offertype(String offertype) {
            if (offertype == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "offertype");
            }
            this.offertype = offertype;
            return this;
        }
        @CustomType.Setter
        public Builder serviceName(String serviceName) {
            if (serviceName == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "serviceName");
            }
            this.serviceName = serviceName;
            return this;
        }
        @CustomType.Setter
        public Builder slamonitoring(Boolean slamonitoring) {
            if (slamonitoring == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "slamonitoring");
            }
            this.slamonitoring = slamonitoring;
            return this;
        }
        @CustomType.Setter
        public Builder state(String state) {
            if (state == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "state");
            }
            this.state = state;
            return this;
        }
        @CustomType.Setter
        public Builder type(String type) {
            if (type == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "type");
            }
            this.type = type;
            return this;
        }
        @CustomType.Setter
        public Builder vcore(Integer vcore) {
            if (vcore == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "vcore");
            }
            this.vcore = vcore;
            return this;
        }
        @CustomType.Setter
        public Builder zone(String zone) {
            if (zone == null) {
              throw new MissingRequiredPropertyException("GetVpsResult", "zone");
            }
            this.zone = zone;
            return this;
        }
        public GetVpsResult build() {
            final var _resultValue = new GetVpsResult();
            _resultValue.VpsURN = VpsURN;
            _resultValue.cluster = cluster;
            _resultValue.datacenter = datacenter;
            _resultValue.displayname = displayname;
            _resultValue.id = id;
            _resultValue.ips = ips;
            _resultValue.keymap = keymap;
            _resultValue.memory = memory;
            _resultValue.model = model;
            _resultValue.name = name;
            _resultValue.netbootmode = netbootmode;
            _resultValue.offertype = offertype;
            _resultValue.serviceName = serviceName;
            _resultValue.slamonitoring = slamonitoring;
            _resultValue.state = state;
            _resultValue.type = type;
            _resultValue.vcore = vcore;
            _resultValue.zone = zone;
            return _resultValue;
        }
    }
}
