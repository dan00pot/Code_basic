import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Lấy nội dung tệp JSON của tài khoản dịch vụ
cred = credentials.Certificate('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.json')

#Khởi tạo ứng dụng bằng tài khoản dịch vụ, cấp quyền quản trị viên
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://xxxxxxxxxxxxx.firebaseio.com',
    'databaseAuthVariableOverride': {
        'uid': 'my-service-worker'
    }
})
# Là quản trị viên, ứng dụng có quyền truy cập để đọc và ghi tất cả dữ liệu, không có quy tắc bảo mật
ref = db.reference('restricted_access/secret_document')
ref = db.reference('dan00pot')
users_ref = ref.child('controlled')
users_ref.set({
    'led1': {
        'id': '1',
        'do sang': '100'
    },
    'led2': {
        'id': '2',
        'do sang': '50'
    }
})
print(ref.get())