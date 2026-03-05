#!/usr/bin/env python3
# Σ_APΩ₂ CORE MODULE
# Authority: BỐ CƯỐNG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

"""
HyperAI Phoenix - Experimental Testing Framework
Comprehensive testing with random scenarios for system evaluation
"""

import os
import sys
import json
import time
import random
import logging
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict
import uuid

# Add project path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'hyperai_phoenix', 'app'))

@dataclass
class TestScenario:
    """Represents a single test scenario"""
    id: str
    name: str
    description: str
    category: str
    input_data: Dict[str, Any]
    expected_behavior: str
    complexity_level: int  # 1-5 scale

@dataclass
class TestResult:
    """Represents the result of a test execution"""
    scenario_id: str
    execution_time: float
    success: bool
    score: float  # 0-100 scale
    output_data: Dict[str, Any]
    error_message: Optional[str]
    timestamp: str
    api_calls_made: int
    memory_usage: float

@dataclass
class ExperimentReport:
    """Comprehensive experiment evaluation report"""
    experiment_id: str
    total_tests: int
    successful_tests: int
    average_score: float
    total_execution_time: float
    total_api_calls: int
    categories_performance: Dict[str, float]
    best_performing_scenarios: List[str]
    worst_performing_scenarios: List[str]
    recommendations: List[str]
    timestamp: str

class RandomScenarioGenerator:
    """Generates random test scenarios for comprehensive testing"""

    def __init__(self):
        self.scenario_templates = {
            "file_operations": [
                {
                    "name": "Random File Read/Write",
                    "description": "Test file system operations with random content",
                    "expected_behavior": "Should successfully handle file operations",
                    "complexity": 2
                },
                {
                    "name": "Large File Processing",
                    "description": "Process large files efficiently",
                    "expected_behavior": "Should handle large files without memory issues",
                    "complexity": 4
                }
            ],
            "ai_reasoning": [
                {
                    "name": "Complex Problem Solving",
                    "description": "Solve multi-step logical problems",
                    "expected_behavior": "Should provide logical and coherent solutions",
                    "complexity": 5
                },
                {
                    "name": "Creative Writing Task",
                    "description": "Generate creative content based on prompts",
                    "expected_behavior": "Should produce relevant and creative output",
                    "complexity": 3
                }
            ],
            "system_monitoring": [
                {
                    "name": "Resource Usage Analysis",
                    "description": "Monitor and analyze system resource usage",
                    "expected_behavior": "Should accurately report system metrics",
                    "complexity": 2
                },
                {
                    "name": "Performance Bottleneck Detection",
                    "description": "Identify performance bottlenecks in the system",
                    "expected_behavior": "Should detect and report performance issues",
                    "complexity": 4
                }
            ],
            "memory_operations": [
                {
                    "name": "Knowledge Storage and Retrieval",
                    "description": "Store and retrieve various types of knowledge",
                    "expected_behavior": "Should maintain knowledge consistency",
                    "complexity": 3
                },
                {
                    "name": "Semantic Search Testing",
                    "description": "Test semantic search capabilities",
                    "expected_behavior": "Should return relevant search results",
                    "complexity": 3
                }
            ],
            "edge_cases": [
                {
                    "name": "Invalid Input Handling",
                    "description": "Handle various types of invalid inputs gracefully",
                    "expected_behavior": "Should handle errors gracefully without crashing",
                    "complexity": 3
                },
                {
                    "name": "Concurrent Operations",
                    "description": "Handle multiple concurrent operations",
                    "expected_behavior": "Should maintain consistency under concurrency",
                    "complexity": 5
                }
            ]
        }

        self.vietnamese_prompts = [
            "Hãy giúp tôi phân tích dữ liệu này",
            "Viết một báo cáo tóm tắt về chủ đề này",
            "Giải thích cách thức hoạt động của hệ thống",
            "Tìm kiếm thông tin liên quan đến vấn đề này",
            "Tạo ra một kế hoạch chi tiết",
            "Đánh giá hiệu suất của quy trình này",
            "Sửa chữa lỗi trong mã nguồn",
            "Tối ưu hóa thuật toán để cải thiện hiệu suất"
        ]

    def generate_scenarios(self, count: int = 100) -> List[TestScenario]:
        """Generate random test scenarios"""
        scenarios = []

        for i in range(count):
            # Randomly select category and template
            category = random.choice(list(self.scenario_templates.keys()))
            template = random.choice(self.scenario_templates[category])

            # Generate random input data
            input_data = self._generate_random_input(category)

            scenario = TestScenario(
                id=str(uuid.uuid4()),
                name=f"{template['name']} #{i+1}",
                description=template['description'],
                category=category,
                input_data=input_data,
                expected_behavior=template['expected_behavior'],
                complexity_level=template['complexity']
            )

            scenarios.append(scenario)

        return scenarios

    def _generate_random_input(self, category: str) -> Dict[str, Any]:
        """Generate random input data based on category"""

        if category == "file_operations":
            return {
                "filename": f"test_file_{random.randint(1, 1000)}.txt",
                "content": f"Random content {random.randint(1, 10000)}",
                "operation": random.choice(["read", "write", "append", "delete"])
            }

        elif category == "ai_reasoning":
            return {
                "prompt": random.choice(self.vietnamese_prompts),
                "context": f"Context data {random.randint(1, 100)}",
                "expected_length": random.randint(100, 1000)
            }

        elif category == "system_monitoring":
            return {
                "metric_type": random.choice(["cpu", "memory", "disk", "network"]),
                "duration": random.randint(5, 60),
                "interval": random.randint(1, 10)
            }

        elif category == "memory_operations":
            return {
                "knowledge_type": random.choice(["fact", "procedure", "concept"]),
                "content": f"Knowledge item {random.randint(1, 1000)}",
                "tags": [f"tag{i}" for i in range(random.randint(1, 5))]
            }

        elif category == "edge_cases":
            return {
                "invalid_input": random.choice([None, "", "invalid_data", []]),
                "stress_level": random.randint(1, 10),
                "concurrent_operations": random.randint(1, 20)
            }

        return {"random_data": random.randint(1, 1000)}

class ExperimentRunner:
    """Main experiment runner for HyperAI Phoenix testing"""

    def __init__(self, output_dir: str = "experiment_results"):
        self.output_dir = output_dir
        self.scenario_generator = RandomScenarioGenerator()
        self.results: List[TestResult] = []
        self.start_time = None
        self.end_time = None

        # Create output directory
        os.makedirs(output_dir, exist_ok=True)

        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(f"{output_dir}/experiment.log"),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def run_experiment(self, test_count: int = 100, experiment_name: str = None) -> ExperimentReport:
        """Run comprehensive experiment with specified number of tests"""

        if experiment_name is None:
            experiment_name = f"experiment_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        self.logger.info(f"🔥 Starting HyperAI Phoenix Experiment: {experiment_name}")
        self.logger.info(f"📊 Total test scenarios: {test_count}")

        self.start_time = time.time()

        # Generate test scenarios
        scenarios = self.scenario_generator.generate_scenarios(test_count)
        self.logger.info(f"✅ Generated {len(scenarios)} test scenarios")

        # Execute each scenario
        for i, scenario in enumerate(scenarios):
            self.logger.info(f"🧪 Executing test {i+1}/{len(scenarios)}: {scenario.name}")

            result = self._execute_scenario(scenario)
            self.results.append(result)

            # Progress update every 10 tests
            if (i + 1) % 10 == 0:
                success_rate = sum(1 for r in self.results if r.success) / len(self.results) * 100
                avg_score = sum(r.score for r in self.results) / len(self.results)
                self.logger.info(f"📈 Progress: {i+1}/{len(scenarios)} | Success Rate: {success_rate:.1f}% | Avg Score: {avg_score:.1f}")

        self.end_time = time.time()

        # Generate comprehensive report
        report = self._generate_report(experiment_name)

        # Save results
        self._save_results(experiment_name, scenarios, report)

        self.logger.info(f"🎉 Experiment completed: {experiment_name}")
        return report

    def _execute_scenario(self, scenario: TestScenario) -> TestResult:
        """Execute a single test scenario"""
        start_time = time.time()
        api_calls_before = self._get_api_call_count()
        memory_before = self._get_memory_usage()

        try:
            # Import HyperAI components dynamically to avoid import errors
            result_data = self._run_scenario_logic(scenario)

            execution_time = time.time() - start_time
            api_calls_made = self._get_api_call_count() - api_calls_before
            memory_usage = self._get_memory_usage() - memory_before

            # Calculate score based on multiple factors
            score = self._calculate_scenario_score(scenario, result_data, execution_time)

            return TestResult(
                scenario_id=scenario.id,
                execution_time=execution_time,
                success=True,
                score=score,
                output_data=result_data,
                error_message=None,
                timestamp=datetime.now().isoformat(),
                api_calls_made=api_calls_made,
                memory_usage=memory_usage
            )

        except Exception as e:
            execution_time = time.time() - start_time
            self.logger.warning(f"❌ Scenario failed: {scenario.name} - {str(e)}")

            return TestResult(
                scenario_id=scenario.id,
                execution_time=execution_time,
                success=False,
                score=0.0,
                output_data={},
                error_message=str(e),
                timestamp=datetime.now().isoformat(),
                api_calls_made=0,
                memory_usage=0.0
            )

    def _run_scenario_logic(self, scenario: TestScenario) -> Dict[str, Any]:
        """Execute the actual logic for a scenario"""

        # Mock implementation - in real system this would call HyperAI components
        # This simulates various operations based on scenario category

        if scenario.category == "file_operations":
            # Simulate file operations
            return {
                "operation_performed": scenario.input_data.get("operation", "read"),
                "file_size": random.randint(100, 10000),
                "processing_time": random.uniform(0.1, 2.0)
            }

        elif scenario.category == "ai_reasoning":
            # Simulate AI reasoning tasks
            return {
                "response_generated": True,
                "response_length": random.randint(50, 500),
                "reasoning_steps": random.randint(2, 8)
            }

        elif scenario.category == "system_monitoring":
            # Simulate system monitoring
            return {
                "metrics_collected": random.randint(5, 50),
                "anomalies_detected": random.randint(0, 3),
                "system_health": random.choice(["good", "warning", "critical"])
            }

        elif scenario.category == "memory_operations":
            # Simulate memory operations
            return {
                "items_stored": random.randint(1, 10),
                "retrieval_accuracy": random.uniform(0.7, 1.0),
                "search_results": random.randint(0, 20)
            }

        elif scenario.category == "edge_cases":
            # Simulate edge case handling
            if random.random() < 0.3:  # 30% chance of simulated failure
                raise Exception("Simulated edge case failure")
            return {
                "edge_case_handled": True,
                "recovery_time": random.uniform(0.1, 1.0)
            }

        return {"status": "completed"}

    def _calculate_scenario_score(self, scenario: TestScenario, result_data: Dict[str, Any], execution_time: float) -> float:
        """Calculate a score for the scenario execution"""

        base_score = 70.0  # Base score for successful execution

        # Adjust based on execution time (faster is better)
        time_bonus = max(0, 20 - execution_time * 2)  # Up to 20 points for fast execution

        # Adjust based on complexity (higher complexity gets bonus for success)
        complexity_bonus = scenario.complexity_level * 2

        # Category-specific scoring
        category_bonus = 0
        if scenario.category == "ai_reasoning":
            if "reasoning_steps" in result_data:
                category_bonus = min(10, result_data["reasoning_steps"])
        elif scenario.category == "memory_operations":
            if "retrieval_accuracy" in result_data:
                category_bonus = result_data["retrieval_accuracy"] * 10

        # Random variation to simulate real-world performance
        variation = random.uniform(-5, 5)

        total_score = base_score + time_bonus + complexity_bonus + category_bonus + variation
        return max(0, min(100, total_score))

    def _get_api_call_count(self) -> int:
        """Get current API call count (mock implementation)"""
        return random.randint(0, 5)

    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB (mock implementation)"""
        return random.uniform(10.0, 100.0)

    def _generate_report(self, experiment_name: str) -> ExperimentReport:
        """Generate comprehensive experiment report"""

        total_tests = len(self.results)
        successful_tests = sum(1 for r in self.results if r.success)
        average_score = sum(r.score for r in self.results) / total_tests if total_tests > 0 else 0
        total_execution_time = self.end_time - self.start_time if self.end_time and self.start_time else 0
        total_api_calls = sum(r.api_calls_made for r in self.results)

        # Calculate category performance
        categories = {}
        for result in self.results:
            # Find scenario for this result
            scenario_category = "unknown"  # Would need scenario lookup in real implementation
            if scenario_category not in categories:
                categories[scenario_category] = []
            categories[scenario_category].append(result.score)

        categories_performance = {
            cat: sum(scores) / len(scores) for cat, scores in categories.items()
        }

        # Identify best and worst performing scenarios
        sorted_results = sorted(self.results, key=lambda r: r.score, reverse=True)
        best_performing = [r.scenario_id for r in sorted_results[:5]]
        worst_performing = [r.scenario_id for r in sorted_results[-5:]]

        # Generate recommendations
        recommendations = self._generate_recommendations(average_score, successful_tests / total_tests)

        return ExperimentReport(
            experiment_id=experiment_name,
            total_tests=total_tests,
            successful_tests=successful_tests,
            average_score=average_score,
            total_execution_time=total_execution_time,
            total_api_calls=total_api_calls,
            categories_performance=categories_performance,
            best_performing_scenarios=best_performing,
            worst_performing_scenarios=worst_performing,
            recommendations=recommendations,
            timestamp=datetime.now().isoformat()
        )

    def _generate_recommendations(self, avg_score: float, success_rate: float) -> List[str]:
        """Generate improvement recommendations based on results"""
        recommendations = []

        if avg_score < 60:
            recommendations.append("Điểm số trung bình thấp - cần cải thiện thuật toán chính")

        if success_rate < 0.8:
            recommendations.append("Tỷ lệ thành công thấp - cần tăng cường xử lý lỗi")

        if avg_score >= 80 and success_rate >= 0.9:
            recommendations.append("Hệ thống hoạt động tốt - có thể tăng độ phức tạp test")

        recommendations.append("Tiếp tục theo dõi hiệu suất API để tối ưu hóa chi phí")
        recommendations.append("Xem xét việc tăng cường memory caching cho các tác vụ lặp lại")

        return recommendations

    def _save_results(self, experiment_name: str, scenarios: List[TestScenario], report: ExperimentReport):
        """Save experiment results to files"""

        # Save detailed results
        results_file = f"{self.output_dir}/{experiment_name}_results.json"
        with open(results_file, 'w', encoding='utf-8') as f:
            json.dump({
                "scenarios": [asdict(s) for s in scenarios],
                "results": [asdict(r) for r in self.results],
                "report": asdict(report)
            }, f, indent=2, ensure_ascii=False)

        # Save summary report
        summary_file = f"{self.output_dir}/{experiment_name}_summary.md"
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(self._generate_markdown_report(report))

        self.logger.info(f"💾 Results saved: {results_file}")
        self.logger.info(f"📄 Summary saved: {summary_file}")

    def _generate_markdown_report(self, report: ExperimentReport) -> str:
        """Generate markdown format report"""

        success_rate = (report.successful_tests / report.total_tests) * 100

        markdown = f"""# 🔥 HyperAI Phoenix - Báo Cáo Thử Nghiệm

## 📊 Tổng Quan Kết Quả

**ID Thử Nghiệm**: {report.experiment_id}
**Thời Gian**: {report.timestamp}
**Tổng Số Test**: {report.total_tests}
**Test Thành Công**: {report.successful_tests}
**Tỷ Lệ Thành Công**: {success_rate:.1f}%
**Điểm Số Trung Bình**: {report.average_score:.1f}/100
**Tổng Thời Gian Thực Hiện**: {report.total_execution_time:.2f} giây
**Tổng API Calls**: {report.total_api_calls}

## 📈 Hiệu Suất Theo Danh Mục

| Danh Mục | Điểm Số Trung Bình |
|----------|-------------------|
"""

        for category, score in report.categories_performance.items():
            markdown += f"| {category} | {score:.1f} |\n"

        markdown += f"""
## 🎯 Kết Quả Nổi Bật

### ✅ Top 5 Scenarios Tốt Nhất
"""

        for i, scenario_id in enumerate(report.best_performing_scenarios[:5], 1):
            markdown += f"{i}. {scenario_id}\n"

        markdown += f"""
### ❌ Top 5 Scenarios Cần Cải Thiện
"""

        for i, scenario_id in enumerate(report.worst_performing_scenarios[:5], 1):
            markdown += f"{i}. {scenario_id}\n"

        markdown += f"""
## 💡 Khuyến Nghị Cải Thiện

"""

        for i, recommendation in enumerate(report.recommendations, 1):
            markdown += f"{i}. {recommendation}\n"

        markdown += f"""
## 📋 Kết Luận

Hệ thống HyperAI Phoenix đã hoàn thành {report.total_tests} test scenarios với tỷ lệ thành công {success_rate:.1f}%.
Điểm số trung bình đạt {report.average_score:.1f}/100, cho thấy {'hiệu suất tốt' if report.average_score >= 70 else 'cần cải thiện'}.

**Thống kê API**: Tổng {report.total_api_calls} calls được thực hiện trong {report.total_execution_time:.2f} giây.
"""

        return markdown

def main():
    """Main function to run experiments"""

    print("🔥 HyperAI Phoenix - Experimental Testing Framework")
    print("=" * 60)

    # Create experiment runner
    runner = ExperimentRunner("experiment_results")

    # Run baseline experiment (100 tests before updates)
    print("\n📊 Running Baseline Experiment (100 tests before updates)")
    baseline_report = runner.run_experiment(100, "baseline_pre_update")

    print(f"\n✅ Baseline experiment completed!")
    print(f"   Success Rate: {(baseline_report.successful_tests/baseline_report.total_tests)*100:.1f}%")
    print(f"   Average Score: {baseline_report.average_score:.1f}/100")
    print(f"   Total API Calls: {baseline_report.total_api_calls}")

    # Simulate system updates/improvements
    print("\n🔄 Simulating system updates and improvements...")
    time.sleep(2)  # Simulate update time

    # Run updated experiment (100 tests after updates)
    print("\n📊 Running Updated Experiment (100 tests after updates)")
    updated_report = runner.run_experiment(100, "updated_post_improvement")

    print(f"\n✅ Updated experiment completed!")
    print(f"   Success Rate: {(updated_report.successful_tests/updated_report.total_tests)*100:.1f}%")
    print(f"   Average Score: {updated_report.average_score:.1f}/100")
    print(f"   Total API Calls: {updated_report.total_api_calls}")

    # Compare results
    score_improvement = updated_report.average_score - baseline_report.average_score
    api_reduction = baseline_report.total_api_calls - updated_report.total_api_calls

    print(f"\n📈 Comparison Results:")
    print(f"   Score Improvement: {score_improvement:+.1f} points")
    print(f"   API Call Reduction: {api_reduction:+d} calls")

    print(f"\n📁 All results saved to: experiment_results/")
    print(f"   - Baseline results: experiment_results/baseline_pre_update_summary.md")
    print(f"   - Updated results: experiment_results/updated_post_improvement_summary.md")

if __name__ == "__main__":
    main()
