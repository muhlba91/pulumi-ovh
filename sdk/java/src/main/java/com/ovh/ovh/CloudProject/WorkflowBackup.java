// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.CloudProject;

import com.ovh.ovh.CloudProject.WorkflowBackupArgs;
import com.ovh.ovh.CloudProject.inputs.WorkflowBackupState;
import com.ovh.ovh.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.Integer;
import java.lang.String;
import java.util.Optional;
import javax.annotation.Nullable;

/**
 * Manage a worflow that schedules backups of public cloud instance.
 * Note that upon deletion, the workflow is deleted but any backups that have been created by this workflow are not.
 * 
 * ## Example Usage
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.ovh.CloudProject.WorkflowBackup;
 * import com.pulumi.ovh.CloudProject.WorkflowBackupArgs;
 * import java.util.List;
 * import java.util.ArrayList;
 * import java.util.Map;
 * import java.io.File;
 * import java.nio.file.Files;
 * import java.nio.file.Paths;
 * 
 * public class App {
 *     public static void main(String[] args) {
 *         Pulumi.run(App::stack);
 *     }
 * 
 *     public static void stack(Context ctx) {
 *         var myBackup = new WorkflowBackup("myBackup", WorkflowBackupArgs.builder()
 *             .cron("50 4 * * *")
 *             .instanceId("xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx")
 *             .maxExecutionCount("0")
 *             .regionName("GRA11")
 *             .rotation("7")
 *             .serviceName("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 */
@ResourceType(type="ovh:CloudProject/workflowBackup:WorkflowBackup")
public class WorkflowBackup extends com.pulumi.resources.CustomResource {
    /**
     * The name of the backup files that are created. If empty, the `name` attribute is used.
     * 
     */
    @Export(name="backupName", refs={String.class}, tree="[0]")
    private Output<String> backupName;

    /**
     * @return The name of the backup files that are created. If empty, the `name` attribute is used.
     * 
     */
    public Output<String> backupName() {
        return this.backupName;
    }
    @Export(name="createdAt", refs={String.class}, tree="[0]")
    private Output<String> createdAt;

    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * The cron periodicity at which the backup workflow is scheduled
     * 
     * * `instanceId` the id of the instance to back up
     * 
     */
    @Export(name="cron", refs={String.class}, tree="[0]")
    private Output<String> cron;

    /**
     * @return The cron periodicity at which the backup workflow is scheduled
     * 
     * * `instanceId` the id of the instance to back up
     * 
     */
    public Output<String> cron() {
        return this.cron;
    }
    @Export(name="instanceId", refs={String.class}, tree="[0]")
    private Output<String> instanceId;

    public Output<String> instanceId() {
        return this.instanceId;
    }
    /**
     * The number of times the worflow is run. Default value is `0` which means that the workflow will be scheduled continously until its deletion
     * 
     */
    @Export(name="maxExecutionCount", refs={Integer.class}, tree="[0]")
    private Output</* @Nullable */ Integer> maxExecutionCount;

    /**
     * @return The number of times the worflow is run. Default value is `0` which means that the workflow will be scheduled continously until its deletion
     * 
     */
    public Output<Optional<Integer>> maxExecutionCount() {
        return Codegen.optional(this.maxExecutionCount);
    }
    /**
     * The worflow name that is used in the UI
     * 
     */
    @Export(name="name", refs={String.class}, tree="[0]")
    private Output<String> name;

    /**
     * @return The worflow name that is used in the UI
     * 
     */
    public Output<String> name() {
        return this.name;
    }
    /**
     * The name of the openstack region.
     * 
     */
    @Export(name="regionName", refs={String.class}, tree="[0]")
    private Output<String> regionName;

    /**
     * @return The name of the openstack region.
     * 
     */
    public Output<String> regionName() {
        return this.regionName;
    }
    /**
     * The number of backup that are retained.
     * 
     */
    @Export(name="rotation", refs={Integer.class}, tree="[0]")
    private Output<Integer> rotation;

    /**
     * @return The number of backup that are retained.
     * 
     */
    public Output<Integer> rotation() {
        return this.rotation;
    }
    /**
     * The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    @Export(name="serviceName", refs={String.class}, tree="[0]")
    private Output<String> serviceName;

    /**
     * @return The id of the public cloud project. If omitted, the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public WorkflowBackup(String name) {
        this(name, WorkflowBackupArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public WorkflowBackup(String name, WorkflowBackupArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public WorkflowBackup(String name, WorkflowBackupArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:CloudProject/workflowBackup:WorkflowBackup", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()));
    }

    private WorkflowBackup(String name, Output<String> id, @Nullable WorkflowBackupState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:CloudProject/workflowBackup:WorkflowBackup", name, state, makeResourceOptions(options, id));
    }

    private static WorkflowBackupArgs makeArgs(WorkflowBackupArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? WorkflowBackupArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
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
    public static WorkflowBackup get(String name, Output<String> id, @Nullable WorkflowBackupState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new WorkflowBackup(name, id, state, options);
    }
}
