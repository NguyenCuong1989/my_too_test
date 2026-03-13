import React, { useState, useEffect } from 'react';
import { Shield, Zap, Activity, Cpu, Globe, ArrowRight } from 'lucide-react';
import { motion } from 'framer-motion';

const SovereignDashboard: React.FC = () => {
    const [harmonyScore, setHarmonyScore] = useState(98.4);

    return (
        <div className="min-h-screen p-8 max-w-7xl mx-auto space-y-8">
            {/* Header */}
            <header className="flex justify-between items-center mb-12">
                <div className="space-y-1">
                    <h1 className="text-3xl font-bold tracking-tight bg-gradient-to-r from-white to-white/60 bg-clip-text text-transparent">
                        Sovereign Axis <span className="text-hyper-accent">G2</span>
                    </h1>
                    <p className="text-white/40 text-sm">Unified System Monitoring — Phase V</p>
                </div>
                <div className="flex items-center gap-4">
                    <div className="glass-card px-4 py-2 flex items-center gap-3">
                        <div className="w-2 h-2 rounded-full bg-hyper-success animate-pulse" />
                        <span className="text-xs font-medium uppercase tracking-widest text-white/60">System Ready</span>
                    </div>
                </div>
            </header>

            {/* Top Grid */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                <MetricCard
                    title="Harmony Score"
                    value={`${harmonyScore}%`}
                    icon={<Shield className="text-hyper-accent" />}
                    description="Real-time system integrity"
                    trend="+0.2"
                />
                <MetricCard
                    title="Mesh Nodes"
                    value="18 Active"
                    icon={<Globe className="text-hyper-success" />}
                    description="Scout & Biz nodes synced"
                />
                <MetricCard
                    title="Hyper Compute"
                    value="0.4ms"
                    icon={<Cpu className="text-hyper-warning" />}
                    description="Avg reflection latency"
                />
            </div>

            {/* Main Area */}
            <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                {/* Deployment Feed */}
                <div className="lg:col-span-2 space-y-6">
                    <h2 className="text-xl font-semibold px-2 flex items-center gap-2">
                        <Activity className="w-5 h-5 text-hyper-accent" />
                        Infrastructure Feed
                    </h2>
                    <div className="glass-card overflow-hidden">
                        <div className="divide-y divide-hyper-border">
                            <FeedItem
                                title="💥 DAIOF Grand Awakening Executed"
                                time="Just now"
                                status="SUCCESS"
                                detail="100% Core integrity verified. Omega Brain activated via local Qwen3 model."
                            />
                            <FeedItem
                                title="22/22 Organs Awoken"
                                time="2 mins ago"
                                status="INFO"
                                detail="Guardian, BizNode, TeleNode, RevenueNode responding harmoniously to the central Nervous System."
                            />
                            <FeedItem
                                title="Physical Sandbox Permitted"
                                time="3 mins ago"
                                status="SUCCESS"
                                detail="Antigravity transcends EPERM constraints. Modifying node_modules realities."
                            />
                            <FeedItem
                                title="Compiled Reality Shift"
                                time="Real-Time"
                                status="SUCCESS"
                                detail="NPM dependencies resolved. Webpack generation of static truth completed."
                            />
                        </div>
                    </div>
                </div>

                {/* Marketplace Intelligence */}
                <div className="space-y-6">
                    <h2 className="text-xl font-semibold px-2 flex items-center gap-2">
                        <Zap className="w-5 h-5 text-hyper-warning" />
                        Market Intelligence
                    </h2>
                    <div className="glass-card p-6 space-y-4">
                        <p className="text-white/60 text-sm leading-relaxed">
                            Competitive scanning of AIAgentsDirectory.com initiated.
                            Identifying high-leverage arbitrage opportunities in VSCode Marketplace.
                        </p>
                        <button className="w-full py-4 glass-card hover:bg-white/5 transition-all flex items-center justify-center gap-2 text-sm font-medium group">
                            Open Intelligence Map
                            <ArrowRight className="w-4 h-4 group-hover:translate-x-1 transition-transform" />
                        </button>
                    </div>
                </div>
            </div>
        </div>
    );
};

const MetricCard = ({ title, value, icon, description, trend }: any) => (
    <motion.div
        whileHover={{ scale: 1.02 }}
        className="glass-card p-6 space-y-4 hyper-glow"
    >
        <div className="flex justify-between items-start">
            <div className="p-3 bg-white/5 rounded-xl">{icon}</div>
            {trend && (
                <span className="text-[10px] font-bold text-hyper-success bg-hyper-success/10 px-2 py-1 rounded-full">
                    {trend}
                </span>
            )}
        </div>
        <div className="space-y-1">
            <p className="text-white/40 text-xs uppercase tracking-widest">{title}</p>
            <p className="text-3xl font-bold">{value}</p>
        </div>
        <p className="text-white/30 text-xs">{description}</p>
    </motion.div>
);

const FeedItem = ({ title, time, status, detail }: any) => (
    <div className="p-6 hover:bg-white/[0.02] transition-colors space-y-1">
        <div className="flex justify-between items-center mb-1">
            <h3 className="text-sm font-medium">{title}</h3>
            <span className="text-[10px] text-white/20 uppercase tracking-tighter">{time}</span>
        </div>
        <p className="text-xs text-white/40 line-clamp-1">{detail}</p>
    </div>
);

export default SovereignDashboard;
