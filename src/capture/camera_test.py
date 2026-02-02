import pyrealsense2 as rs
import numpy as np
import cv2

# Configuração da câmera Intel RealSense
pipeline = rs.pipeline()
config = rs.config()

# Ativar os dois sensores (Colorido e Profundidade)
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Iniciar a transmissão
pipeline.start(config)

print("Câmera conectada com sucesso! Pressione 'q' para fechar.")

try:
    while True:
        # Esperar por um par de frames (cor e profundidade)
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        # Converter para formato que o computador entende (numpy arrays)
        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Aplicar um mapa de cores na profundidade (para humanos conseguirem ver)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Juntar as duas imagens lado a lado
        images = np.hstack((color_image, depth_colormap))

        # Mostrar na tela
        cv2.imshow('CattleWeight-AI: Visualizacao 3D', images)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()