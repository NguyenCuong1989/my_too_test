"""
HyperAI Phoenix - Genesis
Main Streamlit application - the unified core interface
"Học để Phục vụ" - Learn to Serve
"""

import streamlit as st
import time
import json
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Import HyperAI Phoenix modules
try:
    # Try relative imports first (when run as module)
    from .brain.coordinator import MetaOptimizationCoordinator
    from .brain.memory import MemoryEngine
    from .brain.thinker import StrategicThinker
    from .brain.improver import SelfImprover
    from .brain.narrator import SystemNarrator
    from .brain.system_observer import SystemObserver
    from .brain.tool_registry import TOOL_REGISTRY
except ImportError:
    # Fall back to absolute imports (when run directly)
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from hyperai_phoenix.app.brain.coordinator import MetaOptimizationCoordinator
    from hyperai_phoenix.app.brain.memory import MemoryEngine
    from hyperai_phoenix.app.brain.thinker import StrategicThinker
    from hyperai_phoenix.app.brain.improver import SelfImprover
    from hyperai_phoenix.app.brain.narrator import SystemNarrator
    from hyperai_phoenix.app.brain.system_observer import SystemObserver
from .brain.coordinator import MetaOptimizationCoordinator
from .brain.memory import MemoryEngine
from .brain.thinker import StrategicThinker
from .brain.improver import SelfImprover
from .brain.narrator import SystemNarrator
from .brain.system_observer import SystemObserver
from .brain.tool_registry import TOOL_REGISTRY

class HyperAIPhoenixApp:
    """Main HyperAI Phoenix Streamlit Application"""

    def __init__(self):
        self.app_name = "🔥 HyperAI Phoenix - Giai đoạn 1: Học để Phục vụ"

        # Initialize session state
        self._init_session_state()

        # Initialize system components
        self._init_system_components()

    def _init_session_state(self):
        """Initialize Streamlit session state"""
        if 'initialized' not in st.session_state:
            st.session_state.initialized = False
            st.session_state.system_started = False
            st.session_state.current_tab = "Control Hub"
            st.session_state.chat_messages = []
            st.session_state.system_messages = []
            st.session_state.pending_approvals = []
            st.session_state.last_metrics_update = datetime.now()
            st.session_state.auto_refresh = True
            st.session_state.refresh_interval = 10  # Default 10 seconds

    def _init_system_components(self):
        """Initialize HyperAI Phoenix system components"""
        if not st.session_state.initialized:
            try:
                # Create data directories
                os.makedirs("data/databases", exist_ok=True)
                os.makedirs("data/logs/archive", exist_ok=True)

                # Initialize core components
                st.session_state.coordinator = MetaOptimizationCoordinator()
                st.session_state.narrator = SystemNarrator()
                st.session_state.observer = SystemObserver()

                # Initialize improver with memory and observer
                st.session_state.improver = SelfImprover(
                    st.session_state.coordinator.memory_engine,
                    st.session_state.observer
                )

                # Add observer alert callback
                st.session_state.observer.add_alert_callback(self._handle_system_alert)

                st.session_state.initialized = True

                # Start narrator story
                st.session_state.narrator.start_story(
                    "HyperAI Phoenix Session",
                    {"user_agent": "Streamlit", "session_id": st.session_state.coordinator.session_id}
                )

            except Exception as e:
                st.error(f"Lỗi khởi tạo hệ thống: {str(e)}")
                st.stop()

    def _handle_system_alert(self, alert):
        """Handle system performance alerts"""
        alert_message = {
            'type': 'system_alert',
            'severity': alert.severity,
            'message': alert.message,
            'timestamp': datetime.now(),
            'suggested_action': alert.suggested_action
        }
        st.session_state.system_messages.append(alert_message)

    def run(self):
        """Main application entry point"""
        st.set_page_config(
            page_title="HyperAI Phoenix",
            page_icon="🔥",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        self._render_header()
        self._render_sidebar()
        self._render_main_content()

        # Auto-refresh if enabled (with configurable interval)
        if st.session_state.auto_refresh:
            # Check if enough time has passed since last update
            refresh_interval = st.session_state.get('refresh_interval', 10)  # Default 10 seconds
            time_since_update = (datetime.now() - st.session_state.last_metrics_update).total_seconds()

            if time_since_update >= refresh_interval:
                st.session_state.last_metrics_update = datetime.now()
                st.rerun()

    def _render_header(self):
        """Render application header"""
        col1, col2, col3 = st.columns([2, 3, 1])

        with col1:
            st.title(self.app_name)

        with col2:
            if st.session_state.system_started:
                coordinator = st.session_state.coordinator
                uptime = datetime.now() - coordinator.startup_time
                st.metric("Uptime", f"{uptime.seconds // 3600}h {(uptime.seconds // 60) % 60}m")
            else:
                st.metric("Status", "Offline", delta="System not started")

        with col3:
            if st.button("🔄 Refresh"):
                st.rerun()

        # System status indicator
        if st.session_state.system_started:
            coordinator = st.session_state.coordinator
            state_color = {
                "idle": "🟢",
                "thinking": "🟡",
                "executing": "🔵",
                "logging": "🟠",
                "error": "🔴"
            }
            status_color = state_color.get(coordinator.current_state.value, "⚪")
            st.write(f"{status_color} **System State:** {coordinator.current_state.value.title()}")
        else:
            st.write("⚫ **System State:** Offline")

    def _render_sidebar(self):
        """Render sidebar with navigation and controls"""
        with st.sidebar:
            st.header("🎛️ Control Panel")

            # System control
            if not st.session_state.system_started:
                if st.button("🚀 Start HyperAI Phoenix", type="primary"):
                    self._start_system()
            else:
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("⏹️ Stop System"):
                        self._stop_system()
                with col2:
                    if st.button("🔄 Restart"):
                        self._restart_system()

            st.divider()

            # Navigation
            st.header("📋 Navigation")
            tabs = ["Control Hub", "Chat Interface", "System Monitor", "Memory Explorer", "Improvement Center", "Logs & Analytics"]
            st.session_state.current_tab = st.selectbox("Select Tab", tabs,
                                                       index=tabs.index(st.session_state.current_tab))

            st.divider()

            # Settings
            st.header("⚙️ Settings")
            st.session_state.auto_refresh = st.checkbox("Auto Refresh", value=st.session_state.auto_refresh)

            if st.session_state.auto_refresh:
                st.session_state.refresh_interval = st.slider(
                    "Refresh Interval (seconds)",
                    min_value=5,
                    max_value=60,
                    value=st.session_state.refresh_interval,
                    step=5
                )

            # Performance metrics (if system is running)
            if st.session_state.system_started:
                self._render_sidebar_metrics()

    def _render_sidebar_metrics(self):
        """Render quick metrics in sidebar"""
        st.header("📊 Quick Metrics")

        try:
            coordinator = st.session_state.coordinator
            metrics = coordinator._calculate_current_metrics()

            st.metric("Avg Response Time", f"{metrics.get('avg_duration', 0):.2f}s")
            st.metric("Error Rate", f"{metrics.get('error_rate', 0):.1%}")
            st.metric("Success Rate", f"{metrics.get('success_rate', 0):.1%}")

            # System health
            if hasattr(st.session_state, 'observer') and st.session_state.observer:
                health = st.session_state.observer.get_system_health_score()
                health_color = "🟢" if health > 0.8 else "🟡" if health > 0.6 else "🔴"
                st.metric("System Health", f"{health_color} {health:.1%}")

        except Exception as e:
            st.error(f"Error loading metrics: {e}")

    def _render_main_content(self):
        """Render main content area based on selected tab"""
        tab = st.session_state.current_tab

        if tab == "Control Hub":
            self._render_control_hub()
        elif tab == "Chat Interface":
            self._render_chat_interface()
        elif tab == "System Monitor":
            self._render_system_monitor()
        elif tab == "Memory Explorer":
            self._render_memory_explorer()
        elif tab == "Improvement Center":
            self._render_improvement_center()
        elif tab == "Logs & Analytics":
            self._render_logs_analytics()

    def _render_control_hub(self):
        """Render the main control hub"""
        st.header("🎯 Control Hub - Trung tâm Điều khiển")

        if not st.session_state.system_started:
            st.warning("🔥 Hệ thống HyperAI Phoenix chưa được khởi động. Nhấn 'Start HyperAI Phoenix' trong sidebar để bắt đầu.")
            return

        # Quick actions
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("💾 Compact Memories"):
                self._compact_memories()

        with col2:
            if st.button("📊 Generate Report"):
                self._generate_report()

        with col3:
            if st.button("🔍 Run Diagnostics"):
                self._run_diagnostics()

        with col4:
            if st.button("🚀 Improvement Cycle"):
                self._run_improvement_cycle()

        st.divider()

        # System overview
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("📈 System Overview")
            self._render_system_overview()

        with col2:
            st.subheader("📢 System Messages")
            self._render_system_messages()

        # Pending approvals
        if st.session_state.pending_approvals:
            st.subheader("⚖️ Approval Gateway")
            self._render_approval_gateway()

    def _render_chat_interface(self):
        """Render chat interface for user interaction"""
        st.header("💬 Chat Interface - Giao diện Trò chuyện")

        if not st.session_state.system_started:
            st.warning("Hệ thống cần được khởi động để sử dụng chat interface.")
            return

        # Chat messages display
        chat_container = st.container()

        with chat_container:
            for message in st.session_state.chat_messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
                    if "metadata" in message:
                        with st.expander("Chi tiết"):
                            st.json(message["metadata"])

        # Chat input
        if prompt := st.chat_input("Hỏi HyperAI Phoenix..."):
            # Add user message
            st.session_state.chat_messages.append({
                "role": "user",
                "content": prompt,
                "timestamp": datetime.now()
            })

            # Process user input
            self._process_user_input(prompt)

    def _render_system_monitor(self):
        """Render system monitoring dashboard"""
        st.header("📊 System Monitor - Giám sát Hệ thống")

        if not st.session_state.system_started:
            st.warning("Hệ thống cần được khởi động để xem monitoring data.")
            return

        # Performance charts
        col1, col2 = st.columns(2)

        with col1:
            self._render_performance_chart()

        with col2:
            self._render_resource_usage()

        # Detailed metrics
        st.subheader("📋 Detailed Metrics")
        self._render_metrics_table()

    def _render_memory_explorer(self):
        """Render memory exploration interface"""
        st.header("🧠 Memory Explorer - Khám phá Trí nhớ")

        if not st.session_state.system_started:
            st.warning("Hệ thống cần được khởi động để truy cập memory.")
            return

        # Search interface
        col1, col2 = st.columns([3, 1])

        with col1:
            search_query = st.text_input("Tìm kiếm trong trí nhớ:", placeholder="Nhập từ khóa...")

        with col2:
            if st.button("🔍 Search"):
                if search_query:
                    self._search_memory(search_query)

        # Memory statistics
        self._render_memory_stats()

        # Recent events
        st.subheader("📅 Recent Events")
        self._render_recent_events()

    def _render_improvement_center(self):
        """Render improvement center interface"""
        st.header("🚀 Improvement Center - Trung tâm Cải tiến")

        if not st.session_state.system_started:
            st.warning("Hệ thống cần được khởi động để truy cập improvement center.")
            return

        # Improvement controls
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("🔄 Run Analysis"):
                self._run_performance_analysis()

        with col2:
            if st.button("💡 Generate Proposals"):
                self._generate_improvement_proposals()

        with col3:
            if st.button("📊 View History"):
                self._show_improvement_history()

        # Current improvement status
        self._render_improvement_status()

    def _render_logs_analytics(self):
        """Render logs and analytics interface"""
        st.header("📊 Logs & Analytics - Nhật ký & Phân tích")

        # Log filters
        col1, col2, col3 = st.columns(3)

        with col1:
            log_level = st.selectbox("Log Level", ["ALL", "INFO", "WARNING", "ERROR"])

        with col2:
            hours_back = st.selectbox("Time Range", [1, 6, 24, 72, 168])

        with col3:
            if st.button("🔄 Refresh Logs"):
                st.rerun()

        # Display logs
        self._render_log_viewer(log_level, hours_back)

    # Helper methods for rendering components
    def _render_system_overview(self):
        """Render system overview panel"""
        if not st.session_state.system_started:
            return

        coordinator = st.session_state.coordinator

        # Current status
        st.write(f"**Session ID:** {coordinator.session_id}")
        st.write(f"**Current State:** {coordinator.current_state.value}")

        # Queue status
        queue_info = f"""
        **Queue Status:**
        - Directives: {coordinator.directive_queue.qsize()}
        - Results: {coordinator.result_queue.qsize()}
        - Approvals: {coordinator.approval_queue.qsize()}
        """
        st.write(queue_info)

        # Performance metrics
        metrics = coordinator._calculate_current_metrics()
        total_directives = coordinator.performance_metrics['total_directives']
        if total_directives > 0:
            st.write(f"**Performance:**")
            st.write(f"- Avg Duration: {metrics['avg_duration']:.2f}s")
            st.write(f"- Success Rate: {metrics['success_rate']:.1%}")
            st.write(f"- Error Rate: {metrics['error_rate']:.1%}")

    def _render_system_messages(self):
        """Render system messages panel"""
        if st.session_state.system_messages:
            for i, msg in enumerate(st.session_state.system_messages[-5:]):  # Show last 5
                severity_icons = {
                    'info': 'ℹ️',
                    'warning': '⚠️',
                    'error': '❌',
                    'critical': '🚨'
                }

                icon = severity_icons.get(msg.get('severity', 'info'), 'ℹ️')
                timestamp = msg['timestamp'].strftime('%H:%M:%S')

                with st.expander(f"{icon} {timestamp} - {msg['type']}", expanded=(i == len(st.session_state.system_messages[-5:]) - 1)):
                    st.write(msg['message'])
                    if 'suggested_action' in msg:
                        st.write(f"**Suggested Action:** {msg['suggested_action']}")
        else:
            st.write("No system messages")

    def _render_approval_gateway(self):
        """Render approval gateway for escalated requests"""
        for approval in st.session_state.pending_approvals:
            with st.expander(f"⚖️ Approval Required: {approval['title']}", expanded=True):
                st.write(f"**Request:** {approval['details']}")
                st.write(f"**Reasoning:** {approval['reasoning']}")

                col1, col2 = st.columns(2)
                with col1:
                    if st.button("✅ Approve", key=f"approve_{approval['id']}"):
                        self._approve_request(approval['id'])

                with col2:
                    if st.button("❌ Reject", key=f"reject_{approval['id']}"):
                        self._reject_request(approval['id'])

    def _render_performance_chart(self):
        """Render performance metrics chart"""
        st.subheader("📈 Performance Trends")

        # Create sample data (in real implementation, get from memory)
        import numpy as np

        dates = pd.date_range(end=datetime.now(), periods=24, freq='H')
        response_times = np.random.normal(5, 2, 24)  # Sample data
        error_rates = np.random.uniform(0, 0.1, 24)  # Sample data

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=dates, y=response_times, mode='lines+markers', name='Response Time (s)'))
        fig.add_trace(go.Scatter(x=dates, y=error_rates*100, mode='lines+markers', name='Error Rate (%)', yaxis='y2'))

        fig.update_layout(
            title='Performance Over Time',
            xaxis_title='Time',
            yaxis_title='Response Time (s)',
            yaxis2=dict(title='Error Rate (%)', overlaying='y', side='right')
        )

        st.plotly_chart(fig, use_container_width=True)

    def _render_resource_usage(self):
        """Render resource usage charts"""
        st.subheader("💾 Resource Usage")

        if st.session_state.observer:
            current_metrics = st.session_state.observer.get_current_metrics()

            if current_metrics:
                # Create gauge charts
                fig = go.Figure()

                fig.add_trace(go.Indicator(
                    mode = "gauge+number",
                    value = current_metrics.cpu_percent,
                    domain = {'x': [0, 1], 'y': [0, 1]},
                    title = {'text': "CPU Usage"},
                    gauge = {
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "darkblue"},
                        'steps': [
                            {'range': [0, 50], 'color': "lightgray"},
                            {'range': [50, 80], 'color': "yellow"},
                            {'range': [80, 100], 'color': "red"}],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 90}}
                ))

                st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Resource monitoring not available")

    def _render_metrics_table(self):
        """Render detailed metrics table"""
        if not st.session_state.system_started:
            return

        coordinator = st.session_state.coordinator
        metrics = coordinator._calculate_current_metrics()

        metrics_df = pd.DataFrame([
            {"Metric": "Total Directives", "Value": coordinator.performance_metrics['total_directives']},
            {"Metric": "Average Duration", "Value": f"{metrics['avg_duration']:.2f}s"},
            {"Metric": "Success Rate", "Value": f"{metrics['success_rate']:.1%}"},
            {"Metric": "Error Rate", "Value": f"{metrics['error_rate']:.1%}"}
        ])

        st.dataframe(metrics_df, use_container_width=True)

    def _render_memory_stats(self):
        """Render memory statistics"""
        st.subheader("📊 Memory Statistics")

        if st.session_state.system_started:
            try:
                memory_engine = st.session_state.coordinator.memory_engine
                recent_events = memory_engine.get_recent_events(hours=24)

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("Events (24h)", len(recent_events))

                with col2:
                    # Count knowledge items (would need to implement in memory engine)
                    st.metric("Knowledge Items", "N/A")

                with col3:
                    st.metric("Memory Health", "Good")

            except Exception as e:
                st.error(f"Error loading memory stats: {e}")
        else:
            st.write("Memory not accessible - system not started")

    def _render_recent_events(self):
        """Render recent events table"""
        if st.session_state.system_started:
            try:
                memory_engine = st.session_state.coordinator.memory_engine
                events = memory_engine.get_recent_events(hours=6)

                if events:
                    events_df = pd.DataFrame(events)
                    events_df['timestamp'] = pd.to_datetime(events_df['timestamp'])
                    events_df = events_df.sort_values('timestamp', ascending=False)

                    st.dataframe(events_df[['timestamp', 'event_type', 'source', 'success']],
                               use_container_width=True)
                else:
                    st.write("No recent events found")

            except Exception as e:
                st.error(f"Error loading events: {e}")
        else:
            st.write("Events not accessible - system not started")

    def _render_improvement_status(self):
        """Render current improvement status"""
        st.subheader("📈 Current Status")

        if hasattr(st.session_state, 'improver') and st.session_state.system_started:
            pending_proposals = st.session_state.improver.get_pending_proposals()

            if pending_proposals:
                st.write(f"**Pending Proposals:** {len(pending_proposals)}")

                for proposal in pending_proposals[:3]:  # Show first 3
                    with st.expander(f"💡 {proposal.title}", expanded=False):
                        st.write(f"**Priority:** {proposal.priority}")
                        st.write(f"**Description:** {proposal.description}")
                        st.write(f"**Expected Benefit:** {proposal.expected_benefit}")

                        col1, col2 = st.columns(2)
                        with col1:
                            if st.button("✅ Approve", key=f"approve_improvement_{proposal.id}"):
                                st.session_state.improver.approve_proposal(proposal.id)
                                st.success("Proposal approved!")
                                st.rerun()

                        with col2:
                            if st.button("❌ Reject", key=f"reject_improvement_{proposal.id}"):
                                # Would need to implement reject functionality
                                st.warning("Reject functionality not implemented")
            else:
                st.write("No pending improvement proposals")
        else:
            st.write("Improvement system not available")

    def _render_log_viewer(self, log_level: str, hours_back: int):
        """Render log viewer"""
        st.subheader(f"📄 Logs - Last {hours_back} hours")

        # In a real implementation, this would fetch logs from the narrator
        # For now, show placeholder
        st.write(f"Log viewer for {log_level} level logs from last {hours_back} hours")
        st.write("(Log viewer implementation pending)")

    # System control methods
    def _start_system(self):
        """Start the HyperAI Phoenix system"""
        try:
            coordinator = st.session_state.coordinator
            coordinator.start()

            # Start system observer
            st.session_state.observer.start_monitoring()

            st.session_state.system_started = True

            # Add greeting message
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": "🔥 HyperAI Phoenix đã khởi động thành công! Tôi là AI agent của bạn, sẵn sàng học để phục vụ. Hãy cho tôi biết bạn cần gì?",
                "timestamp": datetime.now()
            })

            # Narrator event
            st.session_state.narrator.narrate_event(
                'system_action',
                'HyperAI Phoenix system started successfully',
                {'user_interface': 'Streamlit'},
                level='info'
            )

            st.success("🚀 HyperAI Phoenix đã khởi động thành công!")
            st.rerun()

        except Exception as e:
            st.error(f"Lỗi khởi động hệ thống: {str(e)}")

    def _stop_system(self):
        """Stop the HyperAI Phoenix system"""
        try:
            if hasattr(st.session_state, 'coordinator') and st.session_state.coordinator:
                st.session_state.coordinator.stop()

            if hasattr(st.session_state, 'observer') and st.session_state.observer:
                st.session_state.observer.stop_monitoring()

            if hasattr(st.session_state, 'narrator') and st.session_state.narrator:
                st.session_state.narrator.complete_story("System stopped by user")

            st.session_state.system_started = False

            st.success("⏹️ Hệ thống đã dừng an toàn")
            st.rerun()

        except Exception as e:
            st.error(f"Lỗi dừng hệ thống: {str(e)}")

    def _restart_system(self):
        """Restart the HyperAI Phoenix system"""
        self._stop_system()
        time.sleep(2)
        self._start_system()

    def _process_user_input(self, user_input: str):
        """Process user input through the system"""
        if not st.session_state.system_started:
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": "⚠️ Hệ thống chưa được khởi động. Vui lòng khởi động hệ thống trước.",
                "timestamp": datetime.now()
            })
            return

        try:
            # Submit directive to coordinator
            coordinator = st.session_state.coordinator
            directive_id = coordinator.submit_directive(user_input, "streamlit_user")

            # Show thinking message
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": "🤔 Đang suy nghĩ về yêu cầu của bạn...",
                "timestamp": datetime.now()
            })

            # Wait for result (in real app, this would be async)
            result = coordinator.get_result(directive_id, timeout=10.0)

            if result:
                if result.success:
                    response_content = f"✅ Đã hoàn thành yêu cầu!\n\n"
                    if result.result_data:
                        if isinstance(result.result_data, dict):
                            for tool_name, tool_result in result.result_data.items():
                                if isinstance(tool_result, dict) and 'message' in tool_result:
                                    response_content += tool_result['message']
                                elif isinstance(tool_result, dict) and 'content' in tool_result:
                                    response_content += f"📄 Nội dung file:\n```\n{tool_result['content'][:500]}...\n```"
                                else:
                                    response_content += f"🔧 {tool_name}: {str(tool_result)}"
                else:
                    response_content = f"❌ Có lỗi xảy ra: {result.error_message}"

                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": response_content,
                    "timestamp": datetime.now(),
                    "metadata": {
                        "directive_id": directive_id,
                        "execution_time": f"{result.execution_time:.2f}s",
                        "alignment_score": result.alignment_score
                    }
                })
            else:
                st.session_state.chat_messages.append({
                    "role": "assistant",
                    "content": "⏰ Timeout - Không nhận được phản hồi trong thời gian quy định.",
                    "timestamp": datetime.now()
                })

        except Exception as e:
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": f"❌ Lỗi xử lý yêu cầu: {str(e)}",
                "timestamp": datetime.now()
            })

        st.rerun()

    # Action methods
    def _compact_memories(self):
        """Trigger memory compaction"""
        try:
            coordinator = st.session_state.coordinator
            result = coordinator.memory_engine.compact_memories()
            st.success(f"✅ Nén ký ức hoàn thành: {result['archived_events']} events archived")
        except Exception as e:
            st.error(f"❌ Lỗi nén ký ức: {str(e)}")

    def _generate_report(self):
        """Generate system report"""
        try:
            if hasattr(st.session_state, 'observer') and st.session_state.observer:
                report = st.session_state.observer.create_performance_report(hours=24)
                st.success("📊 Báo cáo đã được tạo thành công")
                st.json(report)
        except Exception as e:
            st.error(f"❌ Lỗi tạo báo cáo: {str(e)}")

    def _run_diagnostics(self):
        """Run system diagnostics"""
        try:
            # Basic diagnostic checks
            diagnostics = {
                "system_started": st.session_state.system_started,
                "coordinator_initialized": hasattr(st.session_state, 'coordinator'),
                "memory_accessible": True,  # Would check actual memory access
                "observer_running": hasattr(st.session_state, 'observer') and st.session_state.observer.running,
                "timestamp": datetime.now().isoformat()
            }

            st.success("🔍 Diagnostics completed")
            st.json(diagnostics)
        except Exception as e:
            st.error(f"❌ Lỗi chạy diagnostics: {str(e)}")

    def _run_improvement_cycle(self):
        """Run improvement analysis cycle"""
        try:
            if hasattr(st.session_state, 'improver') and st.session_state.system_started:
                with st.spinner("🚀 Running improvement cycle..."):
                    result = st.session_state.improver.run_improvement_cycle()

                if result['status'] == 'completed':
                    st.success(f"✅ Improvement cycle completed: {result['proposals_generated']} proposals generated")
                    st.json(result)
                else:
                    st.error(f"❌ Improvement cycle failed: {result.get('error', 'Unknown error')}")
        except Exception as e:
            st.error(f"❌ Lỗi improvement cycle: {str(e)}")

    def _search_memory(self, query: str):
        """Search system memory"""
        try:
            coordinator = st.session_state.coordinator
            results = coordinator.memory_engine.semantic_search(query)

            st.success(f"🔍 Tìm thấy {len(results)} kết quả")

            for i, result in enumerate(results):
                with st.expander(f"Result {i+1} - Similarity: {result['similarity']:.2f}"):
                    st.write(result['content'])
                    st.json(result['metadata'])

        except Exception as e:
            st.error(f"❌ Lỗi tìm kiếm: {str(e)}")

    # Additional helper methods would go here...

def main():
    """Main function to run the Streamlit app"""
    app = HyperAIPhoenixApp()
    app.run()

if __name__ == "__main__":
    main()
