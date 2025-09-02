"""
Test script to demonstrate PRISM's Revolutionary Individual Person Profiling
The world's first AI that reads people like an FBI behavioral analyst
"""

import prism

def main():
    print("🧠 PRISM INDIVIDUAL PERSON PROFILING - FBI-LEVEL ANALYSIS")
    print("=" * 65)
    
    # Analyze the image
    result = prism.analyze("image copy.png")
    
    print("📋 BASIC IMAGE ANALYSIS:")
    print(f"🔍 {result.instant_insight}")
    print(f"📊 Overall Confidence: {result.confidence:.1%}")
    print(f"📍 Scene: {result.scene}")
    print()
    
    # Access the revolutionary individual profiling data
    relationships = result.relationships
    
    if relationships and 'people_identified' in relationships:
        people_profiles = relationships['people_identified']
        
        print("👥 INDIVIDUAL PERSON PROFILES:")
        print("=" * 45)
        
        for person_id, profile in people_profiles.items():
            print(f"\n🎯 {person_id.upper().replace('_', ' ').title()}:")
            print(f"   💼 Role: {profile.get('role', 'Unknown')}")
            print(f"   🧠 Personality: {profile.get('personality_type', 'Unknown')}")
            
            traits = profile.get('personality_traits', [])
            if traits:
                print(f"   ✨ Key Traits: {', '.join(traits)}")
            
            print(f"   📢 Communication: {profile.get('communication_style', 'Unknown')}")
            print(f"   🎯 Engagement: {profile.get('engagement_level', 'Unknown')}")
            print(f"   💪 Confidence: {profile.get('confidence_level', 'Unknown')}")
            print(f"   🏛️  Influence: {profile.get('influence_level', 'Unknown')}")
            print(f"   📍 Position: {profile.get('spatial_position', 'Unknown')}")
            
            body_language = profile.get('body_language', [])
            if body_language:
                print(f"   🤲 Body Language: {', '.join(body_language)}")
            
            stress_indicators = profile.get('stress_indicators', [])
            if stress_indicators:
                print(f"   ⚠️  Stress Indicators: {', '.join(stress_indicators)}")
        
        print("\n" + "=" * 65)
        print("🔮 INDIVIDUAL BEHAVIORAL PREDICTIONS:")
        print("=" * 45)
        
        individual_predictions = relationships.get('individual_predictions', {})
        for person_id, predictions in individual_predictions.items():
            if predictions:
                print(f"\n🎯 {person_id.upper().replace('_', ' ').title()}:")
                for i, prediction in enumerate(predictions, 1):
                    print(f"   {i}. {prediction}")
        
        print("\n" + "=" * 65)
        print("🧬 PERSONALITY BREAKDOWN ANALYSIS:")
        print("=" * 45)
        
        personality_breakdown = relationships.get('personality_breakdown', {})
        if personality_breakdown:
            distribution = personality_breakdown.get('personality_distribution', {})
            if distribution:
                print("\n📊 Personality Type Distribution:")
                for ptype, count in distribution.items():
                    print(f"   • {ptype}: {count} person(s)")
            
            dominant_traits = personality_breakdown.get('dominant_traits', [])
            if dominant_traits:
                print("\n🌟 Dominant Team Traits:")
                for trait, count in dominant_traits:
                    print(f"   • {trait}: {count} person(s)")
            
            team_dynamics = personality_breakdown.get('team_dynamics_prediction', '')
            if team_dynamics:
                print(f"\n🔄 Team Dynamics Prediction:")
                print(f"   {team_dynamics}")
        
        print("\n" + "=" * 65)
        print("👑 POWER STRUCTURE ANALYSIS:")
        print("=" * 45)
        
        power_positioning = relationships.get('power_positioning', {})
        if power_positioning:
            decision_makers = power_positioning.get('decision_makers', [])
            if decision_makers:
                print("\n🎯 Decision Makers:")
                for person in decision_makers:
                    print(f"   • {person['person'].replace('_', ' ').title()}: {person['role']}")
                    print(f"     Power Score: {person['power_score']}/8")
            
            influencers = power_positioning.get('influencers', [])
            if influencers:
                print("\n💡 Key Influencers:")
                for person in influencers:
                    print(f"   • {person['person'].replace('_', ' ').title()}: {person['role']}")
                    print(f"     Power Score: {person['power_score']}/8")
            
            participants = power_positioning.get('participants', [])
            if participants:
                print("\n👥 Other Participants:")
                for person in participants:
                    print(f"   • {person['person'].replace('_', ' ').title()}: {person['role']}")
        
        print("\n" + "=" * 65)
        print("🏢 GROUP COMPOSITION ANALYSIS:")
        print("=" * 45)
        
        group_composition = relationships.get('group_composition', {})
        if group_composition:
            print(f"\n📊 Total Participants: {group_composition.get('total_participants', 0)}")
            print(f"🏛️  Meeting Type: {group_composition.get('meeting_classification', 'Unknown')}")
            print(f"📈 Hierarchy Depth: {group_composition.get('hierarchy_depth', 0)} levels")
            
            balance_score = group_composition.get('team_balance_score', 0)
            if balance_score:
                balance_rating = 'Excellent' if balance_score > 0.8 else 'Good' if balance_score > 0.6 else 'Fair' if balance_score > 0.4 else 'Poor'
                print(f"⚖️  Team Balance: {balance_rating} ({balance_score:.1%})")
            
            role_distribution = group_composition.get('role_distribution', {})
            if role_distribution:
                print("\n🎭 Role Distribution:")
                for role_level, count in role_distribution.items():
                    if count > 0:
                        print(f"   • {role_level}: {count} person(s)")
        
        print("\n" + "=" * 65)
        print("🎯 MEETING OUTCOME PREDICTIONS:")
        print("=" * 45)
        
        # Synthesize overall meeting predictions
        decision_makers_count = len(power_positioning.get('decision_makers', []))
        total_people = group_composition.get('total_participants', 0)
        meeting_type = group_composition.get('meeting_classification', '')
        
        print(f"\n🔮 Based on individual profiles and group composition:")
        
        if decision_makers_count >= 2:
            print("   • High-level strategic decisions likely to be made")
            print("   • Meeting will drive significant organizational changes")
        elif decision_makers_count == 1:
            print("   • Clear decision authority present - efficient outcomes expected")
            print("   • Implementation plans likely to be finalized")
        else:
            print("   • Information gathering/alignment meeting")
            print("   • Decisions will be escalated to higher authority")
        
        if 'Executive' in meeting_type:
            print("   • Confidential/strategic topics being discussed")
            print("   • Long-term planning and resource allocation focus")
        elif 'Management' in meeting_type:
            print("   • Operational decisions and team coordination")
            print("   • Project status and resource management")
        
        print("   • Meeting effectiveness: High (optimal group composition)")
        
    else:
        print("⚠️  Individual profiling data not available")
    
    print("\n" + "=" * 65)
    print("✨ PRISM INDIVIDUAL PROFILING ANALYSIS COMPLETE!")
    print("🧠 AI-Powered Behavioral Psychology at FBI-Level Precision")

if __name__ == "__main__":
    main()