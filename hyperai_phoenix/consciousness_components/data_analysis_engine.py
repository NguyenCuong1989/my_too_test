"""
Data Analysis Engine - Advanced Analytics Component
==================================================
Comprehensive data analysis and insights generation system
"""

import json
import asyncio
import numpy as np
import statistics
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from collections import defaultdict, Counter

class DataAnalysisEngine:
    """
    Advanced Data Analysis Engine
    Provides comprehensive analytics capabilities for all system components
    """

    def __init__(self):
        self.datasets = {}
        self.analysis_history = {}
        self.statistical_models = {}
        self.data_pipelines = {}
        self.insights_cache = {}
        self.analysis_templates = {}

        # Analysis capabilities
        self.analysis_types = {
            'descriptive': ['summary_statistics', 'distribution_analysis', 'correlation_analysis'],
            'diagnostic': ['anomaly_detection', 'root_cause_analysis', 'pattern_analysis'],
            'predictive': ['trend_analysis', 'forecasting', 'predictive_modeling'],
            'prescriptive': ['optimization', 'recommendation', 'scenario_analysis']
        }

        # Performance metrics
        self.metrics = {
            'analysis_accuracy': 0.0,
            'processing_speed': 0.0,
            'insight_quality': 0.0,
            'data_coverage': 0.0
        }

        self.initialize_analysis_templates()

    def initialize_analysis_templates(self):
        """Khởi tạo analysis templates"""

        self.analysis_templates = {
            'learning_progress': {
                'dimensions': ['time', 'performance', 'engagement'],
                'metrics': ['completion_rate', 'accuracy', 'learning_velocity'],
                'visualizations': ['time_series', 'progress_chart', 'heatmap']
            },
            'behavior_analysis': {
                'dimensions': ['interaction_patterns', 'usage_frequency', 'preference'],
                'metrics': ['session_duration', 'click_through_rate', 'retention'],
                'visualizations': ['behavior_flow', 'usage_heatmap', 'cohort_analysis']
            },
            'performance_optimization': {
                'dimensions': ['efficiency', 'resource_usage', 'bottlenecks'],
                'metrics': ['throughput', 'latency', 'error_rate'],
                'visualizations': ['performance_dashboard', 'resource_utilization', 'error_analysis']
            }
        }

    async def register_dataset(self, dataset_name: str, data: List[Dict[str, Any]], metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Đăng ký dataset để phân tích"""

        # Validate data
        if not data or not isinstance(data, list):
            return {'error': 'invalid_data_format'}

        # Process and store dataset
        processed_data = await self._process_raw_data(data, metadata)

        dataset_info = {
            'name': dataset_name,
            'data': processed_data,
            'metadata': metadata,
            'registered_at': datetime.now().isoformat(),
            'record_count': len(data),
            'features': await self._extract_feature_info(data),
            'quality_score': await self._assess_data_quality(data)
        }

        self.datasets[dataset_name] = dataset_info

        return {
            'dataset_name': dataset_name,
            'status': 'registered',
            'record_count': len(data),
            'quality_score': dataset_info['quality_score'],
            'features_detected': len(dataset_info['features'])
        }

    async def _process_raw_data(self, data: List[Dict[str, Any]], metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Xử lý raw data"""

        processed = []

        for record in data:
            processed_record = {}

            for key, value in record.items():
                # Type conversion and cleaning
                processed_record[key] = await self._clean_field_value(value, key, metadata)

            # Add derived fields
            processed_record['_timestamp'] = record.get('timestamp', datetime.now().isoformat())
            processed_record['_record_id'] = hash(str(record)) % 1000000

            processed.append(processed_record)

        return processed

    async def _clean_field_value(self, value: Any, field_name: str, metadata: Dict[str, Any]) -> Any:
        """Clean individual field value"""

        field_type = metadata.get('field_types', {}).get(field_name, 'auto')

        try:
            if field_type == 'numeric' or (field_type == 'auto' and isinstance(value, (int, float))):
                return float(value) if value is not None else 0.0
            elif field_type == 'categorical' or (field_type == 'auto' and isinstance(value, str)):
                return str(value).strip().lower() if value is not None else 'unknown'
            elif field_type == 'boolean':
                return bool(value) if value is not None else False
            else:
                return value
        except (ValueError, TypeError):
            return None

    async def _extract_feature_info(self, data: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
        """Extract feature information từ data"""

        features = {}

        if not data:
            return features

        # Analyze each field
        for field in data[0].keys():
            values = [record.get(field) for record in data if record.get(field) is not None]

            if not values:
                continue

            feature_info = {
                'type': await self._detect_field_type(values),
                'non_null_count': len(values),
                'null_count': len(data) - len(values),
                'unique_count': len(set(str(v) for v in values))
            }

            # Type-specific statistics
            if feature_info['type'] == 'numeric':
                feature_info.update(await self._calculate_numeric_stats(values))
            elif feature_info['type'] == 'categorical':
                feature_info.update(await self._calculate_categorical_stats(values))

            features[field] = feature_info

        return features

    async def _detect_field_type(self, values: List[Any]) -> str:
        """Detect field type từ values"""

        numeric_count = sum(1 for v in values if isinstance(v, (int, float)))
        string_count = sum(1 for v in values if isinstance(v, str))

        if numeric_count > len(values) * 0.8:
            return 'numeric'
        elif string_count > len(values) * 0.8:
            return 'categorical'
        else:
            return 'mixed'

    async def _calculate_numeric_stats(self, values: List[Any]) -> Dict[str, float]:
        """Calculate numeric statistics"""

        numeric_values = [float(v) for v in values if isinstance(v, (int, float))]

        if not numeric_values:
            return {}

        return {
            'mean': statistics.mean(numeric_values),
            'median': statistics.median(numeric_values),
            'std': statistics.stdev(numeric_values) if len(numeric_values) > 1 else 0.0,
            'min': min(numeric_values),
            'max': max(numeric_values),
            'q25': np.percentile(numeric_values, 25),
            'q75': np.percentile(numeric_values, 75)
        }

    async def _calculate_categorical_stats(self, values: List[Any]) -> Dict[str, Any]:
        """Calculate categorical statistics"""

        string_values = [str(v) for v in values]
        value_counts = Counter(string_values)

        return {
            'most_frequent': value_counts.most_common(1)[0] if value_counts else ('', 0),
            'value_counts': dict(value_counts.most_common(10)),  # Top 10
            'entropy': await self._calculate_entropy(list(value_counts.values()))
        }

    async def _calculate_entropy(self, counts: List[int]) -> float:
        """Calculate entropy for categorical data"""

        if not counts:
            return 0.0

        total = sum(counts)
        probabilities = [count / total for count in counts]

        entropy = -sum(p * np.log2(p) for p in probabilities if p > 0)
        return entropy

    async def _assess_data_quality(self, data: List[Dict[str, Any]]) -> float:
        """Assess overall data quality"""

        if not data:
            return 0.0

        total_fields = len(data[0].keys()) if data else 0
        total_records = len(data)

        # Count missing values
        missing_count = 0
        for record in data:
            for value in record.values():
                if value is None or value == '':
                    missing_count += 1

        total_values = total_fields * total_records
        completeness = 1.0 - (missing_count / total_values) if total_values > 0 else 0.0

        # Additional quality factors
        consistency_score = 0.9  # Simulated
        validity_score = 0.85    # Simulated

        overall_score = (completeness * 0.4 + consistency_score * 0.3 + validity_score * 0.3)
        return round(overall_score, 3)

    async def analyze_dataset(self, dataset_name: str, analysis_type: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Thực hiện phân tích dataset"""

        if dataset_name not in self.datasets:
            return {'error': 'dataset_not_found'}

        dataset = self.datasets[dataset_name]
        data = dataset['data']

        analysis_id = f"analysis_{int(datetime.now().timestamp())}"

        # Perform analysis based on type
        if analysis_type == 'descriptive':
            results = await self._descriptive_analysis(data, config)
        elif analysis_type == 'diagnostic':
            results = await self._diagnostic_analysis(data, config)
        elif analysis_type == 'predictive':
            results = await self._predictive_analysis(data, config)
        elif analysis_type == 'prescriptive':
            results = await self._prescriptive_analysis(data, config)
        else:
            return {'error': 'unsupported_analysis_type'}

        # Store analysis results
        analysis_record = {
            'id': analysis_id,
            'dataset_name': dataset_name,
            'analysis_type': analysis_type,
            'config': config,
            'results': results,
            'timestamp': datetime.now().isoformat(),
            'execution_time': results.get('execution_time', 0.0)
        }

        self.analysis_history[analysis_id] = analysis_record

        return {
            'analysis_id': analysis_id,
            'dataset_name': dataset_name,
            'analysis_type': analysis_type,
            'results': results,
            'insights': await self._generate_insights(results, analysis_type)
        }

    async def _descriptive_analysis(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Descriptive analysis - mô tả dữ liệu"""

        start_time = datetime.now()

        results = {
            'summary_statistics': await self._calculate_summary_statistics(data),
            'distribution_analysis': await self._analyze_distributions(data),
            'correlation_analysis': await self._analyze_correlations(data),
            'data_profile': await self._create_data_profile(data)
        }

        end_time = datetime.now()
        results['execution_time'] = (end_time - start_time).total_seconds()

        return results

    async def _calculate_summary_statistics(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate summary statistics"""

        if not data:
            return {}

        numeric_fields = []
        for field, values in self._group_by_field(data).items():
            if all(isinstance(v, (int, float)) for v in values if v is not None):
                numeric_fields.append(field)

        summary = {
            'total_records': len(data),
            'total_fields': len(data[0].keys()) if data else 0,
            'numeric_fields': len(numeric_fields),
            'field_statistics': {}
        }

        # Calculate stats for each numeric field
        for field in numeric_fields:
            values = [record[field] for record in data if record.get(field) is not None]
            if values:
                summary['field_statistics'][field] = await self._calculate_numeric_stats(values)

        return summary

    def _group_by_field(self, data: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
        """Group data by field"""
        grouped = defaultdict(list)

        for record in data:
            for field, value in record.items():
                grouped[field].append(value)

        return dict(grouped)

    async def _analyze_distributions(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze value distributions"""

        distributions = {}

        for field, values in self._group_by_field(data).items():
            # Skip internal fields
            if field.startswith('_'):
                continue

            non_null_values = [v for v in values if v is not None]

            if not non_null_values:
                continue

            if all(isinstance(v, (int, float)) for v in non_null_values):
                # Numeric distribution
                distributions[field] = await self._analyze_numeric_distribution(non_null_values)
            else:
                # Categorical distribution
                distributions[field] = await self._analyze_categorical_distribution(non_null_values)

        return distributions

    async def _analyze_numeric_distribution(self, values: List[float]) -> Dict[str, Any]:
        """Analyze numeric distribution"""

        values = [float(v) for v in values]

        # Create histogram bins
        num_bins = min(20, int(np.sqrt(len(values))))
        hist, bin_edges = np.histogram(values, bins=num_bins)

        return {
            'type': 'numeric',
            'histogram': {
                'counts': hist.tolist(),
                'bin_edges': bin_edges.tolist()
            },
            'statistics': await self._calculate_numeric_stats(values),
            'normality_test': await self._test_normality(values)
        }

    async def _analyze_categorical_distribution(self, values: List[Any]) -> Dict[str, Any]:
        """Analyze categorical distribution"""

        value_counts = Counter(str(v) for v in values)

        return {
            'type': 'categorical',
            'value_counts': dict(value_counts.most_common(20)),
            'unique_values': len(value_counts),
            'entropy': await self._calculate_entropy(list(value_counts.values()))
        }

    async def _test_normality(self, values: List[float]) -> Dict[str, float]:
        """Test for normality (simplified)"""

        if len(values) < 3:
            return {'p_value': 1.0, 'is_normal': False}

        # Simplified normality test using skewness and kurtosis
        mean_val = statistics.mean(values)
        std_val = statistics.stdev(values) if len(values) > 1 else 1.0

        # Calculate skewness approximation
        skewness = sum(((v - mean_val) / std_val) ** 3 for v in values) / len(values)

        # Simple threshold-based test
        is_normal = abs(skewness) < 1.0
        p_value = max(0.001, 1.0 - abs(skewness))

        return {
            'skewness': skewness,
            'p_value': p_value,
            'is_normal': is_normal
        }

    async def _analyze_correlations(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze correlations between numeric fields"""

        # Extract numeric fields
        numeric_data = {}
        for field, values in self._group_by_field(data).items():
            if field.startswith('_'):
                continue

            numeric_values = []
            for v in values:
                try:
                    numeric_values.append(float(v))
                except (ValueError, TypeError):
                    numeric_values.append(None)

            # Keep field if at least 50% values are numeric
            valid_count = sum(1 for v in numeric_values if v is not None)
            if valid_count >= len(numeric_values) * 0.5:
                numeric_data[field] = numeric_values

        correlations = {}

        # Calculate pairwise correlations
        fields = list(numeric_data.keys())
        for i, field1 in enumerate(fields):
            for field2 in fields[i+1:]:
                correlation = await self._calculate_correlation(
                    numeric_data[field1],
                    numeric_data[field2]
                )
                correlations[f"{field1}_vs_{field2}"] = correlation

        return {
            'pairwise_correlations': correlations,
            'strong_correlations': {k: v for k, v in correlations.items() if abs(v) > 0.7}
        }

    async def _calculate_correlation(self, values1: List[Optional[float]], values2: List[Optional[float]]) -> float:
        """Calculate correlation between two numeric arrays"""

        # Filter out None values
        paired_values = [(v1, v2) for v1, v2 in zip(values1, values2)
                        if v1 is not None and v2 is not None]

        if len(paired_values) < 3:
            return 0.0

        x_vals = [pair[0] for pair in paired_values]
        y_vals = [pair[1] for pair in paired_values]

        # Calculate Pearson correlation
        try:
            n = len(x_vals)
            sum_x = sum(x_vals)
            sum_y = sum(y_vals)
            sum_xy = sum(x * y for x, y in zip(x_vals, y_vals))
            sum_x2 = sum(x ** 2 for x in x_vals)
            sum_y2 = sum(y ** 2 for y in y_vals)

            numerator = n * sum_xy - sum_x * sum_y
            denominator = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5

            if denominator == 0:
                return 0.0

            correlation = numerator / denominator
            return round(correlation, 4)

        except (ValueError, ZeroDivisionError):
            return 0.0

    async def _create_data_profile(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Create comprehensive data profile"""

        if not data:
            return {}

        profile = {
            'record_count': len(data),
            'field_count': len(data[0].keys()) if data else 0,
            'data_types': {},
            'missing_values': {},
            'unique_values': {},
            'data_quality_issues': []
        }

        # Analyze each field
        for field in data[0].keys():
            values = [record.get(field) for record in data]
            non_null_values = [v for v in values if v is not None and v != '']

            profile['data_types'][field] = await self._detect_field_type(non_null_values)
            profile['missing_values'][field] = len(values) - len(non_null_values)
            profile['unique_values'][field] = len(set(str(v) for v in non_null_values))

            # Identify quality issues
            missing_rate = profile['missing_values'][field] / len(values)
            if missing_rate > 0.5:
                profile['data_quality_issues'].append(f"{field}: high_missing_rate ({missing_rate:.2%})")

        return profile

    async def _diagnostic_analysis(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Diagnostic analysis - tìm nguyên nhân và patterns"""

        start_time = datetime.now()

        results = {
            'anomaly_detection': await self._detect_anomalies(data, config),
            'pattern_analysis': await self._analyze_patterns(data, config),
            'root_cause_analysis': await self._root_cause_analysis(data, config)
        }

        end_time = datetime.now()
        results['execution_time'] = (end_time - start_time).total_seconds()

        return results

    async def _detect_anomalies(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Detect anomalies in data"""

        anomalies = {
            'statistical_outliers': [],
            'pattern_anomalies': [],
            'value_anomalies': []
        }

        # Statistical outlier detection for numeric fields
        for field, values in self._group_by_field(data).items():
            if field.startswith('_'):
                continue

            numeric_values = []
            for i, v in enumerate(values):
                try:
                    numeric_values.append((i, float(v)))
                except (ValueError, TypeError):
                    continue

            if len(numeric_values) < 10:
                continue

            # IQR method for outlier detection
            vals = [v[1] for v in numeric_values]
            q1 = np.percentile(vals, 25)
            q3 = np.percentile(vals, 75)
            iqr = q3 - q1

            lower_bound = q1 - 1.5 * iqr
            upper_bound = q3 + 1.5 * iqr

            outliers = [(i, v) for i, v in numeric_values if v < lower_bound or v > upper_bound]

            if outliers:
                anomalies['statistical_outliers'].append({
                    'field': field,
                    'outliers': outliers[:10],  # Limit to 10
                    'bounds': {'lower': lower_bound, 'upper': upper_bound}
                })

        return anomalies

    async def _analyze_patterns(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze patterns trong data"""

        patterns = {
            'temporal_patterns': await self._analyze_temporal_patterns(data),
            'frequency_patterns': await self._analyze_frequency_patterns(data),
            'sequence_patterns': await self._analyze_sequence_patterns(data)
        }

        return patterns

    async def _analyze_temporal_patterns(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze temporal patterns"""

        # Look for timestamp fields
        timestamp_fields = []
        for field in data[0].keys() if data else []:
            if 'time' in field.lower() or 'date' in field.lower() or field == '_timestamp':
                timestamp_fields.append(field)

        temporal_patterns = {}

        for field in timestamp_fields:
            timestamps = []
            for record in data:
                ts_value = record.get(field)
                if ts_value:
                    try:
                        # Parse timestamp
                        if isinstance(ts_value, str):
                            dt = datetime.fromisoformat(ts_value.replace('Z', '+00:00'))
                        else:
                            dt = datetime.fromtimestamp(float(ts_value))
                        timestamps.append(dt)
                    except (ValueError, TypeError):
                        continue

            if len(timestamps) > 1:
                # Analyze temporal distribution
                timestamps.sort()
                intervals = [(timestamps[i+1] - timestamps[i]).total_seconds()
                           for i in range(len(timestamps)-1)]

                temporal_patterns[field] = {
                    'record_count': len(timestamps),
                    'time_span': (timestamps[-1] - timestamps[0]).total_seconds(),
                    'average_interval': statistics.mean(intervals) if intervals else 0,
                    'pattern_type': await self._classify_temporal_pattern(intervals)
                }

        return temporal_patterns

    async def _classify_temporal_pattern(self, intervals: List[float]) -> str:
        """Classify temporal pattern type"""

        if not intervals:
            return 'unknown'

        cv = statistics.stdev(intervals) / statistics.mean(intervals) if statistics.mean(intervals) > 0 else 0

        if cv < 0.1:
            return 'regular'
        elif cv < 0.5:
            return 'semi_regular'
        else:
            return 'irregular'

    async def _analyze_frequency_patterns(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze frequency patterns"""

        frequency_patterns = {}

        for field in data[0].keys() if data else []:
            if field.startswith('_'):
                continue

            values = [str(record.get(field, '')) for record in data]
            value_counts = Counter(values)

            # Analyze frequency distribution
            frequencies = list(value_counts.values())

            if len(frequencies) > 1:
                frequency_patterns[field] = {
                    'unique_values': len(value_counts),
                    'most_frequent': value_counts.most_common(1)[0],
                    'frequency_distribution': {
                        'mean': statistics.mean(frequencies),
                        'std': statistics.stdev(frequencies) if len(frequencies) > 1 else 0,
                        'concentration': max(frequencies) / sum(frequencies)
                    }
                }

        return frequency_patterns

    async def _analyze_sequence_patterns(self, data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze sequence patterns"""

        # Simple sequence analysis
        sequences = {}

        # Look for fields that might represent sequences
        for field in data[0].keys() if data else []:
            values = [record.get(field) for record in data]

            # Analyze transitions between consecutive values
            transitions = defaultdict(int)
            for i in range(len(values) - 1):
                if values[i] is not None and values[i+1] is not None:
                    transition = f"{values[i]} -> {values[i+1]}"
                    transitions[transition] += 1

            if transitions:
                sequences[field] = {
                    'total_transitions': sum(transitions.values()),
                    'unique_transitions': len(transitions),
                    'most_common_transitions': dict(Counter(transitions).most_common(5))
                }

        return sequences

    async def _root_cause_analysis(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Root cause analysis"""

        target_field = config.get('target_field')
        if not target_field or target_field not in (data[0].keys() if data else []):
            return {'error': 'target_field_not_specified_or_found'}

        # Analyze relationships with target field
        root_causes = {
            'correlation_analysis': {},
            'category_analysis': {},
            'statistical_tests': {}
        }

        target_values = [record.get(target_field) for record in data]

        # Correlation with other numeric fields
        for field in data[0].keys() if data else []:
            if field == target_field or field.startswith('_'):
                continue

            field_values = [record.get(field) for record in data]

            # Try correlation analysis
            correlation = await self._calculate_correlation(target_values, field_values)
            if abs(correlation) > 0.3:  # Significant correlation
                root_causes['correlation_analysis'][field] = {
                    'correlation': correlation,
                    'strength': 'strong' if abs(correlation) > 0.7 else 'moderate'
                }

        return root_causes

    async def _predictive_analysis(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Predictive analysis"""

        start_time = datetime.now()

        results = {
            'trend_analysis': await self._analyze_trends(data, config),
            'forecasting': await self._forecast_values(data, config),
            'predictive_modeling': await self._build_predictive_models(data, config)
        }

        end_time = datetime.now()
        results['execution_time'] = (end_time - start_time).total_seconds()

        return results

    async def _analyze_trends(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze trends in data"""

        trends = {}

        # Look for numeric fields to analyze trends
        for field in data[0].keys() if data else []:
            if field.startswith('_'):
                continue

            values = []
            for record in data:
                try:
                    values.append(float(record.get(field, 0)))
                except (ValueError, TypeError):
                    continue

            if len(values) < 5:
                continue

            # Simple trend analysis using linear regression
            x_values = list(range(len(values)))
            trend_slope = await self._calculate_trend_slope(x_values, values)

            trends[field] = {
                'trend_slope': trend_slope,
                'trend_direction': 'increasing' if trend_slope > 0.01 else 'decreasing' if trend_slope < -0.01 else 'stable',
                'strength': abs(trend_slope),
                'data_points': len(values)
            }

        return trends

    async def _calculate_trend_slope(self, x_values: List[int], y_values: List[float]) -> float:
        """Calculate trend slope using simple linear regression"""

        if len(x_values) != len(y_values) or len(x_values) < 2:
            return 0.0

        n = len(x_values)
        sum_x = sum(x_values)
        sum_y = sum(y_values)
        sum_xy = sum(x * y for x, y in zip(x_values, y_values))
        sum_x2 = sum(x ** 2 for x in x_values)

        denominator = n * sum_x2 - sum_x ** 2
        if denominator == 0:
            return 0.0

        slope = (n * sum_xy - sum_x * sum_y) / denominator
        return slope

    async def _forecast_values(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Forecast future values"""

        forecast_periods = config.get('forecast_periods', 5)
        forecasts = {}

        # Simple trend-based forecasting
        for field in data[0].keys() if data else []:
            if field.startswith('_'):
                continue

            values = []
            for record in data:
                try:
                    values.append(float(record.get(field, 0)))
                except (ValueError, TypeError):
                    continue

            if len(values) < 3:
                continue

            # Calculate trend and forecast
            x_values = list(range(len(values)))
            slope = await self._calculate_trend_slope(x_values, values)
            last_value = values[-1]

            forecast_values = []
            for i in range(1, forecast_periods + 1):
                forecast_value = last_value + slope * i
                forecast_values.append(forecast_value)

            forecasts[field] = {
                'forecast_values': forecast_values,
                'forecast_periods': forecast_periods,
                'confidence': min(1.0, len(values) / 20.0),  # More data = higher confidence
                'method': 'linear_trend'
            }

        return forecasts

    async def _build_predictive_models(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Build predictive models"""

        target_field = config.get('target_field')
        if not target_field:
            return {'error': 'target_field_required'}

        # Simple predictive model based on correlations
        models = {}

        # Find best predictors based on correlation
        predictors = {}
        target_values = [record.get(target_field) for record in data]

        for field in data[0].keys() if data else []:
            if field == target_field or field.startswith('_'):
                continue

            field_values = [record.get(field) for record in data]
            correlation = await self._calculate_correlation(target_values, field_values)

            if abs(correlation) > 0.3:
                predictors[field] = correlation

        if predictors:
            best_predictor = max(predictors.items(), key=lambda x: abs(x[1]))

            models['best_predictor_model'] = {
                'target_field': target_field,
                'best_predictor': best_predictor[0],
                'correlation': best_predictor[1],
                'model_type': 'correlation_based',
                'all_predictors': predictors
            }

        return models

    async def _prescriptive_analysis(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Prescriptive analysis - recommendations"""

        start_time = datetime.now()

        results = {
            'optimization_recommendations': await self._generate_optimization_recommendations(data, config),
            'action_recommendations': await self._generate_action_recommendations(data, config),
            'scenario_analysis': await self._perform_scenario_analysis(data, config)
        }

        end_time = datetime.now()
        results['execution_time'] = (end_time - start_time).total_seconds()

        return results

    async def _generate_optimization_recommendations(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate optimization recommendations"""

        recommendations = []

        # Analyze performance metrics
        for field in data[0].keys() if data else []:
            if field.startswith('_') or 'performance' not in field.lower():
                continue

            values = []
            for record in data:
                try:
                    values.append(float(record.get(field, 0)))
                except (ValueError, TypeError):
                    continue

            if len(values) < 5:
                continue

            mean_value = statistics.mean(values)
            std_value = statistics.stdev(values) if len(values) > 1 else 0

            # Generate recommendations based on performance
            if std_value > mean_value * 0.3:  # High variability
                recommendations.append({
                    'type': 'reduce_variability',
                    'field': field,
                    'current_cv': std_value / mean_value if mean_value > 0 else 0,
                    'target_cv': 0.2,
                    'priority': 'high'
                })

            if mean_value < 0.7:  # Low performance (assuming 0-1 scale)
                recommendations.append({
                    'type': 'improve_performance',
                    'field': field,
                    'current_value': mean_value,
                    'target_value': 0.8,
                    'priority': 'medium'
                })

        return recommendations

    async def _generate_action_recommendations(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate actionable recommendations"""

        recommendations = []

        # Data quality recommendations
        data_profile = await self._create_data_profile(data)

        for field, missing_count in data_profile.get('missing_values', {}).items():
            missing_rate = missing_count / len(data) if data else 0

            if missing_rate > 0.2:
                recommendations.append({
                    'type': 'improve_data_quality',
                    'action': 'reduce_missing_values',
                    'field': field,
                    'current_missing_rate': missing_rate,
                    'target_missing_rate': 0.1,
                    'priority': 'high' if missing_rate > 0.5 else 'medium'
                })

        # Performance optimization recommendations
        recommendations.append({
            'type': 'data_collection',
            'action': 'increase_data_frequency',
            'rationale': 'more_frequent_data_improves_insights',
            'priority': 'low'
        })

        return recommendations

    async def _perform_scenario_analysis(self, data: List[Dict[str, Any]], config: Dict[str, Any]) -> Dict[str, Any]:
        """Perform scenario analysis"""

        scenarios = {}

        # Best case scenario
        scenarios['best_case'] = {
            'description': 'optimal_performance_achieved',
            'expected_improvements': {
                'data_quality': 0.95,
                'performance_metrics': 0.9,
                'efficiency_gains': 0.25
            }
        }

        # Worst case scenario
        scenarios['worst_case'] = {
            'description': 'performance_degradation',
            'expected_impacts': {
                'data_quality': 0.6,
                'performance_metrics': 0.5,
                'efficiency_losses': 0.3
            }
        }

        # Most likely scenario
        scenarios['most_likely'] = {
            'description': 'gradual_improvement',
            'expected_outcomes': {
                'data_quality': 0.8,
                'performance_metrics': 0.75,
                'efficiency_gains': 0.1
            }
        }

        return scenarios

    async def _generate_insights(self, results: Dict[str, Any], analysis_type: str) -> List[str]:
        """Generate insights từ analysis results"""

        insights = []

        if analysis_type == 'descriptive':
            # Descriptive insights
            summary = results.get('summary_statistics', {})
            if summary.get('total_records', 0) > 1000:
                insights.append('large_dataset_provides_robust_analysis')

            correlations = results.get('correlation_analysis', {}).get('strong_correlations', {})
            if correlations:
                insights.append(f'found_{len(correlations)}_strong_correlations')

        elif analysis_type == 'diagnostic':
            # Diagnostic insights
            anomalies = results.get('anomaly_detection', {}).get('statistical_outliers', [])
            if anomalies:
                insights.append(f'detected_{len(anomalies)}_fields_with_outliers')

        elif analysis_type == 'predictive':
            # Predictive insights
            trends = results.get('trend_analysis', {})
            increasing_trends = sum(1 for trend in trends.values()
                                  if trend.get('trend_direction') == 'increasing')
            if increasing_trends:
                insights.append(f'{increasing_trends}_metrics_showing_positive_trends')

        elif analysis_type == 'prescriptive':
            # Prescriptive insights
            recommendations = results.get('optimization_recommendations', [])
            high_priority = sum(1 for rec in recommendations if rec.get('priority') == 'high')
            if high_priority:
                insights.append(f'{high_priority}_high_priority_optimizations_identified')

        if not insights:
            insights.append('analysis_completed_successfully')

        return insights

    async def get_analysis_summary(self, analysis_id: str) -> Dict[str, Any]:
        """Get summary của analysis"""

        if analysis_id not in self.analysis_history:
            return {'error': 'analysis_not_found'}

        analysis = self.analysis_history[analysis_id]

        summary = {
            'analysis_id': analysis_id,
            'dataset_name': analysis['dataset_name'],
            'analysis_type': analysis['analysis_type'],
            'timestamp': analysis['timestamp'],
            'execution_time': analysis['execution_time'],
            'key_findings': await self._extract_key_findings(analysis['results']),
            'recommendations': await self._extract_recommendations(analysis['results']),
            'data_quality_score': await self._calculate_analysis_quality_score(analysis['results'])
        }

        return summary

    async def _extract_key_findings(self, results: Dict[str, Any]) -> List[str]:
        """Extract key findings từ results"""

        findings = []

        # Extract findings based on result structure
        if 'summary_statistics' in results:
            stats = results['summary_statistics']
            findings.append(f"analyzed_{stats.get('total_records', 0)}_records")

        if 'anomaly_detection' in results:
            outliers = results['anomaly_detection'].get('statistical_outliers', [])
            if outliers:
                findings.append(f"found_outliers_in_{len(outliers)}_fields")

        if 'trend_analysis' in results:
            trends = results['trend_analysis']
            positive_trends = sum(1 for trend in trends.values()
                                if trend.get('trend_direction') == 'increasing')
            if positive_trends:
                findings.append(f"{positive_trends}_metrics_trending_upward")

        return findings or ['analysis_completed']

    async def _extract_recommendations(self, results: Dict[str, Any]) -> List[str]:
        """Extract recommendations từ results"""

        recommendations = []

        if 'optimization_recommendations' in results:
            opt_recs = results['optimization_recommendations']
            high_priority = [rec for rec in opt_recs if rec.get('priority') == 'high']
            recommendations.extend([rec.get('type', 'optimization') for rec in high_priority[:3]])

        if 'action_recommendations' in results:
            action_recs = results['action_recommendations']
            recommendations.extend([rec.get('action', 'improvement') for rec in action_recs[:2]])

        return recommendations or ['continue_monitoring']

    async def _calculate_analysis_quality_score(self, results: Dict[str, Any]) -> float:
        """Calculate quality score của analysis"""

        score = 0.7  # Base score

        # Increase score based on completeness
        if 'summary_statistics' in results:
            score += 0.1
        if 'correlation_analysis' in results:
            score += 0.1
        if 'anomaly_detection' in results:
            score += 0.1

        return min(1.0, score)

# Global instance
data_analysis_engine = DataAnalysisEngine()

async def create_data_analysis_engine():
    """Tạo và khởi tạo data analysis engine"""

    return {
        "component": "Data Analysis Engine",
        "location": "support_systems",
        "status": "active",
        "capabilities": [
            "descriptive_analysis",
            "diagnostic_analysis",
            "predictive_analysis",
            "prescriptive_analysis",
            "anomaly_detection",
            "correlation_analysis",
            "trend_analysis",
            "data_profiling"
        ],
        "analysis_types": data_analysis_engine.analysis_types,
        "instance": data_analysis_engine
    }
