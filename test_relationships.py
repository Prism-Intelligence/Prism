"""
Test script to demonstrate PRISM's Revolutionary Relationship Detection System
"""

import prism

def main():
    print("🚀 Testing PRISM's Revolutionary Relationship Detection")
    print("=" * 60)
    
    # Analyze the image
    result = prism.analyze("image copy.png")
    
    print("📋 BASIC ANALYSIS:")
    print(f"🔍 {result.instant_insight}")
    print(f"📊 Confidence: {result.confidence:.1%}")
    print(f"📍 Scene: {result.scene}")
    print(f"💭 Summary: {result.summary}")
    print()
    
    print("👥 REVOLUTIONARY RELATIONSHIP INSIGHTS:")
    print("=" * 45)
    
    # Access relationship data
    relationships = result.relationships
    human_dynamics = result.human_dynamics
    
    if relationships:
        print("🔬 RELATIONSHIP MAP:")
        rel_map = relationships.get('relationship_map', [])
        for rel in rel_map:
            print(f"   • {rel.get('description', 'Relationship detected')}")
            print(f"     Confidence: {rel.get('confidence', 0):.1%}")
        
        print()
        print("💼 POWER DYNAMICS:")
        power = relationships.get('power_dynamics', {})
        if power.get('hierarchy_detected'):
            print(f"   • Structure: {power.get('power_structure', 'detected').replace('_', ' ').title()}")
            print(f"   • Leadership: {'Identified' if power.get('leader_identified') else 'Distributed'}")
            print(f"   • Decision Style: {power.get('decision_making_style', 'unknown').replace('_', ' ').title()}")
        else:
            print("   • No clear hierarchy detected")
        
        print()
        print("🌡️  EMOTIONAL CLIMATE:")
        emotional = relationships.get('emotional_climate', {})
        print(f"   • Overall Mood: {emotional.get('overall_mood', 'unknown').replace('_', ' ').title()}")
        print(f"   • Stress Level: {emotional.get('stress_level', 'unknown').replace('_', ' ').title()}")
        print(f"   • Engagement: {emotional.get('engagement', 'unknown').title()}")
        
        print()
        print("📈 MEETING ANALYSIS:")
        meeting = relationships.get('meeting_analysis', {})
        if meeting.get('type') != 'social_gathering':
            print(f"   • Type: {meeting.get('meeting_type', 'unknown').replace('_', ' ').title()}")
            print(f"   • Effectiveness: {meeting.get('effectiveness_score', 0):.1%}")
            print(f"   • Formality: {meeting.get('formality_level', 'unknown').title()}")
        
        print()
        print("🔮 BEHAVIORAL PREDICTIONS:")
        predictions = relationships.get('behavioral_predictions', [])
        for pred in predictions:
            print(f"   • {pred.get('prediction', 'Prediction available')}")
            print(f"     Confidence: {pred.get('confidence', 0):.1%}")
            print(f"     Reasoning: {pred.get('reasoning', 'Based on group dynamics')}")
        
        print()
        print("🎯 KEY INSIGHTS:")
        key_insights = relationships.get('key_insights', [])
        for insight in key_insights:
            print(f"   • {insight}")
    else:
        print("⚠️  Relationship analysis data not available")
    
    print()
    print("✨ PRISM'S REVOLUTIONARY ANALYSIS COMPLETE!")

if __name__ == "__main__":
    main()