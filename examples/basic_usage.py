"""
Basic usage example for PRISM
"""

import prism

def main():
    # Replace with path to your test image
    image_path = "test_image.jpg"
    
    try:
        # Analyze the image
        result = prism.analyze(image_path)
        
        # Display results
        print("=== PRISM Analysis Results ===")
        print(f"Summary: {result.summary}")
        print(f"Scene: {result.scene}")
        print(f"Objects: {', '.join(result.objects)}")
        print(f"Confidence: {result.confidence:.2%}")
        print("\nFull result:")
        print(result)
        
    except FileNotFoundError:
        print(f"Please provide a valid image path. '{image_path}' not found.")
    except Exception as e:
        print(f"Analysis failed: {e}")

if __name__ == "__main__":
    main()
