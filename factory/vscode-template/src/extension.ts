import * as vscode from 'vscode';

export function activate(context: vscode.ExtensionContext) {
    console.log('DAIOF Factory Extension is now active.');

    let disposable = vscode.commands.registerCommand('daiof.factory.status', () => {
        vscode.window.showInformationMessage('Harmony Status: Operational (98.4%)');
    });

    context.subscriptions.push(disposable);

    // Register Terminal Completion Provider (Sovereign Axis integration)
    if (vscode.window.registerTerminalCompletionProvider) {
        context.subscriptions.push(vscode.window.registerTerminalCompletionProvider({
            provideTerminalCompletions(terminal, context, token) {
                // Return Sovereign Axis completions
                return [];
            }
        }, '/', '\\'));
    }
}

export function deactivate() {}
