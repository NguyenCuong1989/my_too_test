import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { useQuery } from "@tanstack/react-query";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";

interface AuditRecord {
    timestamp: number;
    Chung: string;
    intent: string;
    command: string;
    verdict: string;
}

export function AuditTracerView() {
    const { data: records } = useQuery<AuditRecord[]>({
        queryKey: ["/api/audit"], // Placeholder for audit stream
        refetchInterval: 5000,
    });

    return (
        <div className="p-6 space-y-6 animate-in slide-in-from-right duration-500">
            <Card className="border-primary/20 shadow-xl">
                <CardHeader>
                    <CardTitle className="text-lg font-bold tracking-tight">
                        ChuỗiChứng (Karma Chain)
                    </CardTitle>
                </CardHeader>
                <CardContent>
                    <Table>
                        <TableHeader>
                            <TableRow>
                                <TableHead className="w-[100px]">Thời Gian</TableHead>
                                <TableHead>Ý Định (Intent)</TableHead>
                                <TableHead>Lệnh (Command)</TableHead>
                                <TableHead>Kết Quả</TableHead>
                                <TableHead className="text-right font-mono">Chung Hash</TableHead>
                            </TableRow>
                        </TableHeader>
                        <TableBody>
                            {records?.map((record, i) => (
                                <TableRow key={i}>
                                    <TableCell className="text-xs opacity-60">
                                        {new Date(record.timestamp * 1000).toLocaleTimeString()}
                                    </TableCell>
                                    <TableCell className="font-medium text-sm">{record.intent}</TableCell>
                                    <TableCell className="font-mono text-xs bg-secondary/20 p-1 rounded">
                                        {record.command}
                                    </TableCell>
                                    <TableCell>
                                        <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${record.verdict === "ALLOW" ? "bg-emerald-500/10 text-emerald-500" : "bg-destructive/10 text-destructive"
                                            }`}>
                                            {record.verdict}
                                        </span>
                                    </TableCell>
                                    <TableCell className="text-right font-mono text-[10px] opacity-40">
                                        {record.Chung.slice(0, 12)}...
                                    </TableCell>
                                </TableRow>
                            )) || (
                                    <TableRow>
                                        <TableCell colSpan={5} className="text-center py-12 opacity-50 italic">
                                            Chưa có nhật ký thực thi...
                                        </TableCell>
                                    </TableRow>
                                )}
                        </TableBody>
                    </Table>
                </CardContent>
            </Card>
        </div>
    );
}
