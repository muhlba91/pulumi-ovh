// *** WARNING: this file was generated by pulumi-java-gen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package com.ovhcloud.pulumi.ovh.Ip;

import com.ovhcloud.pulumi.ovh.Ip.inputs.GetFirewallArgs;
import com.ovhcloud.pulumi.ovh.Ip.inputs.GetFirewallPlainArgs;
import com.ovhcloud.pulumi.ovh.Ip.inputs.GetFirewallRuleArgs;
import com.ovhcloud.pulumi.ovh.Ip.inputs.GetFirewallRulePlainArgs;
import com.ovhcloud.pulumi.ovh.Ip.inputs.GetMitigationArgs;
import com.ovhcloud.pulumi.ovh.Ip.inputs.GetMitigationPlainArgs;
import com.ovhcloud.pulumi.ovh.Ip.inputs.GetServiceArgs;
import com.ovhcloud.pulumi.ovh.Ip.inputs.GetServicePlainArgs;
import com.ovhcloud.pulumi.ovh.Ip.outputs.GetFirewallResult;
import com.ovhcloud.pulumi.ovh.Ip.outputs.GetFirewallRuleResult;
import com.ovhcloud.pulumi.ovh.Ip.outputs.GetMitigationResult;
import com.ovhcloud.pulumi.ovh.Ip.outputs.GetServiceResult;
import com.ovhcloud.pulumi.ovh.Utilities;
import com.pulumi.core.Output;
import com.pulumi.core.TypeShape;
import com.pulumi.deployment.Deployment;
import com.pulumi.deployment.InvokeOptions;
import java.util.concurrent.CompletableFuture;

public final class IpFunctions {
    /**
     * Use this data source to retrieve information about an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallArgs;
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
     *         final var myFirewall = IpFunctions.getFirewall(GetFirewallArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetFirewallResult> getFirewall(GetFirewallArgs args) {
        return getFirewall(args, InvokeOptions.Empty);
    }
    /**
     * Use this data source to retrieve information about an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallArgs;
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
     *         final var myFirewall = IpFunctions.getFirewall(GetFirewallArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetFirewallResult> getFirewallPlain(GetFirewallPlainArgs args) {
        return getFirewallPlain(args, InvokeOptions.Empty);
    }
    /**
     * Use this data source to retrieve information about an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallArgs;
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
     *         final var myFirewall = IpFunctions.getFirewall(GetFirewallArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetFirewallResult> getFirewall(GetFirewallArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("ovh:Ip/getFirewall:getFirewall", TypeShape.of(GetFirewallResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Use this data source to retrieve information about an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallArgs;
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
     *         final var myFirewall = IpFunctions.getFirewall(GetFirewallArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetFirewallResult> getFirewallPlain(GetFirewallPlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("ovh:Ip/getFirewall:getFirewall", TypeShape.of(GetFirewallResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Use this data source to retrieve information about a rule on an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallRuleArgs;
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
     *         final var myFirewallRule = IpFunctions.getFirewallRule(GetFirewallRuleArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .sequence(0)
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetFirewallRuleResult> getFirewallRule(GetFirewallRuleArgs args) {
        return getFirewallRule(args, InvokeOptions.Empty);
    }
    /**
     * Use this data source to retrieve information about a rule on an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallRuleArgs;
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
     *         final var myFirewallRule = IpFunctions.getFirewallRule(GetFirewallRuleArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .sequence(0)
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetFirewallRuleResult> getFirewallRulePlain(GetFirewallRulePlainArgs args) {
        return getFirewallRulePlain(args, InvokeOptions.Empty);
    }
    /**
     * Use this data source to retrieve information about a rule on an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallRuleArgs;
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
     *         final var myFirewallRule = IpFunctions.getFirewallRule(GetFirewallRuleArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .sequence(0)
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetFirewallRuleResult> getFirewallRule(GetFirewallRuleArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("ovh:Ip/getFirewallRule:getFirewallRule", TypeShape.of(GetFirewallRuleResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Use this data source to retrieve information about a rule on an IP firewall.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetFirewallRuleArgs;
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
     *         final var myFirewallRule = IpFunctions.getFirewallRule(GetFirewallRuleArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnFirewall("XXXXXX")
     *             .sequence(0)
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetFirewallRuleResult> getFirewallRulePlain(GetFirewallRulePlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("ovh:Ip/getFirewallRule:getFirewallRule", TypeShape.of(GetFirewallRuleResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Use this resource to retrieve information about an IP permanent mitigation.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetMitigationArgs;
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
     *         final var mitigationData = IpFunctions.getMitigation(GetMitigationArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnMitigation("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetMitigationResult> getMitigation(GetMitigationArgs args) {
        return getMitigation(args, InvokeOptions.Empty);
    }
    /**
     * Use this resource to retrieve information about an IP permanent mitigation.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetMitigationArgs;
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
     *         final var mitigationData = IpFunctions.getMitigation(GetMitigationArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnMitigation("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetMitigationResult> getMitigationPlain(GetMitigationPlainArgs args) {
        return getMitigationPlain(args, InvokeOptions.Empty);
    }
    /**
     * Use this resource to retrieve information about an IP permanent mitigation.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetMitigationArgs;
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
     *         final var mitigationData = IpFunctions.getMitigation(GetMitigationArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnMitigation("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetMitigationResult> getMitigation(GetMitigationArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("ovh:Ip/getMitigation:getMitigation", TypeShape.of(GetMitigationResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Use this resource to retrieve information about an IP permanent mitigation.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetMitigationArgs;
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
     *         final var mitigationData = IpFunctions.getMitigation(GetMitigationArgs.builder()
     *             .ip("XXXXXX")
     *             .ipOnMitigation("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetMitigationResult> getMitigationPlain(GetMitigationPlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("ovh:Ip/getMitigation:getMitigation", TypeShape.of(GetMitigationResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Use this data source to retrieve information about an IP service.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetServiceArgs;
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
     *         final var myIp = IpFunctions.getService(GetServiceArgs.builder()
     *             .serviceName("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetServiceResult> getService(GetServiceArgs args) {
        return getService(args, InvokeOptions.Empty);
    }
    /**
     * Use this data source to retrieve information about an IP service.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetServiceArgs;
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
     *         final var myIp = IpFunctions.getService(GetServiceArgs.builder()
     *             .serviceName("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetServiceResult> getServicePlain(GetServicePlainArgs args) {
        return getServicePlain(args, InvokeOptions.Empty);
    }
    /**
     * Use this data source to retrieve information about an IP service.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetServiceArgs;
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
     *         final var myIp = IpFunctions.getService(GetServiceArgs.builder()
     *             .serviceName("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static Output<GetServiceResult> getService(GetServiceArgs args, InvokeOptions options) {
        return Deployment.getInstance().invoke("ovh:Ip/getService:getService", TypeShape.of(GetServiceResult.class), args, Utilities.withVersion(options));
    }
    /**
     * Use this data source to retrieve information about an IP service.
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
     * import com.pulumi.ovh.Ip.IpFunctions;
     * import com.pulumi.ovh.Ip.inputs.GetServiceArgs;
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
     *         final var myIp = IpFunctions.getService(GetServiceArgs.builder()
     *             .serviceName("XXXXXX")
     *             .build());
     * 
     *     }
     * }
     * }
     * </pre>
     * &lt;!--End PulumiCodeChooser --&gt;
     * 
     */
    public static CompletableFuture<GetServiceResult> getServicePlain(GetServicePlainArgs args, InvokeOptions options) {
        return Deployment.getInstance().invokeAsync("ovh:Ip/getService:getService", TypeShape.of(GetServiceResult.class), args, Utilities.withVersion(options));
    }
}
