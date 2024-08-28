// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovh.ovh.CloudProjectDatabase;

import com.ovh.ovh.CloudProjectDatabase.LogSubscriptionArgs;
import com.ovh.ovh.CloudProjectDatabase.inputs.LogSubscriptionState;
import com.ovh.ovh.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.annotations.Export;
import com.pulumi.core.annotations.ResourceType;
import com.pulumi.core.internal.Codegen;
import java.lang.String;
import java.util.List;
import javax.annotation.Nullable;

/**
 * Creates a log subscrition for a cluster associated with a public cloud project.
 * 
 * ## Example Usage
 * 
 * Create a log subscription for a database.
 * 
 * &lt;!--Start PulumiCodeChooser --&gt;
 * <pre>
 * {@code
 * package generated_program;
 * 
 * import com.pulumi.Context;
 * import com.pulumi.Pulumi;
 * import com.pulumi.core.Output;
 * import com.pulumi.ovh.Dbaas.DbaasFunctions;
 * import com.pulumi.ovh.Dbaas.inputs.GetLogsOutputGraylogStreamArgs;
 * import com.pulumi.ovh.CloudProjectDatabase.CloudProjectDatabaseFunctions;
 * import com.pulumi.ovh.CloudProjectDatabase.inputs.GetDatabaseArgs;
 * import com.pulumi.ovh.CloudProjectDatabase.LogSubscription;
 * import com.pulumi.ovh.CloudProjectDatabase.LogSubscriptionArgs;
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
 *         final var stream = DbaasFunctions.getLogsOutputGraylogStream(GetLogsOutputGraylogStreamArgs.builder()
 *             .serviceName("ldp-xx-xxxxx")
 *             .title("my stream")
 *             .build());
 * 
 *         final var db = CloudProjectDatabaseFunctions.getDatabase(GetDatabaseArgs.builder()
 *             .serviceName("XXX")
 *             .engine("YYY")
 *             .id("ZZZ")
 *             .build());
 * 
 *         var subscription = new LogSubscription("subscription", LogSubscriptionArgs.builder()
 *             .serviceName(db.applyValue(getDatabaseResult -> getDatabaseResult.serviceName()))
 *             .engine(db.applyValue(getDatabaseResult -> getDatabaseResult.engine()))
 *             .clusterId(db.applyValue(getDatabaseResult -> getDatabaseResult.id()))
 *             .streamId(stream.applyValue(getLogsOutputGraylogStreamResult -> getLogsOutputGraylogStreamResult.id()))
 *             .build());
 * 
 *     }
 * }
 * }
 * </pre>
 * &lt;!--End PulumiCodeChooser --&gt;
 * 
 * ## Import
 * 
 * OVHcloud Managed clusters logs subscription can be imported using the `service_name`, `engine`, `cluster_id` and `id` of the subscription, separated by &#34;/&#34; E.g.,
 * 
 * bash
 * 
 * ```sh
 * $ pulumi import ovh:CloudProjectDatabase/logSubscription:LogSubscription sub service_name/engine/cluster_id/id
 * ```
 * 
 */
@ResourceType(type="ovh:CloudProjectDatabase/logSubscription:LogSubscription")
public class LogSubscription extends com.pulumi.resources.CustomResource {
    /**
     * Cluster ID.
     * 
     */
    @Export(name="clusterId", refs={String.class}, tree="[0]")
    private Output<String> clusterId;

    /**
     * @return Cluster ID.
     * 
     */
    public Output<String> clusterId() {
        return this.clusterId;
    }
    /**
     * Creation date of the subscription.
     * 
     */
    @Export(name="createdAt", refs={String.class}, tree="[0]")
    private Output<String> createdAt;

    /**
     * @return Creation date of the subscription.
     * 
     */
    public Output<String> createdAt() {
        return this.createdAt;
    }
    /**
     * The database engine for which you want to manage a subscription. To get a full list of available engine visit.
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     * 
     */
    @Export(name="engine", refs={String.class}, tree="[0]")
    private Output<String> engine;

    /**
     * @return The database engine for which you want to manage a subscription. To get a full list of available engine visit.
     * [public documentation](https://docs.ovh.com/gb/en/publiccloud/databases).
     * 
     */
    public Output<String> engine() {
        return this.engine;
    }
    /**
     * Log kind name of this subscription.
     * 
     */
    @Export(name="kind", refs={String.class}, tree="[0]")
    private Output<String> kind;

    /**
     * @return Log kind name of this subscription.
     * 
     */
    public Output<String> kind() {
        return this.kind;
    }
    /**
     * Name of the destination log service.
     * 
     */
    @Export(name="ldpServiceName", refs={String.class}, tree="[0]")
    private Output<String> ldpServiceName;

    /**
     * @return Name of the destination log service.
     * 
     */
    public Output<String> ldpServiceName() {
        return this.ldpServiceName;
    }
    /**
     * Identifier of the operation.
     * 
     */
    @Export(name="operationId", refs={String.class}, tree="[0]")
    private Output<String> operationId;

    /**
     * @return Identifier of the operation.
     * 
     */
    public Output<String> operationId() {
        return this.operationId;
    }
    /**
     * Name of subscribed resource, where the logs come from.
     * 
     */
    @Export(name="resourceName", refs={String.class}, tree="[0]")
    private Output<String> resourceName;

    /**
     * @return Name of subscribed resource, where the logs come from.
     * 
     */
    public Output<String> resourceName() {
        return this.resourceName;
    }
    /**
     * Type of subscribed resource, where the logs come from.
     * 
     */
    @Export(name="resourceType", refs={String.class}, tree="[0]")
    private Output<String> resourceType;

    /**
     * @return Type of subscribed resource, where the logs come from.
     * 
     */
    public Output<String> resourceType() {
        return this.resourceType;
    }
    /**
     * The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    @Export(name="serviceName", refs={String.class}, tree="[0]")
    private Output<String> serviceName;

    /**
     * @return The id of the public cloud project. If omitted,
     * the `OVH_CLOUD_PROJECT_SERVICE` environment variable is used.
     * 
     */
    public Output<String> serviceName() {
        return this.serviceName;
    }
    /**
     * Id of the target Log data platform stream.
     * 
     */
    @Export(name="streamId", refs={String.class}, tree="[0]")
    private Output<String> streamId;

    /**
     * @return Id of the target Log data platform stream.
     * 
     */
    public Output<String> streamId() {
        return this.streamId;
    }
    /**
     * Last update date of the subscription.
     * 
     */
    @Export(name="updatedAt", refs={String.class}, tree="[0]")
    private Output<String> updatedAt;

    /**
     * @return Last update date of the subscription.
     * 
     */
    public Output<String> updatedAt() {
        return this.updatedAt;
    }

    /**
     *
     * @param name The _unique_ name of the resulting resource.
     */
    public LogSubscription(String name) {
        this(name, LogSubscriptionArgs.Empty);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     */
    public LogSubscription(String name, LogSubscriptionArgs args) {
        this(name, args, null);
    }
    /**
     *
     * @param name The _unique_ name of the resulting resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param options A bag of options that control this resource's behavior.
     */
    public LogSubscription(String name, LogSubscriptionArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:CloudProjectDatabase/logSubscription:LogSubscription", name, makeArgs(args, options), makeResourceOptions(options, Codegen.empty()));
    }

    private LogSubscription(String name, Output<String> id, @Nullable LogSubscriptionState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        super("ovh:CloudProjectDatabase/logSubscription:LogSubscription", name, state, makeResourceOptions(options, id));
    }

    private static LogSubscriptionArgs makeArgs(LogSubscriptionArgs args, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        if (options != null && options.getUrn().isPresent()) {
            return null;
        }
        return args == null ? LogSubscriptionArgs.Empty : args;
    }

    private static com.pulumi.resources.CustomResourceOptions makeResourceOptions(@Nullable com.pulumi.resources.CustomResourceOptions options, @Nullable Output<String> id) {
        var defaultOptions = com.pulumi.resources.CustomResourceOptions.builder()
            .version(Utilities.getVersion())
            .additionalSecretOutputs(List.of(
                "ldpServiceName"
            ))
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
    public static LogSubscription get(String name, Output<String> id, @Nullable LogSubscriptionState state, @Nullable com.pulumi.resources.CustomResourceOptions options) {
        return new LogSubscription(name, id, state, options);
    }
}
