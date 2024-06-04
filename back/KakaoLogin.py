import requests
import os
import pymysql
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
import bcrypt

# 환경 변수 로드
load_dotenv()

KAKAO_CLIENT_ID = os.environ.get('KAKAO_CLIENT_ID')
KAKAO_REDIRECT_URI = os.environ.get('KAKAO_REDIRECT_URI')

kakao_bp = Blueprint('kakao', __name__)

def db_con():
    return pymysql.connect(
        host='project-db-cgi.smhrd.com',
        user='campus_23K_AI18_p3_2',
        password='smhrd2',
        db='campus_23K_AI18_p3_2',
        port=3307,
        charset='utf8'
    )

def get_access_token(auth_code):
    data = {
        'grant_type': 'authorization_code',
        'client_id': KAKAO_CLIENT_ID,
        'redirect_uri': KAKAO_REDIRECT_URI,
        'code': auth_code
    }
    response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
    if response.status_code != 200:
        print(f"Failed to get access token: {response.json()}")
        return None
    access_token = response.json().get('access_token')
    return access_token

def get_user_info(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get('https://kapi.kakao.com/v2/user/me', headers=headers)
    if response.status_code != 200:
        print(f"Failed to get user info: {response.json()}")
        return None
    user_info = response.json()
    return user_info

@kakao_bp.route('/user/kakao/callback', methods=['GET', 'POST'])
def kakao_callback():
    # 1. 카카오 로그인 인증 코드 받기
    code = request.args.get('code')
    print("카카오 로그인 인증 코드: ", code)
    
    if not code:
        return jsonify({'error': 'Authorization code not found'}), 400

    # 2. 인증 코드를 사용하여 액세스 토큰 받기
    access_token = get_access_token(code)
    if not access_token:
        return jsonify({'error': 'Failed to get access token'}), 400
    print("액세스 토큰: ", access_token)
    
    # 3. 액세스 토큰을 사용하여 사용자 정보 받기
    user_info = get_user_info(access_token)
    if not user_info:
        return jsonify({'error': 'Failed to get user info'}), 400
    print("사용자 정보: ", user_info)

    # 사용자 정보와 토큰 반환
    return jsonify({'token': access_token, 'user': user_info})

@kakao_bp.route('/user/kakao/login', methods=['POST'])
def kakao_login():
    data = request.get_json()
    user_id = data.get('id')
    print(f"User ID received: {user_id}")

    # 데이터베이스 연결
    conn = db_con()
    cursor = conn.cursor()

    try:
        # 사용자 ID 확인
        cursor.execute("""
            SELECT u.USER_PW, u.USER_STATUS
            FROM TB_AUTH a
            JOIN TB_USER u ON a.USER_ID = u.USER_ID
            WHERE a.AUTH_ID = %s
        """, (user_id,))
        user_data = cursor.fetchone()
        print(f"User data from DB: {user_data}")

        if user_data is None:
            return jsonify({'success': False})
        
        user_status = user_data[1]  # 저장된 bcrypt 해시 비밀번호와 상태 가져오기

        if user_status == 'stop':
            return jsonify({'message': 'Account is suspended'}), 403  # 계정 사용 정지
        
        # 로그인 성공
        return jsonify({'success': True})
        
    except Exception as e:
        print(f"Database error: {e}")
        return jsonify({'error': 'Database error'}), 500
    finally:
        cursor.close()
        conn.close()
