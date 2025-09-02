"""
PRISM Age Detection Module
Prevents inappropriate analysis of children in corporate context

This module implements age-appropriate analysis to avoid:
- Analyzing children as CEOs/VPs/Managers
- Applying corporate psychology to educational settings
- Inappropriate stress/power analysis for minors
"""

import logging
from typing import Dict, List, Any
import cv2
import numpy as np

logger = logging.getLogger(__name__)

class AgeDetector:
    """
    Detects age groups to ensure appropriate analysis context
    """
    
    def __init__(self):
        """Initialize age detection"""
        self.age_groups = {
            'child': (0, 12),
            'teenager': (13, 17), 
            'young_adult': (18, 25),
            'adult': (26, 40),
            'middle_aged': (41, 60),
            'senior': (60, 100)
        }
        
        # Simple heuristics for age detection without complex models
        self.child_indicators = [
            'classroom', 'school', 'education',
            'whiteboard', 'chalkboard', 'desk'
        ]
        
    def analyze_age_context(self, scene_type: str, object_list: List[str], 
                           people_count: int) -> Dict[str, Any]:
        """
        Analyze the age context of the scene to determine appropriate analysis
        
        Args:
            scene_type: Scene classification from CLIP
            object_list: List of detected objects
            people_count: Number of people detected
            
        Returns:
            Age context analysis with appropriate role mappings
        """
        try:
            # Check for educational context indicators
            educational_indicators = self._detect_educational_context(scene_type, object_list)
            
            # Determine likely age group based on context
            age_context = self._determine_age_context(educational_indicators, people_count)
            
            # Get appropriate role mappings
            role_mappings = self._get_age_appropriate_roles(age_context)
            
            return {
                'age_context': age_context,
                'educational_setting': educational_indicators['is_educational'],
                'appropriate_roles': role_mappings,
                'analysis_mode': self._get_analysis_mode(age_context),
                'confidence': educational_indicators['confidence']
            }
            
        except Exception as e:
            logger.error(f"Age context analysis failed: {e}")
            return self._get_fallback_context()
    
    def _detect_educational_context(self, scene_type: str, object_list: List[str]) -> Dict[str, Any]:
        """Detect if this is an educational setting with children"""
        
        educational_score = 0
        indicators_found = []
        
        # Check scene type and caption for educational keywords
        educational_keywords = ['school', 'classroom', 'education', 'teacher', 'teaching', 'student', 'children', 'learning']
        if any(edu_word in scene_type.lower() for edu_word in educational_keywords):
            educational_score += 0.4
            indicators_found.append('scene_classification')
        
        # Check for educational objects
        educational_objects = ['book', 'pen', 'pencil', 'paper', 'notebook', 'backpack', 
                             'desk', 'chair', 'whiteboard', 'chalkboard']
        
        found_objects = [obj for obj in object_list if obj in educational_objects]
        if found_objects:
            educational_score += min(len(found_objects) * 0.1, 0.3)
            indicators_found.extend(found_objects)
        
        # Check for child-specific indicators
        child_objects = ['toy', 'crayon', 'marker', 'eraser']
        found_child_objects = [obj for obj in object_list if obj in child_objects]
        if found_child_objects:
            educational_score += 0.3
            indicators_found.extend(found_child_objects)
        
        return {
            'is_educational': educational_score > 0.5,
            'confidence': min(educational_score, 1.0),
            'indicators': indicators_found
        }
    
    def _determine_age_context(self, educational_indicators: Dict, people_count: int) -> str:
        """Determine the likely age context of the group"""
        
        if educational_indicators['is_educational']:
            if people_count <= 5:
                return 'mixed_educational'  # Likely teacher + students
            else:
                return 'classroom'  # Larger classroom setting
        
        # Corporate indicators (default for business meetings)
        return 'adult_professional'
    
    def _get_age_appropriate_roles(self, age_context: str) -> Dict[str, List[str]]:
        """Get role mappings appropriate for the age context"""
        
        if age_context in ['mixed_educational', 'classroom']:
            return {
                'authority_figure': ['Teacher', 'Instructor', 'Educator', 'Professor'],
                'participants': ['Student', 'Learner', 'Pupil'],
                'assistant': ['Teaching Assistant', 'Aide', 'Helper'],
                'observer': ['Student Observer', 'Quiet Learner']
            }
        
        else:  # adult_professional
            return {
                'authority_figure': ['CEO', 'President', 'Director', 'VP'],
                'participants': ['Manager', 'Senior Analyst', 'Specialist'],
                'assistant': ['Executive Assistant', 'Coordinator'],
                'observer': ['Junior Analyst', 'Associate', 'Intern']
            }
    
    def _get_analysis_mode(self, age_context: str) -> str:
        """Determine appropriate analysis mode"""
        
        if age_context in ['mixed_educational', 'classroom']:
            return 'educational_psychology'
        else:
            return 'corporate_psychology'
    
    def adapt_personality_analysis(self, age_context: str, base_personalities: Dict) -> Dict:
        """Adapt personality analysis for age-appropriate context"""
        
        if age_context in ['mixed_educational', 'classroom']:
            # Modify personalities to be age-appropriate for educational context
            adapted = {}
            
            for person_id, profile in base_personalities.items():
                adapted_profile = profile.copy()
                
                # Replace corporate traits with educational ones
                if 'Strategic' in profile.get('traits', []):
                    adapted_profile['traits'] = ['Curious', 'Engaged', 'Thoughtful', 'Creative']
                
                if 'Commanding Presence' in profile.get('traits', []):
                    adapted_profile['traits'] = ['Natural Leader', 'Helpful', 'Confident', 'Encouraging']
                
                # Adjust communication styles
                if profile.get('communication_style') == 'Direct and authoritative':
                    adapted_profile['communication_style'] = 'Clear and encouraging'
                
                adapted[person_id] = adapted_profile
            
            return adapted
        
        return base_personalities
    
    def get_appropriate_predictions(self, age_context: str, base_predictions: Dict) -> Dict:
        """Get age-appropriate behavioral predictions"""
        
        if age_context in ['mixed_educational', 'classroom']:
            # Educational predictions
            educational_predictions = {}
            
            for person_id, predictions in base_predictions.items():
                if person_id == 'person_1':  # Likely teacher
                    educational_predictions[person_id] = [
                        'Will guide the discussion and ask questions',
                        'Will encourage student participation',
                        'Will provide feedback and clarification',
                        'Will adapt teaching style to student needs'
                    ]
                else:  # Students
                    educational_predictions[person_id] = [
                        'Will participate when encouraged',
                        'May ask questions for clarification', 
                        'Will learn from peer interactions',
                        'Will show curiosity about the topic'
                    ]
            
            return educational_predictions
        
        return base_predictions
    
    def _get_fallback_context(self) -> Dict[str, Any]:
        """Provide fallback context if analysis fails"""
        return {
            'age_context': 'adult_professional',
            'educational_setting': False,
            'appropriate_roles': self._get_age_appropriate_roles('adult_professional'),
            'analysis_mode': 'corporate_psychology',
            'confidence': 0.5
        }