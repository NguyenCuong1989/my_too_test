import { useState } from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { apiRequest } from "@/lib/queryClient";

export function CommandCenter() {
    const [input, setInput] = useState("");
    const queryClient = useQueryClient();

    const mutation = useMutation({
        mutationFn: async (text: string) => {
            const res = await apiRequest("POST", "/chat", { text });
            return res.json();
        },
        onSuccess: (snapshot) => {
            setInput("");
            queryClient.setQueryData(["/chat"], snapshot);
        },
    });

    const handleSend = () => {
        if (!input.trim() || mutation.isPending) return;
        mutation.mutate(input);
    };

    return (
        <div className="fixed bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-background via-background to-transparent">
            <div className="max-w-4xl mx-auto">
                <Card className="border-primary shadow-2xl bg-background/80 backdrop-blur-md">
                    <CardContent className="p-2 flex gap-2">
                        <Input
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            onKeyDown={(e) => e.key === "Enter" && handleSend()}
                            placeholder="Nhập Ý Định (Intent) hoặc Lệnh (Command)..."
                            className="border-none focus-visible:ring-0 text-lg font-medium"
                            disabled={mutation.isPending}
                        />
                        <Button
                            onClick={handleSend}
                            disabled={mutation.isPending || !input.trim()}
                            className="px-8 font-bold"
                        >
                            {mutation.isPending ? "ĐANG GỬI..." : "LUÂN CHUYỂN"}
                        </Button>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
