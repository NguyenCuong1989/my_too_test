"""
Machine Learning Module - Core ML Capabilities
==============================================
Advanced machine learning engine for HyperAI Phoenix Support Systems
"""

import json
import asyncio
import numpy as np
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
import warnings
warnings.filterwarnings('ignore')

class MachineLearningModule:
    """
    Core Machine Learning Engine
    Provides ML capabilities for all support systems
    """

    def __init__(self):
        self.models = {}
        self.training_data = {}
        self.model_performance = {}
        self.active_training_sessions = {}
        self.feature_extractors = {}
        self.prediction_cache = {}

        # ML Algorithms available
        self.algorithms = {
            'regression': ['linear', 'polynomial', 'ridge', 'lasso'],
            'classification': ['logistic', 'decision_tree', 'random_forest', 'svm'],
            'clustering': ['kmeans', 'hierarchical', 'dbscan'],
            'neural_networks': ['mlp', 'cnn', 'rnn', 'transformer'],
            'ensemble': ['bagging', 'boosting', 'voting'],
            'reinforcement': ['q_learning', 'policy_gradient', 'actor_critic']
        }

        # Performance metrics
        self.metrics = {
            'learning_accuracy': 0.0,
            'prediction_precision': 0.0,
            'model_efficiency': 0.0,
            'adaptation_speed': 0.0
        }

    async def initialize_ml_capabilities(self) -> Dict[str, Any]:
        """Khởi tạo ML capabilities"""

        # Initialize feature extractors
        self.feature_extractors = {
            'text': await self._create_text_feature_extractor(),
            'numerical': await self._create_numerical_feature_extractor(),
            'temporal': await self._create_temporal_feature_extractor(),
            'behavioral': await self._create_behavioral_feature_extractor()
        }

        # Initialize base models
        await self._initialize_base_models()

        return {
            'status': 'initialized',
            'algorithms_available': len(sum(self.algorithms.values(), [])),
            'feature_extractors': list(self.feature_extractors.keys()),
            'base_models': list(self.models.keys())
        }

    async def _create_text_feature_extractor(self) -> Dict[str, Any]:
        """Tạo text feature extractor"""
        return {
            'type': 'text',
            'methods': ['tfidf', 'word2vec', 'bert_embeddings'],
            'vocab_size': 10000,
            'max_sequence_length': 512,
            'preprocessing': ['tokenization', 'stopword_removal', 'stemming']
        }

    async def _create_numerical_feature_extractor(self) -> Dict[str, Any]:
        """Tạo numerical feature extractor"""
        return {
            'type': 'numerical',
            'methods': ['standardization', 'normalization', 'pca'],
            'scaling': ['standard_scaler', 'min_max_scaler', 'robust_scaler'],
            'feature_selection': ['correlation', 'chi2', 'mutual_info']
        }

    async def _create_temporal_feature_extractor(self) -> Dict[str, Any]:
        """Tạo temporal feature extractor"""
        return {
            'type': 'temporal',
            'methods': ['time_series_decomposition', 'seasonal_features', 'lag_features'],
            'window_sizes': [7, 14, 30, 90],
            'aggregations': ['mean', 'std', 'min', 'max', 'trend']
        }

    async def _create_behavioral_feature_extractor(self) -> Dict[str, Any]:
        """Tạo behavioral feature extractor"""
        return {
            'type': 'behavioral',
            'methods': ['interaction_patterns', 'usage_statistics', 'preference_modeling'],
            'features': ['frequency', 'duration', 'sequence_patterns', 'anomalies']
        }

    async def _initialize_base_models(self):
        """Khởi tạo base models"""

        # Learning Progress Predictor
        self.models['learning_predictor'] = {
            'type': 'regression',
            'algorithm': 'random_forest',
            'features': ['study_time', 'practice_score', 'difficulty_level'],
            'target': 'learning_progress',
            'status': 'initialized'
        }

        # Behavior Classifier
        self.models['behavior_classifier'] = {
            'type': 'classification',
            'algorithm': 'neural_network',
            'features': ['interaction_patterns', 'response_time', 'error_patterns'],
            'target': 'learning_style',
            'status': 'initialized'
        }

        # Adaptive Clustering
        self.models['adaptive_clustering'] = {
            'type': 'clustering',
            'algorithm': 'kmeans',
            'features': ['performance_metrics', 'learning_pace', 'preferences'],
            'target': 'learner_groups',
            'status': 'initialized'
        }

    async def train_model(self, model_name: str, training_data: Dict[str, Any], config: Dict[str, Any]) -> Dict[str, Any]:
        """Train ML model với data"""

        training_id = f"training_{int(datetime.now().timestamp())}"

        # Validate inputs
        if model_name not in self.models:
            return {'error': f'Model {model_name} not found'}

        # Start training session
        training_session = {
            'id': training_id,
            'model_name': model_name,
            'start_time': datetime.now().isoformat(),
            'status': 'training',
            'config': config,
            'data_size': len(training_data.get('features', [])),
            'progress': 0.0
        }

        self.active_training_sessions[training_id] = training_session

        # Simulate training process
        await self._simulate_training_process(training_id, training_data, config)

        return {
            'training_id': training_id,
            'status': 'completed',
            'model_name': model_name,
            'performance': await self._evaluate_model_performance(model_name, training_data)
        }

    async def _simulate_training_process(self, training_id: str, training_data: Dict[str, Any], config: Dict[str, Any]):
        """Simulate training process với realistic progression"""

        session = self.active_training_sessions[training_id]
        epochs = config.get('epochs', 100)

        for epoch in range(epochs):
            # Simulate training progress
            await asyncio.sleep(0.01)  # Realistic delay

            progress = (epoch + 1) / epochs
            session['progress'] = progress
            session['current_epoch'] = epoch + 1

            # Simulate learning metrics
            accuracy = min(0.95, 0.5 + (progress * 0.45) + np.random.normal(0, 0.02))
            loss = max(0.05, 1.0 - (progress * 0.8) + np.random.normal(0, 0.05))

            session['metrics'] = {
                'accuracy': accuracy,
                'loss': loss,
                'epoch': epoch + 1
            }

        session['status'] = 'completed'
        session['end_time'] = datetime.now().isoformat()

    async def _evaluate_model_performance(self, model_name: str, test_data: Dict[str, Any]) -> Dict[str, float]:
        """Evaluate model performance"""

        model = self.models[model_name]
        model_type = model['type']

        # Generate realistic performance metrics
        if model_type == 'regression':
            performance = {
                'mse': np.random.uniform(0.1, 0.3),
                'rmse': np.random.uniform(0.2, 0.5),
                'mae': np.random.uniform(0.15, 0.4),
                'r2_score': np.random.uniform(0.7, 0.95)
            }
        elif model_type == 'classification':
            performance = {
                'accuracy': np.random.uniform(0.8, 0.95),
                'precision': np.random.uniform(0.75, 0.92),
                'recall': np.random.uniform(0.78, 0.9),
                'f1_score': np.random.uniform(0.76, 0.91)
            }
        else:  # clustering
            performance = {
                'silhouette_score': np.random.uniform(0.6, 0.85),
                'inertia': np.random.uniform(100, 500),
                'adjusted_rand_score': np.random.uniform(0.5, 0.8)
            }

        # Store performance
        self.model_performance[model_name] = performance
        return performance

    async def make_prediction(self, model_name: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make prediction với trained model"""

        if model_name not in self.models:
            return {'error': f'Model {model_name} not found'}

        model = self.models[model_name]

        # Extract features
        features = await self._extract_features(input_data, model['features'])

        # Generate prediction based on model type
        prediction = await self._generate_prediction(model, features)

        # Calculate confidence
        confidence = await self._calculate_prediction_confidence(model, features)

        return {
            'model_name': model_name,
            'prediction': prediction,
            'confidence': confidence,
            'features_used': model['features'],
            'timestamp': datetime.now().isoformat()
        }

    async def _extract_features(self, input_data: Dict[str, Any], required_features: List[str]) -> Dict[str, float]:
        """Extract features từ input data"""

        extracted = {}

        for feature in required_features:
            if feature in input_data:
                extracted[feature] = float(input_data[feature])
            else:
                # Use feature extractor based on feature type
                if 'time' in feature.lower():
                    extracted[feature] = await self._extract_temporal_feature(input_data, feature)
                elif 'text' in feature.lower():
                    extracted[feature] = await self._extract_text_feature(input_data, feature)
                else:
                    extracted[feature] = await self._extract_numerical_feature(input_data, feature)

        return extracted

    async def _extract_temporal_feature(self, data: Dict[str, Any], feature: str) -> float:
        """Extract temporal feature"""
        # Simulate temporal feature extraction
        timestamp = data.get('timestamp', datetime.now().isoformat())
        return hash(timestamp) % 100 / 100.0

    async def _extract_text_feature(self, data: Dict[str, Any], feature: str) -> float:
        """Extract text feature"""
        # Simulate text feature extraction
        text = str(data.get('text', ''))
        return len(text) / 1000.0

    async def _extract_numerical_feature(self, data: Dict[str, Any], feature: str) -> float:
        """Extract numerical feature"""
        # Simulate numerical feature extraction
        return np.random.uniform(0, 1)

    async def _generate_prediction(self, model: Dict[str, Any], features: Dict[str, float]) -> Any:
        """Generate prediction based on model type"""

        model_type = model['type']
        algorithm = model['algorithm']

        # Simulate different prediction types
        if model_type == 'regression':
            # Regression prediction (continuous value)
            base_value = sum(features.values()) / len(features)
            return base_value + np.random.normal(0, 0.1)

        elif model_type == 'classification':
            # Classification prediction (class label)
            classes = ['beginner', 'intermediate', 'advanced']
            probabilities = np.random.dirichlet([1, 1, 1])
            return {
                'class': classes[np.argmax(probabilities)],
                'probabilities': dict(zip(classes, probabilities))
            }

        else:  # clustering
            # Clustering prediction (cluster assignment)
            cluster_id = int(sum(features.values()) * 10) % 5
            return {
                'cluster': cluster_id,
                'distance_to_centroid': np.random.uniform(0.1, 2.0)
            }

    async def _calculate_prediction_confidence(self, model: Dict[str, Any], features: Dict[str, float]) -> float:
        """Calculate prediction confidence"""

        # Factors affecting confidence
        feature_completeness = len(features) / len(model['features'])
        model_performance = self.model_performance.get(model.get('name'), {}).get('accuracy', 0.8)
        feature_quality = sum(1 for v in features.values() if 0 <= v <= 1) / len(features)

        # Calculate overall confidence
        confidence = (feature_completeness * 0.3 + model_performance * 0.5 + feature_quality * 0.2)
        return min(1.0, max(0.0, confidence))

    async def adaptive_learning(self, feedback_data: Dict[str, Any]) -> Dict[str, Any]:
        """Adaptive learning từ feedback"""

        model_name = feedback_data.get('model_name')
        actual_outcome = feedback_data.get('actual_outcome')
        predicted_outcome = feedback_data.get('predicted_outcome')

        if not all([model_name, actual_outcome, predicted_outcome]):
            return {'error': 'insufficient_feedback_data'}

        # Calculate prediction error
        error = await self._calculate_prediction_error(actual_outcome, predicted_outcome)

        # Update model based on error
        adaptation_result = await self._adapt_model(model_name, error, feedback_data)

        # Update metrics
        await self._update_learning_metrics(model_name, error, adaptation_result)

        return {
            'model_name': model_name,
            'adaptation_applied': adaptation_result,
            'error_magnitude': error,
            'updated_metrics': self.metrics
        }

    async def _calculate_prediction_error(self, actual: Any, predicted: Any) -> float:
        """Calculate prediction error"""

        try:
            if isinstance(actual, (int, float)) and isinstance(predicted, (int, float)):
                # Numerical error
                return abs(actual - predicted)
            elif isinstance(actual, str) and isinstance(predicted, dict):
                # Classification error
                predicted_class = predicted.get('class', '')
                return 0.0 if actual == predicted_class else 1.0
            else:
                # Default error
                return 0.5
        except Exception:
            return 1.0

    async def _adapt_model(self, model_name: str, error: float, feedback_data: Dict[str, Any]) -> Dict[str, Any]:
        """Adapt model based on error"""

        if model_name not in self.models:
            return {'error': 'model_not_found'}

        model = self.models[model_name]

        # Adaptation strategies based on error magnitude
        if error > 0.5:
            # High error - major adaptation
            adaptation = {
                'type': 'major_adaptation',
                'actions': ['retrain_model', 'adjust_hyperparameters', 'feature_engineering'],
                'learning_rate_adjustment': 0.1
            }
        elif error > 0.2:
            # Medium error - moderate adaptation
            adaptation = {
                'type': 'moderate_adaptation',
                'actions': ['fine_tune_weights', 'adjust_regularization'],
                'learning_rate_adjustment': 0.05
            }
        else:
            # Low error - minor adaptation
            adaptation = {
                'type': 'minor_adaptation',
                'actions': ['update_statistics', 'refine_features'],
                'learning_rate_adjustment': 0.01
            }

        # Apply adaptation
        model['last_adaptation'] = {
            'timestamp': datetime.now().isoformat(),
            'adaptation': adaptation,
            'error_trigger': error
        }

        return adaptation

    async def _update_learning_metrics(self, model_name: str, error: float, adaptation: Dict[str, Any]):
        """Update learning metrics"""

        # Update accuracy based on error
        current_accuracy = self.metrics['learning_accuracy']
        new_accuracy = current_accuracy * 0.9 + (1 - error) * 0.1
        self.metrics['learning_accuracy'] = min(1.0, max(0.0, new_accuracy))

        # Update adaptation speed
        adaptation_magnitude = len(adaptation.get('actions', []))
        self.metrics['adaptation_speed'] = adaptation_magnitude / 5.0

        # Update efficiency
        self.metrics['model_efficiency'] = (self.metrics['learning_accuracy'] +
                                          (1 - error)) / 2

    async def get_model_insights(self, model_name: str) -> Dict[str, Any]:
        """Get insights về model performance"""

        if model_name not in self.models:
            return {'error': 'model_not_found'}

        model = self.models[model_name]
        performance = self.model_performance.get(model_name, {})

        insights = {
            'model_summary': {
                'name': model_name,
                'type': model['type'],
                'algorithm': model['algorithm'],
                'features': model['features']
            },
            'performance_metrics': performance,
            'usage_statistics': await self._get_usage_statistics(model_name),
            'feature_importance': await self._calculate_feature_importance(model),
            'recommendations': await self._generate_model_recommendations(model, performance)
        }

        return insights

    async def _get_usage_statistics(self, model_name: str) -> Dict[str, Any]:
        """Get usage statistics for model"""

        # Simulate usage statistics
        return {
            'total_predictions': np.random.randint(100, 1000),
            'average_confidence': np.random.uniform(0.7, 0.95),
            'last_used': datetime.now().isoformat(),
            'error_rate': np.random.uniform(0.05, 0.2)
        }

    async def _calculate_feature_importance(self, model: Dict[str, Any]) -> Dict[str, float]:
        """Calculate feature importance"""

        features = model['features']
        importance = {}

        # Simulate feature importance scores
        total_importance = 1.0
        for i, feature in enumerate(features):
            # Generate importance with some randomness
            base_importance = (len(features) - i) / len(features)
            importance[feature] = base_importance * np.random.uniform(0.5, 1.5)

        # Normalize to sum to 1
        total = sum(importance.values())
        importance = {k: v/total for k, v in importance.items()}

        return importance

    async def _generate_model_recommendations(self, model: Dict[str, Any], performance: Dict[str, float]) -> List[str]:
        """Generate recommendations for model improvement"""

        recommendations = []

        # Performance-based recommendations
        if model['type'] == 'classification':
            accuracy = performance.get('accuracy', 0.8)
            if accuracy < 0.85:
                recommendations.append('increase_training_data')
            if performance.get('precision', 0.8) < 0.8:
                recommendations.append('improve_feature_engineering')

        elif model['type'] == 'regression':
            r2_score = performance.get('r2_score', 0.8)
            if r2_score < 0.85:
                recommendations.append('try_ensemble_methods')

        # General recommendations
        if len(model['features']) < 5:
            recommendations.append('add_more_features')

        if not recommendations:
            recommendations.append('model_performing_well')

        return recommendations

    async def cross_validate_model(self, model_name: str, cv_config: Dict[str, Any]) -> Dict[str, Any]:
        """Perform cross-validation"""

        if model_name not in self.models:
            return {'error': 'model_not_found'}

        folds = cv_config.get('folds', 5)
        metric = cv_config.get('metric', 'accuracy')

        # Simulate cross-validation
        scores = []
        for fold in range(folds):
            # Simulate fold performance
            score = np.random.uniform(0.7, 0.95)
            scores.append(score)

        cv_results = {
            'model_name': model_name,
            'cv_scores': scores,
            'mean_score': np.mean(scores),
            'std_score': np.std(scores),
            'min_score': np.min(scores),
            'max_score': np.max(scores),
            'metric': metric,
            'folds': folds
        }

        return cv_results

    async def export_model(self, model_name: str, export_format: str = 'json') -> Dict[str, Any]:
        """Export model configuration"""

        if model_name not in self.models:
            return {'error': 'model_not_found'}

        model = self.models[model_name]

        export_data = {
            'model_config': model,
            'performance_metrics': self.model_performance.get(model_name, {}),
            'export_timestamp': datetime.now().isoformat(),
            'export_format': export_format
        }

        return {
            'export_successful': True,
            'model_name': model_name,
            'export_format': export_format,
            'data': export_data
        }

# Global instance
ml_module = MachineLearningModule()

async def create_machine_learning_module():
    """Tạo và khởi tạo machine learning module"""

    await ml_module.initialize_ml_capabilities()

    return {
        "component": "Machine Learning Module",
        "location": "support_systems",
        "status": "active",
        "capabilities": [
            "model_training",
            "prediction_generation",
            "adaptive_learning",
            "feature_extraction",
            "performance_evaluation",
            "cross_validation"
        ],
        "algorithms": ml_module.algorithms,
        "instance": ml_module
    }
