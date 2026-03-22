import { genkit, z } from "genkit";
import * as fs from "fs";
import * as path from "path";

// Initialize Genkit
const ai = genkit({});

// Define the flow for Auto-Fixing 'Mất Ly'
export const autoFixLyFlow = ai.defineFlow(
    {
        name: "autoFixLy",
        inputSchema: z.object({
            targetFile: z.string().describe("Path to the file to fix (e.g. core/loop/GiaoTiep.py)")
        }),
        outputSchema: z.object({
            success: z.boolean(),
            message: z.string(),
            replacementsCount: z.number()
        }),
    },
    async (input) => {
        try {
            const fullPath = path.resolve(__dirname, "../../", input.targetFile);
            if (!fs.existsSync(fullPath)) {
                return { success: false, message: `File not found: ${fullPath}`, replacementsCount: 0 };
            }

            let content = fs.readFileSync(fullPath, "utf-8");
            let count = 0;

            // Regex replace to intercept the CLI output prints and proxy them through AuditLogger
            // We will replace: print(f"tool[cli] exit={rc}\n{out}{err}")
            // With: _log_cli_output(loop.logger, rc, out, err); print(...)

            const beforeStr = 'print(f"tool[cli] exit={rc}\\n{out}{err}")';

            const afterStr = `loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": cmd}, policy_decision={}, state_after={}, Chung="cli-output", stop_reason=None))\n                    print(f"tool[cli] exit={rc}\\n{out}{err}")`;

            // A simple split and join for precise replacement if simple string matches
            if (content.includes(beforeStr)) {
                const parts = content.split(beforeStr);
                count = parts.length - 1;
                content = parts.join(afterStr);
                fs.writeFileSync(fullPath, content, "utf-8");
                return { success: true, message: "Fixed 'Mất Ly' via Genkit Flow!", replacementsCount: count };
            }

            return { success: true, message: "Pattern not found or already fixed.", replacementsCount: count };
        } catch (e: any) {
            return { success: false, message: e.message || String(e), replacementsCount: 0 };
        }
    }
);

// Local PoC execution instead of MCP Server for now
async function runPoC() {
    console.log("[Ops Agent] Running PoC Auto-Fix on live GiaoTiep.py...");
    const result = await autoFixLyFlow({ targetFile: "core/loop/GiaoTiep.py" });
    console.log("[Ops Agent] Result:", result);
}

runPoC();
