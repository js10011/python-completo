from google.cloud import vision
import io

def detect_objects(image_path):
    # Create a client
    client = vision.ImageAnnotatorClient()

    # Load the image
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Perform object detection
    response = client.object_localization(image=image)
    localized_object_annotations = response.localized_object_annotations

    # Print the results
    print('Objetos detectados:')
    for obj in localized_object_annotations:
        print(f'\n{obj.name} (confiança: {obj.score})')
        print('Vértices do polígono delimitador:')
        for vertex in obj.bounding_poly.normalized_vertices:
            print(f' - ({vertex.x}, {vertex.y})')

    if response.error.message:
        raise Exception(f'{response.error.message}')


image_path = 'path_to_your_image.jpg'
detect_objects(image_path)