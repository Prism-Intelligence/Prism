import pytest
import os
from PIL import Image
import tempfile

from prism import analyze

def create_test_image():
    """Create a simple test image"""
    img = Image.new('RGB', (100, 100), color='red')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    img.save(temp_file.name)
    return temp_file.name

def test_analyze_basic():
    """Test basic analysis functionality"""
    test_image = create_test_image()
    
    try:
        result = analyze(test_image)
        
        # Check that result has expected attributes
        assert hasattr(result, 'summary')
        assert hasattr(result, 'objects') 
        assert hasattr(result, 'scene')
        assert hasattr(result, 'confidence')
        
        # Check types
        assert isinstance(result.summary, str)
        assert isinstance(result.objects, list)
        assert isinstance(result.scene, str)
        assert isinstance(result.confidence, float)
        
        # Check confidence is in valid range
        assert 0 <= result.confidence <= 1
        
    finally:
        os.unlink(test_image)

def test_analyze_nonexistent_file():
    """Test error handling for nonexistent files"""
    with pytest.raises(FileNotFoundError):
        analyze("nonexistent_file.jpg")
