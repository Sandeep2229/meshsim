import meshpy.triangle as triangle

def generate_mesh(_input_data: str):
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    facets = [(0, 1), (1, 2), (2, 3), (3, 0)]

    info = triangle.MeshInfo()
    info.set_points(points)
    info.set_facets(facets)

    mesh = triangle.build(info)

    # ✅ Convert arrays to regular lists
    return {
        "points": [list(p) for p in mesh.points],
        "elements": [list(e) for e in mesh.elements]
    }
