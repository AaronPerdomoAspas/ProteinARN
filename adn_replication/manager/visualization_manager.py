from vpython import cylinder, vector, color, rate, scene, text
import random

class VisualizationManager:
    @staticmethod
    def representar_proceso_3d(cadena_lider, cadena_rezagada):
        scene.title = "Replicación del ADN en 3D"
        scene.background = color.white

        # Colores para cada base
        color_base = {
            'A': color.red,    # Adenina
            'T': color.yellow, # Timina
            'C': color.blue,   # Citosina
            'G': color.green    # Guanina
        }

        # Posiciones para la visualización
        for i, base in enumerate(cadena_lider):
            rate(2)  # Control de velocidad del proceso en tiempo real
            # Crear cilindros para la cadena líder
            cylinder(pos=vector(i, 1, 0), axis=vector(0, 1, 0), radius=0.1, color=color_base[base])
            # Crear etiquetas para la cadena líder
            text(pos=vector(i, 1, 0), text=base, color=color.black, height=0.2, depth=0.1)

        for i, base in enumerate(cadena_rezagada):
            rate(2)
            # Crear cilindros para la cadena rezagada
            cylinder(pos=vector(i, -1, 0), axis=vector(0, 1, 0), radius=0.1, color=color_base[base])
            # Crear etiquetas para la cadena rezagada
            text(pos=vector(i, -1, 0), text=base, color=color.black, height=0.2, depth=0.1)

        # Simular la adición de nuevas bases (representación simplificada)
        for i in range(len(cadena_lider)):
            rate(1)
            # Adición de una nueva base a la cadena líder
            base_nueva = random.choice(list(color_base.keys()))
            cylinder(pos=vector(i + len(cadena_lider), 1, 0), axis=vector(0, 1, 0), radius=0.1, color=color_base[base_nueva])
            text(pos=vector(i + len(cadena_lider), 1, 0), text=base_nueva, color=color.black, height=0.2, depth=0.1)
