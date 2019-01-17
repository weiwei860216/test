from enum import Enum


class UserType(Enum):
    SystemManager = (0b100000, '系統管理員')
    ExamManager = (0b10000, '考試管理員')
    QuestionManager = (0b1000, '題庫管理員')
    QuestionOperator = (0b100, '題目操作員')
    ScoreViewer = (0b10, '成績檢閱者')
    Tester = (0b1, '受測者')


class QuestionType(Enum):
    QA = (1, '聽力／問答')
    ShortConversation = (2, '聽力／簡短對話')
    Grammar = (3, '閱讀／文法')
    Phrase = (4, '閱讀／名詞片語')
    ParagraphUnderstanding = (5, '閱讀／段落理解')