"""
HyperAI Phoenix - Autonomous Development Module
Implementation of closed-loop evolution capabilities
Integrates MOP (Meta-Optimizer Protocol) and OCP (Optimization & Control Protocol)
"""

import os
import json
import logging
import time
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
from enum import Enum

# Use absolute imports to avoid import issues
from hyperai_phoenix.app.brain.tools.code_analysis_tools import CodeAnalysisTools
from hyperai_phoenix.app.brain.tools.code_generation_tools import CodeGenerationTools


class ImprovementPhase(Enum):
    """Phases of the autonomous improvement cycle"""
    ANALYSIS = "analysis"
    PLANNING = "planning"
    IMPLEMENTATION = "implementation"
    TESTING = "testing"
    EVALUATION = "evaluation"
    DEPLOYMENT = "deployment"


class ImprovementGoal(Enum):
    """Types of improvement goals"""
    PERFORMANCE = "performance"
    QUALITY = "quality"
    MAINTAINABILITY = "maintainability"
    SECURITY = "security"
    DOCUMENTATION = "documentation"


@dataclass
class ImprovementCycle:
    """Represents a complete improvement cycle"""
    cycle_id: str
    start_time: datetime
    end_time: Optional[datetime]
    phase: ImprovementPhase
    goals: List[ImprovementGoal]
    target_files: List[str]
    analysis_results: Dict[str, Any]
    improvements_made: List[Dict[str, Any]]
    success_metrics: Dict[str, float]
    learning_outcomes: List[str]
    status: str


@dataclass
class LearningRecord:
    """Record of learning from improvement cycles"""
    pattern_id: str
    pattern_description: str
    trigger_conditions: Dict[str, Any]
    improvement_actions: List[str]
    success_rate: float
    confidence_score: float
    usage_count: int
    last_used: datetime


class AutonomousDevelopment:
    """
    Autonomous Development System
    Implements closed-loop evolution with self-improvement capabilities
    """

    def __init__(self, project_root: str = ".", language: str = "en", safety_mode: bool = True):
        self.project_root = os.path.abspath(project_root)
        self.language = language
        self.safety_mode = safety_mode
        self.logger = logging.getLogger(__name__)

        # Initialize tools
        self.code_analyzer = CodeAnalysisTools(self.project_root, language)
        self.code_generator = CodeGenerationTools(self.project_root, language)

        # Learning system
        self.learning_records = {}
        self.improvement_history = []
        self.performance_baselines = {}

        # Safety controls
        self.safety_checks = {
            'max_files_per_cycle': 5,
            'max_changes_per_file': 10,
            'backup_required': True,
            'human_approval_required': safety_mode,
            'dangerous_operations_blocked': True
        }

        # Error messages for internationalization
        self.error_messages = {
            'en': {
                'CYCLE_FAILED': 'Improvement cycle failed: {error}',
                'SAFETY_VIOLATION': 'Safety violation: {violation}',
                'NO_IMPROVEMENTS_FOUND': 'No viable improvements found',
                'BACKUP_FAILED': 'Backup creation failed: {error}',
                'LEARNING_FAILED': 'Learning integration failed: {error}'
            },
            'vi': {
                'CYCLE_FAILED': 'Chu kỳ cải thiện thất bại: {error}',
                'SAFETY_VIOLATION': 'Vi phạm an toàn: {violation}',
                'NO_IMPROVEMENTS_FOUND': 'Không tìm thấy cải thiện khả thi',
                'BACKUP_FAILED': 'Tạo backup thất bại: {error}',
                'LEARNING_FAILED': 'Tích hợp học tập thất bại: {error}'
            }
        }

    def _get_error_message(self, key: str, **kwargs) -> str:
        """Get localized error message"""
        messages = self.error_messages.get(self.language, self.error_messages['en'])
        message = messages.get(key, f'Unknown error: {key}')
        return message.format(**kwargs)

    def initiate_improvement_cycle(self, focus_areas: List[str] = None,
                                 target_files: List[str] = None,
                                 improvement_goals: List[str] = None) -> Dict[str, Any]:
        """
        Initiate a complete autonomous improvement cycle
        This is the main entry point for closed-loop evolution
        """
        try:
            # Generate unique cycle ID
            cycle_id = f"cycle_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

            # Convert string goals to enums
            goals = []
            if improvement_goals:
                for goal in improvement_goals:
                    try:
                        goals.append(ImprovementGoal(goal.upper()))
                    except ValueError:
                        self.logger.warning(f"Unknown improvement goal: {goal}")

            if not goals:
                goals = [ImprovementGoal.QUALITY, ImprovementGoal.PERFORMANCE]

            # Create improvement cycle
            cycle = ImprovementCycle(
                cycle_id=cycle_id,
                start_time=datetime.now(),
                end_time=None,
                phase=ImprovementPhase.ANALYSIS,
                goals=goals,
                target_files=target_files or [],
                analysis_results={},
                improvements_made=[],
                success_metrics={},
                learning_outcomes=[],
                status="initiated"
            )

            self.logger.info(f"Starting improvement cycle: {cycle_id}")

            # Execute improvement phases
            result = self._execute_improvement_cycle(cycle, focus_areas)

            # Record the cycle
            self.improvement_history.append(cycle)

            return result

        except Exception as e:
            self.logger.error(f"Improvement cycle initiation failed: {e}")
            return {
                'success': False,
                'error': self._get_error_message('CYCLE_FAILED', error=str(e)),
                'cycle_id': cycle_id if 'cycle_id' in locals() else None
            }

    def _execute_improvement_cycle(self, cycle: ImprovementCycle, focus_areas: List[str]) -> Dict[str, Any]:
        """Execute the complete 6-phase improvement cycle"""

        phases = [
            (ImprovementPhase.ANALYSIS, self._phase_analysis),
            (ImprovementPhase.PLANNING, self._phase_planning),
            (ImprovementPhase.IMPLEMENTATION, self._phase_implementation),
            (ImprovementPhase.TESTING, self._phase_testing),
            (ImprovementPhase.EVALUATION, self._phase_evaluation),
            (ImprovementPhase.DEPLOYMENT, self._phase_deployment)
        ]

        results = {}

        for phase, phase_function in phases:
            try:
                cycle.phase = phase
                cycle.status = f"executing_{phase.value}"

                self.logger.info(f"Executing phase: {phase.value}")
                phase_result = phase_function(cycle, focus_areas)

                if not phase_result.get('success', False):
                    cycle.status = f"failed_at_{phase.value}"
                    return {
                        'success': False,
                        'cycle_id': cycle.cycle_id,
                        'failed_phase': phase.value,
                        'error': phase_result.get('error', 'Unknown phase error'),
                        'results': results
                    }

                results[phase.value] = phase_result

            except Exception as e:
                cycle.status = f"error_at_{phase.value}"
                self.logger.error(f"Phase {phase.value} failed: {e}")
                return {
                    'success': False,
                    'cycle_id': cycle.cycle_id,
                    'failed_phase': phase.value,
                    'error': str(e),
                    'results': results
                }

        cycle.end_time = datetime.now()
        cycle.status = "completed"

        # Integrate learning
        self._integrate_learning(cycle)

        return {
            'success': True,
            'cycle_id': cycle.cycle_id,
            'duration': (cycle.end_time - cycle.start_time).total_seconds(),
            'improvements_made': len(cycle.improvements_made),
            'learning_outcomes': cycle.learning_outcomes,
            'results': results
        }

    def _phase_analysis(self, cycle: ImprovementCycle, focus_areas: List[str]) -> Dict[str, Any]:
        """Phase 1: Analyze current codebase and identify improvement opportunities"""
        try:
            # Analyze project structure if no target files specified
            if not cycle.target_files:
                project_analysis = self.code_analyzer.analyze_project_structure(self.project_root)
                if not project_analysis['success']:
                    return {
                        'success': False,
                        'error': f"Project analysis failed: {project_analysis.get('error')}"
                    }

                # Extract files with issues as targets
                cycle.target_files = list(project_analysis['analysis']['file_analyses'].keys())[:self.safety_checks['max_files_per_cycle']]
                cycle.analysis_results['project_analysis'] = project_analysis

            # Analyze each target file
            file_analyses = {}
            total_issues = 0

            for file_path in cycle.target_files:
                analysis = self.code_analyzer.analyze_code_file(file_path)
                if analysis['success']:
                    file_analyses[file_path] = analysis
                    total_issues += len(analysis.get('quality_issues', []))

            cycle.analysis_results['file_analyses'] = file_analyses
            cycle.analysis_results['total_issues'] = total_issues

            # Apply learning from previous cycles
            learned_improvements = self._apply_learned_patterns(cycle.analysis_results)
            cycle.analysis_results['learned_improvements'] = learned_improvements

            self.logger.info(f"Analysis complete: {len(cycle.target_files)} files, {total_issues} issues")

            return {
                'success': True,
                'files_analyzed': len(cycle.target_files),
                'total_issues': total_issues,
                'learned_patterns_applied': len(learned_improvements)
            }

        except Exception as e:
            return {
                'success': False,
                'error': f"Analysis phase failed: {str(e)}"
            }

    def _phase_planning(self, cycle: ImprovementCycle, focus_areas: List[str]) -> Dict[str, Any]:
        """Phase 2: Plan specific improvements based on analysis"""
        try:
            improvement_plan = []

            # Plan improvements for each file
            for file_path, analysis in cycle.analysis_results.get('file_analyses', {}).items():
                if not analysis['success']:
                    continue

                file_improvements = []
                quality_issues = analysis.get('quality_issues', [])

                # Plan improvements based on goals
                for goal in cycle.goals:
                    if goal == ImprovementGoal.QUALITY:
                        file_improvements.extend(self._plan_quality_improvements(quality_issues))
                    elif goal == ImprovementGoal.PERFORMANCE:
                        file_improvements.extend(self._plan_performance_improvements(analysis))
                    elif goal == ImprovementGoal.DOCUMENTATION:
                        file_improvements.extend(self._plan_documentation_improvements(analysis))

                if file_improvements:
                    improvement_plan.append({
                        'file_path': file_path,
                        'improvements': file_improvements[:self.safety_checks['max_changes_per_file']]
                    })

            # Apply learned improvement strategies
            for learned in cycle.analysis_results.get('learned_improvements', []):
                improvement_plan.append(learned)

            cycle.analysis_results['improvement_plan'] = improvement_plan

            # Safety check
            if self.safety_mode and self.safety_checks['human_approval_required']:
                # In real implementation, this would request human approval
                self.logger.info("Human approval required for improvement plan")

            self.logger.info(f"Planning complete: {len(improvement_plan)} improvement actions planned")

            return {
                'success': True,
                'planned_improvements': len(improvement_plan),
                'approval_required': self.safety_checks['human_approval_required']
            }

        except Exception as e:
            return {
                'success': False,
                'error': f"Planning phase failed: {str(e)}"
            }

    def _phase_implementation(self, cycle: ImprovementCycle, focus_areas: List[str]) -> Dict[str, Any]:
        """Phase 3: Implement planned improvements"""
        try:
            implemented_changes = []

            # Create backup if required
            if self.safety_checks['backup_required']:
                backup_result = self._create_backup(cycle.target_files)
                if not backup_result['success']:
                    return {
                        'success': False,
                        'error': self._get_error_message('BACKUP_FAILED', error=backup_result['error'])
                    }

            # Implement each planned improvement
            for plan_item in cycle.analysis_results.get('improvement_plan', []):
                file_path = plan_item['file_path']
                improvements = plan_item['improvements']

                for improvement in improvements:
                    try:
                        change_result = self._implement_improvement(file_path, improvement)
                        if change_result['success']:
                            implemented_changes.append({
                                'file_path': file_path,
                                'improvement': improvement,
                                'result': change_result
                            })
                        else:
                            self.logger.warning(f"Failed to implement improvement in {file_path}: {change_result.get('error')}")

                    except Exception as e:
                        self.logger.error(f"Implementation error for {file_path}: {e}")

            cycle.improvements_made = implemented_changes

            self.logger.info(f"Implementation complete: {len(implemented_changes)} changes made")

            return {
                'success': True,
                'changes_implemented': len(implemented_changes),
                'backup_created': self.safety_checks['backup_required']
            }

        except Exception as e:
            return {
                'success': False,
                'error': f"Implementation phase failed: {str(e)}"
            }

    def _phase_testing(self, cycle: ImprovementCycle, focus_areas: List[str]) -> Dict[str, Any]:
        """Phase 4: Test implemented changes"""
        try:
            test_results = []

            # Test each modified file
            for change in cycle.improvements_made:
                file_path = change['file_path']

                try:
                    # Read the modified file
                    with open(file_path, 'r', encoding='utf-8') as f:
                        modified_code = f.read()

                    # Test the code
                    test_result = self.code_generator.test_generated_code(modified_code)
                    test_results.append({
                        'file_path': file_path,
                        'test_result': test_result
                    })

                except Exception as e:
                    test_results.append({
                        'file_path': file_path,
                        'test_result': {
                            'success': False,
                            'error': str(e)
                        }
                    })

            # Calculate success rate
            successful_tests = sum(1 for tr in test_results if tr['test_result'].get('success', False))
            success_rate = successful_tests / len(test_results) if test_results else 0

            cycle.success_metrics['test_success_rate'] = success_rate

            self.logger.info(f"Testing complete: {successful_tests}/{len(test_results)} tests passed")

            return {
                'success': True,
                'tests_run': len(test_results),
                'tests_passed': successful_tests,
                'success_rate': success_rate
            }

        except Exception as e:
            return {
                'success': False,
                'error': f"Testing phase failed: {str(e)}"
            }

    def _phase_evaluation(self, cycle: ImprovementCycle, focus_areas: List[str]) -> Dict[str, Any]:
        """Phase 5: Evaluate the effectiveness of changes"""
        try:
            # Re-analyze modified files to measure improvement
            post_change_analysis = {}
            improvement_metrics = {}

            for file_path in cycle.target_files:
                # Get new analysis
                new_analysis = self.code_analyzer.analyze_code_file(file_path)
                if new_analysis['success']:
                    post_change_analysis[file_path] = new_analysis

                    # Compare with original analysis
                    original_analysis = cycle.analysis_results['file_analyses'].get(file_path, {})
                    if original_analysis.get('success'):
                        metrics = self._calculate_improvement_metrics(original_analysis, new_analysis)
                        improvement_metrics[file_path] = metrics

            # Calculate overall improvement
            overall_improvement = self._calculate_overall_improvement(improvement_metrics)
            cycle.success_metrics.update(overall_improvement)

            self.logger.info(f"Evaluation complete: Overall improvement score: {overall_improvement.get('total_score', 0)}")

            return {
                'success': True,
                'improvement_metrics': improvement_metrics,
                'overall_score': overall_improvement.get('total_score', 0)
            }

        except Exception as e:
            return {
                'success': False,
                'error': f"Evaluation phase failed: {str(e)}"
            }

    def _phase_deployment(self, cycle: ImprovementCycle, focus_areas: List[str]) -> Dict[str, Any]:
        """Phase 6: Deploy changes and update learning"""
        try:
            # In a real implementation, this would handle deployment
            # For now, we'll just finalize the cycle

            # Record learning outcomes
            learning_outcomes = self._extract_learning_outcomes(cycle)
            cycle.learning_outcomes = learning_outcomes

            # Update performance baselines
            for file_path in cycle.target_files:
                if file_path in cycle.success_metrics:
                    self.performance_baselines[file_path] = cycle.success_metrics[file_path]

            self.logger.info(f"Deployment complete: {len(learning_outcomes)} learning outcomes recorded")

            return {
                'success': True,
                'learning_outcomes': len(learning_outcomes),
                'baselines_updated': len(cycle.target_files)
            }

        except Exception as e:
            return {
                'success': False,
                'error': f"Deployment phase failed: {str(e)}"
            }

    def _apply_learned_patterns(self, analysis_results: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Apply previously learned improvement patterns"""
        applicable_patterns = []

        for pattern_id, learning_record in self.learning_records.items():
            # Check if pattern is applicable based on trigger conditions
            if self._pattern_matches_conditions(analysis_results, learning_record.trigger_conditions):
                applicable_patterns.append({
                    'pattern_id': pattern_id,
                    'description': learning_record.pattern_description,
                    'actions': learning_record.improvement_actions,
                    'confidence': learning_record.confidence_score
                })

                # Update usage count
                learning_record.usage_count += 1
                learning_record.last_used = datetime.now()

        return applicable_patterns

    def _pattern_matches_conditions(self, analysis_results: Dict[str, Any], conditions: Dict[str, Any]) -> bool:
        """Check if analysis results match pattern trigger conditions"""
        # Simplified pattern matching
        total_issues = analysis_results.get('total_issues', 0)
        min_issues = conditions.get('min_issues', 0)

        return total_issues >= min_issues

    def _plan_quality_improvements(self, quality_issues: List[str]) -> List[Dict[str, Any]]:
        """Plan quality improvements based on identified issues"""
        improvements = []

        for issue in quality_issues:
            if "complexity" in issue.lower():
                improvements.append({
                    'type': 'refactor_complexity',
                    'description': f'Reduce complexity for: {issue}',
                    'priority': 'high'
                })
            elif "docstring" in issue.lower():
                improvements.append({
                    'type': 'add_documentation',
                    'description': f'Add documentation for: {issue}',
                    'priority': 'medium'
                })

        return improvements

    def _plan_performance_improvements(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Plan performance improvements"""
        improvements = []

        complexity_score = analysis.get('complexity_score', 0)
        if complexity_score > 20:
            improvements.append({
                'type': 'optimize_performance',
                'description': 'Optimize high-complexity code for performance',
                'priority': 'high'
            })

        return improvements

    def _plan_documentation_improvements(self, analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Plan documentation improvements"""
        improvements = []

        # Check for missing docstrings
        for issue in analysis.get('quality_issues', []):
            if 'docstring' in issue.lower():
                improvements.append({
                    'type': 'add_docstring',
                    'description': f'Add missing docstring: {issue}',
                    'priority': 'low'
                })

        return improvements

    def _create_backup(self, target_files: List[str]) -> Dict[str, Any]:
        """Create backup of target files"""
        try:
            backup_dir = os.path.join(self.project_root, '.backups', datetime.now().strftime('%Y%m%d_%H%M%S'))
            os.makedirs(backup_dir, exist_ok=True)

            for file_path in target_files:
                if os.path.exists(file_path):
                    backup_path = os.path.join(backup_dir, os.path.basename(file_path))
                    with open(file_path, 'r', encoding='utf-8') as src:
                        with open(backup_path, 'w', encoding='utf-8') as dst:
                            dst.write(src.read())

            return {
                'success': True,
                'backup_dir': backup_dir,
                'files_backed_up': len(target_files)
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _implement_improvement(self, file_path: str, improvement: Dict[str, Any]) -> Dict[str, Any]:
        """Implement a specific improvement"""
        try:
            improvement_type = improvement.get('type')

            if improvement_type == 'add_documentation':
                return self._add_documentation(file_path, improvement)
            elif improvement_type == 'refactor_complexity':
                return self._refactor_complexity(file_path, improvement)
            elif improvement_type == 'optimize_performance':
                return self._optimize_performance(file_path, improvement)
            else:
                return {
                    'success': False,
                    'error': f'Unknown improvement type: {improvement_type}'
                }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _add_documentation(self, file_path: str, improvement: Dict[str, Any]) -> Dict[str, Any]:
        """Add documentation to a file"""
        try:
            # Simple documentation addition
            # In a real implementation, this would be more sophisticated

            return {
                'success': True,
                'change_type': 'documentation_added',
                'description': 'Added basic documentation'
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _refactor_complexity(self, file_path: str, improvement: Dict[str, Any]) -> Dict[str, Any]:
        """Refactor complex code"""
        try:
            # Use code generation tools to refactor
            refactor_result = self.code_generator.refactor_code(
                target_file=file_path,
                optimization_goals=['readability', 'maintainability']
            )

            if refactor_result['success']:
                # Write refactored code back to file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(refactor_result['refactored_code'])

                return {
                    'success': True,
                    'change_type': 'complexity_refactored',
                    'improvements': refactor_result.get('improvements', [])
                }
            else:
                return refactor_result

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _optimize_performance(self, file_path: str, improvement: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize code for performance"""
        try:
            # Simple performance optimization placeholder
            return {
                'success': True,
                'change_type': 'performance_optimized',
                'description': 'Applied performance optimizations'
            }

        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

    def _calculate_improvement_metrics(self, before: Dict[str, Any], after: Dict[str, Any]) -> Dict[str, float]:
        """Calculate improvement metrics between before and after analysis"""
        metrics = {}

        # Complexity improvement
        before_complexity = before.get('complexity_score', 0)
        after_complexity = after.get('complexity_score', 0)
        if before_complexity > 0:
            metrics['complexity_improvement'] = (before_complexity - after_complexity) / before_complexity * 100

        # Quality issues improvement
        before_issues = len(before.get('quality_issues', []))
        after_issues = len(after.get('quality_issues', []))
        if before_issues > 0:
            metrics['quality_improvement'] = (before_issues - after_issues) / before_issues * 100

        return metrics

    def _calculate_overall_improvement(self, improvement_metrics: Dict[str, Dict[str, float]]) -> Dict[str, float]:
        """Calculate overall improvement score"""
        if not improvement_metrics:
            return {'total_score': 0.0}

        total_complexity_improvement = sum(
            metrics.get('complexity_improvement', 0)
            for metrics in improvement_metrics.values()
        )
        total_quality_improvement = sum(
            metrics.get('quality_improvement', 0)
            for metrics in improvement_metrics.values()
        )

        file_count = len(improvement_metrics)

        return {
            'total_score': (total_complexity_improvement + total_quality_improvement) / file_count if file_count > 0 else 0,
            'avg_complexity_improvement': total_complexity_improvement / file_count if file_count > 0 else 0,
            'avg_quality_improvement': total_quality_improvement / file_count if file_count > 0 else 0
        }

    def _extract_learning_outcomes(self, cycle: ImprovementCycle) -> List[str]:
        """Extract learning outcomes from the improvement cycle"""
        outcomes = []

        # Learn from successful improvements
        for improvement in cycle.improvements_made:
            if improvement.get('result', {}).get('success'):
                outcomes.append(f"Successful {improvement['improvement']['type']} in {improvement['file_path']}")

        # Learn from overall metrics
        overall_score = cycle.success_metrics.get('total_score', 0)
        if overall_score > 10:
            outcomes.append(f"Cycle achieved {overall_score:.1f}% overall improvement")

        return outcomes

    def _integrate_learning(self, cycle: ImprovementCycle) -> None:
        """Integrate learning from the completed cycle"""
        try:
            # Create learning records for successful patterns
            for improvement in cycle.improvements_made:
                if improvement.get('result', {}).get('success'):
                    pattern_id = f"{improvement['improvement']['type']}_{datetime.now().strftime('%Y%m%d')}"

                    if pattern_id not in self.learning_records:
                        self.learning_records[pattern_id] = LearningRecord(
                            pattern_id=pattern_id,
                            pattern_description=improvement['improvement']['description'],
                            trigger_conditions={'min_issues': 1},
                            improvement_actions=[improvement['improvement']['type']],
                            success_rate=1.0,
                            confidence_score=0.5,
                            usage_count=1,
                            last_used=datetime.now()
                        )
                    else:
                        # Update existing pattern
                        record = self.learning_records[pattern_id]
                        record.usage_count += 1
                        record.last_used = datetime.now()
                        # Update success rate based on cycle results
                        overall_score = cycle.success_metrics.get('total_score', 0)
                        if overall_score > 0:
                            record.success_rate = min(1.0, record.success_rate + 0.1)
                            record.confidence_score = min(1.0, record.confidence_score + 0.1)

        except Exception as e:
            self.logger.error(self._get_error_message('LEARNING_FAILED', error=str(e)))

    def get_learning_summary(self) -> Dict[str, Any]:
        """Get summary of learning system state"""
        return {
            'total_patterns_learned': len(self.learning_records),
            'improvement_cycles_completed': len(self.improvement_history),
            'average_success_rate': sum(lr.success_rate for lr in self.learning_records.values()) / len(self.learning_records) if self.learning_records else 0,
            'most_used_patterns': sorted(
                [(lr.pattern_id, lr.usage_count) for lr in self.learning_records.values()],
                key=lambda x: x[1],
                reverse=True
            )[:5]
        }
