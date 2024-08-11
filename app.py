from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 簿記の基礎コンテンツ
lessons = {
    'lesson1': {
        'title': 'レッスン1: 簿記の基本',
        'text': '簿記の基礎を学びます。',
        'image': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
        'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ'
    },
    'lesson2': {
        'title': 'レッスン2: 仕訳の基礎',
        'text': '仕訳の基礎を学びます。',
        'image': 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
        'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ'
    },
    'lesson3': {
        'title': 'レッスン3: 貸借対照表の理解',
        'text': '貸借対照表の理解を深めます。',
        'image': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60',
        'video': 'https://www.youtube.com/embed/dQw4w9WgXcQ'
    }
}


# クイズコンテンツ
quizzes = [
    {
        'question': '簿記の目的は何ですか？',
        'options': ['財務状況の把握', '在庫管理', '従業員のスケジュール管理'],
        'answer': '財務状況の把握'
    },
    {
        'question': '仕訳とは何ですか？',
        'options': ['取引を記録するプロセス', '商品を在庫に登録するプロセス', '顧客情報を管理するプロセス'],
        'answer': '取引を記録するプロセス'
    },
    {
        'question': '資産の増加はどの勘定科目に該当しますか？',
        'options': ['借方', '貸方', '収益'],
        'answer': '借方'
    },
    {
        'question': '売上高はどの勘定科目に該当しますか？',
        'options': ['資産', '負債', '収益'],
        'answer': '収益'
    },
    {
        'question': '負債の減少はどの勘定科目に該当しますか？',
        'options': ['借方', '貸方', '資本'],
        'answer': '借方'
    },
    {
        'question': '純資産の増加はどの勘定科目に該当しますか？',
        'options': ['貸方', '借方', '費用'],
        'answer': '貸方'
    },
    {
        'question': '簿記の基本的な帳簿は何ですか？',
        'options': ['総勘定元帳', '貸借対照表', '損益計算書'],
        'answer': '総勘定元帳'
    },
    {
        'question': '貸方に計上されるのは次のどれですか？',
        'options': ['現金の増加', '売上の発生', '費用の発生'],
        'answer': '売上の発生'
    },
    {
        'question': '費用の発生はどの勘定科目に該当しますか？',
        'options': ['借方', '貸方', '収益'],
        'answer': '借方'
    },
    {
        'question': '現金の減少はどの勘定科目に該当しますか？',
        'options': ['借方', '貸方', '費用'],
        'answer': '貸方'
    }
]


@app.route('/')
def index():
   return render_template('index.html', lessons=lessons)

@app.route('/lesson/<lesson_id>')
def lesson(lesson_id):
    lesson_data = lessons.get(lesson_id)
    if lesson_data is None:
        return "Lesson not found", 404
    return render_template('lesson.html', lesson=lesson_data)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0
        for i, quiz in enumerate(quizzes):
            selected = request.form.get(f'question-{i}')
            if selected == quiz['answer']:
                score += 1
        
        # スコアに応じたコメントを設定
        if score == len(quizzes):
            comment = "素晴らしい！全問正解です！"
        elif score > len(quizzes) * 0.7:
            comment = "とても良い結果です。あと少しで全問正解です。"
        elif score > len(quizzes) * 0.4:
            comment = "まあまあの結果です。もう少し頑張りましょう。"
        else:
            comment = "残念！もっと勉強が必要です。頑張りましょう。"

        return render_template('quiz_result.html', score=score, total=len(quizzes), comment=comment)
    
    return render_template('quiz.html', quizzes=quizzes, enumerate=enumerate)

if __name__ == '__main__':
    app.run(debug=True)
