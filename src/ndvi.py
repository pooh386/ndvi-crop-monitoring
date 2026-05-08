import rasterio
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. 경로 설정
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "..", "data")

# 2. 디버깅용
files = os.listdir(data_dir)
print(f"data 폴더 내 파일 목록: {files}")

# 3. 파일명 

red_file = "B04.jp2" #
nir_file = "B08.jp2"

red_path = os.path.join(data_dir, red_file)
nir_path = os.path.join(data_dir, nir_file)

try:
    # 데이터 읽기
    with rasterio.open(red_path) as src:
        red = src.read(1).astype(float)
    with rasterio.open(nir_path) as src:
        nir = src.read(1).astype(float)

    print("✅ 데이터를 성공적으로 불러왔습니다.")

    # 4. NDVI 계산
    # (NIR - RED) / (NIR + RED)
    ndvi = (nir - red) / (nir + red + 1e-10)

    # 5. 시각화
    plt.figure(figsize=(12, 10))
    
    img = plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
    plt.colorbar(img, label='NDVI Value')
    plt.title("Satellite-based NDVI Analysis (Sentinel-2)", fontsize=15)
    plt.xlabel("Pixels (X)")
    plt.ylabel("Pixels (Y)")
    
    print(f"📊 분석 결과 - 최대 NDVI: {np.max(ndvi):.2f}, 평균 NDVI: {np.mean(ndvi):.2f}")
    plt.show()

except Exception as e:
    print(f"❌ 오류가 발생했습니다: {e}")
    print(f"시도한 경로: {red_path}")