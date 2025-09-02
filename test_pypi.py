#!/usr/bin/env python3
"""
Test script for the PRISM package from PyPI
Run this outside the project directory to test the published package
"""

# First install the package: pip install prismintelligence
# Then use it like this:

import prism

print(f"✅ PRISM PyPI package imported! Version: {prism.__version__}")
print()

# Analyze the image
result = prism.analyze("image.png")

print("🎯 PRISM Analysis Results:")
print("=" * 40)
print(f"🔍 {result.instant_insight}")
print(f"📊 Confidence: {result.confidence:.1%}")
print(f"📍 Scene: {result.scene}")
print(f"💭 Summary: {result.summary}")
print(f"🏷️  Objects: {', '.join(result.objects)}")
print()
print("✨ PRISM analysis complete!")