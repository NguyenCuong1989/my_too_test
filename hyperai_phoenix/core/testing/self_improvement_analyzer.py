#!/usr/bin/env python3
"""
HyperAI Phoenix - Integrated Self-Improvement Analyzer
======================================================

Analyzes testing results and system performance to provide actionable
improvement recommendations, integrated with HyperAI Phoenix architecture.
"""

import os
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
import statistics

# Import HyperAI Phoenix components
try:
    from ..subconscious.memory_engine import MemoryEngine
    from ..utils.logging_utils import get_logger
except ImportError:
    pass

from .experiment_runner import ExperimentReport

@dataclass
class ImprovementRecommendation:
    """Represents a specific improvement recommendation"""
    id: str
    category: str
    priority: str  # high, medium, low
    title: str
    description: str
    expected_impact: float  # 0-100 scale
    implementation_effort: str  # low, medium, high
    target_metrics: List[str]
    timestamp: str

@dataclass
class PerformanceTrend:
    """Represents a performance trend over time"""
    metric_name: str
    trend_direction: str  # improving, declining, stable
    trend_strength: float  # 0-1 scale
    recent_values: List[float]
    historical_average: float
    significance: str  # significant, moderate, minimal

class SelfImprovementAnalyzer:
    """Analyzes system performance and generates actionable improvement recommendations"""

    def __init__(self, output_dir: str = None):
        # Default output directory within HyperAI structure
        if output_dir is None:
            output_dir = os.path.join(os.path.dirname(__file__), "../../../data/analysis_results")

        self.output_dir = output_dir
        self.logger = self._setup_logging()

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # HyperAI Phoenix memory integration
        self.memory_engine = None
        try:
            self.memory_engine = MemoryEngine()
            self.logger.info("✅ HyperAI Phoenix memory integration enabled")
        except:
            self.logger.info("⚠️ Running in standalone mode")

        # Analysis configuration
        self.config = {
            "trend_analysis_window": 10,  # Number of recent reports to analyze
            "significance_threshold": 0.1,  # Minimum change to be considered significant
            "recommendation_confidence_threshold": 0.7,
            "performance_targets": {
                "success_rate": 95.0,
                "average_score": 90.0,
                "api_efficiency": 2.0,  # API calls per test
                "execution_time": 1.0   # Seconds per test
            }
        }

        self.logger.info("🔍 Self-Improvement Analyzer initialized")

    def _setup_logging(self) -> logging.Logger:
        """Setup analyzer logging"""
        try:
            return get_logger(f"self_improvement_analyzer_{id(self)}")
        except:
            logger = logging.getLogger(f"self_improvement_analyzer_{id(self)}")
            logger.setLevel(logging.INFO)
            return logger

    def analyze_experiment_results(self, reports: List[ExperimentReport]) -> Dict[str, Any]:
        """Comprehensive analysis of experiment results with improvement recommendations"""

        if not reports:
            return {"error": "No experiment reports provided for analysis"}

        self.logger.info(f"🔍 Analyzing {len(reports)} experiment reports...")

        analysis_results = {
            "analysis_timestamp": datetime.now().isoformat(),
            "reports_analyzed": len(reports),
            "performance_analysis": {},
            "trend_analysis": {},
            "recommendations": [],
            "priority_actions": [],
            "improvement_opportunities": {}
        }

        try:
            # 1. Performance Analysis
            performance_analysis = self._analyze_performance_metrics(reports)
            analysis_results["performance_analysis"] = performance_analysis

            # 2. Trend Analysis
            trend_analysis = self._analyze_performance_trends(reports)
            analysis_results["trend_analysis"] = trend_analysis

            # 3. Category-specific Analysis
            category_analysis = self._analyze_category_performance(reports)
            analysis_results["category_analysis"] = category_analysis

            # 4. Generate Recommendations
            recommendations = self._generate_improvement_recommendations(
                performance_analysis, trend_analysis, category_analysis
            )
            analysis_results["recommendations"] = [asdict(r) for r in recommendations]

            # 5. Identify Priority Actions
            priority_actions = self._identify_priority_actions(recommendations)
            analysis_results["priority_actions"] = priority_actions

            # 6. Calculate Improvement Opportunities
            improvement_opportunities = self._calculate_improvement_opportunities(
                performance_analysis, self.config["performance_targets"]
            )
            analysis_results["improvement_opportunities"] = improvement_opportunities

            # 7. Generate Insights and Patterns
            insights = self._generate_insights(reports, performance_analysis, trend_analysis)
            analysis_results["insights"] = insights

            # Store analysis in HyperAI memory
            self._store_analysis_in_memory(analysis_results)

            # Save analysis to file
            self._save_analysis_results(analysis_results)

            self.logger.info(f"✅ Analysis completed with {len(recommendations)} recommendations")

        except Exception as e:
            self.logger.error(f"❌ Analysis failed: {e}")
            analysis_results["error"] = str(e)

        return analysis_results

    def _analyze_performance_metrics(self, reports: List[ExperimentReport]) -> Dict[str, Any]:
        """Analyze key performance metrics across reports"""

        if not reports:
            return {}

        # Extract metrics from all reports
        success_rates = [(r.successful_tests / r.total_tests * 100) for r in reports]
        average_scores = [r.average_score for r in reports]
        api_efficiencies = [(r.total_api_calls / r.total_tests) for r in reports]
        execution_times = [(r.total_execution_time / r.total_tests) for r in reports]

        # Calculate statistics
        performance_metrics = {
            "success_rate": {
                "current": success_rates[-1] if success_rates else 0,
                "average": statistics.mean(success_rates) if success_rates else 0,
                "std_dev": statistics.stdev(success_rates) if len(success_rates) > 1 else 0,
                "min": min(success_rates) if success_rates else 0,
                "max": max(success_rates) if success_rates else 0,
                "target": self.config["performance_targets"]["success_rate"],
                "meets_target": success_rates[-1] >= self.config["performance_targets"]["success_rate"] if success_rates else False
            },
            "average_score": {
                "current": average_scores[-1] if average_scores else 0,
                "average": statistics.mean(average_scores) if average_scores else 0,
                "std_dev": statistics.stdev(average_scores) if len(average_scores) > 1 else 0,
                "min": min(average_scores) if average_scores else 0,
                "max": max(average_scores) if average_scores else 0,
                "target": self.config["performance_targets"]["average_score"],
                "meets_target": average_scores[-1] >= self.config["performance_targets"]["average_score"] if average_scores else False
            },
            "api_efficiency": {
                "current": api_efficiencies[-1] if api_efficiencies else 0,
                "average": statistics.mean(api_efficiencies) if api_efficiencies else 0,
                "std_dev": statistics.stdev(api_efficiencies) if len(api_efficiencies) > 1 else 0,
                "min": min(api_efficiencies) if api_efficiencies else 0,
                "max": max(api_efficiencies) if api_efficiencies else 0,
                "target": self.config["performance_targets"]["api_efficiency"],
                "meets_target": api_efficiencies[-1] <= self.config["performance_targets"]["api_efficiency"] if api_efficiencies else False
            },
            "execution_time": {
                "current": execution_times[-1] if execution_times else 0,
                "average": statistics.mean(execution_times) if execution_times else 0,
                "std_dev": statistics.stdev(execution_times) if len(execution_times) > 1 else 0,
                "min": min(execution_times) if execution_times else 0,
                "max": max(execution_times) if execution_times else 0,
                "target": self.config["performance_targets"]["execution_time"],
                "meets_target": execution_times[-1] <= self.config["performance_targets"]["execution_time"] if execution_times else False
            }
        }

        # Calculate overall performance score
        targets_met = sum(1 for metric in performance_metrics.values() if metric.get("meets_target", False))
        overall_performance_score = (targets_met / len(performance_metrics)) * 100

        performance_metrics["overall"] = {
            "performance_score": overall_performance_score,
            "targets_met": targets_met,
            "total_targets": len(performance_metrics),
            "performance_grade": self._calculate_performance_grade(overall_performance_score)
        }

        return performance_metrics

    def _analyze_performance_trends(self, reports: List[ExperimentReport]) -> Dict[str, PerformanceTrend]:
        """Analyze performance trends over time"""

        if len(reports) < 3:  # Need at least 3 points for trend analysis
            return {}

        # Extract time series data
        success_rates = [(r.successful_tests / r.total_tests * 100) for r in reports]
        average_scores = [r.average_score for r in reports]
        api_efficiencies = [(r.total_api_calls / r.total_tests) for r in reports]
        execution_times = [(r.total_execution_time / r.total_tests) for r in reports]

        trends = {}

        # Analyze each metric trend
        for metric_name, values in [
            ("success_rate", success_rates),
            ("average_score", average_scores),
            ("api_efficiency", api_efficiencies),
            ("execution_time", execution_times)
        ]:
            trend = self._calculate_trend(metric_name, values)
            trends[metric_name] = trend

        return {metric: asdict(trend) for metric, trend in trends.items()}

    def _analyze_category_performance(self, reports: List[ExperimentReport]) -> Dict[str, Any]:
        """Analyze performance by test category"""

        if not reports:
            return {}

        # Aggregate category performance across all reports
        all_categories = set()
        for report in reports:
            all_categories.update(report.categories_performance.keys())

        category_analysis = {}

        for category in all_categories:
            category_scores = []
            for report in reports:
                if category in report.categories_performance:
                    category_scores.append(report.categories_performance[category])

            if category_scores:
                category_analysis[category] = {
                    "current_score": category_scores[-1],
                    "average_score": statistics.mean(category_scores),
                    "best_score": max(category_scores),
                    "worst_score": min(category_scores),
                    "improvement": category_scores[-1] - category_scores[0] if len(category_scores) > 1 else 0,
                    "consistency": 100 - (statistics.stdev(category_scores) if len(category_scores) > 1 else 0),
                    "performance_level": self._assess_category_performance(category_scores[-1])
                }

        # Identify best and worst performing categories
        sorted_categories = sorted(
            category_analysis.items(),
            key=lambda x: x[1]["current_score"],
            reverse=True
        )

        return {
            "categories": category_analysis,
            "best_performing": sorted_categories[:3] if sorted_categories else [],
            "worst_performing": sorted_categories[-3:] if sorted_categories else [],
            "needs_attention": [cat for cat, data in category_analysis.items() if data["current_score"] < 70]
        }

    def _generate_improvement_recommendations(self, performance_analysis: Dict[str, Any],
                                           trend_analysis: Dict[str, Any],
                                           category_analysis: Dict[str, Any]) -> List[ImprovementRecommendation]:
        """Generate specific improvement recommendations based on analysis"""

        recommendations = []
        timestamp = datetime.now().isoformat()

        # Performance-based recommendations
        for metric, data in performance_analysis.items():
            if metric == "overall":
                continue

            if not data.get("meets_target", False):
                rec = self._create_performance_recommendation(metric, data, timestamp)
                if rec:
                    recommendations.append(rec)

        # Trend-based recommendations
        for metric, trend_data in trend_analysis.items():
            if trend_data["trend_direction"] == "declining" and trend_data["significance"] in ["significant", "moderate"]:
                rec = self._create_trend_recommendation(metric, trend_data, timestamp)
                if rec:
                    recommendations.append(rec)

        # Category-based recommendations
        if "needs_attention" in category_analysis:
            for category in category_analysis["needs_attention"]:
                rec = self._create_category_recommendation(category, category_analysis["categories"][category], timestamp)
                if rec:
                    recommendations.append(rec)

        # Sort recommendations by priority and expected impact
        recommendations.sort(key=lambda x: (
            {"high": 3, "medium": 2, "low": 1}[x.priority],
            x.expected_impact
        ), reverse=True)

        return recommendations

    def _calculate_trend(self, metric_name: str, values: List[float]) -> PerformanceTrend:
        """Calculate trend for a specific metric"""

        if len(values) < 3:
            return PerformanceTrend(
                metric_name=metric_name,
                trend_direction="unknown",
                trend_strength=0.0,
                recent_values=values,
                historical_average=statistics.mean(values) if values else 0,
                significance="minimal"
            )

        # Calculate trend using linear regression (simple slope)
        n = len(values)
        x = list(range(n))
        x_mean = statistics.mean(x)
        y_mean = statistics.mean(values)

        numerator = sum((x[i] - x_mean) * (values[i] - y_mean) for i in range(n))
        denominator = sum((x[i] - x_mean) ** 2 for i in range(n))

        slope = numerator / denominator if denominator != 0 else 0

        # Determine trend direction and strength
        trend_strength = abs(slope) / (y_mean if y_mean != 0 else 1)

        if slope > self.config["significance_threshold"]:
            trend_direction = "improving"
        elif slope < -self.config["significance_threshold"]:
            trend_direction = "declining"
        else:
            trend_direction = "stable"

        # Determine significance
        if trend_strength > 0.1:
            significance = "significant"
        elif trend_strength > 0.05:
            significance = "moderate"
        else:
            significance = "minimal"

        return PerformanceTrend(
            metric_name=metric_name,
            trend_direction=trend_direction,
            trend_strength=trend_strength,
            recent_values=values[-5:],  # Last 5 values
            historical_average=statistics.mean(values),
            significance=significance
        )

    def _create_performance_recommendation(self, metric: str, data: Dict[str, Any], timestamp: str) -> Optional[ImprovementRecommendation]:
        """Create a recommendation based on performance metrics"""

        current = data["current"]
        target = data["target"]
        gap = abs(target - current)

        if metric == "success_rate":
            return ImprovementRecommendation(
                id=f"perf_success_rate_{int(datetime.now().timestamp())}",
                category="performance",
                priority="high" if gap > 10 else "medium",
                title="Improve Success Rate",
                description=f"Current success rate ({current:.1f}%) is below target ({target:.1f}%). "
                          f"Focus on error handling and edge case management.",
                expected_impact=min(gap * 2, 100),
                implementation_effort="medium",
                target_metrics=["success_rate", "error_handling"],
                timestamp=timestamp
            )
        elif metric == "average_score":
            return ImprovementRecommendation(
                id=f"perf_avg_score_{int(datetime.now().timestamp())}",
                category="performance",
                priority="high" if gap > 15 else "medium",
                title="Enhance Average Score Performance",
                description=f"Current average score ({current:.1f}) is below target ({target:.1f}). "
                          f"Optimize algorithms and decision-making processes.",
                expected_impact=min(gap * 1.5, 100),
                implementation_effort="high",
                target_metrics=["average_score", "algorithm_efficiency"],
                timestamp=timestamp
            )
        elif metric == "api_efficiency":
            return ImprovementRecommendation(
                id=f"perf_api_eff_{int(datetime.now().timestamp())}",
                category="efficiency",
                priority="medium",
                title="Optimize API Usage",
                description=f"Current API calls per test ({current:.2f}) exceed target ({target:.2f}). "
                          f"Implement better caching and experience reuse.",
                expected_impact=min((current - target) * 20, 100),
                implementation_effort="medium",
                target_metrics=["api_efficiency", "caching_effectiveness"],
                timestamp=timestamp
            )
        elif metric == "execution_time":
            return ImprovementRecommendation(
                id=f"perf_exec_time_{int(datetime.now().timestamp())}",
                category="performance",
                priority="medium" if gap > 1 else "low",
                title="Improve Execution Speed",
                description=f"Current execution time per test ({current:.2f}s) exceeds target ({target:.2f}s). "
                          f"Optimize processing algorithms and reduce computational overhead.",
                expected_impact=min(gap * 30, 100),
                implementation_effort="high",
                target_metrics=["execution_time", "algorithm_optimization"],
                timestamp=timestamp
            )

        return None

    def _create_trend_recommendation(self, metric: str, trend_data: Dict[str, Any], timestamp: str) -> Optional[ImprovementRecommendation]:
        """Create a recommendation based on declining trends"""

        trend_strength = trend_data["trend_strength"]
        significance = trend_data["significance"]

        priority = "high" if significance == "significant" else "medium" if significance == "moderate" else "low"

        return ImprovementRecommendation(
            id=f"trend_{metric}_{int(datetime.now().timestamp())}",
            category="trend_correction",
            priority=priority,
            title=f"Address Declining {metric.replace('_', ' ').title()} Trend",
            description=f"Detected {significance} declining trend in {metric}. "
                      f"Trend strength: {trend_strength:.3f}. Investigate root causes and implement corrective measures.",
            expected_impact=min(trend_strength * 100, 100),
            implementation_effort="medium",
            target_metrics=[metric, "trend_stabilization"],
            timestamp=timestamp
        )

    def _create_category_recommendation(self, category: str, data: Dict[str, Any], timestamp: str) -> Optional[ImprovementRecommendation]:
        """Create a recommendation for underperforming categories"""

        current_score = data["current_score"]

        return ImprovementRecommendation(
            id=f"category_{category}_{int(datetime.now().timestamp())}",
            category="capability_improvement",
            priority="medium" if current_score < 50 else "low",
            title=f"Improve {category.replace('_', ' ').title()} Performance",
            description=f"Category '{category}' shows low performance ({current_score:.1f}). "
                      f"Focus on domain-specific optimizations and capability enhancements.",
            expected_impact=min((80 - current_score) * 1.2, 100),
            implementation_effort="medium",
            target_metrics=[f"{category}_performance", "capability_score"],
            timestamp=timestamp
        )

    def _identify_priority_actions(self, recommendations: List[ImprovementRecommendation]) -> List[Dict[str, Any]]:
        """Identify the highest priority actions from recommendations"""

        # Filter high priority recommendations
        high_priority = [r for r in recommendations if r.priority == "high"]

        # Sort by expected impact
        high_priority.sort(key=lambda x: x.expected_impact, reverse=True)

        priority_actions = []
        for rec in high_priority[:5]:  # Top 5 priority actions
            priority_actions.append({
                "title": rec.title,
                "description": rec.description,
                "expected_impact": rec.expected_impact,
                "implementation_effort": rec.implementation_effort,
                "target_metrics": rec.target_metrics
            })

        return priority_actions

    def _calculate_improvement_opportunities(self, performance_analysis: Dict[str, Any],
                                          targets: Dict[str, float]) -> Dict[str, Any]:
        """Calculate potential improvement opportunities"""

        opportunities = {}

        for metric, target in targets.items():
            if metric in performance_analysis:
                current = performance_analysis[metric]["current"]

                if metric in ["success_rate", "average_score"]:
                    # Higher is better
                    potential_gain = max(0, target - current)
                    improvement_percentage = (potential_gain / current) * 100 if current > 0 else 0
                else:
                    # Lower is better (api_efficiency, execution_time)
                    potential_gain = max(0, current - target)
                    improvement_percentage = (potential_gain / current) * 100 if current > 0 else 0

                opportunities[metric] = {
                    "current_value": current,
                    "target_value": target,
                    "potential_gain": potential_gain,
                    "improvement_percentage": improvement_percentage,
                    "opportunity_level": self._assess_opportunity_level(improvement_percentage)
                }

        return opportunities

    def _generate_insights(self, reports: List[ExperimentReport],
                         performance_analysis: Dict[str, Any],
                         trend_analysis: Dict[str, Any]) -> List[str]:
        """Generate insights and patterns from the analysis"""

        insights = []

        # Performance insights
        overall_score = performance_analysis.get("overall", {}).get("performance_score", 0)
        if overall_score >= 80:
            insights.append("System demonstrates strong overall performance across key metrics")
        elif overall_score >= 60:
            insights.append("System shows moderate performance with room for targeted improvements")
        else:
            insights.append("System requires significant performance improvements across multiple areas")

        # Trend insights
        improving_trends = [metric for metric, data in trend_analysis.items()
                          if data.get("trend_direction") == "improving"]
        declining_trends = [metric for metric, data in trend_analysis.items()
                          if data.get("trend_direction") == "declining"]

        if improving_trends:
            insights.append(f"Positive trends detected in: {', '.join(improving_trends)}")

        if declining_trends:
            insights.append(f"Concerning declining trends in: {', '.join(declining_trends)}")

        # Consistency insights
        if len(reports) >= 5:
            recent_scores = [r.average_score for r in reports[-5:]]
            score_std = statistics.stdev(recent_scores) if len(recent_scores) > 1 else 0

            if score_std < 5:
                insights.append("System demonstrates high consistency in performance")
            elif score_std > 15:
                insights.append("System shows high variability - investigate stability issues")

        return insights

    def _store_analysis_in_memory(self, analysis_results: Dict[str, Any]):
        """Store analysis results in HyperAI Phoenix memory"""

        if not self.memory_engine:
            return

        try:
            # Store as a post-mortem analysis
            self.memory_engine.store_post_mortem({
                "type": "performance_analysis",
                "analysis_summary": self._extract_analysis_summary(analysis_results),
                "recommendations_count": len(analysis_results.get("recommendations", [])),
                "performance_grade": analysis_results.get("performance_analysis", {}).get("overall", {}).get("performance_grade", "unknown"),
                "timestamp": analysis_results["analysis_timestamp"]
            })

            self.logger.info("💾 Analysis results stored in HyperAI memory")

        except Exception as e:
            self.logger.warning(f"Failed to store analysis in memory: {e}")

    def _save_analysis_results(self, analysis_results: Dict[str, Any]):
        """Save analysis results to file"""

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save detailed JSON analysis
        analysis_file = f"{self.output_dir}/self_analysis_{timestamp}_analysis.json"
        with open(analysis_file, 'w') as f:
            json.dump(analysis_results, f, indent=2, default=str)

        # Generate markdown summary
        summary_file = f"{self.output_dir}/self_analysis_{timestamp}_summary.md"
        self._generate_analysis_markdown(analysis_results, summary_file)

        self.logger.info(f"📄 Analysis saved: {analysis_file}")
        self.logger.info(f"📋 Summary saved: {summary_file}")

    def _generate_analysis_markdown(self, analysis_results: Dict[str, Any], filename: str):
        """Generate markdown summary of analysis"""

        with open(filename, 'w') as f:
            f.write("# HyperAI Phoenix - Self-Improvement Analysis\\n\\n")
            f.write(f"**Analysis Date:** {analysis_results['analysis_timestamp']}\\n")
            f.write(f"**Reports Analyzed:** {analysis_results['reports_analyzed']}\\n\\n")

            # Performance Summary
            if "performance_analysis" in analysis_results:
                perf = analysis_results["performance_analysis"]
                f.write("## 📊 Performance Analysis\\n\\n")

                overall = perf.get("overall", {})
                f.write(f"**Overall Performance Score:** {overall.get('performance_score', 0):.1f}%\\n")
                f.write(f"**Performance Grade:** {overall.get('performance_grade', 'Unknown')}\\n")
                f.write(f"**Targets Met:** {overall.get('targets_met', 0)}/{overall.get('total_targets', 0)}\\n\\n")

            # Recommendations
            if "recommendations" in analysis_results:
                recommendations = analysis_results["recommendations"]
                f.write(f"## 💡 Improvement Recommendations ({len(recommendations)})\\n\\n")

                high_priority = [r for r in recommendations if r["priority"] == "high"]
                medium_priority = [r for r in recommendations if r["priority"] == "medium"]

                if high_priority:
                    f.write("### High Priority\\n\\n")
                    for rec in high_priority:
                        f.write(f"- **{rec['title']}**: {rec['description']}\\n")
                        f.write(f"  - Expected Impact: {rec['expected_impact']:.1f}%\\n")
                        f.write(f"  - Implementation Effort: {rec['implementation_effort']}\\n\\n")

                if medium_priority:
                    f.write("### Medium Priority\\n\\n")
                    for rec in medium_priority[:3]:  # Show top 3 medium priority
                        f.write(f"- **{rec['title']}**: {rec['description']}\\n\\n")

            # Insights
            if "insights" in analysis_results:
                insights = analysis_results["insights"]
                f.write("## 🔍 Key Insights\\n\\n")
                for insight in insights:
                    f.write(f"- {insight}\\n")

    def _calculate_performance_grade(self, score: float) -> str:
        """Calculate performance grade based on score"""
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    def _assess_category_performance(self, score: float) -> str:
        """Assess category performance level"""
        if score >= 85:
            return "excellent"
        elif score >= 75:
            return "good"
        elif score >= 65:
            return "satisfactory"
        elif score >= 50:
            return "needs_improvement"
        else:
            return "poor"

    def _assess_opportunity_level(self, improvement_percentage: float) -> str:
        """Assess improvement opportunity level"""
        if improvement_percentage >= 25:
            return "high"
        elif improvement_percentage >= 15:
            return "medium"
        elif improvement_percentage >= 5:
            return "low"
        else:
            return "minimal"

    def _extract_analysis_summary(self, analysis_results: Dict[str, Any]) -> Dict[str, Any]:
        """Extract key analysis summary for memory storage"""

        summary = {
            "recommendations_count": len(analysis_results.get("recommendations", [])),
            "high_priority_count": len([r for r in analysis_results.get("recommendations", []) if r.get("priority") == "high"])
        }

        if "performance_analysis" in analysis_results:
            overall = analysis_results["performance_analysis"].get("overall", {})
            summary["performance_score"] = overall.get("performance_score", 0)
            summary["performance_grade"] = overall.get("performance_grade", "unknown")

        return summary

if __name__ == "__main__":
    # Example usage
    analyzer = SelfImprovementAnalyzer()

    print("🔍 HyperAI Phoenix - Self-Improvement Analyzer Test")
    print("=" * 60)

    # Create mock experiment reports for testing
    from .experiment_runner import ExperimentReport

    mock_reports = [
        ExperimentReport(
            experiment_id="test_1",
            total_tests=100,
            successful_tests=85,
            average_score=78.5,
            total_execution_time=120.0,
            total_api_calls=350,
            categories_performance={"reasoning": 80, "memory": 75, "creativity": 82},
            best_performing_scenarios=["scenario_1"],
            worst_performing_scenarios=["scenario_5"],
            recommendations=["Improve error handling"],
            timestamp=datetime.now().isoformat()
        )
    ]

    # Run analysis
    results = analyzer.analyze_experiment_results(mock_reports)

    print(f"Analysis completed with {len(results.get('recommendations', []))} recommendations")
    if "performance_analysis" in results:
        overall = results["performance_analysis"].get("overall", {})
        print(f"Overall Performance: {overall.get('performance_score', 0):.1f}% (Grade: {overall.get('performance_grade', 'N/A')})")
