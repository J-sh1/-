
# 📄프로젝트 정보

## 1. 프로젝트 소개
> 프로젝트 명 : 윌리를찾아라👕👖(PAR(Pedestrian-Attribute-Recognition) 기반 CCTV 영상 속 인상착의를 통한 실종자 찾기)
>> 사용자로부터 인상착의 정보를 받아 CCTV영상에서 인상착의 정보와 일치하는 객체를 찾아 실종자를 찾아주는 서비스

## 2. 제작기간
> 24.05.22 ~ 24.06.20

## 3. 참여인원
> | 이름 | 역할 |
> | --- | --- |
> | 김자영 | PM / Back / Front |
> | 박덕근 | Front / Model / Back |
> | 안영빈 | Back |
> | 이대길 | Back / Front |
> | **조승혁** | **Model / Back** |

![팀원역할](https://jsh-1.s3.ap-northeast-2.amazonaws.com/image-2.png)

## 4. 내가 맡은 역할

### 1. **서버 및 환경 구축**
  - **CCTV 데이터 수집 환경 구축**: CCTV 데이터를 안정적으로 수집할 수 있는 시스템 환경 설정.
  - **DB - 백엔드 - 딥러닝 모델 연동**: 데이터베이스와 백엔드를 딥러닝 모델과 연동하여 데이터 처리 흐름을 구축.

### 2. **모델링 및 기능 구현**
  - **해당 인상착의 실종자 후보 인식 시 캡처 기능**: 분석된 인상착의가 실종자와 유사할 때 해당 영상을 캡처하는 기능 구현.
  - **모델 비동기 처리**: 시스템의 성능을 높이기 위해 딥러닝 모델의 비동기 처리 구현.
  - **해당 인상착의의 실종자가 추정되는 영상 선택**: 실종자로 추정되는 인물이 포함된 영상을 자동으로 선택하는 기능 개발.
  - **정확도 향상(모델 성능 개선)**: 모델의 성능을 향상시키기 위한 다양한 기술적 개선 작업 수행.
  - **CCTV 객체 인상착의 분석 모델링 검증**: 분석된 결과를 검증하여 모델의 신뢰성을 확인하는 기능 구현.

### 3. **관리자 기능 구현**
  - **관리자 포스터 관리 기능**: 사용자가 등록한 포스터 수정, 삭제할 수 있는 기능 구현.
  - **관리자 CCTV 관리 기능**: 관리자가 CCTV 영상을 관리하고 조회할 수 있는 기능 구현.
  - **관리자 회원 관리 기능**: 관리자가 시스템 내 회원 정보를 관리하는 기능 구현.
  - **관리자 실종자 관리 기능**: 실종자 정보를 관리하고 업데이트할 수 있는 기능 구현.
  - **관리자 제보 관리 기능**: 관리자가 접수된 제보를 관리하고 처리하는 기능 구현.
  - **관리자 페이지 - 제보 관리**: 관리자 페이지에서 제보 사항을 효율적으로 관리할 수 있는 UI 및 기능 구현.

### 4. **테스트**
  - **단위 테스트 및 통합 테스트 진행**


#  💻사용기술
## 1. Front-end
> ![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)

## 2. Back-end
> ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## 3. AI/Model
> ![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)
![CLIP](https://img.shields.io/badge/CLIP-00875A?style=for-the-badge&logo=ai&logoColor=white)
![ViT-B/16](https://img.shields.io/badge/ViT--B%2F16-4A90E2?style=for-the-badge&logo=ai&logoColor=white)

## 4. 기타
> ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS%20S3-569A31?style=for-the-badge&logo=amazonaws&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

<br>


# 📋시스템아키텍처, 서비스흐름도, 시연영상

## 1. 시스템 아키텍처
<details>
<summary>시스템 아키텍처 펼쳐보기</summary>
  
![시스템 아키텍처](https://jsh-1.s3.ap-northeast-2.amazonaws.com/image.png)

</details>

## 2. 서비스 흐름도

<details>
<summary>서비스 흐름도 펼쳐보기</summary>

![서비스 흐름도](https://jsh-1.s3.ap-northeast-2.amazonaws.com/image-1.png)

</details>

## 3. 화면구성(시연영상)
[클릭 시 영상이 재생됩니다.](https://jsh-1.s3.ap-northeast-2.amazonaws.com/%EC%9C%8C%EB%A6%AC%EB%A5%BC%EC%B0%BE%EC%95%84%EB%9D%BC(%EA%B9%80%EC%9E%90%EC%98%81%ED%8C%80)+%EC%8B%9C%EC%97%B0+%EC%98%81%EC%83%81.mp4) <br>
소리가 클 수 있으니 주의 해주세요!!

# 💿핵심기능
1. 사용자가 입력한 인상착의 정보를 DB에 저장하고 모델로 전송.
2. 모델이 실종자 최종 위치를 기반으로 CCTV를 조회.
3. 인상착의와 일치하는 인물 발견 시, CCTV 화면을 캡처하여 사용자에게 전송.
4. 사용자는 캡처 화면을 확인하여 실종자와 비교.
5. CCTV 위치를 기반으로 실종자 위치로 이동하여 찾음.
6. 인상착의 정보를 사용해 생성형 AI로 포스터 생성.
7. 다른 사용자가 포스터 사진으로 위치 제보 가능.



# 🗂️산출문서
[산출문서 바로가기](https://drive.google.com/drive/folders/1bOiFvosGpsRhw1ICjjSDMV4lGheyBWIu?usp=sharing)



# 🛠️초기 세팅
## 1. Git 설치 및 사용자 등록
### Git 설치
1. [Git 공식 사이트](https://git-scm.com/download/win/)에서 Git을 다운로드하여 설치합니다.

### Git 사용자 등록
1. 터미널을 열고 다음 명령어를 실행합니다.
    ```sh
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"
    ```

### 프로젝트 클론
1. [VSCode](https://code.visualstudio.com/download) 또는 [다른 IDE](https://www.cursor.com/)를 실행합니다.
2. 터미널 창을 엽니다.
3. 다음 명령어를 실행하여 프로젝트를 클론합니다.
    ```sh
    git clone https://github.com/memorygreen/final_project_K18.git
    ```

## 2. Front 실행 환경 구성
### 노드 설치하기
1. [Node.js 공식 사이트](https://nodejs.org/en)에서 Node.js를 다운로드하여 설치합니다.

### 프로젝트 설정
1. VSCode에서 `final_project_K18` 폴더를 엽니다.
2. 터미널에서 다음 명령어를 실행합니다.
    ```sh
    cd final_project_K18/front
    npm install
    npm start
    ```
3. `.env` 파일을 생성하여 보안 관련 코드를 작성합니다.

## 3. Back 실행 환경 구성
### 파이썬 설치하기
1. [Python 공식 사이트](https://www.python.org/downloads/)에서 Python을 다운로드하여 설치합니다.

### 프로젝트 설정
1. VSCode에서 `final_project_K18` 폴더를 엽니다.
2. `Ctrl + Shift + P`를 누르고 `>Python: Select Interpreter`를 선택합니다.
3. 파이썬 버전을 선택합니다.
4. 터미널에서 다음 명령어를 실행합니다.
    ```sh
    cd back
    pip install -r requirements.txt
    python app.py
    ```
5. 만약 `pip install` 명령어가 작동하지 않는다면 다음을 수행합니다.
    - 윈도우 검색창에 시스템 환경 변수 편집을 입력하고 엽니다.
    - 고급 탭에서 환경 변수를 클릭합니다.
    - 시스템 변수 목록에서 Path를 찾아 클릭한 후 편집을 클릭합니다.
    - 새로 만들기를 클릭하고 다음 경로를 추가합니다.
        ```sh
        C:\Users\{사용자이름}\AppData\Local\Programs\Python\Python312\Scripts
        ```
    - VSCode를 재실행하고 `final_project_K18` 폴더를 엽니다.
    - 터미널에서 해당 명령어를 다시 실행합니다.
        ```sh
        cd back
        pip install -r requirements.txt
        python app.py
        ```
    - 문제가 해결되지 않으면 컴퓨터를 재부팅합니다.
6. `.env` 파일을 생성하여 보안 관련 코드를 작성합니다.

## 4. Model 실행 환경 구성
### 모델 설치
1. [모델 다운로드](https://www.dropbox.com/scl/fo/e1l7kwn6qdnu91auiw13m/AIQCWlAnK3vJwwoc7pgUak4?rlkey=1e6pwpoa3x14nk6fmg8ewhvva&st=8ydslwcc&dl=0) 링크를 클릭해서 모델을 설치합니다.
2. 모델을 설치한 후 프로젝트 폴더에 위치시킵니다.
3. 터미널에서 다음 명령어를 실행합니다.
    ```sh
    cd model
    pip install -r requirements.txt
    python app.py
    ```
4. `.env` 파일을 생성하여 보안 관련 코드를 작성합니다.

