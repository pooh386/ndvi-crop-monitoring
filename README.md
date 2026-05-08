# NDVI Crop Monitoring: Mongolia Ulaanbaatar School No. 60 Case Study


**1. Project Motivation**

2024년 PNU 해외전공봉사단 활동 중, 몽골 울란바토르 60번 학교에 스마트팜을 구축하고 적양배추를 식재하였습니다.
귀국 후 해당 지역의 작물 생육 상태를 지속적으로 확인하기 어려운 한계를 해결하고자,컴퓨터공학 복수전공 역량을 결합하여 위성 기반 원격 모니터링 시스템을 직접 구현하였습니다.


**2. Analysis Workflow**

Step 1: Data Filtering & Selection
- Target Area: 몽골 울란바토르 60번 학교 (School No. 60, Ulaanbaatar, Mongolia) 주변 농지
- Satellite: Sentinel-2 (ESA)
- Process: 구름의 영향을 최소화한 최신 위성 데이터를 필터링하여 분석에 적합한 영상 확보 (구름 10% 아래조건으로 필터링)


Step 2: Data Pre-processing
- Bands Used: Red Band (B04), NIR Band (B08)
- Format: .jp2 (JPEG 2000) 위성 원본 데이터 로딩 및 행렬(Array) 변환


Step 3: 
- NDVI Calculation식물의 광합성 활성도를 정량화하기 위해 다음 수식을 적용하였습니다.
<img width="219" height="69" alt="image" src="https://github.com/user-attachments/assets/2ebfc82f-390e-4949-bc58-79ed0b3b3296" />
- Rasterio와 NumPy를 활용하여 수천만 개의 픽셀 연산을 수행하였습니다.


**3. Results**

**데이터 필터링 (Area of Interest)**

<img width="1912" height="902" alt="image" src="https://github.com/user-attachments/assets/4fd0ec79-69ae-4e65-aad3-4a72297844d3" />
<img width="1919" height="915" alt="몽골 울란바토르 60번학교 필터링 다운로드 과정" src="https://github.com/user-attachments/assets/66f6e353-2a5c-42e3-ab62-848b3236dcea" />


**분석 결과 (NDVI Heatmap)**

<img width="1196" height="997" alt="몽골 울란바토르 60번학교 부근 NDVI 결과값" src="https://github.com/user-attachments/assets/bb3f03a0-02c6-481e-8f3f-173d26009904" />


Result Analysis:
식생 건강도 포착: 학교 주변 지역의 NDVI 값을 산출한 결과, 
짙은 녹색으로 표시된 지점(NDVI > 0.6)에서 활발한 식생 활동이 일어나고 있음을 확인하였습니다.

정량적 통계: 분석 결과, 해당 지역의 최대 NDVI 값은 0.82, 평균 값은 0.45로 산출되었습니다. 
이를 통해 현장에 직접 방문하지 않고도 적양배추 등 작물의 생육 상태를 추정할 수 있는 기반을 마련하였습니다.


**4. Tech Stack**
Language: Python 3.12+
Libraries: rasterio, numpy, matplotlib, os


