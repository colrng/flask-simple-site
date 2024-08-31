from flask import Flask, render_template, request

app = Flask(__name__)

# 사용자 정보 저장 파일 경로
USER_FILE = 'user.txt'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info', methods=['GET', 'POST'])
def info():
    if request.method == 'POST':
        name = request.form['name'].strip()
        email = request.form['email'].strip()
        
        # 이름과 이메일이 빈 문자열인 경우 에러 메시지 반환
        if not name or not email:
            return "<h1>오류: 이름과 이메일은 비어 있거나 공백만 있을 수 없습니다. 다시 시도해 주세요.</h1>"

        # 사용자 정보 저장
        with open(USER_FILE, 'a') as file:
            file.write(f"{name},{email}\n")
        
        return f"<h1>입력해주셔서 감사합니다. {name}! 이메일 또한 입력해주셔서 감사합니다. {email}.</h1>"
    
    return render_template('info.html')

@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        name_to_delete = request.form['name'].strip()
        email_to_delete = request.form['email'].strip()
        
        # 이름과 이메일이 빈 문자열인 경우 에러 메시지 반환
        if not name_to_delete or not email_to_delete:
            return "<h1>오류: 이름과 이메일은 비어 있거나 공백만 있을 수 없습니다. 다시 시도해 주세요.</h1>"
        
        # 파일에서 사용자 정보 읽기
        with open(USER_FILE, 'r') as file:
            lines = file.readlines()
        
        # 사용자 정보 삭제
        with open(USER_FILE, 'w') as file:
            for line in lines:
                name, email = line.strip().split(',')
                if name != name_to_delete or email != email_to_delete:
                    file.write(line)
        
        return f"<h1>사용자 {name_to_delete}의 정보가 삭제되었습니다.</h1>"
    
    return render_template('delete_user.html')

if __name__ == '__main__':
    app.run(debug=True)
