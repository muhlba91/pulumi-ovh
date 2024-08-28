// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.CloudProject.inputs;

import com.pulumi.core.Output;
import com.pulumi.core.annotations.Import;
import com.pulumi.exceptions.MissingRequiredPropertyException;
import java.lang.String;
import java.util.List;
import java.util.Map;
import java.util.Objects;


public final class KubeNodePoolTemplateMetadataArgs extends com.pulumi.resources.ResourceArgs {

    public static final KubeNodePoolTemplateMetadataArgs Empty = new KubeNodePoolTemplateMetadataArgs();

    /**
     * annotations
     * 
     */
    @Import(name="annotations", required=true)
    private Output<Map<String,String>> annotations;

    /**
     * @return annotations
     * 
     */
    public Output<Map<String,String>> annotations() {
        return this.annotations;
    }

    /**
     * finalizers
     * 
     */
    @Import(name="finalizers", required=true)
    private Output<List<String>> finalizers;

    /**
     * @return finalizers
     * 
     */
    public Output<List<String>> finalizers() {
        return this.finalizers;
    }

    /**
     * labels
     * 
     */
    @Import(name="labels", required=true)
    private Output<Map<String,String>> labels;

    /**
     * @return labels
     * 
     */
    public Output<Map<String,String>> labels() {
        return this.labels;
    }

    private KubeNodePoolTemplateMetadataArgs() {}

    private KubeNodePoolTemplateMetadataArgs(KubeNodePoolTemplateMetadataArgs $) {
        this.annotations = $.annotations;
        this.finalizers = $.finalizers;
        this.labels = $.labels;
    }

    public static Builder builder() {
        return new Builder();
    }
    public static Builder builder(KubeNodePoolTemplateMetadataArgs defaults) {
        return new Builder(defaults);
    }

    public static final class Builder {
        private KubeNodePoolTemplateMetadataArgs $;

        public Builder() {
            $ = new KubeNodePoolTemplateMetadataArgs();
        }

        public Builder(KubeNodePoolTemplateMetadataArgs defaults) {
            $ = new KubeNodePoolTemplateMetadataArgs(Objects.requireNonNull(defaults));
        }

        /**
         * @param annotations annotations
         * 
         * @return builder
         * 
         */
        public Builder annotations(Output<Map<String,String>> annotations) {
            $.annotations = annotations;
            return this;
        }

        /**
         * @param annotations annotations
         * 
         * @return builder
         * 
         */
        public Builder annotations(Map<String,String> annotations) {
            return annotations(Output.of(annotations));
        }

        /**
         * @param finalizers finalizers
         * 
         * @return builder
         * 
         */
        public Builder finalizers(Output<List<String>> finalizers) {
            $.finalizers = finalizers;
            return this;
        }

        /**
         * @param finalizers finalizers
         * 
         * @return builder
         * 
         */
        public Builder finalizers(List<String> finalizers) {
            return finalizers(Output.of(finalizers));
        }

        /**
         * @param finalizers finalizers
         * 
         * @return builder
         * 
         */
        public Builder finalizers(String... finalizers) {
            return finalizers(List.of(finalizers));
        }

        /**
         * @param labels labels
         * 
         * @return builder
         * 
         */
        public Builder labels(Output<Map<String,String>> labels) {
            $.labels = labels;
            return this;
        }

        /**
         * @param labels labels
         * 
         * @return builder
         * 
         */
        public Builder labels(Map<String,String> labels) {
            return labels(Output.of(labels));
        }

        public KubeNodePoolTemplateMetadataArgs build() {
            if ($.annotations == null) {
                throw new MissingRequiredPropertyException("KubeNodePoolTemplateMetadataArgs", "annotations");
            }
            if ($.finalizers == null) {
                throw new MissingRequiredPropertyException("KubeNodePoolTemplateMetadataArgs", "finalizers");
            }
            if ($.labels == null) {
                throw new MissingRequiredPropertyException("KubeNodePoolTemplateMetadataArgs", "labels");
            }
            return $;
        }
    }

}
