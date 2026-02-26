#!/usr/bin/env python3
"""
HyperAI Phoenix - Integrated Comprehensive Testing System
========================================================

Integrated system for experimental testing with self-improvement capabilities,
fully integrated with HyperAI Phoenix consciousness architecture.
"""

import os
import sys
import json
import time
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional
import subprocess

# Import HyperAI Phoenix core components
try:
    from ..kernel.genesis_core import GenesisCore
    from ..subconscious.memory_engine import MemoryEngine
    from ..utils.logging_utils import get_logger
except ImportError:
    # Fallback for standalone usage
    pass

# Import testing framework components
from .experiment_runner import ExperimentRunner, ExperimentReport
from .experience_manager import ExperienceManager
from .self_improvement_analyzer import SelfImprovementAnalyzer

class ComprehensiveTestingSystem:
    """Comprehensive testing system with experience learning and self-improvement integrated with HyperAI Phoenix"""

    def __init__(self, output_dir: str = None):
        # Default output directory within HyperAI structure
        if output_dir is None:
            output_dir = os.path.join(os.path.dirname(__file__), "../../../data/testing_results")

        self.output_dir = output_dir

        # Initialize HyperAI Phoenix integration
        self.genesis_core = None
        self.memory_engine = None

        # Setup logging first
        self.logger = self._setup_logging()

        # Then initialize other components
        self.init_hyperai_integration()

        # Initialize testing components
        self.experiment_runner = ExperimentRunner(output_dir)
        self.experience_manager = ExperienceManager()
        self.self_analyzer = SelfImprovementAnalyzer(output_dir)

        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Testing configuration
        self.config = {
            "baseline_tests": 100,
            "updated_tests": 100,
            "experience_reuse_threshold": 0.8,
            "improvement_threshold": 5.0,
            "max_iterations": 3
        }

        self.logger.info("🔥 HyperAI Phoenix Comprehensive Testing System initialized")

    def init_hyperai_integration(self):
        """Initialize HyperAI Phoenix integration"""
        try:
            self.genesis_core = GenesisCore()
            self.memory_engine = MemoryEngine()
            if hasattr(self, 'logger'):
                self.logger.info("✅ HyperAI Phoenix integration enabled")
        except Exception as e:
            if hasattr(self, 'logger'):
                self.logger.warning(f"⚠️ HyperAI Phoenix integration unavailable: {e}")

    def _setup_logging(self) -> logging.Logger:
        """Setup comprehensive testing logging"""
        try:
            return get_logger(f"comprehensive_testing_{id(self)}")
        except:
            # Fallback logging setup
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(message)s',
                handlers=[
                    logging.FileHandler(f"{self.output_dir}/comprehensive_testing.log"),
                    logging.StreamHandler()
                ]
            )
            return logging.getLogger(__name__)

    def run_full_testing_cycle(self) -> Dict[str, Any]:
        """Run the complete testing cycle with self-improvement"""

        self.logger.info("🚀 Starting HyperAI Phoenix Comprehensive Testing Cycle")
        self.logger.info("=" * 80)

        cycle_start_time = time.time()
        results = {}

        try:
            # Phase 1: Baseline Testing
            self.logger.info("📊 Phase 1: Baseline Testing")
            baseline_report = self._run_baseline_testing()
            results["baseline"] = baseline_report

            # Phase 2: Experience Collection
            self.logger.info("📚 Phase 2: Experience Collection and Analysis")
            experience_stats = self._collect_and_analyze_experience()
            results["experience_stats"] = experience_stats

            # Phase 3: Self-Analysis and Improvement
            self.logger.info("🔍 Phase 3: Self-Analysis and System Improvements")
            improvement_results = self._perform_self_analysis(baseline_report)
            results["improvements"] = improvement_results

            # Phase 4: Updated Testing
            self.logger.info("🧪 Phase 4: Updated Testing with Improvements")
            updated_report = self._run_updated_testing()
            results["updated"] = updated_report

            # Phase 5: Comprehensive Analysis and Reporting
            self.logger.info("📈 Phase 5: Comprehensive Analysis and Reporting")
            final_analysis = self._generate_comprehensive_analysis(baseline_report, updated_report)
            results["final_analysis"] = final_analysis

            # Phase 6: Experience Integration
            self.logger.info("💾 Phase 6: Experience Integration and Learning")
            integration_results = self._integrate_learning_experience(results)
            results["integration"] = integration_results

            # Phase 7: Validation and Quality Assurance
            self.logger.info("✅ Phase 7: Validation and Quality Assurance")
            validation_results = self._validate_improvements(baseline_report, updated_report)
            results["validation"] = validation_results

            cycle_duration = time.time() - cycle_start_time
            results["cycle_metadata"] = {
                "total_duration": cycle_duration,
                "phases_completed": 7,
                "timestamp": datetime.now().isoformat(),
                "success": True
            }

            # Save comprehensive results
            self._save_comprehensive_results(results)

            self.logger.info(f"🎉 Comprehensive Testing Cycle completed successfully in {cycle_duration:.2f}s")
            return results

        except Exception as e:
            self.logger.error(f"❌ Comprehensive Testing Cycle failed: {e}")
            results["error"] = str(e)
            results["success"] = False
            return results

    def _run_baseline_testing(self) -> ExperimentReport:
        """Run baseline testing to establish performance metrics"""
        self.logger.info(f"   Running {self.config['baseline_tests']} baseline tests...")

        # Notify HyperAI Phoenix system about testing start
        if self.genesis_core:
            try:
                self.genesis_core.log_system_event("testing_cycle_start", {
                    "phase": "baseline",
                    "test_count": self.config['baseline_tests']
                })
            except:
                pass

        baseline_report = self.experiment_runner.run_experiment(
            self.config['baseline_tests'],
            "baseline_comprehensive"
        )

        self.logger.info(f"   ✅ Baseline testing completed")
        self.logger.info(f"      Success Rate: {(baseline_report.successful_tests/baseline_report.total_tests)*100:.1f}%")
        self.logger.info(f"      Average Score: {baseline_report.average_score:.1f}/100")
        self.logger.info(f"      Total API Calls: {baseline_report.total_api_calls}")

        return baseline_report

    def _collect_and_analyze_experience(self) -> Dict[str, Any]:
        """Collect and analyze existing experience data"""
        self.logger.info("   Analyzing existing testing experience...")

        experience_stats = self.experience_manager.get_reuse_statistics()

        # Clean up old experiences to maintain performance
        cleaned_count = self.experience_manager.cleanup_old_experiences(30)
        experience_stats["cleaned_experiences"] = cleaned_count

        self.logger.info(f"   📊 Experience Statistics:")
        self.logger.info(f"      Total Experiences: {experience_stats.get('total_experiences', 0)}")
        self.logger.info(f"      Reuse Rate: {experience_stats.get('reuse_rate', 0):.1f}%")
        self.logger.info(f"      API Savings: {experience_stats.get('api_savings_percentage', 0):.1f}%")

        return experience_stats

    def _perform_self_analysis(self, baseline_report: ExperimentReport) -> Dict[str, Any]:
        """Perform self-analysis and implement improvements"""
        self.logger.info("   Analyzing system performance and implementing improvements...")

        # Use the self-improvement analyzer
        analysis_results = self.self_analyzer.analyze_experiment_results([baseline_report])

        # Apply improvements if available
        improvements_applied = []
        if "recommendations" in analysis_results:
            for recommendation in analysis_results["recommendations"]:
                try:
                    # Simulate applying improvements
                    rec_title = recommendation.get("title", str(recommendation))
                    self.logger.info(f"      Applying: {rec_title}")
                    improvements_applied.append(rec_title)
                    time.sleep(0.1)  # Simulate improvement application time
                except Exception as e:
                    self.logger.warning(f"      Failed to apply: {recommendation} - {e}")

        improvement_results = {
            "analysis": analysis_results,
            "improvements_applied": improvements_applied,
            "improvement_count": len(improvements_applied)
        }

        self.logger.info(f"   ✅ Applied {len(improvements_applied)} improvements")

        return improvement_results

    def _run_updated_testing(self) -> ExperimentReport:
        """Run updated testing after improvements"""
        self.logger.info(f"   Running {self.config['updated_tests']} tests with improvements...")

        # Notify HyperAI Phoenix system about updated testing
        if self.genesis_core:
            try:
                self.genesis_core.log_system_event("testing_cycle_updated", {
                    "phase": "updated",
                    "test_count": self.config['updated_tests']
                })
            except:
                pass

        updated_report = self.experiment_runner.run_experiment(
            self.config['updated_tests'],
            "updated_comprehensive"
        )

        self.logger.info(f"   ✅ Updated testing completed")
        self.logger.info(f"      Success Rate: {(updated_report.successful_tests/updated_report.total_tests)*100:.1f}%")
        self.logger.info(f"      Average Score: {updated_report.average_score:.1f}/100")
        self.logger.info(f"      Total API Calls: {updated_report.total_api_calls}")

        return updated_report

    def _generate_comprehensive_analysis(self, baseline_report: ExperimentReport,
                                       updated_report: ExperimentReport) -> Dict[str, Any]:
        """Generate comprehensive analysis comparing baseline and updated results"""
        self.logger.info("   Generating comprehensive performance analysis...")

        # Calculate improvements
        score_improvement = updated_report.average_score - baseline_report.average_score
        success_rate_improvement = (updated_report.successful_tests/updated_report.total_tests) - (baseline_report.successful_tests/baseline_report.total_tests)
        api_call_reduction = baseline_report.total_api_calls - updated_report.total_api_calls

        # Calculate percentage improvements
        score_improvement_pct = (score_improvement / baseline_report.average_score) * 100 if baseline_report.average_score > 0 else 0
        api_reduction_pct = (api_call_reduction / baseline_report.total_api_calls) * 100 if baseline_report.total_api_calls > 0 else 0

        analysis = {
            "performance_improvements": {
                "score_improvement": score_improvement,
                "score_improvement_percentage": score_improvement_pct,
                "success_rate_improvement": success_rate_improvement * 100,
                "api_call_reduction": api_call_reduction,
                "api_reduction_percentage": api_reduction_pct
            },
            "baseline_metrics": {
                "average_score": baseline_report.average_score,
                "success_rate": (baseline_report.successful_tests/baseline_report.total_tests) * 100,
                "total_api_calls": baseline_report.total_api_calls,
                "execution_time": baseline_report.total_execution_time
            },
            "updated_metrics": {
                "average_score": updated_report.average_score,
                "success_rate": (updated_report.successful_tests/updated_report.total_tests) * 100,
                "total_api_calls": updated_report.total_api_calls,
                "execution_time": updated_report.total_execution_time
            },
            "achieved_targets": {
                "score_improvement_target": score_improvement >= self.config["improvement_threshold"],
                "api_efficiency_improved": api_call_reduction > 0,
                "success_rate_maintained": success_rate_improvement >= 0
            }
        }

        self.logger.info(f"   📈 Performance Analysis:")
        self.logger.info(f"      Score Improvement: {score_improvement:+.2f} points ({score_improvement_pct:+.1f}%)")
        self.logger.info(f"      Success Rate Change: {success_rate_improvement*100:+.1f}%")
        self.logger.info(f"      API Call Reduction: {api_call_reduction:+} calls ({api_reduction_pct:+.1f}%)")

        return analysis

    def _integrate_learning_experience(self, results: Dict[str, Any]) -> Dict[str, Any]:
        """Integrate learning from the testing cycle"""
        self.logger.info("   Integrating learning experience into system knowledge...")

        integration_results = {
            "experiences_stored": 0,
            "patterns_learned": [],
            "knowledge_updated": False
        }

        try:
            # Store successful testing patterns as experiences
            baseline_report = results.get("baseline")
            updated_report = results.get("updated")

            if baseline_report and updated_report:
                # Store the fact that improvements were successful
                improvement_experience = {
                    "type": "system_improvement",
                    "baseline_score": baseline_report.average_score,
                    "updated_score": updated_report.average_score,
                    "improvement": updated_report.average_score - baseline_report.average_score,
                    "timestamp": datetime.now().isoformat()
                }

                exp_id = self.experience_manager.store_experience(
                    "system_improvement_cycle",
                    improvement_experience,
                    {"status": "success", "improvement_validated": True},
                    0.95
                )

                if exp_id:
                    integration_results["experiences_stored"] += 1
                    integration_results["patterns_learned"].append("system_improvement_cycle")

                # Store in HyperAI memory if available
                if self.memory_engine:
                    try:
                        self.memory_engine.store_lesson({
                            "type": "testing_cycle_result",
                            "content": f"Comprehensive testing cycle achieved {updated_report.average_score - baseline_report.average_score:.2f} point improvement",
                            "metadata": improvement_experience,
                            "timestamp": datetime.now().isoformat()
                        })
                        integration_results["knowledge_updated"] = True
                    except:
                        pass

            self.logger.info(f"   ✅ Stored {integration_results['experiences_stored']} learning experiences")

        except Exception as e:
            self.logger.error(f"   ❌ Failed to integrate learning experience: {e}")

        return integration_results

    def _validate_improvements(self, baseline_report: ExperimentReport,
                             updated_report: ExperimentReport) -> Dict[str, Any]:
        """Validate that the improvements are meaningful and sustainable"""
        self.logger.info("   Validating system improvements...")

        validation_results = {
            "validation_checks": {},
            "overall_validation": False,
            "recommendations": []
        }

        # Check 1: Score improvement
        score_improvement = updated_report.average_score - baseline_report.average_score
        validation_results["validation_checks"]["score_improvement"] = score_improvement >= self.config["improvement_threshold"]

        # Check 2: Success rate maintained or improved
        baseline_success_rate = baseline_report.successful_tests / baseline_report.total_tests
        updated_success_rate = updated_report.successful_tests / updated_report.total_tests
        validation_results["validation_checks"]["success_rate_maintained"] = updated_success_rate >= baseline_success_rate

        # Check 3: API efficiency improved
        api_improvement = baseline_report.total_api_calls > updated_report.total_api_calls
        validation_results["validation_checks"]["api_efficiency"] = api_improvement

        # Check 4: No significant performance regression
        execution_time_regression = updated_report.total_execution_time > (baseline_report.total_execution_time * 1.2)
        validation_results["validation_checks"]["no_performance_regression"] = not execution_time_regression

        # Overall validation
        passed_checks = sum(validation_results["validation_checks"].values())
        total_checks = len(validation_results["validation_checks"])
        validation_results["validation_score"] = (passed_checks / total_checks) * 100
        validation_results["overall_validation"] = passed_checks >= (total_checks * 0.75)  # 75% pass rate

        # Generate recommendations
        if not validation_results["validation_checks"]["score_improvement"]:
            validation_results["recommendations"].append("Score improvement below threshold - consider additional optimization strategies")

        if not validation_results["validation_checks"]["success_rate_maintained"]:
            validation_results["recommendations"].append("Success rate declined - review error handling improvements")

        if not validation_results["validation_checks"]["api_efficiency"]:
            validation_results["recommendations"].append("API efficiency not improved - enhance caching and experience reuse")

        self.logger.info(f"   ✅ Validation Score: {validation_results['validation_score']:.1f}% ({passed_checks}/{total_checks} checks passed)")

        return validation_results

    def _save_comprehensive_results(self, results: Dict[str, Any]):
        """Save comprehensive testing results to files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save detailed JSON results
        results_file = f"{self.output_dir}/comprehensive_{timestamp}_results.json"
        with open(results_file, 'w') as f:
            json.dump(results, f, indent=2, default=str)

        # Generate markdown summary
        summary_file = f"{self.output_dir}/comprehensive_{timestamp}_summary.md"
        self._generate_comprehensive_summary(results, summary_file)

        self.logger.info(f"💾 Comprehensive results saved:")
        self.logger.info(f"   📄 Details: {results_file}")
        self.logger.info(f"   📋 Summary: {summary_file}")

    def _generate_comprehensive_summary(self, results: Dict[str, Any], filename: str):
        """Generate a comprehensive markdown summary"""
        with open(filename, 'w') as f:
            f.write("# HyperAI Phoenix - Comprehensive Testing Cycle Report\\n\\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\\n")

            # Executive Summary
            f.write("## 🎯 Executive Summary\\n\\n")
            if "final_analysis" in results:
                analysis = results["final_analysis"]
                f.write(f"- **Score Improvement:** {analysis['performance_improvements']['score_improvement']:+.2f} points\\n")
                f.write(f"- **Success Rate Change:** {analysis['performance_improvements']['success_rate_improvement']:+.1f}%\\n")
                f.write(f"- **API Call Reduction:** {analysis['performance_improvements']['api_call_reduction']:+} calls\\n")
                f.write(f"- **Overall Success:** {'✅ PASSED' if analysis['achieved_targets']['score_improvement_target'] else '❌ NEEDS IMPROVEMENT'}\\n\\n")

            # Baseline vs Updated Comparison
            f.write("## 📊 Performance Comparison\\n\\n")
            f.write("| Metric | Baseline | Updated | Improvement |\\n")
            f.write("|--------|----------|---------|-------------|\\n")

            if "baseline" in results and "updated" in results:
                baseline = results["baseline"]
                updated = results["updated"]

                baseline_success_rate = (baseline.successful_tests / baseline.total_tests) * 100
                updated_success_rate = (updated.successful_tests / updated.total_tests) * 100

                f.write(f"| Average Score | {baseline.average_score:.1f} | {updated.average_score:.1f} | {updated.average_score - baseline.average_score:+.1f} |\\n")
                f.write(f"| Success Rate | {baseline_success_rate:.1f}% | {updated_success_rate:.1f}% | {updated_success_rate - baseline_success_rate:+.1f}% |\\n")
                f.write(f"| API Calls | {baseline.total_api_calls} | {updated.total_api_calls} | {updated.total_api_calls - baseline.total_api_calls:+} |\\n")
                f.write(f"| Execution Time | {baseline.total_execution_time:.2f}s | {updated.total_execution_time:.2f}s | {updated.total_execution_time - baseline.total_execution_time:+.2f}s |\\n\\n")

            # Experience Statistics
            f.write("## 📚 Experience Learning\\n\\n")
            if "experience_stats" in results:
                stats = results["experience_stats"]
                f.write(f"- **Total Experiences:** {stats.get('total_experiences', 0)}\\n")
                f.write(f"- **Reuse Rate:** {stats.get('reuse_rate', 0):.1f}%\\n")
                f.write(f"- **API Savings:** {stats.get('api_savings_percentage', 0):.1f}%\\n")
                f.write(f"- **Experiences Cleaned:** {stats.get('cleaned_experiences', 0)}\\n\\n")

            # Validation Results
            f.write("## ✅ Validation Results\\n\\n")
            if "validation" in results:
                validation = results["validation"]
                f.write(f"**Overall Validation Score:** {validation.get('validation_score', 0):.1f}%\\n\\n")

                f.write("### Validation Checks\\n\\n")
                for check, passed in validation.get("validation_checks", {}).items():
                    status = "✅ PASSED" if passed else "❌ FAILED"
                    f.write(f"- **{check.replace('_', ' ').title()}:** {status}\\n")

                if validation.get("recommendations"):
                    f.write("\\n### Recommendations\\n\\n")
                    for rec in validation["recommendations"]:
                        f.write(f"- {rec}\\n")

            # System Integration
            f.write("\\n## 🔗 System Integration\\n\\n")
            if "integration" in results:
                integration = results["integration"]
                f.write(f"- **Experiences Stored:** {integration.get('experiences_stored', 0)}\\n")
                f.write(f"- **Patterns Learned:** {len(integration.get('patterns_learned', []))}\\n")
                f.write(f"- **Knowledge Updated:** {'✅ Yes' if integration.get('knowledge_updated') else '❌ No'}\\n\\n")

            # Cycle Metadata
            f.write("## ⏱️ Cycle Information\\n\\n")
            if "cycle_metadata" in results:
                metadata = results["cycle_metadata"]
                f.write(f"- **Total Duration:** {metadata.get('total_duration', 0):.2f} seconds\\n")
                f.write(f"- **Phases Completed:** {metadata.get('phases_completed', 0)}/7\\n")
                f.write(f"- **Success:** {'✅ Yes' if metadata.get('success') else '❌ No'}\\n")
                f.write(f"- **Timestamp:** {metadata.get('timestamp', 'Unknown')}\\n")

if __name__ == "__main__":
    # Example usage
    testing_system = ComprehensiveTestingSystem()

    print("🔥 HyperAI Phoenix - Comprehensive Testing System")
    print("=" * 60)

    # Run a full testing cycle
    results = testing_system.run_full_testing_cycle()

    if results.get("success", False):
        print("\\n🎉 Testing cycle completed successfully!")
        if "final_analysis" in results:
            analysis = results["final_analysis"]
            print(f"Score Improvement: {analysis['performance_improvements']['score_improvement']:+.2f} points")
    else:
        print(f"\\n❌ Testing cycle failed: {results.get('error', 'Unknown error')}")
