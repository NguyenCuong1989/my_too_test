import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useQuery } from "@tanstack/react-query";
import { apiRequest } from "@/lib/queryClient";

interface Snapshot {
    system: {
        mode: string;
        simulation: boolean;
        ax_enabled: boolean;
        shell_enabled: boolean;
    };
    input: {
        raw: string | null;
        type: string;
    };
    intent: {
        kind: string;
        value: string | null;
        source: string;
    };
    ui: {
        requires_confirm: boolean;
        prompt: string | null;
        suggestions: string[];
    };
    audit: {
        timestamp: string;
        Chung: string;
        recorded: boolean;
        error?: string;
    };
    decision: {
        verdict: string;
        command: string | null;
    };
    execution: {
        executed: boolean;
        executor: string;
        result: string | null;
    };
    stop: {
        reason: string;
        message: string | null;
    };
}

export function DashboardView() {
    const { data: snapshot, isLoading } = useQuery<Snapshot>({
        queryKey: ["/chat"],
        queryFn: async () => {
            const res = await apiRequest("POST", "/chat", { text: "status?" });
            return res.json();
        },
        refetchInterval: 1000,
    });

    if (isLoading) return <div className="p-8 text-center animate-pulse">Scanning Reality...</div>;

    return (
        <div className="p-6 space-y-6 animate-in fade-in duration-500">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {/* State Card: THẾ */}
                <Card className="border-primary/20 shadow-lg bg-secondary/10">
                    <CardHeader>
                        <CardTitle className="text-xs font-bold tracking-widest uppercase text-muted-foreground">
                            Thế (System State)
                        </CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="text-3xl font-mono font-bold text-primary">
                            {snapshot?.system.mode.toUpperCase() || "IDLE"}
                        </div>
                        <div className="text-[10px] mt-2 font-mono opacity-50 truncate">
                            HASH: {snapshot?.audit.Chung || "UNSIGNED"}
                        </div>
                    </CardContent>
                </Card>

                {/* Stop Card */}
                <Card className="border-primary/20 shadow-lg bg-secondary/10">
                    <CardHeader>
                        <CardTitle className="text-xs font-bold tracking-widest uppercase text-muted-foreground">
                            Stop State
                        </CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="space-y-1">
                            <div className="text-sm font-bold">{snapshot?.stop.reason || "NONE"}</div>
                            <div className="text-xs opacity-70 truncate">{snapshot?.stop.message || "No message"}</div>
                        </div>
                    </CardContent>
                </Card>

                {/* UI Hint Card */}
                <Card className="border-primary/20 shadow-lg bg-secondary/10">
                    <CardHeader>
                        <CardTitle className="text-xs font-bold tracking-widest uppercase text-muted-foreground">
                            UI Hints
                        </CardTitle>
                    </CardHeader>
                    <CardContent>
                        <div className="space-y-1">
                            <div className="text-sm font-bold">
                                Confirm: {snapshot?.ui.requires_confirm ? "YES" : "NO"}
                            </div>
                            <div className="text-xs opacity-70 truncate">{snapshot?.ui.prompt || "No prompt"}</div>
                        </div>
                    </CardContent>
                </Card>
            </div>

            {/* Decision Block: PHÁN */}
            <Card className={`border-l-4 ${snapshot?.decision?.verdict === "ALLOW" ? "border-l-emerald-500" : "border-l-destructive"}`}>
                <CardContent className="py-4">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-2 text-sm">
                        <div>
                            <span className="text-xs font-bold uppercase mr-2">Verdict:</span>
                            <span className={`font-mono font-bold ${snapshot?.decision?.verdict === "ALLOW" ? "text-emerald-500" : "text-destructive"}`}>
                                {snapshot?.decision?.verdict || "IDLE"}
                            </span>
                        </div>
                        <div className="font-mono text-xs truncate">Command: {snapshot?.decision?.command || "None"}</div>
                        <div className="font-mono text-xs truncate">Executor: {snapshot?.execution?.executor || "NONE"}</div>
                        <div className="font-mono text-xs truncate">Recorded: {snapshot?.audit?.recorded ? "true" : "false"}</div>
                        <div className="font-mono text-xs truncate col-span-1 md:col-span-2">
                            Input: {snapshot?.input?.raw || "(none)"} [{snapshot?.input?.type || "NONE"}]
                        </div>
                    </div>
                </CardContent>
            </Card>
        </div>
    );
}
