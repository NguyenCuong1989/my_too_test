import { Switch, Route } from "wouter";
import { useState } from "react";
import { queryClient } from "./lib/queryClient";
import { QueryClientProvider } from "@tanstack/react-query";
import { Toaster } from "@/components/ui/toaster";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";

function LoginView({ onSuccess }: { onSuccess: () => void }) {
  const [user, setUser] = useState("");
  const [pass, setPass] = useState("");
  const [error, setError] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (user === "admin" && pass === "admin") {
      setError("");
      onSuccess();
    } else {
      setError("Invalid credentials");
    }
  };

  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-background p-6">
      <Card className="w-full max-w-md border-border shadow-sm">
        <CardContent className="pt-6 space-y-4">
          <div className="space-y-1 text-center">
            <p className="text-sm font-medium tracking-wider uppercase text-muted-foreground">
              AXCONTROL ACCESS
            </p>
            <h1 className="text-2xl font-bold">Sign in</h1>
          </div>
          <form className="space-y-4" onSubmit={handleSubmit}>
            <div className="space-y-2">
              <Label htmlFor="user">Username</Label>
              <Input
                id="user"
                value={user}
                onChange={(e) => setUser(e.target.value)}
                placeholder="admin"
                autoComplete="username"
              />
            </div>
            <div className="space-y-2">
              <Label htmlFor="pass">Password</Label>
              <Input
                id="pass"
                type="password"
                value={pass}
                onChange={(e) => setPass(e.target.value)}
                placeholder="admin"
                autoComplete="current-password"
              />
            </div>
            {error && (
              <p className="text-sm text-destructive" role="alert">
                {error}
              </p>
            )}
            <Button className="w-full" size="lg" type="submit">
              Enter
            </Button>
          </form>
        </CardContent>
      </Card>
    </div>
  );
}

function Home() {
  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center p-6 bg-background">
      <div className="w-full max-w-md space-y-8 animate-in fade-in slide-in-from-bottom-4 duration-700">
        
        {/* Header Section */}
        <div className="space-y-2 text-center">
          <div className="inline-block px-3 py-1 mb-4 text-xs font-medium tracking-wider uppercase border border-border bg-secondary/50 rounded-sm">
            Local-First Template
          </div>
          <h1 className="text-4xl md:text-5xl font-bold tracking-tighter">
            Hello, World.
          </h1>
          <p className="text-muted-foreground text-lg leading-relaxed max-w-[80%] mx-auto">
            A minimal skeleton for orchestrated builds.
          </p>
        </div>

        {/* Content Card */}
        <Card className="border-border shadow-sm">
          <CardContent className="pt-6 space-y-4">
            <div className="grid gap-2">
              <div className="flex items-center gap-3 p-3 rounded-md bg-secondary/30">
                <div className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
                <span className="text-sm font-medium">System Operational</span>
              </div>
              <div className="flex items-center gap-3 p-3 rounded-md bg-secondary/30">
                <div className="h-2 w-2 rounded-full bg-blue-500" />
                <span className="text-sm font-medium">Mobile-First Ready</span>
              </div>
              <div className="flex items-center gap-3 p-3 rounded-md bg-secondary/30">
                <div className="h-2 w-2 rounded-full bg-orange-500" />
                <span className="text-sm font-medium">Local Environment</span>
              </div>
            </div>
            
            <div className="pt-4 flex gap-3">
              <Button className="w-full font-medium" size="lg">
                Get Started
              </Button>
              <Button variant="outline" className="w-full font-medium" size="lg">
                Documentation
              </Button>
            </div>
          </CardContent>
        </Card>

        {/* Footer */}
        <div className="text-center text-xs text-muted-foreground pt-8">
          <p>v1.0.0 • Mobile-First Tool-Orchestrated Build Method</p>
        </div>
      </div>
    </div>
  );
}

function NotFound() {
  return (
    <div className="min-h-screen w-full flex items-center justify-center bg-background p-4">
      <Card className="w-full max-w-md border-border">
        <CardContent className="pt-6 text-center space-y-4">
          <h1 className="text-2xl font-bold text-destructive">404 Page Not Found</h1>
          <p className="text-muted-foreground">The requested resource is missing.</p>
        </CardContent>
      </Card>
    </div>
  );
}

function Router() {
  return (
    <Switch>
      <Route path="/" component={Home} />
      <Route component={NotFound} />
    </Switch>
  );
}

function App() {
  const [authed, setAuthed] = useState(false);

  return (
    <QueryClientProvider client={queryClient}>
      {authed ? <Router /> : <LoginView onSuccess={() => setAuthed(true)} />}
      <Toaster />
    </QueryClientProvider>
  );
}

export default App;
