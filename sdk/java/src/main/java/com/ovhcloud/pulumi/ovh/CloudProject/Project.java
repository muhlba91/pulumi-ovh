// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.CloudProject;

import com.ovhcloud.pulumi.ovh.CloudProject.ProjectArgs;
import com.ovhcloud.pulumi.ovh.CloudProject.inputs.ProjectState;
import com.ovhcloud.pulumi.ovh.CloudProject.outputs.ProjectOrder;
import com.ovhcloud.pulumi.ovh.CloudProject.outputs.ProjectPlan;
import com.ovhcloud.pulumi.ovh.CloudProject.outputs.ProjectPlanOption;
import com.ovhcloud.pulumi.ovh.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.List;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * ## Import
 * 
 * Cloud project can be imported using the `project_id`.
 * 
 * Using the following configuration:
 * 
 * terraform
 * 
 * import {
 * 
 *   to = ovh_cloud_project.my_cloud_project
 * 
 *   id = &#34;&lt;project ID&gt;&#34;
 * 
 * }
 * 
 * You can then run:
 * 
 * bash
 * 
 * $ pulumi preview -generate-config-out=cloudproject.tf
 * 
 * $ pulumi up
 * 
 * The file `cloudproject.tf` will then contain the imported resource&#39;s configuration, that can be copied next to the `import` block above. See https://developer.hashicorp.com/terraform/language/import/generating-configuration for more details.
 * 
 */
@ResourceType(type="ovh:CloudProject/project:Project")
public class Project extends com.pulumi.resources.CustomResource {
    /**
     * The URN of the cloud project
     * 
     */
    @Export(name="ProjectURN", refs={String.class}, tree="[0]")
    private Output<String> ProjectURN;

    /**
     * @return The URN of the cloud project
     * 
     */
    public Output<String> ProjectURN() {
        return this.ProjectURN;
    }
    @Export(name="access", refs={String.class}, tree="[0]")
    private Output<String> access;

    public Output<String> access() {
        return this.access;
    }
    /**
     * A description associated with the user.
     * 
     */
    @Export(name="description", refs={String.class}, tree="[0]")
    private Output<String> description;

    /**
     * @return A description associated with the user.
     * 
     */
    public Output<String> description() {
        return this.description;
    }
    /**
     * Details about the order that was used to create the public cloud project
     * 
     */
    @Export(name="orders", refs={List.class,ProjectOrder.class}, tree="[0,1]")
    private Output<List<ProjectOrder>> orders;

    /**
     * @return Details about the order that was used to create the public cloud project
     * 
     */
    public Output<List<ProjectOrder>> orders() {
        return this.orders;
    }
    /**
     * OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     * 
     */
    @Export(name="ovhSubsidiary", refs={String.class}, tree="[0]")
    private Output<String> ovhSubsidiary;

    /**
     * @return OVHcloud Subsidiary. Country of OVHcloud legal entity you&#39;ll be billed by. List of supported subsidiaries available on API at [/1.0/me.json under `models.nichandle.OvhSubsidiaryEnum`](https://eu.api.ovh.com/1.0/me.json)
     * 
     */
    public Output<String> ovhSubsidiary() {
        return this.ovhSubsidiary;
    }
    /**
     * Ovh payment mode
     * 
     * @deprecated
     * This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used.
     * 
     */
    @Deprecated /* This field is not anymore used since the API has been deprecated in favor of /payment/mean. Now, the default payment mean is used. */
    @Export(name="paymentMean", refs={String.class}, tree="[0]")
    private Output</* @Nullable */ String> paymentMean;

    /**
     * @return Ovh payment mode
     * 
     */
    public Output<Optional<String>> paymentMean() {
        return Codegen.optional(this.paymentMean);
    }
    /**
     * Product Plan to order
     * 
     */
    @Export(name="plan", refs={ProjectPlan.class}, tree="[0]")
    private Output<ProjectPlan> plan;

    /**
     * @return Product Plan to order
     * 
     */
    public Output<ProjectPlan> plan() {
        return this.plan;
    }
    /**
     * Product Plan to order
     * 
     */
    @Export(name="planOptions", refs={List.class,ProjectPlanOption.class}, tree="[0,1]")
    private Output</* @Nullable */ List<ProjectPlanOption>> planOptions;

    /**
     * @return Product Plan to order
     * 
     */
    public Output<Optional<List<ProjectPlanOption>>> planOptions() {
        return Codegen.optional(this.planOptions);
    }
    /**
     * openstack project id
     * 
     */
    @Export(name="projectId", refs={String.class}, tree="[0]")
    private Output<String> projectId;

    /**
     * @return openstack project id
     * 
     */
    public Output<String> projectId() {
        return this.projectId;
    }
    /**
     * openstack project name
     * 
     */
    @Export(name="projectName", refs={String.class}, tree="[0]")
    private Output<String> projectName;

    /**
     * @return openstack project name
     * 
     */
    public Output<String> projectName() {
        return this.projectName;
    }
    /**
     * project status
     * 
     */
    @Export(name="status", refs={String.class}, tree="[0]")
    private Output<String> status;

    /**
     * @return project status
     * 
     */
    public Output<String> status() {
        return this.status;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public Project(java.lang.String name) {
        this(name, ProjectArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public Project(java.lang.String name, @Nullable ProjectArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public Project(java.lang.String name, @Nullable ProjectArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:CloudProject/project:Project", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()), false);
    }

    private Project(java.lang.String name, Output<java.lang.String> id, @Nullable ProjectState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:CloudProject/project:Project", name, state, makeResourceOptions(options, id), false);
    }

    private static ProjectArgs makeArgs(@Nullable ProjectArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? ProjectArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<java.lang.String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .build();
        return com.pulumi.resources.CustomResourceOptions.merge(defaultOptions, options, id);
    }

    /**
     * Get an existing Host resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state
     * @param options Optional settings to control the behavior of the CustomResource.
     */
    public static Project get(java.lang.String name, Output<java.lang.String> id, @Nullable ProjectState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new Project(name, id, state, options);
    }
}
